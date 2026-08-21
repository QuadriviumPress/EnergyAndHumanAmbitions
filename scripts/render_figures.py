"""Cut every figure out of the source PDF and write it to ``images/``.

Nearly all of the book's artwork is vector, so figures are exported as SVG by
re-rendering a cropped one-page PDF through ``mutool``.  The handful of blocks
that are really a single photograph (the chapter openers) are written out as
JPEG instead, at their native resolution.

Run ``python3 scripts/render_figures.py`` after ``extract.py``.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile

import pymupdf
from PIL import Image, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "220222_2.pdf")
IMAGES = os.path.join(ROOT, "images")

PAD = 2.0
TRIM_DPI = 72
#: past this size an SVG's path soup is bigger than a good raster of it
SVG_BUDGET = 600_000
RASTER_DPI = 220
#: chapter-opener photographs come at print resolution; the web needs less
MAX_PHOTO_WIDTH = 1600


def union(rects):
    return (min(r[0] for r in rects), min(r[1] for r in rects),
            max(r[2] for r in rects), max(r[3] for r in rects))


def trim(page, rect):
    """Shrink a rectangle to the ink it actually contains."""
    clip = pymupdf.Rect(*rect)
    if clip.width < 4 or clip.height < 4:
        return rect
    pix = page.get_pixmap(dpi=TRIM_DPI, clip=clip)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    bg = Image.new("RGB", img.size, (255, 255, 255))
    box = ImageChops.difference(img, bg).convert("L").point(lambda v: 255 if v > 6 else 0).getbbox()
    if box is None:
        return rect
    sx = clip.width / pix.width
    sy = clip.height / pix.height
    return (clip.x0 + box[0] * sx - PAD, clip.y0 + box[1] * sy - PAD,
            clip.x0 + box[2] * sx + PAD, clip.y0 + box[3] * sy + PAD)


def dominant_image(page, rect):
    """Return an embedded raster that fills the rectangle, if there is one."""
    area = (rect[2] - rect[0]) * (rect[3] - rect[1])
    for info in page.get_images(full=True):
        xref = info[0]
        for bbox in page.get_image_rects(xref):
            inter = (max(bbox.x0, rect[0]), max(bbox.y0, rect[1]),
                     min(bbox.x1, rect[2]), min(bbox.y1, rect[3]))
            if inter[2] <= inter[0] or inter[3] <= inter[1]:
                continue
            covered = (inter[2] - inter[0]) * (inter[3] - inter[1])
            if covered > 0.9 * area and bbox.width * bbox.height > 0.75 * area:
                return xref
    return None


def write_svg(doc, pno, rect, path):
    clip = pymupdf.Rect(*rect)
    out = pymupdf.open()
    page = out.new_page(width=clip.width, height=clip.height)
    page.show_pdf_page(pymupdf.Rect(0, 0, clip.width, clip.height), doc, pno, clip=clip)
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as fh:
        tmp = fh.name
    out.save(tmp)
    out.close()
    try:
        svg = subprocess.run(["mutool", "draw", "-F", "svg", "-o", "-", tmp],
                             check=True, capture_output=True).stdout.decode()
    finally:
        os.unlink(tmp)
    svg = _add_backdrop(svg, clip.width, clip.height)
    with open(path, "w") as fh:
        fh.write(svg)


def _add_backdrop(svg, width, height):
    """Paint the artwork onto white so it stays legible on a dark page."""
    rect = (f'<rect x="0" y="0" width="{width:.2f}" height="{height:.2f}" '
            f'fill="#ffffff"/>')
    m = re.search(r"<svg[^>]*>", svg)
    if not m:
        return svg
    return svg[:m.end()] + "\n" + rect + svg[m.end():]


def write_raster(doc, xref, path_base):
    """Write an embedded photograph, downsampled to a web-sensible width."""
    info = doc.extract_image(xref)
    with tempfile.NamedTemporaryFile(suffix="." + info["ext"], delete=False) as fh:
        fh.write(info["image"])
        tmp = fh.name
    try:
        img = Image.open(tmp)
        img.load()
    finally:
        os.unlink(tmp)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    if img.width > MAX_PHOTO_WIDTH:
        height = round(img.height * MAX_PHOTO_WIDTH / img.width)
        img = img.resize((MAX_PHOTO_WIDTH, height), Image.LANCZOS)
    path = path_base + ".jpg"
    img.save(path, "JPEG", quality=82, optimize=True, progressive=True)
    return os.path.basename(path)


def write_png(page, rect, path):
    page.get_pixmap(dpi=RASTER_DPI, clip=pymupdf.Rect(*rect)).save(path)


def slab_of(page, shared, rank, count):
    """Cut a shared artwork block into ``count`` slabs along its blank rows."""
    clip = pymupdf.Rect(*shared)
    pix = page.get_pixmap(dpi=90, clip=clip)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
    rows = [min(img.crop((0, y, img.width, y + 1)).getdata()) for y in range(img.height)]
    blank = [y for y, v in enumerate(rows) if v > 248]
    gaps, run = [], []
    for y in blank:
        if run and y == run[-1] + 1:
            run.append(y)
        else:
            if len(run) > 3:
                gaps.append((run[0], run[-1]))
            run = [y]
    if len(run) > 3:
        gaps.append((run[0], run[-1]))
    inner = [g for g in gaps if g[0] > 2 and g[1] < img.height - 3]
    inner.sort(key=lambda g: g[0] - g[1])          # widest first
    cuts = sorted(0.5 * (g[0] + g[1]) for g in inner[:count - 1])
    if len(cuts) < count - 1:
        step = img.height / count
        cuts = [step * (k + 1) for k in range(count - 1)]
    edges = [0.0] + cuts + [float(img.height)]
    scale = clip.height / img.height
    return (clip.x0, clip.y0 + edges[rank] * scale,
            clip.x1, clip.y0 + edges[rank + 1] * scale)


def _clear_of_captions(rect, captions):
    """Trim a rectangle back so it cannot swallow a neighbouring caption."""
    x0, y0, x1, y1 = rect
    for c in captions:
        if c[3] <= y0 + 2 or c[1] >= y1 - 2:
            continue                       # no vertical overlap
        if c[2] > x0 and c[0] <= x0 + 2:
            x0 = max(x0, c[2] + 2)
        elif c[0] < x1 and c[2] >= x1 - 2:
            x1 = min(x1, c[0] - 2)
    return (x0, y0, x1, y1) if x1 - x0 > 20 else rect


def main():
    doc = pymupdf.open(PDF)
    data = json.load(open(os.path.join(ROOT, "build", "document.json")))
    os.makedirs(IMAGES, exist_ok=True)
    manifest = {}
    counters = {}
    for page in data["pages"]:
        pno = page["index"]
        pg = doc[pno]
        captions = [tuple(b["bbox"]) for b in page["blocks"] if b["kind"] == "caption"]
        for block in page["blocks"]:
            if block["kind"] == "caption" and block["captionkind"] == "figure" \
                    and block.get("number"):
                name = "fig-" + block["number"].replace(".", "-").lower()
            elif block["kind"] == "artwork":
                counters[pno] = counters.get(pno, 0) + 1
                name = f"art-p{pno:03d}-{counters[pno]}"
            else:
                continue
            rects = [tuple(r) for r in block["art"]]
            if not rects:
                continue
            if block.get("shared") and block.get("slab"):
                rect = slab_of(pg, block["shared"], *block["slab"])
            else:
                rect = union(rects)
            rect = (max(rect[0], 14.0), max(rect[1], 30.0),
                    min(rect[2], 542.0), min(rect[3], 700.0))
            rect = _clear_of_captions(rect, captions)
            rect = trim(pg, rect)
            rect = _clear_of_captions(rect, captions)
            xref = dominant_image(pg, rect)
            base = os.path.join(IMAGES, name)
            if xref:
                fname = write_raster(doc, xref, base)
            else:
                write_svg(doc, pno, rect, base + ".svg")
                fname = name + ".svg"
                if os.path.getsize(base + ".svg") > SVG_BUDGET:
                    os.unlink(base + ".svg")
                    write_png(pg, rect, base + ".png")
                    fname = name + ".png"
            manifest.setdefault(str(pno), {})[block.get("number", name)] = fname
            block["image"] = fname
        print(f"\rpage {pno}", end="", file=sys.stderr)
    with open(os.path.join(ROOT, "build", "document.json"), "w") as fh:
        json.dump(data, fh)
    print(f"\nwrote {sum(len(v) for v in manifest.values())} images to images/")


if __name__ == "__main__":
    main()
