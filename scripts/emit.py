"""Markdown emission for :mod:`build_book`."""

from __future__ import annotations

import re

from textutil import join_lines, link_references, slug

BULLET_TOKEN = "\u0001BULLET\u0001"
MONO_MARK = "\u0002"
NBSP = "\u00a0"

SECTION_RE = re.compile(r"^\*{0,2}((?:[A-D]|\d+)(?:\.\d+){1,2})\s+(.*?)\*{0,2}$")
BOX_TITLE = re.compile(r"^\*\*Box\s+((?:[A-D]|\d+)\.\d+):\s*(.*?)\*\*\s*")
DEF_HEAD = re.compile(r"^\*\*Definition\s+((?:[A-D]|\d+)\.\d+\.\d+)\s*(.*?)\*\*\s*:?\s*")
EX_HEAD = re.compile(r"^\*\*Example\s+((?:[A-D]|\d+)\.\d+\.\d+)\s*(.*?)\*\*\s*:?\s*")
CAP_PREFIX = re.compile(r"^\*\*(Figure|Table)\s+((?:[A-D]|\d+)\.\d+):\*\*\s*")
MARGIN_NOTE = re.compile(r"^(\d{1,3}):\s*")
PROBLEM_ITEM = re.compile(r"^(\d{1,3})\.\s+")


def _mono_run(text):
    """Collapse a typewriter run: URLs lose the spaces justification added."""
    lead = " " if text[:1].isspace() else ""
    trail = " " if text[-1:].isspace() else ""
    body = re.sub(r"\s+", "", text)
    if not body:
        return lead or trail
    if re.match(r"^https?://", body):
        inner = f"<{body}>"
    elif re.match(r"^10\.\d{4,}/", body):
        inner = f"[{body}](https://doi.org/{body})"
    else:
        inner = f"`{body}`"
    return lead + inner + trail


