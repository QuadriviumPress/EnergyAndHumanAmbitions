"""Turn the source PDF into a structured block stream, one entry per page.

Run ``python3 scripts/extract.py`` to write ``build/document.json``.
"""

from __future__ import annotations

import json
import os
import re
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from layout import (  # noqa: E402
    Char, CAPTION_RE, FOOTER_Y, HEADER_Y, LEADING, PARA_GAP,
    SIZE_BODY, SIZE_CHAPTER, SIZE_PART, SIZE_PART_LABEL, SIZE_SECTION,
    SIZE_SUBSECTION, WIDE_COLUMNS, Frag, artwork_clusters, attach_figure_text, columns_for,
    page_frags, shaded_boxes, _inflate, _overlap, _union,
)
from mathtext import (  # noqa: E402
    _is_mathchar, font_class, render_fraction_region, render_line, render_math_only,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "220222_2.pdf")

# icon colours drawn in the margin
ICON_COLORS = {
    (0.93, 0.11, 0.14): "caution",
    (0.08, 0.46, 0.74): "info",
    (0.34, 0.69, 0.89): "info",
    (0.18, 0.19, 0.57): "info",
}

DOT_LEADER = re.compile(r"\.\s?\.\s?\.\s?\.")


# --------------------------------------------------------------------------
# fragment merging
# --------------------------------------------------------------------------


def _same_line(a, b):
    """Do two fragments belong to one visual line?"""
    if abs(a.baseline - b.baseline) <= 1.6:
        return True
    # a lone superscript or subscript that pdfTeX split into its own line
    gap = max(b.bbox[0] - a.bbox[2], a.bbox[0] - b.bbox[2])
    if -1.0 <= gap <= 5 and abs(a.baseline - b.baseline) <= 5.5:
        small, large = sorted((a, b), key=lambda f: f.maxsize)
        if small.maxsize <= 0.82 * large.maxsize:
            return True
    # tall maths glyphs (big parentheses, fraction bars) sit on their own
    # baseline; join them when the boxes overlap vertically and touch
    if abs(a.baseline - b.baseline) > 6.5 and not (a.is_delimiter or b.is_delimiter):
        return False
    lo, hi = max(a.bbox[1], b.bbox[1]), min(a.bbox[3], b.bbox[3])
    if hi - lo < 0.55 * min(a.bbox[3] - a.bbox[1], b.bbox[3] - b.bbox[1]):
        return False
    if not -1.0 <= gap <= 12:
        return False
    return _has_math(a) or _has_math(b)


