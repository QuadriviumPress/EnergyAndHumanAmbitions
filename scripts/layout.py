"""Layout-aware reading of the source PDF.

The book is set with a ``tufte``-style two-column geometry: a wide *main* text
column and a narrow *margin* column holding sidenotes, small figures and
tables.  Which side the margin sits on alternates with page parity, and
PyMuPDF's own block segmentation happily merges the two columns into a single
block, so the columns have to be separated by hand before any text is
assembled.

Everything here works at the level of PyMuPDF *lines*: lines never straddle the
gutter, while blocks routinely do.  A single visual line of body text is often
broken into several PyMuPDF lines (a sidenote interrupting the baseline, an
equation number set flush right, a superscript sitting in its own fragment), so
fragments sharing a baseline are re-joined afterwards.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import pymupdf

from mathtext import FLAT_FONTS, font_class

# --------------------------------------------------------------------------
# page geometry (points; page is 554.17 x 715.04)
# --------------------------------------------------------------------------

HEADER_Y = 42.0        # running heads live above this
FOOTER_Y = 688.0       # copyright/URL lines live below this
LEADING = 12.8         # body-text baseline separation
PARA_GAP = 15.6        # baseline separation that implies a new paragraph

# (main_x0, main_x1, margin_x0, margin_x1) keyed by ``page_index % 2``
COLUMNS = {
    0: (60.0, 375.0, 375.0, 540.0),    # margin on the right
    1: (180.0, 500.0, 14.0, 180.0),    # margin on the left
}

# heading sizes, largest first
SIZE_PART = 24.0
SIZE_PART_LABEL = 18.6
SIZE_CHAPTER = 20.0
SIZE_SECTION = 13.9
SIZE_SUBSECTION = 11.6
SIZE_BODY = 9.8
SIZE_MARGIN = 7.8

# fill colours of the shaded call-out rectangles
BOX_COLORS = {
    (0.83, 0.87, 0.95): "box",
    (1.0, 0.95, 0.75): "example",
    (0.99, 0.88, 0.93): "definition",
    (0.8, 1.0, 0.8): "explore",
}


def columns_for(page_index: int):
    return COLUMNS[page_index % 2]


# --------------------------------------------------------------------------
# data model
# --------------------------------------------------------------------------


@dataclass
class Char:
    c: str
    x: float
    y: float          # baseline origin
    size: float
    font: str
    color: int = 0
    w: float = 0.0    # advance width, used to spot missing inter-word spaces


@dataclass
class Frag:
    chars: list
    bbox: tuple
    column: str

    @property
    def baseline(self):
        """Baseline of the full-size text, ignoring scripts and delimiters."""
        vis = [c for c in self.chars if c.c.strip() and c.font not in FLAT_FONTS]
        if not vis:
            vis = [c for c in self.chars if c.c.strip()]
        if not vis:
            return round(self.chars[0].y, 1)
        top = max(c.size for c in vis)
        counts = {}
        for ch in vis:
            if ch.size >= top - 0.7:
                counts[round(ch.y, 1)] = counts.get(round(ch.y, 1), 0) + 1
        return max(counts.items(), key=lambda kv: kv[1])[0]

    @property
    def is_delimiter(self):
        return all(c.font in FLAT_FONTS for c in self.chars if c.c.strip())

    @property
    def size(self):
        vis = [round(c.size, 1) for c in self.chars if c.c.strip()]
        if not vis:
            return SIZE_BODY
        counts = {}
        for v in vis:
            counts[v] = counts.get(v, 0) + 1
        return max(counts.items(), key=lambda kv: (kv[1], v))[0]

    @property
    def maxsize(self):
        vis = [c.size for c in self.chars if c.c.strip()]
        return max(vis) if vis else SIZE_BODY

    @property
    def raw(self):
        return "".join(c.c for c in self.chars)

    @property
    def fonts(self):
        return {c.font for c in self.chars if c.c.strip()}


def _classify_column(x0, x1, geom):
    m0, m1, g0, g1 = geom
    in_main = x0 >= m0 - 6 and x1 <= m1 + 10
    in_margin = x0 >= g0 - 6 and x1 <= g1 + 10
    if in_main and not in_margin:
        return "main"
    if in_margin and not in_main:
        return "margin"
    if in_main and in_margin:
        return "main" if abs(x0 - m0) < abs(x0 - g0) else "margin"
    return "wide"


#: geometry of the back-matter pages, which run the full measure
WIDE_COLUMNS = (60.0, 502.0, 506.0, 545.0)


def page_frags(page, page_index, wide=False):
    geom = WIDE_COLUMNS if wide else columns_for(page_index)
    out = []
    for block in page.get_text("rawdict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            chars = []
            for span in line["spans"]:
                for ch in span["chars"]:
                    if ch["c"] == "�":
                        continue
                    chars.append(Char(ch["c"], ch["origin"][0], ch["origin"][1],
                                      span["size"], span["font"], span.get("color", 0),
                                      ch["bbox"][2] - ch["bbox"][0]))
            if not chars:
                continue
            bbox = tuple(line["bbox"])
            if bbox[3] < HEADER_Y or bbox[1] > FOOTER_Y:
                continue
            chars.sort(key=lambda c: c.x)
            out.append(Frag(chars, bbox, _classify_column(bbox[0], bbox[2], geom)))
    out.sort(key=lambda f: (f.bbox[1], f.bbox[0]))
    return out


# --------------------------------------------------------------------------
# shaded call-out rectangles
# --------------------------------------------------------------------------


def shaded_boxes(page):
    """Rectangles that mark Boxes, Examples, Definitions and margin call-outs."""
    found = []
    for dr in page.get_drawings():
        fill = dr.get("fill")
        if fill is None:
            continue
        key = tuple(round(v, 2) for v in fill)
        kind = BOX_COLORS.get(key)
        if kind is None:
            continue
        r = dr["rect"]
        if r.width < 100 or r.height < 14:
            continue
        found.append((kind, (r.x0, r.y0, r.x1, r.y1)))
    # a box is drawn as a body rectangle plus a title strip; keep the largest
    merged = []
    for kind, rect in sorted(found, key=lambda kr: -(kr[1][3] - kr[1][1])):
        if any(k == kind and rect[0] >= m[0] - 2 and rect[2] <= m[2] + 2
               and rect[1] >= m[1] - 2 and rect[3] <= m[3] + 2 for k, m in merged):
            continue
        merged.append((kind, rect))
    return merged


# --------------------------------------------------------------------------
# figure artwork
# --------------------------------------------------------------------------

CAPTION_RE = re.compile(r"^(Figure|Table)\s+((?:[A-D]|\d+)\.\d+):")


def _inflate(r, d):
    return (r[0] - d, r[1] - d, r[2] + d, r[3] + d)


def _overlap(a, b):
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])


def _union(a, b):
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


#: fills used by the margin's information and caution symbols
ICON_FILLS = {(0.93, 0.11, 0.14), (0.08, 0.46, 0.74), (0.34, 0.69, 0.89),
              (0.18, 0.19, 0.57), (0.73, 0.73, 1.0)}


def artwork_clusters(page, boxes, pad=9, frags=()):
    """Cluster the page's vector drawings and images into figure candidates."""
    box_rects = [r for _, r in boxes]
    text_rects = [f.bbox for f in frags
                  if any(font_class(c.font) == "text" for c in f.chars if c.c.strip())]
    rects = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.is_empty or r.is_infinite:
            continue
        rect = (r.x0, r.y0, r.x1, r.y1)
        if rect[3] < HEADER_Y + 4 or rect[1] > FOOTER_Y:
            continue
        if rect[2] - rect[0] > 520 and rect[3] - rect[1] > 620:
            continue
        # box backgrounds, their title strips and their rules are not artwork
        if any(rect[0] >= b[0] - 2 and rect[2] <= b[2] + 2
               and rect[1] >= b[1] - 2 and rect[3] <= b[3] + 2 for b in box_rects):
            continue
        stroke = dr.get("color")
        if stroke is not None and tuple(round(v, 2) for v in stroke) == (0.8, 0.76, 0.48):
            continue                     # the bracket linking a margin call-out
        if rect[2] - rect[0] <= 17 and rect[3] - rect[1] <= 17:
            fill = dr.get("fill")
            if fill is not None and tuple(round(v, 2) for v in fill) in ICON_FILLS:
                continue                 # a margin information/caution symbol
        # hyperlink and glossary underlines are drawings too
        if rect[3] - rect[1] <= 3.0 and any(
                rect[0] >= t[0] - 3 and rect[2] <= t[2] + 3
                and rect[1] >= t[1] - 3 and rect[3] <= t[3] + 4 for t in text_rects):
            continue
        rects.append(rect)
    for block in page.get_text("dict")["blocks"]:
        if block["type"] == 1:
            rects.append(tuple(block["bbox"]))
    # union-find style agglomeration
    clusters = []
    for rect in rects:
        hit = [c for c in clusters if _overlap(_inflate(rect, pad), _inflate(c, pad))]
        for c in hit:
            clusters.remove(c)
            rect = _union(rect, c)
        clusters.append(rect)
    changed = True
    while changed:
        changed = False
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if _overlap(_inflate(clusters[i], pad), _inflate(clusters[j], pad)):
                    clusters[i] = _union(clusters[i], clusters[j])
                    del clusters[j]
                    changed = True
                    break
            if changed:
                break
    return clusters


def attach_figure_text(clusters, frags, pad=9):
    """Grow clusters over the text that belongs to the artwork."""
    out = list(clusters)
    changed = True
    while changed:
        changed = False
        for f in frags:
            if all(font_class(c.font) != "figure" for c in f.chars if c.c.strip()):
                continue
            for i, c in enumerate(out):
                if _overlap(_inflate(f.bbox, pad + 3), _inflate(c, pad + 3)):
                    new = _union(c, f.bbox)
                    if new != c:
                        out[i] = new
                        changed = True
                    break
            else:
                out.append(f.bbox)
                changed = True
    # merge again after growth
    changed = True
    while changed:
        changed = False
        for i in range(len(out)):
            for j in range(i + 1, len(out)):
                if _overlap(_inflate(out[i], pad - 3), _inflate(out[j], pad - 3)):
                    out[i] = _union(out[i], out[j])
                    del out[j]
                    changed = True
                    break
            if changed:
                break
    return [c for c in out if (c[2] - c[0]) * (c[3] - c[1]) > 400]
