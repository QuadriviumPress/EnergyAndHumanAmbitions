---
title: "Errata"
short_title: "Errata"
label: errata
---

# Errata

A list of typos, grammatical errors, factual/numerical mistakes and conversion
defects found in this edition of *Energy and Human Ambitions on a Finite
Planet*.

## About this list

Every entry cites `file:line` against the Markdown sources in this repository
and quotes the text as it currently stands. Entries are grouped by kind, and
within each group ordered by where they appear in the book.

Two kinds of error are mixed together here and are labelled as such:

- **Author errata** — mistakes that are in the text itself (a wrong number, a
  misspelling, a grammatical slip). These should also be reported upstream at
  <https://tmurphy.physics.ucsd.edu/energy-text/>.
- **Conversion defects** — damage introduced when the print PDF was converted
  to Markdown by [`scripts/`](scripts/): lost characters, scrambled reading
  order, broken equations. These are bugs in this edition only.

How the list was compiled: `hunspell` spell-check over prose with math, code,
URLs and MyST directives stripped; scripted structural checks (footnote
pairing and numbering, cross-reference resolution, table column counts,
math-delimiter balance, quote balance, bold-marker balance, unlinked
references); pattern sweeps for recurring grammar and punctuation faults; and
a full manual read of all twenty chapters, four appendices and the back matter
with the arithmetic re-derived independently.

Where a claim is arithmetic, the recomputation is shown so it can be checked.

---

## 1. Numerical and factual errors

These are the highest-consequence items: the text as printed states something
that is wrong or that contradicts the book's own tables.

All of 1.1–1.17 (bacteria jar percentage, interest example, Dyson-sphere
atmosphere thickness, Table 1.4 rows and caption, Problem 18 energy value,
Table 9.6 ice mass, Boltzmann constant exponent/units, Stefan–Boltzmann units
in `back/notation.md`, the Chapter 14 table cross-reference, National Ignition
Facility naming, the Chapter 15 margin note, footnote 58's missing "million",
the Chapter 16 Scotland/UK phrasing, the Montreal Protocol date, "Max Planck",
and the four bibliography misspellings) have been fixed in the source.

### 1.1 Minor numerical inconsistencies between tables

These are small and may be deliberate rounding, but they are internal
mismatches a reader will trip over:

- `ch-09` Table 9.1 gives coal 7.8 kcal/g, but Table 9.2 (line 100), Box 9.1
  and Problem 9 (line 733) all use **6.5 kcal/g** for coal with no explanation.
  The 6.5 value is the one that reproduces the stated 1.4 ppm$_\mathrm{v}$/yr
  from coal, so the tables are consistent internally but not with each other;
  a note would help.
- `ch-06` Table 6.2 gives U.S. gas 35.3% and wind 6.6% of electricity;
  `ch-07` Table 7.2 gives 34.9% and 6.5% for the same 2018 data.
- `ch-12:334` says the U.S. had "about **94** GW of installed wind capability"
  while Table 12.2 (line 267) lists **97** GW.
- `ch-13:495` gives lithium-ion at 0.17 kcal/g; `ch-16` Table 16.1 gives 0.15.

---

## 2. Structural and markup defects (fixed)

All conversion-introduced structural and markup defects have been fixed in
the source:

- **47 numbered margin notes** that had gone missing (neither referenced nor
  defined) were recovered against the source PDF and restored as proper
  footnotes, across `ch-02`, `ch-03`, `ch-05`, `ch-06`, `ch-08`, `ch-09`,
  `ch-11`, `ch-12`, `ch-13`, `ch-14`, `ch-15`, `ch-18`, `ch-20`, `app-b` and
  `app-d`. This included un-fusing note text that had been absorbed into a
  neighboring note, converting raw math-superscript markers back into proper
  footnote references, and — in two cases (`ch-12`, `ch-13`) — restoring
  whole paragraphs that the missing markers belonged to.
- **All figure alt-texts** are now generated correctly: `scripts/emit.py`'s
  `_alt_text()` was fixed to convert inline LaTeX math to readable plain text
  instead of stripping it (preserving units, exponents, chemical subscripts,
  degree signs, etc.), to truncate at word boundaries instead of mid-word,
  and to clean up the spacing artifacts math-stripping had left behind. Every
  labelled figure's alt text was regenerated from its caption.
- **Split captions and admonition titles** are fixed: Box 6.4, Box 9.1, Box
  15.2, and the various figure captions that had spilled into a margin block
  were rejoined; the unlabeled `Example` admonition in `ch-10` was merged
  back into Example 10.3.2, to which it belonged.
- **Destroyed tables** are fixed: `ch-04` Table 4.2, `ch-05` Table 5.2, `ch-09`
  Table 9.2, `ch-13` Table 13.1, the `ch-15` isotope tables, and `ch-13`
  Problem 26 are all correctly structured; `ch-06` Table 6.2's header was
  repaired to properly label its three columns.
- **Stray artefacts** (OCR leftovers, axis-label fragments, warning-symbol
  runs, unbalanced bold markers, dropped ⌘ symbols, run-together lyric lines,
  a dangling margin fragment, a mid-sentence paragraph break, and a broken
  answer-blank list) have been removed or repaired throughout.
- **Cross-references and citations**: the bibliography citations and internal
  cross-references that had been left unlinked are now linked, and the two
  malformed sub-subsection references (`ch-15`, `ch-17`) now include the
  `.2` component inside the link.

`scripts/verify_book.py` passes cleanly (954 labels, no orphaned or dangling
footnotes, no ragged tables).

---

## 3. Appendix C (fixed)

`appendices/app-c-selected-answers.md` was regenerated from scratch by reading
the two print columns of the original PDF (pages 395–403) in the correct
order, instead of the converter's straight-across-both-columns reading order
that had interleaved answers from different chapters throughout all 810
lines. All twenty chapters' answer keys are now in order, under correct
headings, with the "then"/"than" author erratum on the Chapter 1 answer also
fixed. One residual ambiguity is flagged in place with an HTML comment:
Chapter 17 has two answers both numbered "10" in the source PDF's own
column-split layout; both are preserved in original reading order pending
verification against the print edition.

---

## 4. Edition-consistency notes

Not errors in the source text, but places where this edition contradicts itself
or the original:

- `front/how-to-use-this-book.md:66` — "Finally, a full alphabetical Index
  appears at the end to facilitate finding information in the text." This
  edition deliberately omits the index (see `README.md` and `index.md`). The
  `:::{note}` at the top of the file flags the margin/hyperlink conventions but
  not the index.
- `front/how-to-use-this-book.md:43` — refers to "the list starting on **page
  367**"; several page references of this kind survive in
  `back/image-attributions.md` (33 of them) and in body text ("p. 175",
  "p. 268", …), though the README states that page-number tails were dropped
  from the glossary and bibliography. The convention is applied inconsistently.
- `front/preface.md:19` — "[Chapters 1](#ch-1), 3, and 6 are perhaps the most
  math-intense": only the first of the three chapter numbers is linked. The same
  pattern recurs throughout (e.g. `ch-01:223` "[Eqs. 1.1](#eq-1-1), 1.3, 1.6,
  and 1.7"; `ch-13:329` "[Figures 13.8](#fig-13-8) and 13.9").
- `front/how-to-use-this-book.md:24` — "Some **mouses**…have additional
  buttons": *mice* is the more usual plural, though *mouses* is attested for
  the computer sense.

---

## Summary of counts

| Class | Count |
| --- | --- |
| Numerical / factual errors (remaining, likely-deliberate) | 4 |
| Unlinked cross-references | 31 |