def merge_baselines(frags, bars=()):
    """Join fragments that make up one visual line inside the same column."""
    out = []
    for column in ("main", "margin", "wide"):
        group = [f for f in frags if f.column == column]
        group.sort(key=lambda f: (f.baseline, f.bbox[0]))
        parent = list(range(len(group)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a in range(len(group)):
            for b in range(a + 1, len(group)):
                if group[b].baseline - group[a].baseline > 14:
                    break
                if _same_line(group[a], group[b]):
                    parent[find(b)] = find(a)
        for bar in bars:
            members = _bar_members(group, bar)
            for k in members[1:]:
                parent[find(k)] = find(members[0])
        buckets = {}
        for k, f in enumerate(group):
            buckets.setdefault(find(k), []).append(f)
        for members in buckets.values():
            out.append(_join(members, column))
    out.sort(key=lambda f: (f.baseline, f.bbox[0]))
    return out


def _bar_members(group, bar):
    """Fragments that make up one fraction or radical drawn around ``bar``."""
    wide = bar[2] - bar[0] >= 12
    kind = bar[3] if len(bar) > 3 else "frac"
    lo, hi = bar[0] - 1.0, bar[2] + 1.0
    host_lo, host_hi = (-4.5, 12.0) if kind == "sqrt" else (-4.5, 4.5)
    members = []
    for k, f in enumerate(group):
        if f.bbox[2] < bar[0] - 3 or f.bbox[0] > bar[2] + 3:
            continue
        delta = f.baseline - bar[1]
        if wide:
            if abs(delta) <= 19:
                members.append(k)
            continue
        # the numerator or denominator: script-sized characters straddling the rule
        top = f.maxsize
        stacked = any(c.c.strip() and lo <= c.x + (c.w or 0.0) / 2 <= hi
                      and abs(c.y - bar[1]) <= 10 and c.size <= 0.86 * top
                      for c in f.chars)
        if stacked or host_lo <= delta <= host_hi:
            members.append(k)
    if wide:
        members += [k for k, f in enumerate(group)
                    if abs(f.baseline - bar[1]) <= 5.5
                    and f.bbox[2] > bar[0] - 26 and f.bbox[0] < bar[2] + 26]
    return sorted(set(members))


def _join(frags, column):
    frags = sorted(frags, key=lambda f: f.bbox[0])
    chars = []
    for k, f in enumerate(frags):
        mono_run = (chars and font_class(chars[-1].font) == "mono"
                    and f.chars and font_class(f.chars[0].font) == "mono")
        if k and f.bbox[0] - frags[k - 1].bbox[2] > 1.2 and chars \
                and chars[-1].c != " " and not mono_run:
            gap = f.bbox[0] - frags[k - 1].bbox[2]
            chars.append(type(chars[-1])(" ", frags[k - 1].bbox[2], chars[-1].y,
                                         chars[-1].size, chars[-1].font))
            chars[-1].gap = gap
        chars.extend(f.chars)
    bbox = (min(f.bbox[0] for f in frags), min(f.bbox[1] for f in frags),
            max(f.bbox[2] for f in frags), max(f.bbox[3] for f in frags))
    return Frag(chars, bbox, column)


# --------------------------------------------------------------------------
# per-page model
# --------------------------------------------------------------------------


def icons(page):
    out = []
    for dr in page.get_drawings():
        fill = dr.get("fill")
        if fill is None:
            continue
        key = tuple(round(v, 2) for v in fill)
        if key not in ICON_COLORS:
            continue
        r = dr["rect"]
        if r.width > 16 or r.height > 16 or r.width < 4:
            continue
        out.append((ICON_COLORS[key], (r.x0, r.y0, r.x1, r.y1)))
    return out


def usable_clusters(page, frags, boxes, pad=9):
    clusters = attach_figure_text(artwork_clusters(page, boxes, pad, frags), frags, pad)
    keep = []
    for c in clusters:
        w, h = c[2] - c[0], c[3] - c[1]
        if w < 14 or h < 12:
            continue
        if w * h < 900:
            continue
        keep.append((max(c[0], 20.0), max(c[1], HEADER_Y),
                     min(c[2], 540.0), min(c[3], FOOTER_Y)))
    return keep


def caption_blocks(frags):
    """Group caption fragments (they wrap over several lines)."""
    blocks = []
    used = set()
    for i, f in enumerate(frags):
        if i in used:
            continue
        m = CAPTION_RE.match(f.raw.strip())
        if not m:
            continue
        members = [f]
        used.add(i)
        prev = f
        for j in range(i + 1, len(frags)):
            if j in used:
                continue
            g = frags[j]
            if g.column != f.column:
                continue
            if CAPTION_RE.match(g.raw.strip()):
                break
            if g.baseline - prev.baseline > LEADING * 1.5 or g.baseline <= prev.baseline:
                if g.baseline - prev.baseline > LEADING * 1.5:
                    break
                continue
            if abs(g.size - f.size) > 0.8:
                break
            if g.bbox[0] > f.bbox[0] + 14 or g.bbox[0] < f.bbox[0] - 14:
                break
            members.append(g)
            used.add(j)
            prev = g
        blocks.append({
            "kind": m.group(1).lower(),
            "number": m.group(2),
            "frags": members,
            "column": f.column,
            "bbox": (min(x.bbox[0] for x in members), min(x.bbox[1] for x in members),
                     max(x.bbox[2] for x in members), max(x.bbox[3] for x in members)),
        })
    return blocks, used


def fraction_bars(page, frags, clusters, skip_y=()):
    """Thin rules with mathematics stacked above and below: fraction bars."""
    bars = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.height > 1.6 or not (1.8 < r.width < 210):
            continue
        if not (HEADER_Y < r.y0 < FOOTER_Y):
            continue
        rect = (r.x0, 0.5 * (r.y0 + r.y1), r.x1)
        if any(abs(rect[1] - y) < 1.5 for y in skip_y):
            continue                     # the rule above a page note
        if any(rect[0] >= c[0] - 3 and rect[2] <= c[2] + 3
               and rect[1] >= c[1] - 3 and rect[1] <= c[3] + 3 for c in clusters):
            continue
        radical = False
        for f in frags:
            for c in f.chars:
                if c.c == "\u221a" and -12 < rect[0] - (c.x + (c.w or 0.0)) < 4 \
                        and -14 < c.y - rect[1] < 4:
                    radical = True
        above = below = False
        for f in frags:
            if f.bbox[2] < rect[0] - 2 or f.bbox[0] > rect[2] + 2:
                continue
            for c in f.chars:
                if not c.c.strip() or not (rect[0] - 1 <= c.x <= rect[2] + 1):
                    continue
                if 0.3 < rect[1] - c.y < 16:
                    above = True
                elif 0.3 < c.y - rect[1] < 18:
                    below = True
        if radical:
            bars.append(rect + ("sqrt",))
        elif above and below:
            bars.append(rect + ("frac",))
    return bars


def note_rules(page, geom):
    """The short rule that separates a page note from the body text."""
    m0 = geom[0]
    out = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.height > 2 or not (90 < r.width < 210):
            continue
        if abs(r.x0 - m0) > 8 or r.y0 < 380:
            continue
        out.append(0.5 * (r.y0 + r.y1))
    return out


def horizontal_rules(page, boxes, clusters):
    """Thin horizontal lines: in this book they only ever rule tables."""
    box_rects = [r for _, r in boxes]
    out = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.height > 1.9 or r.width < 25:
            continue
        if not (HEADER_Y < r.y0 < FOOTER_Y):
            continue
        rect = (r.x0, r.y0, r.x1, r.y1)
        if any(rect[0] >= b[0] - 2 and rect[2] <= b[2] + 2
               and rect[1] >= b[1] - 2 and rect[3] <= b[3] + 2 for b in box_rects):
            continue
        if any(rect[0] >= c[0] - 3 and rect[2] <= c[2] + 3
               and rect[1] >= c[1] - 3 and rect[3] <= c[3] + 3 for c in clusters):
            continue
        out.append(rect)
    return sorted(out, key=lambda r: r[1])


def rule_chains(rules):
    """Group table rules into the individual tables they belong to."""
    chains = []
    for r in rules:
        placed = False
        for ch in chains:
            if r[1] - ch[-1][3] <= 240 and abs(r[0] - ch[-1][0]) <= 10 \
                    and abs(r[2] - ch[-1][2]) <= 10:
                ch.append(r)
                placed = True
                break
        if not placed:
            chains.append([r])
    out = []
    for ch in chains:
        if len(ch) < 2:
            continue
        x0 = min(r[0] for r in ch)
        x1 = max(r[2] for r in ch)
        out.append({
            "rect": (x0 - 3, ch[0][1] - 12, x1 + 3, ch[-1][3] + 3),
            "header_y": ch[1][3] if len(ch) >= 3 else None,
        })
    return out


def assign_tables(chains, captions):
    """Give every table caption the ruled block nearest to it."""
    tabs = [c for c in captions if c["kind"] == "table"]
    used = set()
    for cap in tabs:
        best, bestd = None, 1e9
        for k, ch in enumerate(chains):
            if k in used:
                continue
            d = _dist(ch["rect"], cap["bbox"])
            if d < bestd:
                best, bestd = k, d
        if best is not None and bestd < 110:
            used.add(best)
            cap["region"] = chains[best]["rect"]
            cap["header_y"] = chains[best]["header_y"]
        else:
            cap["region"] = None
            cap["header_y"] = None
    return [c for k, c in enumerate(chains) if k not in used]


def _split_cells(frag):
    """Break one fragment at the wide gaps that separate table columns."""
    out, run, last = [], [], None
    for ch in frag.chars:
        if last is not None and ch.c.strip():
            if ch.x - (last.x + (last.w or 0.0)) > 0.45 * max(last.size, ch.size) + 1.0:
                out.append(run)
                run = []
        run.append(ch)
        if ch.c.strip():
            last = ch
    if run:
        out.append(run)
    cells = []
    for run in out:
        vis = [c for c in run if c.c.strip()]
        if not vis:
            continue
        bbox = (vis[0].x, frag.bbox[1], vis[-1].x + (vis[-1].w or 0.0), frag.bbox[3])
        cells.append(Frag(vis, bbox, frag.column))
    return cells


def table_rows(region, frags, header_y=None):
    """Reconstruct a ruled table as rows of cells."""
    inside = [f for f in frags
              if f.bbox[0] >= region[0] - 4 and f.bbox[2] <= region[2] + 6
              and f.bbox[1] >= region[1] - 2 and f.bbox[3] <= region[3] + 2]
    if not inside:
        return []
    inside = [c for f in inside for c in _split_cells(f)]
    rows = []
    for f in sorted(inside, key=lambda f: (f.baseline, f.bbox[0])):
        if rows and abs(f.baseline - rows[-1][0]) <= 2.2:
            rows[-1][1].append(f)
        else:
            rows.append((f.baseline, [f]))
    # column bands from the union of every cell's horizontal extent
    spans = sorted((f.bbox[0], f.bbox[2]) for _, cells in rows for f in cells)
    bands = []
    for a, b in spans:
        if bands and a <= bands[-1][1] + 2.5:
            bands[-1][1] = max(bands[-1][1], b)
        else:
            bands.append([a, b])
    table = []
    for base, cells in rows:
        line = [""] * len(bands)
        for f in sorted(cells, key=lambda f: f.bbox[0]):
            best, cover = 0, -1
            for k, (a, b) in enumerate(bands):
                ov = min(f.bbox[2], b) - max(f.bbox[0], a)
                if ov > cover:
                    best, cover = k, ov
            txt = render_line(f.chars, sidenotes=False)
            line[best] = (line[best] + " " + txt).strip() if line[best] else txt
        table.append({"cells": line, "header": header_y is not None and base < header_y})
    return table


def _dist(cluster, bbox):
    dx = max(0.0, max(cluster[0] - bbox[2], bbox[0] - cluster[2]))
    dy = max(0.0, max(cluster[1] - bbox[3], bbox[1] - cluster[3]))
    return (dx * dx + dy * dy) ** 0.5


def _coalesce_loose_artwork(rects):
    """Join the pieces of an uncaptioned illustration, and drop stray marks."""
    out = list(rects)
    changed = True
    while changed:
        changed = False
        for i in range(len(out)):
            for j in range(i + 1, len(out)):
                if _overlap(_inflate(out[i], 25), _inflate(out[j], 25)):
                    out[i] = _union(out[i], out[j])
                    del out[j]
                    changed = True
                    break
            if changed:
                break
    return [r for r in out if (r[2] - r[0]) * (r[3] - r[1]) >= 1500]


def _ink_rects(page):
    """Every drawing and image rectangle on the page, unmerged."""
    out = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.is_empty or r.is_infinite or r.height > 600:
            continue
        out.append((r.x0, r.y0, r.x1, r.y1))
    for block in page.get_text("dict")["blocks"]:
        if block["type"] == 1:
            out.append(tuple(block["bbox"]))
    return out


def _refine_cut(ink, rect, cut):
    """Move a slab boundary into the nearest band of whitespace."""
    span = rect[3] - rect[1]
    bands = []
    for r in sorted(ink, key=lambda r: r[1]):
        if r[3] < rect[1] or r[1] > rect[3]:
            continue
        if r[2] < rect[0] or r[0] > rect[2]:
            continue
        if r[3] - r[1] > 0.55 * span:
            continue                     # a figure-wide background patch
        lo, hi = max(r[1], rect[1]), min(r[3], rect[3])
        if bands and lo <= bands[-1][1] + 1.0:
            bands[-1][1] = max(bands[-1][1], hi)
        else:
            bands.append([lo, hi])
    gaps = [(bands[k][1], bands[k + 1][0]) for k in range(len(bands) - 1)
            if bands[k + 1][0] - bands[k][1] > 4]
    if not gaps:
        return cut
    best = min(gaps, key=lambda g: abs(0.5 * (g[0] + g[1]) - cut))
    if abs(0.5 * (best[0] + best[1]) - cut) > 90:
        return cut
    return 0.5 * (best[0] + best[1])


def _split_shared_artwork(caps, assignment, leftovers, ink=()):
    """Share one merged artwork block between the captions stacked against it.

    Some pages draw several figures so close together that no clustering
    tolerance separates them.  Rather than guess a boundary here, the whole
    block and the caption's rank within it are recorded, and the renderer —
    which can see actual ink — makes the cut.
    """
    figs = [c for c in caps if c["kind"] == "figure"]
    empty = [c for c in figs if not assignment[id(c)]]
    if not empty:
        return
    owners = [(c, assignment[id(c)][0]) for c in figs if len(assignment[id(c)]) == 1]
    for owner, rect in owners:
        members = [owner]
        for cap in empty:
            if assignment[id(cap)]:
                continue
            if rect[1] - 40 <= cap["bbox"][1] and rect[3] + 40 >= cap["bbox"][3]:
                members.append(cap)
        if len(members) < 2:
            continue
        members.sort(key=lambda c: c["bbox"][1])
        for rank, cap in enumerate(members):
            cut0 = rect[1] + (rect[3] - rect[1]) * rank / len(members)
            cut1 = rect[1] + (rect[3] - rect[1]) * (rank + 1) / len(members)
            assignment[id(cap)] = [(rect[0], cut0, rect[2], cut1)]
            cap["shared"] = [round(v, 1) for v in rect]
            cap["slab"] = [rank, len(members)]


def _is_chapter_opener(cluster):
    """The full-bleed photograph banded across the top of a chapter's first page."""
    return (cluster[1] <= HEADER_Y + 2 and cluster[2] - cluster[0] > 460
            and cluster[3] < 260)


def _score(cluster, cap):
    """How strongly one artwork cluster belongs to one caption."""
    d = _dist(cluster, cap["bbox"]) + 1.0
    x_overlap = not (cluster[2] < cap["bbox"][0] - 8 or cluster[0] > cap["bbox"][2] + 8)
    y_overlap = not (cluster[3] < cap["bbox"][1] - 6 or cluster[1] > cap["bbox"][3] + 6)
    if cluster[3] <= cap["bbox"][1] + 4 and x_overlap:
        d *= 0.2                       # artwork sitting directly above its caption
    elif cap["column"] == "margin" and y_overlap:
        d *= 0.25                      # margin caption set alongside its artwork
    return d


def assign_clusters(clusters, captions):
    """Give every figure caption the artwork nearest to it.

    Captions are served round-robin so that two figures stacked on one page
    cannot both be swallowed by whichever caption happens to be closest.
    """
    figs = [c for c in captions if c["kind"] == "figure"]
    assignment = {id(c): [] for c in figs}
    if not figs:
        return assignment, list(clusters)
    free = [k for k in range(len(clusters)) if not _is_chapter_opener(clusters[k])]
    openers = [clusters[k] for k in range(len(clusters)) if _is_chapter_opener(clusters[k])]
    pairs = sorted(((_score(clusters[k], cap), k, ci)
                    for k in free for ci, cap in enumerate(figs)),
                   key=lambda t: t[0])
    taken_cluster, served = set(), set()
    for score, k, ci in pairs:
        if k in taken_cluster or ci in served or score > 260:
            continue
        assignment[id(figs[ci])].append(clusters[k])
        taken_cluster.add(k)
        served.add(ci)
    leftovers = list(openers)
    for k in free:
        if k in taken_cluster:
            continue
        best, bestd = None, 1e9
        for cap in figs:
            d = _dist(clusters[k], cap["bbox"])
            if d < bestd:
                best, bestd = cap, d
        if best is not None and bestd < 60:
            assignment[id(best)].append(clusters[k])
        else:
            leftovers.append(clusters[k])
    return assignment, leftovers


# --------------------------------------------------------------------------
# line classification
# --------------------------------------------------------------------------

EQ_NUM_RE = re.compile(r"\((\d+\.\d+)\)\s*$")
EQ_TRAIL_RE = re.compile(r"\(((?:[A-D]|\d+)\.\d+[a-z]?)\)\s*$")
LIST_NUM_RE = re.compile(r"^(\d{1,3})\.\s")
BULLET_RE = re.compile(r"^[▶■]\s*")
BOX_TITLE_RE = re.compile(r"^Box\s+((?:[A-D]|\d+)\.\d+):")
DEF_TITLE_RE = re.compile(r"^Definition\s+((?:[A-D]|\d+)\.\d+\.\d+)\s")
EX_TITLE_RE = re.compile(r"^Example\s+((?:[A-D]|\d+)\.\d+\.\d+)\s")
MARGIN_NUM_RE = re.compile(r"^(\d{1,3}):\s")


def line_kind(frag, left, right, container, wide=False):
    raw = frag.raw.strip()
    size = frag.maxsize
    bold = any("Bold" in c.font for c in frag.chars if c.c.strip())
    if size >= SIZE_PART - 1 and bold:
        return "part-title"
    if size >= SIZE_PART_LABEL - 0.6 and "TeXGyreHeros" in "".join(frag.fonts):
        return "part-label"
    if size >= SIZE_CHAPTER - 0.8 and bold:
        return "chapter-title"
    if abs(size - SIZE_SECTION) < 0.6 and bold:
        return "section"
    if abs(size - SIZE_SUBSECTION) < 0.6 and bold:
        return "subsection"
    if frag.column != "margin" and not wide:
        indented = frag.bbox[0] > left + 32
        if indented and _math_density(frag) >= 0.3:
            return "equation"
        # a flush-right equation number settles the matter
        if EQ_TRAIL_RE.search(raw) and frag.bbox[2] >= right - 34 \
                and frag.bbox[0] > left + 8 and _has_math(frag):
            return "equation"
    return "text"


def _has_math(frag):
    return any(_is_mathchar(c) for c in frag.chars if c.c.strip())


def _math_density(frag):
    """Fraction of a line's visible characters that are mathematics."""
    vis = [c for c in frag.chars if c.c.strip()]
    if not vis:
        return 0.0
    hits = sum(1 for c in vis if _is_mathchar(c) or font_class(c.font) == "math")
    scripts = sum(1 for c in vis if c.size < frag.maxsize - 1.2)
    return (hits + scripts) / len(vis)


# --------------------------------------------------------------------------
# page processing
# --------------------------------------------------------------------------


def _is_wide_page(frags):
    """Back matter (bibliography, notation, glossary) runs the full measure."""
    body = [f for f in frags if len(f.raw.strip()) > 3]
    if len(body) < 8:
        return False
    across = sum(1 for f in body if f.column == "wide")
    return across / len(body) >= 0.3


def process_page(doc, i):
    page = doc[i]
    m0, m1, g0, g1 = columns_for(i)
    frags = page_frags(page, i)
    wide = _is_wide_page(frags)
    if wide:
        frags = page_frags(page, i, wide=True)
        m0, m1, g0, g1 = WIDE_COLUMNS
    boxes = shaded_boxes(page)
    marks = icons(page)
    caps, cap_ids = caption_blocks(frags)
    wanted = sum(1 for c in caps if c["kind"] == "figure")
    clusters = usable_clusters(page, frags, boxes)
    for pad in (6, 4, 3, 2, 1):
        if len(clusters) >= wanted:
            break
        tighter = usable_clusters(page, frags, boxes, pad)
        if len(tighter) > len(clusters):
            clusters = tighter
    rules = horizontal_rules(page, boxes, clusters)
    spare = assign_tables(rule_chains(rules), caps)
    for cap in caps:
        if cap["kind"] == "table" and cap.get("region"):
            cap["rows"] = table_rows(cap["region"], frags, cap.get("header_y"))
        else:
            cap["rows"] = []
    for chain in spare:
        rows = table_rows(chain["rect"], frags, chain["header_y"])
        if len(rows) < 2:
            continue
        caps.append({"kind": "table", "number": None, "frags": [], "rows": rows,
                     "column": "main", "bbox": chain["rect"], "art": [],
                     "region": chain["rect"], "header_y": chain["header_y"]})
    assignment, leftovers = assign_clusters(clusters, caps)
    _split_shared_artwork(caps, assignment, leftovers, _ink_rects(page))
    leftovers = _coalesce_loose_artwork(leftovers)

    # fragments swallowed by artwork are figure labels, not prose
    art_rects = [r for lst in assignment.values() for r in lst] + leftovers
    art_rects += [c["region"] for c in caps if c["kind"] == "table" and c.get("region")]
    art_rects += [c["bbox"] for c in caps if c["kind"] == "table" and not c["number"]]
    consumed = set()
    for k, f in enumerate(frags):
        for r in art_rects:
            if f.bbox[0] >= r[0] - 3 and f.bbox[2] <= r[2] + 3 and \
               f.bbox[1] >= r[1] - 3 and f.bbox[3] <= r[3] + 3:
                consumed.add(k)
                break

    cap_frag_ids = {id(fr) for c in caps for fr in c["frags"]}
    body = [f for k, f in enumerate(frags)
            if k not in consumed and id(f) not in cap_frag_ids]
    notes = note_rules(page, (m0, m1, g0, g1))
    bars = fraction_bars(page, frags, clusters, notes)
    merged = merge_baselines(body, bars)
    _insert_caution_marks(merged, marks)

    items = []
    for cap in caps:
        cap["text"] = _render_frags(cap["frags"])
        cap["art"] = assignment.get(id(cap), [])
        items.append({"type": "caption", "obj": cap, "y": cap["bbox"][1],
                      "bbox": cap["bbox"], "column": cap["column"]})
    for r in leftovers:
        items.append({"type": "artwork", "bbox": r, "y": r[1],
                      "column": _column_of(r, (m0, m1, g0, g1))})

    lines = []
    for f in merged:
        container = _container_of(f, boxes)
        left = container[1][0] + 6 if container else (m0 if f.column == "main" else g0)
        right = container[1][2] - 6 if container else (m1 if f.column == "main" else g1)
        lines.append({
            "frag": f, "container": container[0] if container else None,
            "container_rect": container[1] if container else None,
            "left": left, "right": right,
            "kind": line_kind(f, left, right,
                              container[0] if container else None, wide),
        })
    return {
        "index": i,
        "wide": wide,
        "notes": notes,
        "bars": bars,
        "columns": (m0, m1, g0, g1),
        "lines": lines,
        "items": items,
        "boxes": boxes,
        "icons": marks,
        "clusters": clusters,
    }


def _insert_caution_marks(frags, marks):
    """Put the caution triangle back into the text where it was drawn."""
    for kind, rect in marks:
        if kind != "caution":
            continue
        cx, cy = 0.5 * (rect[0] + rect[2]), 0.5 * (rect[1] + rect[3])
        inside = [f for f in frags
                  if f.bbox[1] - 6 <= cy <= f.bbox[3] + 6
                  and f.bbox[0] - 30 <= cx <= f.bbox[2] + 30]
        if not inside:
            continue
        host = min(inside, key=lambda f: min(abs(f.bbox[0] - cx), abs(f.bbox[2] - cx)))
        mark = Char("\u26a0", rect[0], host.baseline, host.size,
                    "TeXGyrePagellaX-Regular", 0, rect[2] - rect[0])
        at = 0
        while at < len(host.chars) and host.chars[at].x < rect[0]:
            at += 1
        host.chars.insert(at, mark)


def _column_of(rect, geom):
    m0, m1, g0, g1 = geom
    cx = 0.5 * (rect[0] + rect[2])
    if rect[2] - rect[0] > 330:
        return "wide"
    return "main" if abs(cx - 0.5 * (m0 + m1)) < abs(cx - 0.5 * (g0 + g1)) else "margin"


def _container_of(frag, boxes):
    cx = 0.5 * (frag.bbox[0] + frag.bbox[2])
    cy = 0.5 * (frag.bbox[1] + frag.bbox[3])
    for kind, rect in boxes:
        if rect[0] - 4 <= cx <= rect[2] + 4 and rect[1] - 2 <= cy <= rect[3] + 2:
            return kind, rect
    return None


def _render_frags(frags):
    return " ".join(render_line(f.chars) for f in frags)


# --------------------------------------------------------------------------
# paragraph assembly
# --------------------------------------------------------------------------

MAIN_GAP = 15.6
MARGIN_GAP = 12.6


def page_blocks(pg):
    """Group a page's lines into paragraph-level blocks, in reading order."""
    cuts = pg.get("notes") or []
    out = []
    for stream, gap in (("main", MAIN_GAP), ("margin", MARGIN_GAP)):
        sel = [l for l in pg["lines"]
               if (l["frag"].column in ("main", "wide")) == (stream == "main")]
        sel.sort(key=lambda l: l["frag"].baseline)
        cur = None
        for l in sel:
            solo = l["kind"] in ("equation", "section", "subsection",
                                 "chapter-title", "part-title", "part-label")
            limit = gap if l["container"] is None else 16.5
            outdent = (cur is not None and cur["lines"]
                       and l["frag"].bbox[0] < cur["lines"][-1]["frag"].bbox[0] - 6)
            if not outdent and cur is not None and cur["lines"] and any(
                    cur["lines"][-1]["frag"].bbox[3] <= y <= l["frag"].bbox[1] for y in cuts):
                outdent = True
            if not outdent and cur is not None and cur["lines"] \
                    and LIST_NUM_RE.match(l["frag"].raw.lstrip()) \
                    and l["frag"].bbox[0] <= cur["lines"][-1]["frag"].bbox[0] + 4:
                outdent = True
            joinable = (
                cur is not None and not solo and cur["kind"] == "text"
                and cur["container"] == l["container"]
                and l["frag"].baseline - cur["lines"][-1]["frag"].baseline <= limit
                and not outdent
            )
            if joinable:
                cur["lines"].append(l)
                continue
            if cur:
                out.append(cur)
            cur = {"kind": l["kind"], "container": l["container"],
                   "container_rect": l["container_rect"], "stream": stream,
                   "lines": [l]}
            if solo:
                out.append(cur)
                cur = None
        if cur:
            out.append(cur)
    for b in out:
        b["y0"] = min(l["frag"].bbox[1] for l in b["lines"])
        b["note"] = bool(cuts) and b["stream"] == "main" and b["y0"] > min(cuts)
        b["y1"] = max(l["frag"].bbox[3] for l in b["lines"])
        b["x0"] = min(l["frag"].bbox[0] for l in b["lines"])
        b["x1"] = max(l["frag"].bbox[2] for l in b["lines"])
    out.sort(key=lambda b: (b["y0"], 0 if b["stream"] == "main" else 1))
    return out


# --------------------------------------------------------------------------
# whole-document extraction
# --------------------------------------------------------------------------

INLINE_BAR = 12.0


def apply_inline_fractions(frag, bars, raised_only=False):
    """Replace a fraction set inside running text with an inline ``\\frac``."""
    narrow = [b for b in bars
              if b[2] - b[0] < INLINE_BAR
              and (not raised_only or frag.baseline - b[1] > 5.0)
              and frag.bbox[0] - 3 <= b[0] and b[2] <= frag.bbox[2] + 3
              and frag.bbox[1] - 3 <= b[1] <= frag.bbox[3] + 3]
    if not narrow:
        return frag
    chars = frag.chars
    for bar in narrow:
        lo, hi = bar[0] - 1.2, bar[2] + 1.2
        over, under, rest = [], [], []
        for c in chars:
            centre = c.x + (c.w or 0.0) / 2.0
            if c.c.strip() and lo <= centre <= hi and abs(c.y - bar[1]) < 14:
                (over if c.y < bar[1] else under).append(c)
            else:
                rest.append(c)
        if bar[3] == "sqrt":
            if not under:
                continue
            rest = [c for c in rest
                    if not (c.c == "\u221a" and abs(c.x + (c.w or 0.0) - bar[0]) < 4)]
            latex = "$\\sqrt{" + render_math_only(under) + "}$"
        elif not over or not under:
            continue
        else:
            body = "\\frac{" + render_math_only(over) + "}{" + render_math_only(under) + "}"
            raised = frag.baseline - bar[1] > 5.0
            latex = "$^{" + body + "}$" if raised else "$" + body + "$"
        marker = Char(latex, bar[0], frag.baseline, frag.size,
                      "TeXGyrePagellaX-Regular", 0, bar[2] - bar[0])
        rest.append(marker)
        chars = sorted(rest, key=lambda c: c.x)
    return Frag(chars, frag.bbox, frag.column)


def _strip_eq_number(frag, right):
    """Split a trailing, flush-right equation number off a display equation."""
    raw = frag.raw.rstrip()
    m = EQ_TRAIL_RE.search(raw)
    if not m or frag.bbox[2] < right - 34:
        return frag, None
    keep = frag.chars[:]
    tail = len(raw) - m.start()
    dropped = 0
    while keep and dropped < tail:
        keep.pop()
        dropped += 1
    while keep and not keep[-1].c.strip():
        keep.pop()
    if not keep:
        return frag, None
    bbox = (frag.bbox[0], frag.bbox[1], keep[-1].x, frag.bbox[3])
    return Frag(keep, bbox, frag.column), m.group(1)


def block_records(doc, i):
    pg = process_page(doc, i)
    m0, m1, g0, g1 = pg["columns"]
    bars = pg["bars"]
    records = []
    for b in page_blocks(pg):
        right = b["lines"][0]["right"]
        eqnum = None
        texts = []
        for l in b["lines"]:
            frag = l["frag"]
            if b["kind"] == "equation":
                frag, num = _strip_eq_number(frag, right)
                eqnum = eqnum or num
            frag = apply_inline_fractions(frag, bars) if b["kind"] != "equation" else frag
            own = [bar for bar in bars
                   if frag.bbox[0] - 3 <= bar[0] and bar[2] <= frag.bbox[2] + 3
                   and frag.bbox[1] - 3 <= bar[1] <= frag.bbox[3] + 3]
            if own and b["kind"] == "equation":
                lifted = [bar for bar in own
                          if bar[2] - bar[0] < INLINE_BAR and frag.baseline - bar[1] > 5.0]
                if lifted:
                    frag = apply_inline_fractions(frag, lifted, raised_only=True)
                    own = [bar for bar in own if bar not in lifted]
                if own:
                    texts.append("$" + render_fraction_region(frag.chars, own) + "$")
                else:
                    texts.append(render_line(frag.chars, sidenotes=False))
            else:
                texts.append(render_line(
                    frag.chars,
                    sidenotes=(b["kind"] != "equation"),
                    italics=(b["container"] != "definition")))
        records.append({
            "page": i, "kind": b["kind"], "stream": b["stream"],
            "container": b["container"],
            "container_rect": [round(v, 1) for v in b["container_rect"]] if b["container_rect"] else None,
            "lines": texts, "eqnum": eqnum,
            "line_x": [round(l["frag"].bbox[0], 1) for l in b["lines"]],
            "note": b.get("note", False),
            "bbox": [round(b["x0"], 1), round(b["y0"], 1), round(b["x1"], 1), round(b["y1"], 1)],
        })
    for it in pg["items"]:
        if it["type"] == "caption":
            cap = it["obj"]
            records.append({
                "page": i, "kind": "caption", "stream": "main" if cap["column"] != "margin" else "margin",
                "container": None, "container_rect": None,
                "captionkind": cap["kind"], "number": cap["number"],
                "rows": cap.get("rows", []),
                "shared": cap.get("shared"), "slab": cap.get("slab"),
                "lines": [render_line(f.chars, sidenotes=False) for f in cap["frags"]],
                "art": [[round(v, 1) for v in r] for r in cap["art"]],
                "column": cap["column"],
                "bbox": [round(v, 1) for v in cap["bbox"]],
            })
        else:
            records.append({
                "page": i, "kind": "artwork", "stream": "main",
                "container": None, "container_rect": None,
                "art": [[round(v, 1) for v in it["bbox"]]],
                "column": it["column"],
                "bbox": [round(v, 1) for v in it["bbox"]],
            })
    records.sort(key=lambda r: (r["bbox"][1], 0 if r["stream"] == "main" else 1))
    for r in records:
        r["icons"] = [k for k, rect in pg["icons"]
                      if rect[1] >= r["bbox"][1] - 8 and rect[3] <= r["bbox"][3] + 8
                      and rect[0] >= r["bbox"][0] - 22 and rect[2] <= r["bbox"][2] + 22]
    return records


def main():
    doc = pymupdf.open(PDF)
    pages = []
    for i in range(len(doc)):
        try:
            pages.append({"index": i, "blocks": block_records(doc, i)})
        except Exception as exc:                      # pragma: no cover
            print(f"page {i}: {exc}", file=sys.stderr)
            pages.append({"index": i, "blocks": []})
        if i % 40 == 0:
            print(f"  page {i}", file=sys.stderr)
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    with open(os.path.join(ROOT, "build", "document.json"), "w") as fh:
        json.dump({"toc": doc.get_toc(), "pages": pages}, fh)
    print("wrote build/document.json")


if __name__ == "__main__":
    main()
