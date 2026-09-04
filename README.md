# Energy and Human Ambitions on a Finite Planet

A web-native [MyST Markdown](https://mystmd.org/) edition of Tom Murphy's open
textbook *Energy and Human Ambitions on a Finite Planet: Assessing and Adapting
to Planetary Limits* (UC San Diego, published by eScholarship).

The Markdown under `chapters/`, `appendices/`, `front/` and `back/` is the
primary, editable edition. It is generated from the author's print-format PDF by
the scripts in [`scripts/`](scripts/), and the generator is kept in the
repository so the conversion can be re-run and improved.

## Source and license

The original textbook is available from
[eScholarship](https://escholarship.org/uc/item/9js5291m)
(ISBN 978-0-578-86717-5, DOI
[10.21221/S2978-0-578-86717-5](https://doi.org/10.21221/S2978-0-578-86717-5)) and
is licensed [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
Attributions and permissions for images not created by the author are listed in
[`back/image-attributions.md`](back/image-attributions.md).

Suggested citation: Murphy, T. W., Jr. (2021). *Energy and Human Ambitions on a
Finite Planet: Assessing and Adapting to Planetary Limits*. eScholarship,
University of California.

## Repository layout

| Path | Contents |
| --- | --- |
| [`myst.yml`](myst.yml) | Project metadata and table of contents |
| [`index.md`](index.md) | Home page |
| [`front/`](front/) | Preface, How to Use This Book |
| [`chapters/`](chapters/) | The twenty chapters, in four parts |
| [`appendices/`](appendices/) | Math, chemistry, selected answers, tangents |
| [`back/`](back/) | Epilogue, attributions, bibliography, notation, glossary |
| [`images/`](images/) | 162 figures plus chapter-opening photographs |
| [`scripts/`](scripts/) | The PDF → MyST conversion pipeline |

## Build

Targets MyST CLI 1.10.1; needs [Node.js](https://nodejs.org/).

```bash
npm install
npm run start          # local preview with live reload
npm run build          # static site in _build/html/
npm run verify         # structural checks
```

Generated files under `_build/` are not committed. CI runs on pull requests
(`.github/workflows/ci.yml`); pushes to `main` deploy via
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

## How the source PDF is converted

The print edition is set in a Tufte-style two-column geometry: a wide main
column and a narrow margin column that alternates sides with page parity, and
which carries sidenotes, small figures and small tables. Mathematics is drawn as
positioned glyphs with no structural markup at all — superscripts, subscripts,
fractions and radicals exist only as font sizes, baselines and thin rules.

[`scripts/`](scripts/) rebuilds that structure:

| Script | Role |
| --- | --- |
| [`mathtext.py`](scripts/mathtext.py) | Character runs → Markdown + LaTeX: Unicode math alphanumerics, script nesting from geometry, units in `\mathrm`, typewriter runs, ligatures |
| [`layout.py`](scripts/layout.py) | Column separation, shaded call-out boxes, artwork clustering |
| [`extract.py`](scripts/extract.py) | Page model: paragraphs, headings, display equations, stacked fractions, ruled tables, figure/caption pairing → `build/document.json` |
| [`render_figures.py`](scripts/render_figures.py) | Crops each figure out of the PDF: SVG for vector artwork, JPEG for photographs |
| [`build_book.py`](scripts/build_book.py), [`textutil.py`](scripts/textutil.py), [`emit.py`](scripts/emit.py) | Assembles chapters, undoes hyphenation, links cross-references, writes Markdown |
| [`verify_book.py`](scripts/verify_book.py) | Structural checks used by CI |

Re-run the whole pipeline with:

```bash
sh scripts/build.sh
```

It needs `PyMuPDF`, `Pillow` and the `mutool` binary, plus the source PDF
`220222_2.pdf` in the repository root. That is the two-sided, made-to-print
release (2022-02-22); the single-sided eScholarship download of the same edition
was used only to cross-check readings, since it carries the identical text with
the margin material set on one side.

## Conventions of this edition

The print design maps onto web equivalents as follows.

- **Numbered margin notes** become Markdown footnotes, anchored at the word they
  annotated. **Unnumbered margin notes** become `:::{margin}` blocks beside the
  paragraph they belong to.
- **Definitions** (pink panels), **Boxes** (blue) and **Examples** (yellow)
  become `important`, `tip` and `seealso` call-outs, each with a stable label
  (`def-1-1-1`, `box-1-1`, `ex-1-1-1`) so cross-references resolve.
- Figures, tables and numbered equations keep the book's own numbering through
  the `:enumerator:` option, and carry `fig-`, `tab-` and `eq-` labels.
- Figures are re-cut from the PDF: SVG where the artwork is vector, PNG where an
  SVG would be larger than a good raster, JPEG for photographs.
- The alphabetical index is omitted — its page numbers have no web equivalent,
  and site search covers the same ground. Page-number tails in the glossary and
  the "cited on pages" tails in the bibliography are dropped for the same reason.

## Verification

```bash
python3 scripts/verify_book.py
```

checks chapter and appendix counts, figure/table/equation coverage against the
source PDF, missing image files, unresolved labels, footnote pairing and common
conversion artifacts.

## Deployment

Pushes to `main` trigger [GitHub Actions](.github/workflows/deploy.yml), which
verifies the conversion, builds the HTML site and deploys it to GitHub Pages.
