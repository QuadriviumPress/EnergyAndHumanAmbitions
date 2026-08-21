"""Shared text helpers for assembling the MyST edition."""

from __future__ import annotations

import collections
import re

# --------------------------------------------------------------------------
# text tidying
# --------------------------------------------------------------------------

MATH_SPLIT = re.compile(r"(\$[^$]*\$)")


def outside_math(text, fn):
    """Apply ``fn`` to the prose of ``text``, leaving maths untouched."""
    return "".join(part if part.startswith("$") and part.endswith("$") else fn(part)
                   for part in MATH_SPLIT.split(text))


def build_vocabulary(pages):
    """Count every word that is not touched by a line break."""
    words = collections.Counter()
    for page in pages:
        for block in page["blocks"]:
            for line in block.get("lines", []):
                plain = outside_math(line, lambda s: s)
                plain = MATH_SPLIT.sub(" ", plain)
                tokens = re.findall(r"[A-Za-z][A-Za-z'’-]*", plain)
                for k, tok in enumerate(tokens):
                    if k == len(tokens) - 1 and plain.rstrip().endswith("-"):
                        continue
                    words[tok.lower()] += 1
    return words


def join_lines(lines, vocab):
    """Glue a paragraph's lines back together, undoing hyphenation."""
    out = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not out:
            out = line
            continue
        m = re.search(r"([A-Za-z’']+)-(\*{1,3})?$", out)
        n = re.match(r"(\*{1,3})?([A-Za-z’']+)", line)
        if m and n:
            left, right = m.group(1), n.group(2)
            marks = len(m.group(2) or "")
            merged = (left + right).lower()
            kept = (left + "-" + right).lower()
            tail = len(n.group(1) or "")
            head = out[: len(out) - marks]
            rest = line[tail:]
            if vocab[kept] > 0 or (vocab[merged] == 0
                                   and vocab[left.lower()] > 2 and vocab[right.lower()] > 2):
                out = head + rest        # a genuine hyphenated compound
            else:
                out = head[:-1] + rest   # TeX broke the word across lines
            continue
        out += " " + line
    return out


# --------------------------------------------------------------------------
# cross references
# --------------------------------------------------------------------------

REFS = [
    (re.compile(r"\b(Figures?|Figs?\.)\s+((?:[A-D]|\d+)\.\d+)"), "fig"),
    (re.compile(r"\b(Tables?)\s+((?:[A-D]|\d+)\.\d+)"), "tab"),
    (re.compile(r"\b(Eqs?\.|Equations?)\s+((?:[A-D]|\d+)\.\d+)"), "eq"),
    (re.compile(r"\b(Boxe?s?)\s+((?:[A-D]|\d+)\.\d+)"), "box"),
    (re.compile(r"\b(Definitions?)\s+((?:[A-D]|\d+)\.\d+\.\d+)"), "def"),
    (re.compile(r"\b(Examples?)\s+((?:[A-D]|\d+)\.\d+\.\d+)"), "ex"),
    (re.compile(r"\b(Sections?|Secs?\.)\s+((?:[A-D]|\d+)\.\d+(?:\.\d+)?)"), "sec"),
    (re.compile(r"\b(Chapters?)\s+(\d+)"), "ch"),
    (re.compile(r"\b(Appendix)\s+([A-D])\b"), "app"),
]

def slug(prefix, number):
    return f"{prefix}-" + str(number).replace(".", "-").lower()


def link_references(text, known):
    def rewrite(chunk):
        for pattern, prefix in REFS:
            def sub(m):
                label = slug(prefix, m.group(2))
                if label not in known:
                    return m.group(0)
                return f"[{m.group(0)}](#{label})"
            chunk = pattern.sub(sub, chunk)
        # bibliography tags
        chunk = re.sub(r"(?<!\^)\[(\d+(?:[,;]\s*\d+)*)\]",
                       lambda m: "[" + ", ".join(
                           f"[{n.strip()}](#ref-{n.strip()})" if f"ref-{n.strip()}" in known
                           else n.strip() for n in re.split(r"[,;]", m.group(1))) + "]",
                       chunk)
        return chunk
    return outside_math(text, rewrite)


