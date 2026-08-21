"""Convert PyMuPDF character runs from the source PDF into Markdown + LaTeX.

The source PDF is pdfTeX output using the ``newpx``/``TeX Gyre Pagella`` font
set.  Mathematics is encoded with Unicode Mathematical Alphanumeric Symbols
(U+1D400..U+1D7FF) drawn from the ``NewPXMI`` family, while operators come from
``pxsys``/``pxmiaX``.  Superscripts and subscripts carry no structural markup at
all: they are ordinary characters set at a smaller size and a shifted baseline.

This module rebuilds that structure from character geometry.
"""

from __future__ import annotations

import re
import unicodedata

# --------------------------------------------------------------------------
# font classification
# --------------------------------------------------------------------------

#: fonts used by the book's body text
TEXT_FONTS = {
    "TeXGyrePagellaX-Regular",
    "TeXGyrePagellaX-Bold",
    "TeXGyrePagellaX-Italic",
    "TeXGyrePagellaX-BoldItal",
    "TeXGyrePagella-Regular",
    "TeXGyrePagella-Italic",
    "TeXGyreHeros-Regular",
    "TeXGyreHeros-Bold",
}

#: fonts that only ever carry mathematics
MATH_FONTS = {
    "NewPXMI",
    "NewPXMI_gnu",
    "pxmiaX",
    "pxsys",
    "txexs",
    "Cmmi10",
    "Cmr10",
    "wasy9",
    "Symbol",
}

#: typewriter font, used for URLs and file paths; never mathematics
MONO_FONTS = {"BeraSansMono-Roman"}

#: glyph fonts used only to draw the margin's information/caution symbols
ICON_FONTS = {"CalistoMT-BoldItalic", "MSAM10", "txsya"}

#: fonts that only appear *inside* figures (matplotlib, screenshots, logos)
FIGURE_FONTS = {
    "BitstreamVeraSans-Roman",
    "MyriadPro-Regular",
    "MyriadPro-Bold",
    "MyriadPro-Semibold",
    "MyriadPro-It",
    "ArialMT",
    "Arial-BoldMT",
    "Arial-ItalicMT",
    "Arial-Black,Bold",
    "ArialNarrow-Bold",
    "ArialNarrow-Italic",
    "ACaslonPro-Semibold",
    "NewsGothicMT",
    "NewsGothicMT-Bold",
    "CalistoMT-BoldItalic",
    "CopperplateGothic-Light",
}


def font_class(font: str) -> str:
    if font in ICON_FONTS:
        return "icon"
    if font in MONO_FONTS:
        return "mono"
    if font in MATH_FONTS:
        return "math"
    if font in FIGURE_FONTS:
        return "figure"
    if font in TEXT_FONTS:
        return "text"
    # unknown fonts default to text so nothing is silently dropped
    return "text"


# --------------------------------------------------------------------------
# Unicode math alphanumerics -> LaTeX
# --------------------------------------------------------------------------

_GREEK_NAMES = {
    "ALPHA": "alpha", "BETA": "beta", "GAMMA": "gamma", "DELTA": "delta",
    "EPSILON": "epsilon", "ZETA": "zeta", "ETA": "eta", "THETA": "theta",
    "IOTA": "iota", "KAPPA": "kappa", "LAMDA": "lambda", "LAMBDA": "lambda",
    "MU": "mu", "NU": "nu", "XI": "xi", "OMICRON": "omicron", "PI": "pi",
    "RHO": "rho", "SIGMA": "sigma", "TAU": "tau", "UPSILON": "upsilon",
    "PHI": "phi", "CHI": "chi", "PSI": "psi", "OMEGA": "omega",
}