def clean(text):
    text = text.replace(NBSP, " ")
    text = re.sub(MONO_MARK + r"\s*" + MONO_MARK, "", text)
    text = re.sub(MONO_MARK + r"([^" + MONO_MARK + r"]*)" + MONO_MARK,
                  lambda m: _mono_run(m.group(1)), text)
    text = text.replace(MONO_MARK, "")
    text = text.replace("****", "")
    text = re.sub(r"(?<!\\)\$\$", "", text)   # weld adjacent inline maths runs
    text = re.sub(r"(?<!\\)\$ \$", " ", text)
    text = re.sub(r"\*\*\s+\*\*", " ", text)
    text = re.sub(r"(?<!\*)\*\s+\*(?!\*)", " ", text)
    text = re.sub(r"\.\s\.\s\.(\s|$)", "\u2026\\1", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def container_head(container, head):
    """Split a call-out's opening line into (title, label, class, remainder)."""
    if container == "box":
        m = BOX_TITLE.match(head)
        if m:
            return (f"Box {m.group(1)}: {m.group(2)}", slug("box", m.group(1)),
                    "tip", head[m.end():])
        return ("Box", None, "tip", head)
    if container == "definition":
        m = DEF_HEAD.match(head)
        if m:
            title = f"Definition {m.group(1)}"
            term = m.group(2).strip().strip(":").strip()
            if term:
                title += f" — {term}"
            return (title, slug("def", m.group(1)), "important", head[m.end():])
        return ("Definition", None, "important", head)
    m = EX_HEAD.match(head)
    if m:
        extra = m.group(2).strip().strip(":").strip()
        title = f"Example {m.group(1)}"
        if extra:
            title += f" — {extra}"
        rest = head[m.end():].lstrip(": ")
        return (title, slug("ex", m.group(1)), "seealso", rest)
    return ("Example", None, "seealso", head)


class Writer:
    """Accumulates the Markdown for one output file."""

    def __init__(self, known, vocab):
        self.known = known
        self.vocab = vocab
        self.out = []
        self.footnotes = {}
        self.in_problems = False
        self.used = set()
        self.note_anchors = {}

    # -- helpers ---------------------------------------------------------
    def text(self, lines):
        return clean(join_lines(lines, self.vocab))

    def emit(self, s=""):
        self.out.append(s)

    def label(self, name):
        if not name or name in self.used:
            return None
        self.used.add(name)
        return name

    def para(self, text, indent=""):
        text = link_references(text, self.known)
        chunks = [c.strip() for c in text.split(BULLET_TOKEN)]
        lead, items = chunks[0], [c for c in chunks[1:] if c]
        if lead:
            self.emit(indent + lead)
            self.emit()
        for item in items:
            wrapped = ("\n" + indent + "  ").join(item.split("\n"))
            self.emit(indent + "- " + wrapped)
        if items:
            self.emit()

    # -- block kinds -----------------------------------------------------
    def heading(self, block, depth):
        raw = self.text(block["lines"]).strip("*").strip()
        m = SECTION_RE.match(raw)
        if m:
            number, title = m.group(1), m.group(2).strip("*").strip()
            name = self.label(slug("sec", number))
            if name:
                self.emit(f"({name})=")
            self.emit(f"{'#' * depth} {number} {title}")
            self.in_problems = title.lower().startswith("problem")
        else:
            self.emit(f"{'#' * depth} {raw}")
            self.in_problems = raw.lower().startswith("problem")
        self.emit()

    def equation(self, block, indent=""):
        body = " ".join(block["lines"]).strip()
        body = re.sub(r"^\$|\$$", "", body).strip()
        body = re.sub(r"\s+", " ", body.replace("$", " ")).strip()
        name = self.label(slug("eq", block["eqnum"])) if block.get("eqnum") else None
        pad = indent
        self.emit(pad + ":::{math}")
        if name:
            self.emit(pad + f":label: {name}")
            self.emit(pad + f":enumerator: {block['eqnum']}")
        self.emit(pad + body)
        self.emit(pad + ":::")
        self.emit()

    def figure(self, block, indent=""):
        caption = self.text(block["lines"])
        m = CAP_PREFIX.match(caption)
        caption = caption[m.end():] if m else caption
        caption = link_references(caption, self.known)
        name = self.label(slug("fig", block["number"]))
        image = block.get("image")
        if not image:
            return
        self.emit(indent + f":::{{figure}} ../images/{image}")
        if name:
            self.emit(indent + f":label: {name}")
            self.emit(indent + f":enumerator: {block['number']}")
        self.emit(indent + f":alt: {_alt_text(caption)}")
        self.emit(indent)
        self.emit(indent + caption)
        self.emit(indent + ":::")
        self.emit()

    def artwork(self, block, indent=""):
        image = block.get("image")
        if not image:
            return
        self.emit(indent + f":::{{figure}} ../images/{image}")
        self.emit(indent + ":alt: Illustration from the original text")
        self.emit(indent + ":::")
        self.emit()

    def table(self, block, indent=""):
        rows = block.get("rows") or []
        if not block.get("number"):
            self._table_body(rows, indent)
            return
        caption = self.text(block["lines"])
        m = CAP_PREFIX.match(caption)
        caption = caption[m.end():] if m else caption
        caption = link_references(caption, self.known)
        name = self.label(slug("tab", block["number"]))
        self.emit(indent + ":::{table} " + caption)
        if name:
            self.emit(indent + f":label: {name}")
            self.emit(indent + f":enumerator: {block['number']}")
        self.emit(indent)
        self._table_body(rows, indent, fenced=False)
        self.emit(indent + ":::")
        self.emit()

    def _table_body(self, rows, indent="", fenced=True):
        if rows:
            width = max(len(r["cells"]) for r in rows)
            head = [r for r in rows if r["header"]]
            body = [r for r in rows if not r["header"]]
            if not head:
                head, body = rows[:1], rows[1:]
            merged = [""] * width
            for r in head:
                for k, cell in enumerate(r["cells"]):
                    if cell:
                        merged[k] = (merged[k] + " " + cell).strip()
            self.emit(indent + "| " + " | ".join(_cell(c) for c in merged) + " |")
            self.emit(indent + "|" + "|".join([" --- "] * width) + "|")
            for r in body:
                cells = r["cells"] + [""] * (width - len(r["cells"]))
                self.emit(indent + "| " + " | ".join(_cell(c) for c in cells) + " |")
        if fenced:
            self.emit()

    def container(self, kind, group, page_width_right):
        head = clean(" ".join(group[0]["lines"][:1]))
        title, name, cls, remainder = container_head(kind, head)
        # four colons, because the body may hold its own ::: directives
        self.emit(f"::::{{admonition}} {title}")
        self.emit(f":class: {cls}")
        name = self.label(name)
        if name:
            self.emit(f":label: {name}")
        self.emit()
        first = True
        for block in group:
            lines = block["lines"][:]
            if first:
                lines = [remainder] + lines[1:] if remainder else lines[1:]
                first = False
            if block["kind"] == "equation":
                self.equation(block)
                continue
            body = self.text(lines)
            if body:
                self.para(body)
        self.emit("::::")
        self.emit()

    def margin(self, block):
        body = self.text(block["lines"])
        symbols = set(block.get("symbols") or []) | set(block.get("icons") or [])
        lead = ""
        while body[:1] in ("\u26a0", "\u24d8"):
            lead += body[0]
            body = body[1:].lstrip()
        m = MARGIN_NOTE.match(body)
        if m:
            note = (lead + " " if lead else "") + body[m.end():]
            self.footnotes[m.group(1)] = link_references(note, self.known)
            self.note_anchors[m.group(1)] = len(self.out)
            return
        if not body:
            return
        prefix = "**Try it:** " if block["container"] == "explore" else ""
        body = (lead + " " + body).strip() if lead else body
        self.emit(":::{margin}")
        self.para(prefix + body)
        self.emit(":::")
        self.emit()

    def problem(self, block):
        body = self.text(block["lines"])
        m = PROBLEM_ITEM.match(body)
        if not m:
            self.para(body, indent="   ")
            return
        rest = link_references(body[m.end():], self.known)
        rest = rest.replace(BULLET_TOKEN, "\n   - ")
        self.emit(f"{m.group(1)}. {rest}")
        self.emit()


_MATH_SYMBOLS = {
    r"\times": "×", r"\cdot": "·", r"\approx": "≈", r"\sim": "~",
    r"\pm": "±", r"\circ": "°", r"\rightarrow": "→", r"\leftarrow": "←",
    r"\ldots": "…", r"\odot": "Sun", r"\oplus": "Earth", r"\%": "%",
    r"\pi": "π", r"\alpha": "alpha", r"\beta": "beta", r"\gamma": "gamma",
    r"\delta": "delta", r"\Delta": "Delta", r"\epsilon": "epsilon",
    r"\theta": "theta", r"\lambda": "lambda", r"\mu": "mu", r"\nu": "nu",
    r"\rho": "rho", r"\sigma": "sigma", r"\Sigma": "Sigma", r"\phi": "phi",
    r"\omega": "omega", r"\infty": "infinity",
}


def _sup_repl(m):
    c = m.group(1)
    return c if len(c) == 1 and not c.isalnum() else "^" + c


def _math_to_text(expr):
    """Render a snippet of inline LaTeX math as plain text, for alt text."""
    s = expr
    for k, v in _MATH_SYMBOLS.items():
        s = s.replace(k, v)
    s = re.sub(r"\\(?:mathrm|mathbf|mathcal|text)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", s)
    s = re.sub(r"_\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"_(\S)", r"\1", s)
    s = re.sub(r"\^\{([^{}]*)\}", _sup_repl, s)
    s = re.sub(r"\^(\S)", _sup_repl, s)
    s = re.sub(r"\\([a-zA-Z]+)", r"\1", s)
    s = s.replace("{", "").replace("}", "")
    return s.strip()


def _alt_text(caption):
    """A short plain-text description for screen readers."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", caption)
    text = re.sub(r"\$([^$]*)\$", lambda m: _math_to_text(m.group(1)), text)
    text = re.sub(r"[*`_<>]", "", text)
    # Collapse spacing left behind by stripped/substituted math (e.g. "disk , while" -> "disk, while").
    text = re.sub(r"\s+([,;:.!?])", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > 250:
        # Truncate at a word boundary rather than mid-word.
        cut = text.rfind(" ", 0, 250)
        text = text[:cut if cut > 0 else 250]
    return text.rstrip(" ,;:")


def _cell(text):
    text = (text or "").replace("|", "\\|").strip()
    if text in ("$...$", "$\\ldots$", "..."):
        text = "\u22ee"
    return text or " "


# --------------------------------------------------------------------------
# back-matter styles
# --------------------------------------------------------------------------

BIB_ENTRY = re.compile(r"^\\?\[(\d+)\\?\]\s*")
CITED_ON = re.compile(r"\s*\(cited on pages?\s+[^)]*\)\.?")
PAGE_TAIL = re.compile(
    r"\s+\d{1,3}(?:[–-]\d{1,3})?(?:,\s*\d{1,3}(?:[–-]\d{1,3})?)*\.?\s*$")
URL = re.compile(r"(?<![\(\[])(https?://[^\s,)\]]+[^\s,.)\];])")
DOI = re.compile(r"\bdoi:\s*(10\.\d{4,}/\S+?)(?=[\s,)]|$)")


def linkify(text):
    text = DOI.sub(lambda m: f"doi: [{m.group(1)}](https://doi.org/{m.group(1)})", text)
    return URL.sub(lambda m: f"<{m.group(1)}>", text)


URL = re.compile(r"(?<![<\(\[])(https?://[^\s,)\]<>]+[^\s,.)\];<>])")


def _bib_writer(self, items):
    self.emit("References are numbered in order of first appearance in the book. "
              "Page numbers from the print edition have been omitted.")
    self.emit()
    pending = []
    started = False

    def flush():
        if not pending:
            return
        body = clean(join_lines(pending, self.vocab))
        m = BIB_ENTRY.match(body)
        if not m:
            self.emit(linkify(body))
            self.emit()
            pending.clear()
            return
        number = m.group(1)
        rest = CITED_ON.sub("", body[m.end():]).strip()
        self.emit(f"({slug('ref', number)})=")
        self.emit(f"**[{number}]**  " + linkify(rest))
        self.emit()
        pending.clear()

    for entry in items:
        if entry[0] != "block":
            continue
        block = entry[1]
        if block["kind"] in ("caption", "artwork"):
            continue
        lines = block.get("lines") or []
        if not lines:
            continue
        if BIB_ENTRY.match(lines[0].strip()):
            flush()
            started = True
        if not started:
            continue
        pending.extend(lines)
    flush()


def _glossary_writer(self, items):
    self.emit("Terms used throughout the book, as defined in the original edition.")
    self.emit()
    self.emit(":::{glossary}")
    for entry in items:
        if entry[0] != "block":
            continue
        block = entry[1]
        if block["kind"] in ("caption", "artwork") or not block.get("lines"):
            continue
        body = clean(join_lines(block["lines"], self.vocab))
        m = re.match(r"^\*\*(.+?)\*\*\s*", body)
        if not m:
            continue
        term = m.group(1).strip()
        definition = PAGE_TAIL.sub("", body[m.end():].strip()).strip()
        if not definition:
            continue
        self.emit()
        self.emit(term)
        self.emit(": " + link_references(definition, self.known))
    self.emit(":::")
    self.emit()


Writer.bibliography = _bib_writer
Writer.glossary = _glossary_writer
