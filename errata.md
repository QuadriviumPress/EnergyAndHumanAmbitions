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

### 1.1 `chapters/ch-01-exponential-growth.md:61` — bacteria jar percentage

> At 11 PM, the jar is at one-64th capacity, or **1.7%** full.

1/64 = 1.5625%, which rounds to **1.6%**, not 1.7%.
*Author erratum.*

### 1.2 `chapters/ch-01-exponential-growth.md:112` — interest example contradicts Table 1.2

> Then in three years it will be **\$106.18**, or \$100 times $1.02^{3}$.

$100 \times 1.02^3 = \$106.12$, and [Table 1.2](#tab-1-2) — eleven lines below —
correctly lists `| 3 | 1.0612 | \$106.12 |`. The prose contradicts the table.
*Author erratum.*

### 1.3 `chapters/ch-01-exponential-growth.md:315` — Dyson-sphere atmosphere thickness off by 1000×

> The earth's atmosphere distributed over this area would be **0.015 m** thick.

Atmospheric mass $5.15\times10^{18}$ kg at sea-level density 1.225 kg/m³ is
$4.2\times10^{18}$ m³. Spread over the $2.81\times10^{23}$ m² sphere at 1 AU
that is $1.5\times10^{-5}$ m — **0.015 mm**, not 0.015 m. As printed the
atmosphere would be four times *thicker* than the 4 mm shell made from the
entire mass of the Earth, which is impossible.
*Author erratum (or a lost "m" → "mm").*

### 1.4 `chapters/ch-01-exponential-growth.md:454` — Table 1.4 rows do not reproduce

Recomputing Table 1.4 from [Eq. 1.11](#eq-1-11) —
$T=\left[(0.707\times1360+P)/4\sigma\right]^{1/4}+33$ — reproduces the 100-,
200-, 300- and 417-year rows exactly (288.1, 288.9, 296.9, 373.0), which
confirms the model. Two rows do not reproduce:

| Years | $P$ (W/m²) | Printed $T$ / $\Delta T$ | Recomputed $T$ / $\Delta T$ |
| --- | --- | --- | --- |
| 400 | 1,400 | 344 / 56 | **352** / **64** |
| 417 | 2,070 | 373 / **100** | 373 / **85** |
| 1,000 | $1.4\times10^{9}$ | 8,600 / 8,300 | **8,900** / **8,600** |

For the 417-year row the printed $\Delta T$ of 100 looks like the Celsius
temperature (373 K = 100 °C) rather than a difference; the row's own $T$ and
$\Delta T$ are mutually inconsistent (373 − 288 = 85). For the 1,000-year row
the printed $T$ (8,600) equals the correct $\Delta T$, suggesting a
column shift.
*Author erratum.*

### 1.5 `chapters/ch-01-exponential-growth.md:445` — Table 1.4 caption: "by 900 years Earth is hotter than the sun"

At 900 years $P = 1.4\times10^{8}$ W/m² gives $T \approx 5{,}020$ K, which is
*below* the sun's ~5,800 K. The crossing happens at ~926 years. The body text
at line 425 says "inside of 1,000 years", which is correct; the caption is not.
*Author erratum.*

### 1.6 `chapters/ch-04-space-colonization.md:458` — Problem 18 energy off by 10×

> It takes about **5 $\times 10^{10}$ J** of energy to win the fight against gravity.

Footnote [^33] specifies $mgh$ with $m \approx 1{,}500$ kg, and the problem
gives $h = 320$ km: $1500 \times 9.8 \times 3.2\times10^{5} = 4.7\times10^{9}$ J.
The value should be **$5 \times 10^{9}$ J**.

This is confirmed by the answer key: `appendices/app-c-selected-answers.md:93`
says "Will take 15–20 tanks of gas". $4.7\times10^{9}/2.5\times10^{7} = 188$
gallons ≈ 15 tanks. The printed $5\times10^{10}$ J would give 2,000 gallons
(≈ 150 tanks).
*Author erratum.*

### 1.7 `chapters/ch-09-climate-change.md:522` — Table 9.6 ice mass off by 10×

Table 9.6 lists ice as volume $29\times10^{15}$ m³, density 917 kg/m³, and
mass **$2.6\times10^{18}$ kg**. But $29\times10^{15} \times 917 =
2.66\times10^{19}$ kg, i.e. **$26\times10^{18}$ kg**.

Table 9.7 is right and Table 9.6 is wrong: Table 9.7's "total charge" for ice
of $8.8\times10^{24}$ J requires $2.66\times10^{19}\ \mathrm{kg} \times
3.34\times10^{5}\ \mathrm{J/kg}$. Using the printed Table 9.6 mass gives
$0.87\times10^{24}$ J.
*Author erratum.*

### 1.8 `chapters/ch-13-solar-energy.md:100` — Boltzmann constant wrong exponent and wrong units

> $k_{\mathrm{B}}\approx 1.38 \times 10^{-33}$ J $\cdot$ K is the Boltzmann constant

Two errors: the exponent should be **−23**, and the units should be **J/K**,
not J·K. Every other occurrence in the book is correct
(`ch-06:194`, `app-b:235`, `back/notation.md:19`, `back/glossary.md:80`).
*Author erratum.*

### 1.9 `back/notation.md:31` — Stefan–Boltzmann constant units

> $\sigma$ Stefan-Boltzmann constant: $5.67 \times 10^{-8}\mathrm{W/K/m}^{2}$

The units are W/m²/K⁴. As printed the fourth power on kelvin is missing and
the order is inverted. All four other occurrences in the book
(`ch-01:362`, `ch-09:206`, `ch-13:87`, `back/glossary.md:599`) correctly read
$\mathrm{W/m}^{2}/\mathrm{K}^{4}$.
*Author erratum.*

### 1.10 `chapters/ch-14-biological-energy.md:155` — wrong table cross-referenced (twice)

> …the 3.09 factor for octane. In terms of CO$_{2}$ energy intensity, ethanol
> produces 64 g of CO$_{2}$ for every 1 MJ of energy: exactly the same as
> petroleum (**[Table 8.2](#tab-8-2)**).

The 3.09 g/g and 64 g/MJ figures are in **Table 9.1**, not Table 8.2. Table 8.2
has no CO₂ columns at all (its columns are molar mass, kJ/mol, kJ/g, kcal/g).
The earlier reference in the same sentence — 11.5 kcal/g in Table 8.2 — is
correct.
*Author erratum.*

### 1.11 `chapters/ch-15-nuclear-energy.md:963` — National Ignition Facility misnamed

> An effort in the U.S. called the **nuclear ignition facility** (NIF)

The facility is the **National** Ignition Facility.
*Author erratum.*

### 1.12 `chapters/ch-15-nuclear-energy.md:997` — margin note names the wrong two sections' subjects

> Pros and cons are listed separately for **PV and ST** in
> [Section 15.4.8](#sec-15-4-8) and [Section 15.5.3](#sec-15-5-3), respectively.

Sections 15.4.8 and 15.5.3 are "Pros and Cons of Fission" and "Pros and Cons of
Fusion". "PV and ST" is carried over verbatim from the identical margin note in
`chapters/ch-13-solar-energy.md:798`. It should read "fission and fusion".
*Author erratum.*

### 1.13 `chapters/ch-15-nuclear-energy.md:1227` — footnote 58 drops "million" twice

> …to get **153 kcal/g**. Starting with two deuterium nuclei reduces energy
> yield a bit **to to 137 kcal/g**, and for deuterium-tritium reactions it's
> down to 81 **million** kcal/g.

The body text at line 900 correctly says "153 million kcal/g". Recomputing:
p–p 153 million, D–D 136 million, D–T 81 million kcal/g. The first two are
missing "million" (and "to to" was a doubled word).
*Author erratum.*

### 1.14 `chapters/ch-16-small-players.md:203` — Scotland listed as separate from the UK

> Two other large tidal stations in the 300–400 MW capacity range are in the
> works for **the UK and Scotland**.

Scotland is part of the UK. Presumably one of the two should name a different
jurisdiction (e.g. England and Wales, or a specific site).
*Author erratum.*

### 1.15 `chapters/ch-19-a-plan-might-be-welcome.md:88` — Montreal Protocol date

> A global agreement in **1989** called the Montreal Protocol banned the use of
> chlorofluorocarbons.

The Montreal Protocol was agreed and signed in **1987**; it entered into force
on 1 January 1989. As phrased ("a global agreement in 1989 called…") the date
attaches to the agreement rather than to its entry into force.
*Author erratum — worth verifying against the author's intent.*

### 1.16 `back/image-attributions.md:15` — "Max Plank Institute"

> produced by Volker Springel et al. at the **Max Plank** Institute

Should be **Max Planck**. (The book spells "Planck" correctly in all five
physics contexts: `back/glossary.md:74, 502, 505, 593, 674`.)
*Author erratum.*

### 1.17 Bibliography — four misspelled proper names

| Line | As printed | Should be | Evidence |
| --- | --- | --- | --- |
| `back/bibliography.md:24` | *Exponential Economist Meets Finite **Pysicist*** | Physicist | the entry's own URL is `…/economist-meets-physicist/` |
| `back/bibliography.md:45` | T J **Garret** | Garrett | the entry's own URL is `…/~tgarrett/…`; also `ch-02:202` |
| `back/bibliography.md:132, 135` | University of **Calgory** | Calgary | ×2 |
| `back/bibliography.md:51` | K Klein **Goldewĳk** | Goldewijk | the Dutch "ij" ligature (U+0133) survived conversion; it is the only occurrence of that character in the book |

*Mixture of author errata and conversion artifacts.*

### 1.18 Minor numerical inconsistencies between tables

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

## 2. Missing space after inline math (conversion defect)

58 places where a closing `$` is followed immediately by an English word, e.g.
`ch-01:362` "$\sigma$is the Stefan–Boltzmann constant", `ch-05:215` "$m$is 10
kg", `ch-13:100` "$\lambda$and $T$ are variable", `ch-15:173` "$A$by 4",
`ch-16:184` "$\epsilon$is the efficiency". Concentrated in
`ch-13-solar-energy.md` (37) and `ch-09-climate-change.md` (5).

---

## 3. Lost and scrambled text (conversion defects)

### 3.1 Text reordered across the print columns

Four paragraphs read as nonsense because margin-column and body-column runs
were interleaved:

**`chapters/ch-09-climate-change.md:604`**
> $1^{\circ}\mathrm{C}$ (at a 1 $\mathrm{W/m}^{2}$ imbalance).top 300
> $\mathrm{m}^{62}$temperature rise of about $0.035^{\circ}\mathrm{C}$ per year,
> or about 30 years to climbof water, the excess $1.6 \times 10^{22}$ J per year
> leads to an annual

Reconstructed: "If we confine ocean heating to the **top 300 m of water, the
excess $1.6\times10^{22}$ J per year leads to an annual temperature rise of
about 0.035 °C per year, or about 30 years to climb 1 °C (at a 1 W/m²
imbalance).**"

**`appendices/app-b-chemistry-primer.md:157`**
> product at the end of the energy process. H$_{2}$O, as another
> commonboundary cases.$^{17}$CO$_{2}$, calculating for CO$_{2}$ should offer
> no energy to us, since it's a "waste"Since one ubiquitous end-product of
> combustion is

Reconstructed: "…by testing it on some known **boundary cases. Since one
ubiquitous end-product of combustion is CO₂, calculating for CO₂ should offer
no energy to us, since it's a 'waste' product at the end of the energy process.
H₂O, as another common** combustion product, is likewise effectively
neutralized…"

**`chapters/ch-20-adaptation-strategies.md:429`**
> These are just a few of thethereof to evaluate the energy impact of dietary
> choices.countless examples that may be explored using Eq. 20.1 or variants

Reconstructed: "These are just a few of the **countless examples that may be
explored using Eq. 20.1 or variants thereof to evaluate the energy impact of
dietary choices.**"

**`appendices/app-c-selected-answers.md`** — the whole file; see §5.

### 3.2 Sentences truncated or lost outright

- `chapters/ch-11-hydroelectric-energy.md:240` — an orphaned sentence fragment
  sits alone between two margin blocks: "*unusual, having already developed a
  generation capacity 2.5 times larger*". The sentence it belonged to (about
  Washington state) is gone.
- `chapters/ch-13-solar-energy.md:569` — "[Figure 13.17](#fig-13-17) shows the
  situation in the U.S. **California is**" — the sentence about California is
  cut off mid-clause and never resumes.
- `chapters/ch-13-solar-energy.md:319` — Figure 13.9's caption reads "the
  break-points between 5.75 kWh/m²/day in steps of 0.25"; the missing "4.0 and"
  is stranded in a margin block at line 323 ("colors running from 4.0 to").
- `chapters/ch-14-biological-energy.md:126` — a stray word is left in the body:
  "…or nuclear energy.[^13] **matter.** Biofuels therefore occupy…"
- `back/glossary.md:20, 164, 194` — **three glossary definitions are gone**,
  replaced by a single orphaned isotope superscript:

  ```
  alpha decay
  : 4

  D–D fusion
  : 2

  D–T fusion
  : 2
  ```

### 3.3 Isotope superscripts detached throughout Chapter 15

Mass-number superscripts were extracted as separate text runs and dumped onto
their own lines, leaving the prose wrong. Examples:

| Location | As printed | Should read |
| --- | --- | --- |
| `ch-15:163–167` | "…which is predominantly\n\n**5 8**\n\nseen only in heavier nuclei (aside from **Li** and **Be**)." | $^{5}$Li and $^{8}$Be |
| `ch-15:171–175` | "…two protons and two **4**\n\nneutrons—essentially a **He** nucleus…For example, $^{8}$Be **4**\n\ndecays this way, essentially splitting into two **He** nuclei" | a $^{4}$He nucleus; two $^{4}$He nuclei |
| `ch-15:228–234` | "…the fate of **He**…decay mechanism of **He8**…**8**\n\nsecond. It will become **Li**…decay to **Be**." | $^{8}$He, $^{8}$Li, $^{8}$Be |
| `ch-15:394` | "But deuterium **( H)** has a proton and a neutron" | ($^{2}$H) |
| `ch-15:683–687` | "75% hydrogen **( H)** and 25% **4 2 3**\n\nhelium **( He)**. Deuterium **( H)** and **He**…" | $^{1}$H, $^{4}$He, $^{2}$H, $^{3}$He |
| `ch-15:898–908` | "Putting four **H** nuclei together…forming **He**…Using **H** nuclei…instead of **H** (protons)…a triton **( H** nucleus…)" | $^{1}$H, $^{4}$He, $^{2}$H, $^{1}$H, $^{3}$H |
| `ch-15:969–971` | "…not one that produces dangerous **4**\n\ndirect products **( He** is okay!)" | ($^{4}$He |
| `ch-15:1098` | "…from two deuterium **( H)** nuclei to **He**" | ($^{2}$H) … $^{4}$He |
| `ch-15:1188` | footnote 67: "… one **H**, one **H** and one oxygen" | one $^{1}$H, one $^{2}$H |

Stray digit-only lines survive at `ch-15:165` ("5 8"), `:226` ("8"), `:942`
("1 2"), `:1089` ("2"), and `appendices/app-a-math-and-equations.md:200`
("1 1 3").

### 3.4 Isotope superscripts turned into *footnote references* — Chapter 15 boron

Three places where `$^{10}$B` / `$^{11}$B` became `[^10]` / `[^11]`, which is
worse than a lost character: MyST resolves them as links to real footnotes with
entirely unrelated content (footnote 10 in this chapter is about helium in
natural gas; footnote 11 is about neutrinos).

| Location | As printed | Should read |
| --- | --- | --- |
| `ch-15:84` | "19.9% of boron is found in the form of **[^10]**, while the other**B** 80.1% is **[^11].B**" | in the form of $^{10}$B, while the other 80.1% is $^{11}$B |
| `ch-15:478` | "Boron (**[^10]** ) is a**B** favorite choice" | Boron ($^{10}$B) is a favorite choice |
| `ch-15:1031` | "…tend to contain **[^10]**, which has**B** a high neutron absorption cross section" | contain $^{10}$B, which has a high… |

### 3.5 Words fused where a line break was removed

The de-hyphenation step joined words that were never hyphenated. 26 instances:

`offthe` (`ch-16:254`, `ch-17:32`), `tounconditioned` (`ch-06:802`),
`thethereof` (`ch-20:429`), `stuffinto` (`app-b:75`), `nutsand-bolts`
(`epilogue:36`), `offis` (`ch-20:63`), `offinfrared` (`ch-09:792`), `offin`
(`app-d:28`), `offand` (`app-d:77`), `asthe` and `mightdo` (`ch-13:166`),
`cooledinside` (`ch-06:509`), `commonboundary` (`app-b:157`), `climbof`
(`ch-09:604`), `cuffassumptions` (`ch-12:88`), `debasketball` (`app-c:55`),
`resourcehogging` (`ch-02:396`), `naturallyoccurring` (`ch-15:73, 75`),
`mutuallyrepelling` (`ch-15:1193`), `wellstocked` (`ch-04:217`), `twofinger`
(`ch-04:129`), `fuelaided` (`ch-03:806`), `illconsidered` (`epilogue:59`),
`doublepaned` (`ch-13:694, 696`), `overcrack` (`ch-08:159`), `valitself`
(`app-c:101`), `termForecasting` (`back/image-attributions.md:39`),
`fourfactorial` (`app-a:542`).

Related: `ch-06:833` has "expend-**ing**" — a print hyphenation that was *not*
rejoined.

### 3.6 Dangling word fragments at page boundaries

Words split across a printed page were left split, so a paragraph begins with
half a word:

| Location | Fragment |
| --- | --- |
| `chapters/ch-02-economic-growth-limits.md:341` | "**sumed.** The real world is not partitioned…" (from "con-sumed") |
| `chapters/ch-04-space-colonization.md:298` | "**tation** as a *good* idea" (from "habi-tation"; `:296` ends "ocean floor habi-") |
| `chapters/ch-05-energy-and-power-units.md:761` | "**ence** is $10^{\circ}\mathrm{C}$" (from "differ-ence") |
| `chapters/ch-07-the-energy-landscape.md:144` | "**sured** by electrical *output*" (from "mea-sured"; `:142` ends "mea-") |

---

## 4. Structural and markup defects (conversion)

### 4.1 47 numbered margin notes lost

The print edition's numbered margin notes became Markdown footnotes, but 47 of
them are gone — neither referenced nor defined — leaving gaps in the numbering:

| File | Missing footnote numbers |
| --- | --- |
| `chapters/ch-02-economic-growth-limits.md` | 27 |
| `chapters/ch-03-population.md` | 36, 38 |
| `chapters/ch-05-energy-and-power-units.md` | 4, 14, 41 |
| `chapters/ch-06-putting-thermal-energy-to-work.md` | 16, 37 |
| `chapters/ch-08-fossil-fuels.md` | 27 |
| `chapters/ch-09-climate-change.md` | 7, 31, 62 |
| `chapters/ch-11-hydroelectric-energy.md` | 13, 16, 24, 25, 28, 40, 41 |
| `chapters/ch-12-wind-energy.md` | 27, 28, 30, 38, 39, 43 |
| `chapters/ch-13-solar-energy.md` | 15, 83, 87, 93 |
| `chapters/ch-14-biological-energy.md` | 5, 16 |
| `chapters/ch-15-nuclear-energy.md` | 30, 31, 86, 89 |
| `chapters/ch-18-human-factors.md` | 24, 49 |
| `chapters/ch-20-adaptation-strategies.md` | 1, 2, 17, 38, 49 |
| `appendices/app-b-chemistry-primer.md` | 17 |
| `appendices/app-d-alluring-tangents.md` | 13, 32, 34, 43 |

Two related symptoms:

1. **The marker survives as a raw math superscript** in the body, e.g.
   `ch-05:80` "…the height it is lifted through**.$^{4}$** The weight (force)…";
   `ch-02:354` "…of the total budget**.$^{27}$**"; `ch-11:255` "…capacity of
   20.7 GW**.$^{28}$**"; `ch-12:414` "…a lump of air moving at speed
   **$^{38}v$**"; `ch-13:889`; `ch-15:1116`; `ch-20:307`. Fourteen such
   markers remain (`app-a:148, 226`; `app-c:504`; `app-d:104`; `ch-02:354`;
   `ch-03:647, 658`; `ch-05:80`; `ch-08:169`; `ch-09:369`; `ch-11:255`;
   `ch-12:414`; `ch-14:135`; `ch-15:1116`).
2. **The note's text is absorbed into the preceding note or margin block**,
   with the number left inline. Examples: `ch-02:399` ("…missing
   transportation, for instance. **27: Federal grants comprise most of the
   rest**…"); `ch-03:704` ("…**36: The green bars indicate**…");
   `ch-05:100` ("More on gravitational potential energy in Chapter 11. **4:
   Another example of work**…"); `ch-08:164` (inside Figure 8.5's caption:
   "From U. Calgary. **27: Losing even a drop per second**…"); `ch-11:449`;
   `ch-12:417`; `ch-13:551`; `ch-14:415`; `ch-15:1214`.

### 4.2 202 figure alt-texts damaged

Every `:alt:` line is generated by stripping math from the caption and then
truncating. Consequences:

- **125 of 202** are hard-truncated at ~140 characters, mid-word. Example
  (`ch-01:66`): `:alt: The last 90 minutes in the sequence of bacteria (green)
  growing in a jar, doubling every 10 minutes. For the first 22.5 hours, hardly
  anythi`
- Stripped math leaves dangling punctuation and broken sentences, e.g.
  `ch-01:405` and `ch-09:209` "…across the projected area of the Earth's disk
  **, while radiating**…"; `ch-05:337` "…raises its temperature by **.**";
  `ch-13:413` "Panel tilts for Table 13.2, for **.**"; `ch-04:250` "the farthest
  humans have been…for the last **years**"; `ch-17:198` "red is bad **point)**".
- Em dashes are flattened to hyphens (`ch-01:405` "Earth-shown here in northern
  hemisphere summer-intercepts"), and cross-references are stripped to bare
  numbers.

For screen-reader users these are the *only* description of 202 figures.

### 4.3 Captions and titles split across block boundaries

The caption or admonition title ends up partly outside its own block, so it
renders in the wrong place:

- **Admonition titles split:** `ch-06:583` `::::{admonition} Box 6.4: Is`
  with `$>100\%$ **Really Possible?**` in the body; `ch-09:81`
  `::::{admonition} Box 9.1: Computing` with `CO$_{2}$ **ppm**$_\mathrm{v}$
  **from TW**` in the body; `ch-15:269` `::::{admonition} Box 15.2:` with
  `$E = mc^{2}$ **Everywhere**` in the body.
- **Admonitions with no title or label at all:** `ch-10:178`
  (`::::{admonition} Example`) and `ch-15:223` (`::::{admonition} Example`,
  whose real heading `**Example 15.2.2**` sits in the body — so Example 15.2.2
  cannot be cross-referenced).
- **Captions continuing outside the figure block:** `ch-06:290` (Figure 6.3,
  with "separation." alone in a margin), `ch-13:720` (Figure 13.23),
  `ch-13:453` (Figure 13.15, "been cloudless." in a margin), `ch-13:312`
  (Figure 13.8), `ch-15:163, 207, 405, 467, 501, 798` (Figures 15.5, 15.7,
  15.10, 15.13, 15.14, 15.19), `ch-07:193` (Figure 7.5), `ch-09:248`
  (Figure 9.7).
- **Paragraph breaks lost between list entries:**
  `ch-17-comparison-of-alternatives.md:131` ("…backyard-ready technology.
  **Hydroelectric** ([Chapter 11](#ch-11)): Despite…") and `:182`
  ("…waves in their backyard. **D–T Fusion** ([Sec. 15.5]…"). Also
  `ch-15:989`, where the paragraph beginning "The smaller number of positive
  points…" is swallowed into the final bullet of the fusion cons list.

### 4.4 Tables whose rows or columns were destroyed

- **`ch-04` Table 4.2** (line 118) is unusable. The fraction numerators became
  their own rows and the astronomical symbols were replaced by ASCII:

  ```
  | Moon | $\$$ | $4R_{\oplus}$ |   | $60R_{\oplus}\approx 240R\$$ |
  |   |   |   | 400 |   |
  | Sun | $\odot$ | $100R_{\oplus}$ | 1 | $240R_{\odot}$ |
  |   |   | 1 |   |   |
  | Mars | $\mars$ | $2R_{\oplus}$ | 0.4–2.7 |   |
  ```

  Per [Definition 4.1.1](#def-4-1-1) the Moon's radius is $\frac14 R_\oplus$
  (not $4R_\oplus$), Mars is $\frac12 R_\oplus$ (not $2R_\oplus$) and Jupiter is
  $\approx\frac{1}{10}R_\odot$ (not $10R_\odot$) — the stray `1` rows are the
  lost numerators. The Moon symbol renders as `$\$$` and Jupiter/Neptune as
  `$X$` / `$[$`.
- **`ch-05` Table 5.2** (line 148): the kinetic-energy row reads
  `| kinetic | $_{2}mv^{2}$ |` with a bare `| 1 |` row above it —
  $\frac12mv^2$ split in two.
- **`ch-06` Table 6.2** (line 226): a three-column table collapsed to two; the
  header is `| Source | % elec. therm. turb./ in U.S. gen. |` and the data
  cells read `35.3 ✓ ✓`.
- **`ch-09` Table 9.2** (line 97): `| Operation | Resulting Units | Coal Oil |
  Gas |` — the Coal and Oil columns merged; data cells read
  `$x = 6.5$ $x = 11.5$`.
- **`ch-13` Table 13.1** (line 294): the ⊕ subscripts became their own rows —
  `| Absorbed by $\pi R^{2}$ | 960 |` / `| $\oplus$ | |` (twice).
- **`ch-15` Tables 15.3, 15.5, 15.7, 15.9, 15.10**: same pattern — every
  isotope's mass number occupies a blank row of its own above the element
  symbol, e.g. `| 56 | | |` then `| Fe | 56 | 55.935 |`.
- **`ch-13` Problem 26** (line 879): a full 13-column month table crushed into
  a single table cell (and Problem 27 at line 889 refers back to it).

### 4.5 Stray artefacts left in the body text

- `chapters/ch-05-energy-and-power-units.md:15` — a line of OCR from the
  chapter-opening photograph of a utility bill is sitting in the body directly
  under the chapter heading: `Gas Jun 29, 2020 - Jul 29, 2020 4 Therms 7.01`
- `chapters/ch-08-fossil-fuels.md:30–35` — leftover axis labels from the
  hand-drawn Figure: a two-row table `| 0 |` / `| 0 |`, plus three margin
  blocks reading `-10,000 10,000`, `10,000`, `10,000`.
- `chapters/ch-06-putting-thermal-energy-to-work.md:275` — a stray `4:0 (1)`
  line and a `4 (1)` margin, both from inside Figure 6.3.
- `chapters/ch-10-renewable-overview.md:120–124` — a stray `[63–65].` line and
  a math block containing only `\ , \odot`.
- `chapters/ch-12-wind-energy.md:218` — a stray `5D` line (a figure label).
- `chapters/ch-15-nuclear-energy.md:153` — `⚠⚠⚠ $\alpha$ ⚠⚠`; `:305` —
  `⚠⚠⚠⚠⚠⚠+ Energy ⚠ ⚠`.
- `chapters/ch-09-climate-change.md:18, 53, 69` — unbalanced bold markers left
  in section headings, which will render literally:
  `## 9.1 The Source of** CO$_{2}$`, `### 9.1.1** CO$_{2}$ **Measurements`,
  `### 9.1.2** CO$_{2}$ **Expectations`. As a side effect the `(sec-9-1-1)=`
  and `(sec-9-1-2)=` anchors are missing, so those two subsections cannot be
  cross-referenced.
- `front/how-to-use-this-book.md:24` — the ⌘ key symbols were dropped, leaving
  "the back and forward functions are accomplished with cursor/arrow keys as
  **-and -**. In Mac Preview, **-[ and -]** go back and forward."
- `chapters/ch-04-space-colonization.md:344` — the four lines of the *Stressed
  Out* lyric are run together into a single paragraph with no line breaks.
- `chapters/ch-01-exponential-growth.md:161` — a margin note begins abruptly
  with `$5^{12}$.`; it is the continuation of footnote 6, which itself ends
  mid-sentence ("…which is just 12 fives multiplied, **or**").
- `chapters/ch-07-the-energy-landscape.md:267` — a footnote marker survives as
  the literal text `$^{0\mathrm{mm}}$`: "almost 8 times$^{0\mathrm{mm}}$ the
  global average", with the margin note beginning `0mm: The math is…`.
- `chapters/ch-06-putting-thermal-energy-to-work.md:770` — Problem 12 has prose
  pulled inside a math block: `:::{math}` `relation that \Delta Q = T\Delta S ?`
  `:::`. Same at `chapters/ch-13-solar-energy.md:816`.
- `chapters/ch-03-population.md:756–766` — Problem 22's answer blanks render as
  a broken list: `1.` `2.` `3.` `4.` then `5. E.`
- Many multi-part problems lost their line breaks, so options run together on
  one line: `ch-03:690`, `ch-04:439`, `ch-07:295`, `ch-09:759`, `ch-15:1053`,
  `ch-20:610`.

### 4.6 Cross-references and citations not converted

- **12 bibliography citations** were not turned into links, so they render as
  bare bracketed numbers: `ch-02:43`, `ch-02:76`, `ch-03:26`, `ch-04:10`,
  `ch-04:191`, `ch-08:343`, `ch-10:120`, `ch-10:162`, `ch-12:264`, `ch-13:440`,
  `ch-15:666`, `ch-18:50`.
- **31 internal cross-references** in body text remain unlinked while the
  surrounding ones are linked — e.g. `ch-05:546` "(Eq. 5.2)", `ch-12:169` and
  `:247` "Eq. 12.2", `ch-13:546` "(Figure 13.16)", `ch-15:666` "(Fig. 13.16;
  p. 225)", `ch-19:250` "Table 15.9 (p. 268)", `ch-20:423–466` "Eq. 20.1" (×4),
  and all ten `Chap. NN` entries in `ch-10:24–42`.
- **Sub-subsection references are malformed**, with the last component falling
  outside the link: `ch-15:445` and `ch-17:157` both read
  `[Section 15.4.4](#sec-15-4-4)**.2**`.

The good news: footnote pairing is otherwise complete (0 orphans, 0 dangling
references), all 947 labels resolve, no table has ragged columns, and all 129
bibliography entries are present, unduplicated and correctly targeted.

---

## 5. Appendix C is unusable

`appendices/app-c-selected-answers.md` needs to be regenerated from scratch.
The print edition sets the answer key in two narrow columns; the converter read
across both columns, so answers from different chapters are interleaved line by
line throughout all 810 lines. Every entry in the file is affected.

Representative sample (`app-c:75–99`):

```
4. Comparable to world population 200 years 9. A good deal farther than the moon, but still

ago well short of the sun/Mars

...

13. Add almost a half million; more than half 19. Double the gasoline from previous prob-

million born; less than half million died lem; gasoline mass almost as much as the car

14. Answers should round to the table valitself

ues
```

Consequences:

- **Chapter headings are contaminated** with answer text and carry unbalanced
  bold markers: `## Chapter 1** 20. A smidge higher then boiling` (line 15),
  `## Chapter 5** 29. Between 1 and 2 hours per day` (119),
  `## Chapter 9** 29. Sum to about 700 years…` (321),
  `## Chapter 13** 26. Best at latitude…` (526),
  `## Chapter 17** 8. Wait; who has my…` (744),
  `## Chapter 18** 2. What needs to happen to avert?` (762).
- **Two headings are not headings at all** but promoted answer text:
  `## 10. May help to think of something once preva- **Chapter 4` (49) and
  `## 13. Sensibly, a little less than 2 minutes **Chapter 6` (145).
- **Chapters 7, 8, 11, 12 and 15 have no heading at all.**
- **The chapters are out of order**: Chapter 4 (49) precedes Chapter 3 (63);
  Chapter 20 (760) precedes Chapter 18 (762) and Chapter 19 (794).
- **No section anchors** are emitted anywhere in the file.
- Words are split across the column join, leaving fragments as separate
  paragraphs: `ues` (103), `ond` (468), `lem` (99), `ment` (167), `tive` (700),
  `mand` (806), `pendencies` (57), `entries` (87).

One author erratum is visible through the damage, at line 15: "A smidge higher
**then** boiling" — should be **than**.

---

## 6. Edition-consistency notes

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
| Numerical / factual errors | 17 |
| Missing space after inline math | 58 |
| Scrambled paragraphs | 4 (+ all of Appendix C) |
| Sentences lost or truncated | 5 |
| Glossary definitions lost | 3 |
| Chapter 15 isotope superscripts detached | 9 passages + 3 turned into wrong footnote links |
| Words fused at line breaks | 26 |
| Dangling word fragments | 4 |
| Footnotes lost entirely | 47 |
| Footnote markers left as raw superscripts | 14 |
| Figure alt-texts truncated mid-word | 125 (of 202 damaged) |
| Split captions / admonition titles | 15 |
| Tables with destroyed structure | 9 |
| Stray artefacts in body text | 14 |
| Unlinked citations | 12 |
| Unlinked cross-references | 31 |