_CAP_GREEK = {
    "GAMMA": r"\Gamma", "DELTA": r"\Delta", "THETA": r"\Theta",
    "LAMDA": r"\Lambda", "LAMBDA": r"\Lambda", "XI": r"\Xi", "PI": r"\Pi",
    "SIGMA": r"\Sigma", "UPSILON": r"\Upsilon", "PHI": r"\Phi",
    "PSI": r"\Psi", "OMEGA": r"\Omega",
}

#: direct single-character translations (operators, relations, symbols)
SYMBOL_MAP = {
    "×": r"\times", "·": r"\cdot", "−": "-", "–": "--", "—": "---",
    "∼": r"\sim", "≈": r"\approx", "≡": r"\equiv", "≠": r"\neq",
    "≤": r"\le", "≥": r"\ge", "≪": r"\ll", "≫": r"\gg",
    "→": r"\rightarrow", "←": r"\leftarrow", "⇒": r"\Rightarrow",
    "↔": r"\leftrightarrow", "∝": r"\propto", "∞": r"\infty",
    "±": r"\pm", "∓": r"\mp", "÷": r"\div", "√": r"\sqrt",
    "∫": r"\int", "∑": r"\sum", "∏": r"\prod", "∂": r"\partial",
    "∇": r"\nabla", "∈": r"\in", "∘": r"\circ", "◦": r"\circ",
    "°": r"\circ", "⊕": r"\oplus", "⊙": r"\odot", "♂": r"\mars",
    "ℎ": "h", "ℓ": r"\ell", "ℏ": r"\hbar", "µ": r"\mu", "μ": r"\mu",
    "Δ": r"\Delta", "Σ": r"\Sigma", "Ξ": r"\Xi", "Γ": r"\Gamma",
    "Π": r"\Pi", "Θ": r"\Theta", "Υ": r"\Upsilon", "Φ": r"\Phi",
    "Λ": r"\Lambda", "Ψ": r"\Psi", "Ω": r"\Omega",
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta",
    "ε": r"\epsilon", "ζ": r"\zeta", "η": r"\eta", "θ": r"\theta",
    "λ": r"\lambda", "ν": r"\nu", "ξ": r"\xi", "π": r"\pi", "ρ": r"\rho",
    "σ": r"\sigma", "τ": r"\tau", "φ": r"\phi", "χ": r"\chi",
    "ψ": r"\psi", "ω": r"\omega",
    "⟨": r"\langle", "⟩": r"\rangle", "‖": r"\|",
    "′": "'", "″": "''",
    "▶": r"\blacktriangleright", "✓": r"\checkmark",
    "\u0010": "(", "\u0011": ")", "\u0012": "[", "\u0013": "]",
    "\u0000": "(", "\u0001": ")",
}

_MATH_ALNUM_CACHE: dict[str, str] = {}


def math_alnum_to_latex(ch: str) -> str | None:
    """Map a Mathematical Alphanumeric Symbol to its LaTeX-in-math equivalent.

    PyMuPDF reports these glyphs truncated to sixteen bits (U+1D443 arrives as
    U+D443, which Unicode calls a Hangul syllable), so the high bit has to be
    put back before the character can be named.
    """
    if ch in _MATH_ALNUM_CACHE:
        return _MATH_ALNUM_CACHE[ch]
    cp = ord(ch)
    if 0xD400 <= cp <= 0xD7FF:
        cp += 0x10000
        ch = chr(cp)
    if not (0x1D400 <= cp <= 0x1D7FF):
        return None
    try:
        name = unicodedata.name(ch)
    except ValueError:
        return None
    if not name.startswith("MATHEMATICAL "):
        return None
    body = name[len("MATHEMATICAL "):]
    variant = body.endswith(" SYMBOL")
    if variant:
        body = body[: -len(" SYMBOL")]
    parts = body.split()
    letter = parts[-1]
    qualifiers = parts[:-1]
    small = "SMALL" in qualifiers or variant
    if variant and letter in _GREEK_NAMES:
        out = "\\var" + _GREEK_NAMES[letter]
        _MATH_ALNUM_CACHE[ch] = out
        return out
    if "GREEK" in qualifiers or letter in _GREEK_NAMES:
        if small:
            out = "\\" + _GREEK_NAMES.get(letter, letter.lower())
        else:
            out = _CAP_GREEK.get(letter, "\\" + _GREEK_NAMES.get(letter, letter.lower()).capitalize())
    elif "DIGIT" in qualifiers or letter in (
        "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
    ):
        digits = {
            "ZERO": "0", "ONE": "1", "TWO": "2", "THREE": "3", "FOUR": "4",
            "FIVE": "5", "SIX": "6", "SEVEN": "7", "EIGHT": "8", "NINE": "9",
        }
        out = digits.get(letter, letter)
    elif len(letter) == 1 and letter.isalpha():
        out = letter.lower() if small else letter
    else:
        return None
    _MATH_ALNUM_CACHE[ch] = out
    return out


