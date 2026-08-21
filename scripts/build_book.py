"""Assemble the extracted block stream into a MyST Markdown book.

Reads ``build/document.json`` (written by ``extract.py`` and annotated by
``render_figures.py``) and writes ``index.md``, ``front/``, ``chapters/``,
``appendices/``, ``back/`` and the table of contents in ``myst.yml``.
"""

from __future__ import annotations

import json
import os
import re
import sys

import emit
from textutil import (
    build_vocabulary, join_lines, link_references, outside_math, slug,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# book structure: (output path, title, short title, first page, last page)
# page numbers are zero-based indices into the source PDF
# --------------------------------------------------------------------------

CHAPTERS = [
    ("chapters/ch-01-exponential-growth.md", "Exponential Growth", 24, 39),
    ("chapters/ch-02-economic-growth-limits.md", "Economic Growth Limits", 40, 53),
    ("chapters/ch-03-population.md", "Population", 54, 77),
    ("chapters/ch-04-space-colonization.md", "Space Colonization", 78, 91),
    ("chapters/ch-05-energy-and-power-units.md", "Energy and Power Units", 94, 109),
    ("chapters/ch-06-putting-thermal-energy-to-work.md", "Putting Thermal Energy to Work", 110, 127),
    ("chapters/ch-07-the-energy-landscape.md", "The Energy Landscape", 128, 139),
    ("chapters/ch-08-fossil-fuels.md", "Fossil Fuels", 140, 163),
    ("chapters/ch-09-climate-change.md", "Climate Change", 164, 189),
    ("chapters/ch-10-renewable-overview.md", "Renewable Overview", 192, 201),
    ("chapters/ch-11-hydroelectric-energy.md", "Hydroelectric Energy", 202, 213),
    ("chapters/ch-12-wind-energy.md", "Wind Energy", 214, 227),
    ("chapters/ch-13-solar-energy.md", "Solar Energy", 228, 257),
    ("chapters/ch-14-biological-energy.md", "Biological Energy", 258, 269),
    ("chapters/ch-15-nuclear-energy.md", "Nuclear Energy", 270, 305),
    ("chapters/ch-16-small-players.md", "Small Players", 306, 319),
    ("chapters/ch-17-comparison-of-alternatives.md", "Comparison of Alternatives", 320, 333),
    ("chapters/ch-18-human-factors.md", "Human Factors", 336, 347),
    ("chapters/ch-19-a-plan-might-be-welcome.md", "A Plan Might Be Welcome", 348, 359),
    ("chapters/ch-20-adaptation-strategies.md", "Adaptation Strategies", 360, 381),
]

APPENDICES = [
    ("appendices/app-a-math-and-equations.md", "Math and Equations", "A", 392, 407),
    ("appendices/app-b-chemistry-primer.md", "Chemistry Primer/Refresher", "B", 408, 415),
    ("appendices/app-c-selected-answers.md", "Selected Answers", "C", 416, 425),
    ("appendices/app-d-alluring-tangents.md", "Alluring Tangents", "D", 426, 445),
]

EXTRAS = [
    ("front/preface.md", "Preface: Before Taking the Plunge", "Preface", 6, 9),
    ("front/how-to-use-this-book.md", "How to Use This Book", "How to Use", 10, 13),
    ("back/epilogue.md", "Epilogue", "Epilogue", 382, 385),
    ("back/image-attributions.md", "Image Attributions", "Image Attributions", 386, 387),
    ("back/changes-and-corrections.md", "Changes and Corrections", "Changes", 388, 389),
    ("back/bibliography.md", "Bibliography", "Bibliography", 446, 453, "bibliography"),
    ("back/notation.md", "Notation", "Notation", 454, 455),
    ("back/glossary.md", "Glossary", "Glossary", 456, 473, "glossary"),
]

#: editorial framing for the one section that describes the print artefact
PREAMBLES = {
    "front/how-to-use-this-book.md": (
        ":::{note} About this section\n"
        "The author wrote this guide for the printed and PDF editions. Its "
        "description of margins, blue hyperlinks and “back” navigation refers "
        "to those editions; the [home page](../index.md) explains how the same "
        "conventions appear here. Everything it says about the structure of the "
        "book — call-out boxes, examples, appendices, bibliography, glossary — "
        "applies to this edition too.\n"
        ":::"
    ),
}

PARTS = [
    ("Part I — Setting the Stage: Growth and Limitations", 0, 4),
    ("Part II — Energy and Fossil Fuels", 4, 9),
    ("Part III — Alternative Energy", 9, 17),
    ("Part IV — Going Forward", 17, 20),
]

# --------------------------------------------------------------------------
# block grouping
# --------------------------------------------------------------------------


def chapter_blocks(pages, first, last):
    """All blocks of a page range, with paragraphs rejoined across breaks."""
    out = []
    for page in pages[first:last + 1]:
        page_main = [b for b in page["blocks"] if b["stream"] == "main"]
        for k, block in enumerate(page["blocks"]):
            block = dict(block)
            block["first_main"] = page_main and block is not None and \
                page_main[0] is page["blocks"][k]
            block["last_main"] = page_main and page_main[-1] is page["blocks"][k]
            out.append(block)
    return out


def merge_across_pages(blocks, right_edges):
    """Join a paragraph that runs off the bottom of one page onto the next."""
    merged = []
    for block in blocks:
        if merged:
            prev = merged[-1]
            if (prev["kind"] == "text" and block["kind"] == "text"
                    and prev["stream"] == "main" and block["stream"] == "main"
                    and prev["container"] == block["container"]
                    and block["page"] == prev["page"] + 1
                    and prev.get("last_main") and block.get("first_main")
                    and not prev.get("note") and not block.get("note")
                    and prev["bbox"][2] >= right_edges[prev["page"] % 2] - 14
                    and not re.match(r"^\s*(\d{1,3}\.\s|\\?\[\d+\\?\]|[▶•])", block["lines"][0])):
                prev["lines"] = prev["lines"] + block["lines"]
                prev["bbox"] = block["bbox"]
                prev["page"] = block["page"]
                prev["last_main"] = block.get("last_main")
                continue
        merged.append(block)
    return merged


def group_containers(blocks):
    """Collect the runs of blocks that share one shaded call-out box."""
    out = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if b["stream"] == "main" and b["container"] in ("box", "example", "definition"):
            group, asides, j = [b], [], i + 1
            while j < len(blocks):
                nxt = blocks[j]
                if nxt["stream"] == "margin":
                    asides.append(nxt)
                    j += 1
                    continue
                same_box = (nxt["container"] == b["container"]
                            and (nxt["container_rect"] == group[-1]["container_rect"]
                                 or nxt["page"] != group[-1]["page"]))
                if same_box:
                    group.append(nxt)
                    j += 1
                    continue
                break
            out.append(("container", b["container"], group))
            out.extend(("block", a) for a in asides)
            i = j
        else:
            out.append(("block", b))
            i += 1
    return out


# --------------------------------------------------------------------------
# labels
# --------------------------------------------------------------------------


def collect_labels(files):
    known = set()
    for spec in files:
        known.add(spec["label"])
        for entry in spec["items"]:
            if entry[0] == "container":
                head = " ".join(entry[2][0]["lines"][:1])
                for pattern, prefix in (
                    (r"^\*\*Box\s+((?:[A-D]|\d+)\.\d+):", "box"),
                    (r"^\*\*Definition\s+((?:[A-D]|\d+)\.\d+\.\d+)", "def"),
                    (r"^\*\*Example\s+((?:[A-D]|\d+)\.\d+\.\d+)", "ex"),
                ):
                    m = re.match(pattern, head)
                    if m:
                        known.add(slug(prefix, m.group(1)))
                continue
            block = entry[1]
            if block["kind"] == "caption" and block.get("number"):
                known.add(slug("fig" if block["captionkind"] == "figure" else "tab",
                               block["number"]))
            elif block["kind"] == "equation" and block.get("eqnum"):
                known.add(slug("eq", block["eqnum"]))
            elif block["kind"] in ("section", "subsection"):
                m = emit.SECTION_RE.match(" ".join(block["lines"]).strip())
                if m:
                    known.add(slug("sec", m.group(1)))
    return known


# --------------------------------------------------------------------------
# per-file writing
# --------------------------------------------------------------------------

FRONT_MATTER = """---
title: "{title}"
short_title: "{short}"
label: {label}
---
"""


def reconcile_footnotes(w):
    """Make every sidenote marker and every sidenote body agree.

    A raised digit that no margin note claims was never a sidenote marker in
    the first place — it is an exponent, so it is put back as one.  A margin
    note that nothing points at keeps its text as an ordinary aside rather
    than vanishing into an unreferenced footnote definition.
    """
    body = "\n".join(w.out)
    used = set(re.findall(r"\[\^(\d+)\](?!:)", body))
    for num in sorted(used - set(w.footnotes)):
        marker, exponent = f"[^{num}]", f"$^{{{num}}}$"
        w.out = [line.replace(marker, exponent) for line in w.out]
    orphans = sorted(set(w.footnotes) - used, key=lambda n: -w.note_anchors.get(n, 0))
    for num in orphans:
        at = w.note_anchors.get(num)
        text = w.footnotes.pop(num)
        if at is None:
            continue
        w.out[at:at] = [":::{margin}", text, ":::", ""]


def write_body(w, spec):
    for entry in spec["items"]:
        if entry[0] == "container":
            w.container(entry[1], entry[2], None)
            continue
        block = entry[1]
        kind = block["kind"]
        if kind == "caption" and block["captionkind"] == "figure":
            w.figure(block, indent="   " if w.in_problems else "")
        elif kind == "caption":
            w.table(block, indent="   " if w.in_problems else "")
        elif kind == "artwork":
            w.artwork(block, indent="   " if w.in_problems else "")
        elif block["stream"] == "margin":
            w.margin(block)
        elif kind == "section":
            w.heading(block, 2)
        elif kind == "subsection":
            w.heading(block, 3)
        elif kind == "equation":
            w.equation(block, indent="   " if w.in_problems else "")
        elif kind in ("part-title", "part-label", "chapter-title"):
            continue
        else:
            if w.in_problems:
                w.problem(block)
            else:
                w.para(w.text(block["lines"]))


def write_file(spec, known, vocab):
    w = emit.Writer(known, vocab)
    w.emit(FRONT_MATTER.format(title=spec["title"].replace('"', "'"),
                               short=spec["short"].replace('"', "'"),
                               label=spec["label"]))
    if spec.get("hero"):
        w.emit(f":::{{figure}} ../images/{spec['hero']}")
        w.emit(":alt: Chapter opening illustration")
        if spec.get("hero_credit"):
            w.emit()
            w.emit(w.text(spec["hero_credit"]))
        w.emit(":::")
        w.emit()
    w.emit(f"# {spec['heading']}")
    w.emit()
    if spec.get("preamble"):
        w.emit(spec["preamble"])
        w.emit()
    style = spec.get("style", "default")
    if style == "bibliography":
        w.bibliography(spec["items"])
    elif style == "glossary":
        w.glossary(spec["items"])
    else:
        write_body(w, spec)
    reconcile_footnotes(w)
    if w.footnotes:
        w.emit()
        for num in sorted(w.footnotes, key=int):
            w.emit(f"[^{num}]: {w.footnotes[num]}")
        w.emit()
    body = "\n".join(w.out)
    body = re.sub(r"\n{3,}", "\n\n", body)
    path = os.path.join(ROOT, spec["path"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(body.rstrip() + "\n")
    return w


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


DOT_LEADER = re.compile(r"\.\s?\.\s?\.\s?\.")
CREDIT = re.compile(r"(photo|image|graphic)\s+credit", re.I)


def is_chapter_toc(block):
    text = " ".join(block.get("lines", []))
    return block["stream"] == "margin" and bool(DOT_LEADER.search(text))


def hero_image(blocks):
    """The chapter-opening photograph, if the first page carries one."""
    for block in blocks:
        if block["kind"] == "artwork" and block.get("image") and block["bbox"][1] < 60:
            return block
    return None


def build_specs(pages):
    specs = []
    for path, title, first, last in CHAPTERS:
        number = int(re.search(r"ch-(\d+)", path).group(1))
        specs.append({"path": path, "title": f"{number}. {title}",
                      "short": f"Chapter {number}", "label": f"ch-{number}",
                      "heading": f"{number}. {title}", "first": first, "last": last})
    for path, title, letter, first, last in APPENDICES:
        specs.append({"path": path, "title": f"{letter}. {title}",
                      "short": f"Appendix {letter}", "label": f"app-{letter.lower()}",
                      "heading": f"{letter}. {title}", "first": first, "last": last})
    for entry in EXTRAS:
        path, title, short, first, last = entry[:5]
        style = entry[5] if len(entry) > 5 else "default"
        label = re.sub(r"[^a-z0-9]+", "-", os.path.basename(path)[:-3].lower())
        specs.append({"path": path, "title": title, "short": short, "label": label,
                      "heading": title, "first": first, "last": last, "style": style,
                      "preamble": PREAMBLES.get(path)})
    for spec in specs:
        blocks = chapter_blocks(pages, spec["first"], spec["last"])
        blocks = merge_across_pages(blocks, {0: 375.0, 1: 500.0})
        hero = hero_image(blocks)
        if hero:
            spec["hero"] = hero["image"]
            blocks = [b for b in blocks if b is not hero]
            credits = [b for b in blocks
                       if b.get("note") and b["page"] == hero["page"]]
            if credits:
                spec["hero_credit"] = [ln for b in credits for ln in b["lines"]]
                blocks = [x for x in blocks if x not in credits]
        blocks = [b for b in blocks if not is_chapter_toc(b)]
        spec["items"] = group_containers(blocks)
    return specs


def main():
    data = json.load(open(os.path.join(ROOT, "build", "document.json")))
    pages = data["pages"]
    vocab = build_vocabulary(pages)
    specs = build_specs(pages)
    known = collect_labels(specs)
    known |= {f"ref-{n}" for n in range(1, 400)}
    stats = []
    for spec in specs:
        w = write_file(spec, known, vocab)
        stats.append((spec["path"], len(w.out), len(w.footnotes)))
    for path, n, fn in stats:
        print(f"  {path:52s} {n:5d} lines  {fn:3d} notes")
    print(f"wrote {len(specs)} files")


if __name__ == "__main__":
    main()
