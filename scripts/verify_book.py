"""Structural checks on the generated MyST edition.

Compares the Markdown against the block stream extracted from the PDF, so that
a regression in the conversion pipeline fails loudly rather than quietly losing
a figure, a footnote or a cross-reference.

Run ``python3 scripts/verify_book.py``; a non-zero exit means something broke.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_CHAPTERS = 20
EXPECTED_APPENDICES = 4

problems: list[str] = []


def fail(msg):
    problems.append(msg)


def markdown_files():
    return sorted(glob.glob(os.path.join(ROOT, d, "*.md"))
                  for d in ("chapters", "appendices", "front", "back"))


def all_files():
    out = []
    for group in markdown_files():
        out.extend(group)
    out.append(os.path.join(ROOT, "index.md"))
    return out


def read(path):
    with open(path) as fh:
        return fh.read()


def main():
    chapters = sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md")))
    appendices = sorted(glob.glob(os.path.join(ROOT, "appendices", "*.md")))
    if len(chapters) != EXPECTED_CHAPTERS:
        fail(f"expected {EXPECTED_CHAPTERS} chapters, found {len(chapters)}")
    if len(appendices) != EXPECTED_APPENDICES:
        fail(f"expected {EXPECTED_APPENDICES} appendices, found {len(appendices)}")

    texts = {p: read(p) for p in all_files()}
    corpus = "\n".join(texts.values())

    # ---- labels and references ------------------------------------------
    labels = set(re.findall(r"^:label:\s*(\S+)", corpus, re.M))
    labels |= set(re.findall(r"^\((\S+?)\)=", corpus, re.M))
    labels |= set(re.findall(r"^label:\s*(\S+)", corpus, re.M))
    targets = set(re.findall(r"\]\(#([A-Za-z0-9_.-]+)\)", corpus))
    missing = sorted(targets - labels)
    if missing:
        fail(f"{len(missing)} cross-references without a target, e.g. {missing[:8]}")

    # ---- footnotes -------------------------------------------------------
    for path, text in texts.items():
        used = set(re.findall(r"\[\^(\d+)\](?!:)", text))
        defined = set(re.findall(r"^\[\^(\d+)\]:", text, re.M))
        if used - defined:
            fail(f"{os.path.basename(path)}: footnote markers without a definition: "
                 f"{sorted(used - defined)[:6]}")
        if defined - used:
            fail(f"{os.path.basename(path)}: footnote definitions never referenced: "
                 f"{sorted(defined - used)[:6]}")

    # ---- images ----------------------------------------------------------
    referenced = set(re.findall(r"^:::+\{figure\}\s+\.\./images/(\S+)", corpus, re.M))
    for name in sorted(referenced):
        if not os.path.exists(os.path.join(ROOT, "images", name)):
            fail(f"missing image file: images/{name}")

    # ---- coverage against the source extraction -------------------------
    doc_path = os.path.join(ROOT, "build", "document.json")
    if os.path.exists(doc_path):
        with open(doc_path) as fh:
            data = json.load(fh)
        figures = {b["number"] for p in data["pages"] for b in p["blocks"]
                   if b.get("captionkind") == "figure" and b.get("number")}
        tables = {b["number"] for p in data["pages"] for b in p["blocks"]
                  if b.get("captionkind") == "table" and b.get("number")}
        equations = {b["eqnum"] for p in data["pages"] for b in p["blocks"]
                     if b.get("eqnum")}
        for kind, numbers, prefix in (("figure", figures, "fig"),
                                      ("table", tables, "tab"),
                                      ("equation", equations, "eq")):
            want = {prefix + "-" + n.replace(".", "-").lower() for n in numbers}
            lost = sorted(want - labels)
            if lost:
                fail(f"{len(lost)} {kind}s extracted but not emitted, e.g. {lost[:6]}")
    else:
        print("note: build/document.json absent, skipping coverage checks "
              "(run scripts/extract.py against the source PDF to enable them)")

    # ---- conversion artifacts -------------------------------------------
    artifacts = [
        (r"\u0001", "unresolved bullet sentinel"),
        (r"\u0002", "unresolved typewriter marker"),
        (r"\$\s*\$", "empty maths run"),
        (r"[a-z]- [a-z]{2,}", "hyphenation left un-joined"),
        (r"\\mathrm\{[A-Za-z]{9,}\}", "prose captured inside maths"),
        # stacked-fraction / multi-baseline merge: adjacent lines zipped by x
        (r"\\frac\{\$", "nested maths inside \\frac"),
        (r"(?:\*[A-Za-z0-9]\*){3,}", "single-letter italic scramble"),
    ]
    for path, text in texts.items():
        for pattern, label in artifacts:
            hits = re.findall(pattern, text)
            # zero tolerance for zip/scramble; others allow a few stragglers
            limit = 0 if label in (
                "nested maths inside \\frac",
                "single-letter italic scramble",
            ) else 6
            if len(hits) > limit:
                fail(f"{os.path.basename(path)}: {len(hits)} instances of {label}")

    # ---- directive fences ------------------------------------------------
    for path, text in texts.items():
        depth = {3: 0, 4: 0}
        for line in text.splitlines():
            t = line.strip()
            if re.match(r"^::::(\{|$)", t):
                depth[4] += 1 if t.startswith("::::{") else -1
            elif re.match(r"^:::(\{|$)", t):
                depth[3] += 1 if t.startswith(":::{") else -1
        if depth[3] or depth[4]:
            fail(f"{os.path.basename(path)}: unbalanced directive fences {depth}")

    if problems:
        print("verification failed:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"ok: {len(chapters)} chapters, {len(appendices)} appendices, "
          f"{len(labels)} labels, {len(referenced)} images")
    return 0


if __name__ == "__main__":
    sys.exit(main())