def char_to_latex(ch: str) -> str:
    """Translate one character into math-mode LaTeX."""
    if len(ch) != 1:
        return ch
    m = math_alnum_to_latex(ch)
    if m is not None:
        return m
    if ch in SYMBOL_MAP:
        return SYMBOL_MAP[ch]
    if ch in "%$#&_":
        return "\\" + ch
    if ch == "\u00a0":
        return "~"
    return ch


_LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
              "\ufb03": "ffi", "\ufb04": "ffl"}


def char_to_text(ch: str) -> str:
    """Translate one character into Markdown body text."""
    if len(ch) > 1:
        return ch                       # a synthetic, already-formatted run
    if ch in _LIGATURES:
        return _LIGATURES[ch]
    if ch == "\u0001BULLET\u0001":
        return ch
    if ch in "$*_`<>\\":
        return "\\" + ch
    if ch == "\u00a4":
        return ""
    return ch


# --------------------------------------------------------------------------
# multi-letter operator names that should be typeset upright
# --------------------------------------------------------------------------

_OPNAMES = ["ln", "log", "exp", "sin", "cos", "tan", "max", "min", "arctan"]


def _tidy_math(s: str) -> str:
    """Cosmetic clean-up of a generated math fragment."""
    s = s.replace("\u2009", r"\,").replace("\u2005", r"\,").replace("\u200a", "")
    s = re.sub(r"\s+", " ", s).strip()
    # upright operator names
    for op in _OPNAMES:
        s = re.sub(rf"(?<![\\A-Za-z]){op}(?![A-Za-z])", "\\\\" + op + " ", s)
    s = re.sub(r"\\(ln|log|exp|sin|cos|tan|max|min|arctan)\s+", r"\\\1 ", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace(" }", "}")
    s = re.sub(r"\\dot\{\}\s*(\\?[A-Za-z]+)", r"\\dot{\1}", s)
    for _ in range(6):
        merged = re.sub(r"\\mathrm\{([^{}]*)\}([./,-]?)\\mathrm\{",
                        lambda m: "\\mathrm{" + m.group(1) + m.group(2), s)
        if merged == s:
            break
        s = merged
    s = re.sub(r"\\sqrt\s*(\d+(?:\.\d+)?|\\?[A-Za-z]+(?:\^\{[^}]*\})?)", r"\\sqrt{\1}", s)
    s = re.sub(r"\s+([)\]}.,;])", r"\1", s)
    s = re.sub(r"([([{])\s+", r"\1", s)
    s = re.sub(r"\s*\^\{\s*\\circ\s*\}", "^{\\\\circ}", s)
    s = re.sub(r"(?<![{^])\\circ", "^{\\\\circ}", s)
    return s


# --------------------------------------------------------------------------
# line rendering: characters -> Markdown with embedded LaTeX
# --------------------------------------------------------------------------

#: unit symbols that may legitimately carry a raised digit, so that ``m2``
#: reads as an exponent while ``sentences5`` reads as a sidenote marker
UNIT_TOKENS = {
    "m", "km", "cm", "mm", "nm", "pm", "s", "ms", "ns", "yr", "hr", "ft", "mi",
    "W", "kW", "MW", "GW", "TW", "mW", "J", "kJ", "MJ", "GJ", "TJ", "EJ",
    "kg", "g", "mg", "L", "mL", "N", "Pa", "K", "V", "A", "Hz", "mol",
    "Wh", "kWh", "MWh", "GWh", "TWh", "cal", "Btu", "AU", "ly", "Mt", "Gt",
    "px", "bbl", "R", "M", "T", "C", "E", "P", "Q", "d",
}

MATH_WORDS = {"ln", "log", "exp", "sin", "cos", "tan", "max", "min", "arctan"}
_NEUTRAL_CHARS = set("0123456789.,()[]{}/+-=<>%|'")
_TAIL_PUNCT = set(",.;:!?")


def _modal(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    return max(counts.items(), key=lambda kv: kv[1])[0]


MONO_MARK = "\u0002"
DELIM_FONTS = {"txexs", "Symbol"}
FLAT_FONTS = DELIM_FONTS | MONO_FONTS


def _script_levels(chars):
    """Assign a script-nesting path to every character from its geometry."""
    vis = [c for c in chars if c.c.strip() and c.font not in FLAT_FONTS]
    if not vis:
        vis = [c for c in chars if c.c.strip()]
    if not vis:
        return [(c, ()) for c in chars]
    base_y = _modal([round(c.y, 1) for c in vis])
    base_size = max(round(c.size, 1) for c in vis
                    if abs(round(c.y, 1) - base_y) <= 0.7) if any(
        abs(round(c.y, 1) - base_y) <= 0.7 for c in vis) else max(
        round(c.size, 1) for c in vis)
    stack = [(base_y, base_size, None)]
    out = []
    for ch in chars:
        if ch.font in FLAT_FONTS and ch.c.strip():
            # an extensible delimiter closes any script it encloses
            del stack[1:]
            out.append((ch, ()))
            continue
        if not ch.c.strip():
            out.append((ch, tuple(s[2] for s in stack[1:])))
            continue
        y, sz = round(ch.y, 1), round(ch.size, 1)
        while len(stack) > 1:
            top = stack[-1]
            if abs(y - top[0]) <= 0.8 and abs(sz - top[1]) <= 0.6:
                break
            if sz <= top[1] - 0.45 and abs(y - top[0]) > 0.55:
                break                       # a deeper script; keep the stack
            stack.pop()
        top = stack[-1]
        if abs(y - top[0]) <= 0.8 and abs(sz - top[1]) <= 0.6:
            pass
        elif sz <= top[1] - 0.45 and abs(y - top[0]) > 0.55:
            stack.append((y, sz, "^" if y < top[0] - 0.4 else "_"))
        else:
            # a plain change of size on the same baseline is a font change
            stack = [(y, sz, None)]
        out.append((ch, tuple(s[2] for s in stack[1:])))
    return out


def _is_mathchar(ch):
    if font_class(ch.font) == "math":
        return True
    cp = ord(ch.c[0])
    return 0x1D400 <= cp <= 0x1D7FF or (0xD400 <= cp <= 0xD7FF and font_class(ch.font) != "figure")


def _token_before(atoms, k):
    """The alphabetic token ending just before index ``k``, at its own level."""
    if k <= 0:
        return ""
    level = atoms[k - 1][1]
    j = k - 1
    letters = []
    while j >= 0:
        ch, path, _ = atoms[j]
        if path != level or not ch.c.strip() or not ch.c.isalpha():
            break
        letters.append(ch.c)
        j -= 1
    return "".join(reversed(letters))


def strip_icons(chars):
    """Remove margin symbols, reporting which ones were present."""
    kinds = []
    kept = []
    body = [c for c in chars if c.c.strip() and font_class(c.font) not in ("icon",)]
    base_size = max((c.size for c in body), default=9.8)
    base_y = body[0].y if body else 0.0
    for ch in chars:
        if font_class(ch.font) == "icon":
            kinds.append({"i": "info", "\u25a0": "change",
                          "\u25b6": "bullet", "\u2713": "check"}.get(ch.c, "info"))
            glyph = {"\u25b6": "\u0001BULLET\u0001", "i": "\u24d8", "\u2713": "\u2713"}
            if ch.c in glyph:
                kept.append(type(ch)(glyph[ch.c], ch.x, base_y, base_size,
                                     "TeXGyrePagellaX-Regular", 0, ch.w))
            continue
        kept.append(ch)
    while kept and not kept[0].c.strip():
        kept.pop(0)
    return kept, kinds


def _insert_spaces(chars):
    """Re-introduce word spaces that pdfTeX expressed purely as kerning."""
    out = []
    for ch in chars:
        if out and ch.c.strip() and out[-1].c.strip() \
                and not (font_class(ch.font) == "mono" and font_class(out[-1].font) == "mono"):
            prev = out[-1]
            gap = ch.x - (prev.x + (prev.w or 0.0))
            if gap > 0.22 * max(prev.size, ch.size):
                spacer = type(ch)(" ", prev.x + (prev.w or 0.0), prev.y,
                                  prev.size, prev.font)
                out.append(spacer)
        out.append(ch)
    return out


def render_line(chars, *, allow_math=True, sidenotes=True, italics=True):
    """Render one merged logical line into Markdown."""
    chars, _ = strip_icons(chars)
    if not chars:
        return ""
    chars = _insert_spaces(chars)
    levelled = _script_levels(chars)
    atoms = [[ch, path, ""] for ch, path in levelled]
    n = len(atoms)
    if n == 0:
        return ""

    core = [False] * n
    for k, (ch, path, _) in enumerate(atoms):
        if ch.c.strip() and _is_mathchar(ch):
            core[k] = True

    # -- sidenote markers ---------------------------------------------------
    marks = [False] * n
    if sidenotes:
        k = 0
        while k < n:
            ch, path, _ = atoms[k]
            if path == ("^",) and ch.c.isdigit() and not _is_mathchar(ch):
                j = k
                while j + 1 < n and atoms[j + 1][1] == ("^",) \
                        and atoms[j + 1][0].c.isdigit() and not _is_mathchar(atoms[j + 1][0]):
                    j += 1
                prev = None
                p = k - 1
                while p >= 0 and not atoms[p][0].c.strip():
                    p -= 1
                if p >= 0:
                    prev = atoms[p][0]
                nxt = None
                q = j + 1
                while q < n and not atoms[q][0].c.strip():
                    q += 1
                if q < n:
                    nxt = atoms[q][0]
                exponent = False
                if prev is not None:
                    if _is_mathchar(prev) or prev.c.isdigit() or prev.c in ")]":
                        exponent = True
                    elif prev.c.isalpha() and _token_before(atoms, p + 1) in (
                            UNIT_TOKENS | MATH_WORDS):
                        exponent = True
                # an isotope label: raised digits welded to the element symbol
                if nxt is not None and not exponent and q == j + 1 \
                        and (nxt.c.isupper() or atoms[q][1]):
                    exponent = True
                if nxt is not None and _is_mathchar(nxt) and not exponent:
                    if prev is not None and (prev.c.isdigit() or prev.c.isalpha()):
                        exponent = True
                if not exponent:
                    for t in range(k, j + 1):
                        marks[t] = True
                k = j + 1
            else:
                k += 1

    # -- ordinals (64th, 1st) are prose, not exponents ---------------------
    ordinal = [False] * n
    k = 0
    while k < n:
        ch, path, _ = atoms[k]
        if path == ("^",) and ch.c.isalpha() and font_class(ch.font) == "text":
            j = k
            while j + 1 < n and atoms[j + 1][1] == ("^",) and atoms[j + 1][0].c.isalpha():
                j += 1
            word = "".join(atoms[t][0].c for t in range(k, j + 1)).lower()
            p = k - 1
            while p >= 0 and not atoms[p][0].c.strip():
                p -= 1
            if word in ("st", "nd", "rd", "th") and p >= 0 and not atoms[p][1]:
                for t in range(k, j + 1):
                    ordinal[t] = True
            k = j + 1
        else:
            k += 1

    # -- scripts belong to the mathematics ---------------------------------
    for k, (ch, path, _) in enumerate(atoms):
        if path and ch.c.strip() and not marks[k] and not ordinal[k]:
            core[k] = True

    ismath = list(core) if allow_math else [False] * n
    if allow_math:
        _absorb(atoms, ismath, marks)

    return _emit(atoms, ismath, marks, italics=italics)


def _absorb(atoms, ismath, marks):
    for _ in range(4):
        before = list(ismath)
        _absorb_once(atoms, ismath, marks)
        if ismath == before:
            break
    _drop_empty_runs(atoms, ismath)


def _absorb_once(atoms, ismath, marks):
    n = len(atoms)

    def visible(k):
        return atoms[k][0].c.strip() != ""

    # neutral characters directly attached to mathematics
    changed = True
    while changed:
        changed = False
        for k in range(n):
            if ismath[k] or marks[k] or not visible(k):
                continue
            c = atoms[k][0].c
            if c not in _NEUTRAL_CHARS:
                continue
            left = k > 0 and ismath[k - 1] and visible(k - 1)
            right = k + 1 < n and ismath[k + 1] and visible(k + 1)
            if not (left or right):
                continue
            if c in _TAIL_PUNCT and not (left and right):
                nxt = atoms[k + 1][0].c if k + 1 < n else ""
                prv = atoms[k - 1][0].c if k else ""
                grouped = c in ".," and prv.isdigit() and nxt.isdigit()
                if not (grouped and (left or right)):
                    continue
            ismath[k] = True
            changed = True

    # short unit-like words welded to a maths run with no intervening space
    k = 0
    while k < n:
        ch, path, _ = atoms[k]
        if path or not ch.c.isalpha() or ismath[k] or font_class(ch.font) == "mono":
            k += 1
            continue
        j = k
        while j + 1 < n and atoms[j + 1][0].c.isalpha() and not atoms[j + 1][1]:
            j += 1
        token = "".join(atoms[t][0].c for t in range(k, j + 1))
        touch_left = k > 0 and ismath[k - 1] and visible(k - 1)
        touch_right = j + 1 < n and ismath[j + 1] and visible(j + 1)
        if token in MATH_WORDS:
            near_left = k > 0 and ismath[k - 1] and (visible(k - 1) or (k > 1 and ismath[k - 2]))
            near_right = j + 1 < n and (ismath[j + 1] or (j + 2 < n and not visible(j + 1) and ismath[j + 2]))
            touch_left, touch_right = touch_left or near_left, touch_right or near_right
        if (touch_left or touch_right) and (token in UNIT_TOKENS or token in MATH_WORDS):
            for t in range(k, j + 1):
                ismath[t] = True
        k = j + 1

    # bridge two maths runs separated only by digits, spaces and operators
    for k in range(n):
        if not ismath[k]:
            continue
        j = k + 1
        buf = []
        while j < n and not ismath[j] and not marks[j]:
            c = atoms[j][0].c
            if len(c) != 1 or c.isalpha() or c in ";:":
                break
            buf.append(j)
            j += 1
        if j < n and ismath[j] and buf and len(buf) <= 7:
            for b in buf:
                ismath[b] = True

    # a trailing operator invites the number that follows it
    _OPS = set("=+-<>/") | {"\u00d7", "\u2212", "\u2248", "\u223c", "\u2264", "\u2265",
                            "\u00b7", "\u2261", "\u221d", "\u00f7"}
    for k in range(n):
        if not ismath[k]:
            continue
        if k + 1 < n and ismath[k + 1]:
            continue
        if atoms[k][0].c not in _OPS:
            continue
        j = k + 1
        if j < n and not visible(j):
            j += 1
        start = j
        while j < n and (atoms[j][0].c.isdigit() or atoms[j][0].c in ".,"):
            j += 1
        while j > start and atoms[j - 1][0].c in ".,":
            j -= 1
        if j > start and (j >= n or not atoms[j][0].c.isalpha()):
            for t in range(k + 1, j):
                ismath[t] = True


def _drop_empty_runs(atoms, ismath):
    """A run with no genuine mathematics in it is prose after all."""
    n = len(atoms)
    k = 0
    while k < n:
        if ismath[k]:
            j = k
            while j + 1 < n and ismath[j + 1]:
                j += 1
            has_math = any(atoms[t][0].c.strip() and
                           (_is_mathchar(atoms[t][0]) or atoms[t][1])
                           for t in range(k, j + 1))
            visible_any = any(atoms[t][0].c.strip() for t in range(k, j + 1))
            if not has_math or not visible_any:
                for t in range(k, j + 1):
                    ismath[t] = False
            k = j + 1
        else:
            k += 1


def _style_of(ch):
    bold = "Bold" in ch.font
    italic = "Ital" in ch.font
    return ("**" if bold and not italic else
            "***" if bold and italic else
            "*" if italic else "")


def _emit(atoms, ismath, marks, italics=True):
    n = len(atoms)
    pieces = []          # (kind, payload) with kind in {"t","m","f"}
    k = 0
    while k < n:
        if ismath[k]:
            j = k
            while j + 1 < n and ismath[j + 1]:
                j += 1
            while j > k and not atoms[j][0].c.strip():
                j -= 1
            while k < j and not atoms[k][0].c.strip():
                pieces.append(("t", " ", ""))
                k += 1
            pieces.append(("m", _emit_math(atoms[k:j + 1]), ""))
            k = j + 1
        elif marks[k]:
            j = k
            digits = ""
            while j < n and marks[j]:
                digits += atoms[j][0].c
                j += 1
            pieces.append(("f", digits, ""))
            k = j
        elif font_class(atoms[k][0].font) == "mono":
            j = k
            run = ""
            while j < n and (font_class(atoms[j][0].font) == "mono"
                             or (not atoms[j][0].c.strip() and j + 1 < n
                                 and font_class(atoms[j + 1][0].font) == "mono")):
                run += atoms[j][0].c
                j += 1
            pieces.append(("u", run, ""))
            k = j
        else:
            ch = atoms[k][0]
            style = _style_of(ch) if ch.c.strip() else None
            if style and not italics:
                style = "**" if "**" in style else ""
            pieces.append(("t", char_to_text(ch.c), style))
            k += 1

    # coalesce text with identical styling, ignoring the style of spaces
    out = []
    cur_style = ""
    buf = []

    def flush():
        nonlocal buf, cur_style
        if not buf:
            return
        text = "".join(buf)
        if cur_style and text.strip():
            lead = len(text) - len(text.lstrip())
            trail = len(text) - len(text.rstrip())
            out.append(text[:lead] + cur_style + text[lead:len(text) - trail]
                       + cur_style + (text[len(text) - trail:] if trail else ""))
        else:
            out.append(text)
        buf = []

    for kind, payload, style in pieces:
        if kind == "t":
            if style is None or style == cur_style:
                buf.append(payload)
            else:
                flush()
                cur_style = style
                buf.append(payload)
        else:
            flush()
            cur_style = ""
            if kind == "m":
                out.append("$" + payload + "$")
            elif kind == "u":
                out.append(MONO_MARK + payload + MONO_MARK)
            else:
                out.append(f"[^{payload}]")
    flush()
    return "".join(out)


def _emit_math(atoms):
    out = []
    open_paths = []
    upright = []

    def flush_upright():
        if upright:
            word = "".join(upright)
            out.append("\\" + word + " " if word in MATH_WORDS
                       else "\\mathrm{" + word + "}")
            upright.clear()

    for ch, path, _ in atoms:
        path = list(path)
        if path != open_paths[:len(path)] or len(path) != len(open_paths):
            flush_upright()
        while len(open_paths) > len(path) or (open_paths and path[:len(open_paths)] != open_paths):
            out.append("}")
            open_paths.pop()
        while len(open_paths) < len(path):
            kind = path[len(open_paths)]
            out.append(kind + "{")
            open_paths.append(kind)
        c = ch.c
        if not c.strip():
            flush_upright()
            out.append(" ")
            continue
        if len(c) != 1:
            flush_upright()
            out.append(c)
            continue
        if c == "\u00a4":
            flush_upright()
            out.append("\\dot{}")
            continue
        if font_class(ch.font) == "text" and c.isalpha():
            upright.append(c)
            continue
        flush_upright()
        piece = char_to_latex(c)
        out.append(piece + " " if re.fullmatch(r"\\[a-zA-Z]+", piece) else piece)
    flush_upright()
    out.extend("}" * len(open_paths))
    return _tidy_math("".join(out))


# --------------------------------------------------------------------------
# stacked fractions
# --------------------------------------------------------------------------


def render_math_only(chars):
    """LaTeX for a run of characters that is known to be mathematics."""
    chars, _ = strip_icons(chars)
    if not chars:
        return ""
    chars = _insert_spaces(chars)
    levelled = _script_levels(chars)
    atoms = [[ch, path, ""] for ch, path in levelled]
    return _emit_math(atoms)


def render_fraction_region(chars, bars):
    """Rebuild ``\\frac`` structures that pdfTeX drew as stacked rows and a rule.

    ``bars`` are the fraction rules as ``(x0, y, x1)``; the widest one is the
    outermost fraction, and everything to its left and right, and above and
    below it, is laid out recursively.
    """
    chars = [c for c in chars if c.c.strip()]
    if not chars:
        return ""
    bars = sorted(bars, key=lambda b: -(b[2] - b[0]))
    if not bars:
        return render_math_only(chars)
    bar = bars[0]
    rest = bars[1:]
    lo, hi = bar[0] - 1.0, bar[2] + 1.0
    kind = bar[3] if len(bar) > 3 else "frac"

    def mid(c):
        return c.x + (c.w or 0.0) / 2.0

    left = [c for c in chars if mid(c) < lo]
    right = [c for c in chars if mid(c) > hi]
    over = [c for c in chars if lo <= mid(c) <= hi and c.y < bar[1]]
    under = [c for c in chars if lo <= mid(c) <= hi and c.y > bar[1]]

    def pick(pred):
        return [b for b in rest if pred(b)]

    out = []
    if kind == "sqrt":
        left = [c for c in left
                if not (c.c == "\u221a" and abs(c.x + (c.w or 0.0) - bar[0]) < 4)]
        under = under + over
    if left:
        out.append(render_fraction_region(left, pick(lambda b: b[2] <= lo)))
    num = render_fraction_region(over, pick(lambda b: b[0] >= lo and b[2] <= hi and b[1] < bar[1]))
    den = render_fraction_region(under, pick(lambda b: b[0] >= lo and b[2] <= hi and b[1] > bar[1]))
    if kind == "sqrt":
        out.append("\\sqrt{" + den + "}")
    else:
        out.append("\\frac{" + num + "}{" + den + "}")
    if right:
        out.append(render_fraction_region(right, pick(lambda b: b[0] >= hi)))
    return _tidy_math(" ".join(p for p in out if p))
