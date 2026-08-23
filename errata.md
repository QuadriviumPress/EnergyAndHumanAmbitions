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
missing "million" (and "to to" is a doubled word — see §3.1).
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

## 2. Spelling and wrong-word errors

All confirmed by inspection; the ones flagged by `hunspell` are noted.

| Location | As printed | Should be |
| --- | --- | --- |
| `chapters/ch-04-space-colonization.md:142` | "not enough to allow it **climb** out" | allow it **to** climb out |
| `chapters/ch-04-space-colonization.md:167` | "a brightly **growing** grain of sand" | brightly **glowing** |
| `chapters/ch-06-putting-thermal-energy-to-work.md:218` | "Steam…races **though** the turbine" | **through** |
| `chapters/ch-06-putting-thermal-energy-to-work.md:757` | "**equipped a** 5,000 W heater" | equipped **with** a |
| `chapters/ch-08-fossil-fuels.md:564` | "on American's **behalfs**" | **behalf** |
| `chapters/ch-12-wind-energy.md:396` | "sits atop **very** square meter" | **every** |
| `chapters/ch-15-nuclear-energy.md:878` | "oppose building more nuclear **plant**" | **plants** |
| `chapters/ch-15-nuclear-energy.md:994` | "a significant fraction **the** world's power" | fraction **of** the |
| `chapters/ch-15-nuclear-energy.md:1157` | "lose in a year **trough** pure energy conversion" | **through** |
| `chapters/ch-16-small-players.md:87` | "thermal energy under **out** feet" | **our** |
| `chapters/ch-16-small-players.md:381` | "than **as set** of hopeful candidates" | as **a** set |
| `chapters/ch-16-small-players.md:447` | "moderating the tides by **filing** in the gaps" | **filling** |
| `chapters/ch-19-a-plan-might-be-welcome.md:88` | "particularly acute **aver** the Antarctic" | **over** |
| `chapters/ch-19-a-plan-might-be-welcome.md:142` | "evidence that the ground **rushing up**" | the ground **is** rushing up |
| `chapters/ch-19-a-plan-might-be-welcome.md:260` | "monosodium-**glutimate** (MSG)" | glut**a**mate (hunspell) |
| `chapters/ch-20-adaptation-strategies.md:215` | "natural gas **form** a power plant" | **from** |
| `chapters/ch-20-adaptation-strategies.md:308` | "among those for whom air travel **is a utilized**" | is **utilized** / is a utilized **option** |
| `chapters/ch-20-adaptation-strategies.md:493` | "author's 2019 **expenditures energy**" (Table 20.4 caption) | **energy expenditures** |
| `chapters/ch-20-adaptation-strategies.md:562` | "we do get to **chose** the plan" | **choose** |
| `chapters/ch-20-adaptation-strategies.md:582` | "should not **underestimated**" | should not **be** underestimated |
| `appendices/app-a-math-and-equations.md:449` | "It would **like like** this" | would **look like** |
| `appendices/app-d-alluring-tangents.md:461` | "made **possble** by" | **possible** (hunspell) |
| `back/image-attributions.md:19` | "The History Trust of South **Australian**" | South **Australia** |

Also: `chapters/ch-17-comparison-of-alternatives.md:17` uses "**lynchpin**", a
nonstandard variant of *linchpin*.

---

## 3. Grammar

### 3.1 Doubled words

Twelve genuine cases (a thirteenth, "ha ha" at `ch-14:374`, is intentional):

| Location | Text |
| --- | --- |
| `chapters/ch-03-population.md:46` | "If we extend **the the** 0.04% line" |
| `chapters/ch-03-population.md:793` | "recalling **that that** the natural log" (footnote 3) |
| `chapters/ch-04-space-colonization.md:88` | "about 25,000 light years **away away**" |
| `chapters/ch-08-fossil-fuels.md:88` | "it can serve **to to** counterbalance" |
| `chapters/ch-09-climate-change.md:837` | "how/why **in in** [Section 13.2]" (footnote 19) |
| `chapters/ch-11-hydroelectric-energy.md:410` | "Each millimeter **of of** water depth" |
| `chapters/ch-13-solar-energy.md:920` | "solar payback **time time**" |
| `chapters/ch-15-nuclear-energy.md:405` | "profitable on **the the** left-hand side" |
| `chapters/ch-15-nuclear-energy.md:1227` | "reduces energy yield a bit **to to** 137" |
| `chapters/ch-16-small-players.md:149` | "produced **in in** Nevada" |
| `appendices/app-a-math-and-equations.md:250` | "Notice that **the the** symbols" |
| `back/glossary.md:542` | "a broad term that **can can** describe light" |

### 3.2 Subject–verb agreement

| Location | Text | Fix |
| --- | --- | --- |
| `front/how-to-use-this-book.md:26` | "supplemental content that **build** useful contextual links" | build**s** |
| `chapters/ch-02-economic-growth-limits.md:159` | "6 rabbits **does** not imply" | **do** |
| `chapters/ch-02-economic-growth-limits.md:354` | "student payments…**accounts** for 40%" | account |
| `chapters/ch-02-economic-growth-limits.md:421` | "Growth in both workforce and investments **are** essential" | **is** (footnote 22) |
| `chapters/ch-03-population.md:499` | "**Asia's** demands…**their** already-dominant population" | **its** |
| `chapters/ch-05-energy-and-power-units.md:180` | "The **differences**…**is** about *coherence*" | difference is / differences are |
| `chapters/ch-07-the-energy-landscape.md:190` | "the recent **entry** of wind and solar…**are** the most interesting" | **is** (Fig. 7.5 caption) |
| `chapters/ch-07-the-energy-landscape.md:238` | "The **source** of numbers for this section **mix**" | mix**es** (Box 7.3) |
| `chapters/ch-08-fossil-fuels.md:153`, `:417` | "the **chances** of finding any…**is** about 0.01%"; "The **chances** of striking oil…**is**" | **are** (twice) |
| `chapters/ch-08-fossil-fuels.md:302` | "past civilizations **overextend** and collapsed" | overextend**ed** |
| `chapters/ch-08-fossil-fuels.md:361` | "the **amount** of oil and gas remaining **are**" | amount**s**…are |
| `chapters/ch-08-fossil-fuels.md:588` | "what…**experiences** do you imagine **contributes**" | contribute |
| `chapters/ch-12-wind-energy.md:186` | "**Each** of the 7 designs shown **have** arched curves" | **has** (Fig. 12.4 caption) |
| `chapters/ch-12-wind-energy.md:356` | "Life-cycle CO₂ **emissions** for wind **is** only 2%" | **are** |
| `chapters/ch-13-solar-energy.md:734` | "a **field** of PV panels **outperform** an ST installation" | outperform**s** |
| `chapters/ch-15-nuclear-energy.md:857` | "Life-cycle CO₂ **emissions** for nuclear fission **is** only 2%" | **are** |
| `chapters/ch-18-human-factors.md:112` | "The prevailing **narrative** of growth and progress **are** so firmly rooted" | **is** |
| `chapters/ch-18-human-factors.md:207` | "The **combination** of capitalism and democracy **have** been ideal" | **has** |
| `chapters/ch-18-human-factors.md:207` | "how **do either work** in a decline scenario" | **does** either work |
| `appendices/app-b-chemistry-primer.md:242` | "$N$…and $n$…**differs** simply by a factor" | differ |

Also, `ch-13:851` and `ch-13:876` use "emissions are…smaller than **that** of";
should be "**those** of".

### 3.3 Other grammatical faults

- `chapters/ch-08-fossil-fuels.md:271` — spurious comma between subject and
  verb: "Extracting energy from fossil fuels**,**[^43] leaves no choice…"
- `chapters/ch-10-renewable-overview.md:142` — same fault: "human
  metabolism**,**[^17] is about 0.8 TW".
- `chapters/ch-10-renewable-overview.md:63` — missing comma: "Solar energy, for
  instance is not 'used up'" → "for instance**,** is".
- `chapters/ch-15-nuclear-energy.md:888` — "**It's** main problem is that it is
  incredibly difficult" → possessive **Its**.
- `chapters/ch-01-exponential-growth.md:599` — "more intense there due to
  **it's** being closer to the sun" → **its**.
- `chapters/ch-01-exponential-growth.md:567` — "Ignoring the fact that **it
  impossible** to get to them" → "that it **is** impossible".
- `chapters/ch-17-comparison-of-alternatives.md:17` — spurious comma before the
  verb: "Hydroelectricity, nuclear fission, wind, and solar photovoltaics**,**
  had all been invented."
- `chapters/ch-17-comparison-of-alternatives.md:257` — "**What is at about** the
  backyard attribute" → "What is **it** about".
- `chapters/ch-18-human-factors.md:24` — "**both** individually **or**
  collectively" → "both individually **and** collectively".
- `chapters/ch-18-human-factors.md:216` — "climate change or other
  resource/planetary limitations **removes** the fossil fuel source" — with
  *or* the verb should agree with the nearer subject: **remove**.
- `chapters/ch-19-a-plan-might-be-welcome.md:175` — "that from which all value
  ultimately **depends** and derives" → "**on** which all value ultimately
  depends".
- `chapters/ch-20-adaptation-strategies.md:638` — Problem 22 opens with a
  subjectless fragment: "Comparing the human body to a car with a gas tank, and
  recognizing that a human can *live* for about two weeks without food,
  provided adequate water and shelter."
- `appendices/app-a-math-and-equations.md:210` — sentence fragment: "**Since**
  $\frac{1}{3}$ is larger than $\frac{1}{4}$**.** So adding…" — the *Since*
  clause has no main clause.
- `appendices/app-b-chemistry-primer.md:45` — garbled sentence: "This means
  that an accurate count of how many of each atom type are present at the
  start, a proper count at the end should yield *exactly* the same results."
- `appendices/app-b-chemistry-primer.md:113` — "This problem can be approached
  in **Two** equivalent ways" — stray capital.
- `chapters/ch-02-economic-growth-limits.md:394` — "Justify what, **In** your
  mind, is a reasonable lower limit" — stray capital.
- `chapters/ch-03-population.md:341` — "As suggested by [Figure 3.9](#fig-3-9),
  **Human** population is *not* following…" — stray capital.
- `chapters/ch-12-wind-energy.md:332` — "Putting a few of the previous results
  together, **If** the entire contiguous U.S…." — stray capital.

---

## 4. Punctuation and typography

### 4.1 Missing sentence-ending punctuation

| Location | Text |
| --- | --- |
| `chapters/ch-02-economic-growth-limits.md:159` | "…any more (e.g., see [Figure 2.3](#fig-2-3))**_** One way to put it is…" — missing period after the parenthesis |
| `chapters/ch-03-population.md:787` | "…a biological child of their own[^45]**_** Consider not only personal contexts…" |
| `chapters/ch-06-putting-thermal-energy-to-work.md:649` | "…works out to 30/10, or 3.0**_** The COP is then simply 3.0." |
| `chapters/ch-09-climate-change.md:649` | "…sea level has risen about 230 mm**_** At the *current* rate…" |
| `chapters/ch-18-human-factors.md:301` | "…experiencing 5% less energy each year[^50]**_** A new renewable energy infrastructure effort…" |
| `back/glossary.md:23` | "…ejected from a larger nucleus in an alpha decay**_** It therefore consists of two protons…" |

### 4.2 Doubled or stray punctuation

- `chapters/ch-04-space-colonization.md:270` — "breathtaking views**!.**"
- `chapters/ch-08-fossil-fuels.md:131` — "…goes to industrial processes.[^23]**.**"
- `chapters/ch-08-fossil-fuels.md:182` — "…and 22% globally.[^33]**.**"
- `chapters/ch-13-solar-energy.md:889` — "…highest number for each month.[^114]**.**"
- `chapters/ch-13-solar-energy.md:844` — "whose band gap is 1.1 eV**„**" — a
  comma followed by U+201E (the only occurrence of that character in the book)
- `chapters/ch-05-energy-and-power-units.md:816` — "(it **doesn't'**)" — stray apostrophe
- `chapters/ch-10-renewable-overview.md:200` — "at a rate of 30 MW**,**[^24]**,** then we *could*…" — doubled comma
- `appendices/app-a-math-and-equations.md:116` — "…perimeter of the square**,**[^11]**,** but a good deal larger…" — doubled comma
- `chapters/ch-06-putting-thermal-energy-to-work.md:751` — "…at a rate of 700 W**.** How long should you run…" — the period makes a fragment of the conditional clause; should be a comma
- `chapters/ch-15-nuclear-energy.md:380` and `back/glossary.md:530` — "56.46340 a.m.u**..**" / "1.0072765 a.m.u**..**"

### 4.3 Quotation marks

The book has 578 opening and 576 closing curly double quotes — a mismatch of
two. Five specific faults:

| Location | Text |
| --- | --- |
| `front/preface.md:25` | internalize (**“own"**) — straight closing quote |
| `chapters/ch-05-energy-and-power-units.md:318` | note the capital **”C”** — the opening mark is a *closing* curly quote |
| `chapters/ch-06-putting-thermal-energy-to-work.md:803` | not **“thermally woke"** — straight closing quote |
| `chapters/ch-08-fossil-fuels.md:588` | **“run out one day,"** — straight closing quote |
| `chapters/ch-16-small-players.md:17` | some of the **"but what about *insert-scheme*?"** questions — both marks straight |

Additionally, `chapters/ch-19-a-plan-might-be-welcome.md:156` has an **unclosed
quotation**: Dr. Daly's first line of dialogue opens with `“great, now draw a
box around this and label it: The Environment.` and is never closed — the
narration "The obvious point is that all economic activity takes place *inside*
the environment." runs on inside the quotation.

### 4.4 Declarative/imperative sentences ending in a question mark

Seven cases where a command is punctuated as a question:

- `chapters/ch-02-economic-growth-limits.md:385`, `:392` — "Based on your present state of knowledge, **detail** what you think an optimist/pessimist might say…**?**"
- `chapters/ch-02-economic-growth-limits.md:394` — "**Justify** what…is a reasonable lower limit…**?**"
- `chapters/ch-03-population.md:718` — "In a few clear sentences, **explain** why the maps…look so different…**?**"
- `chapters/ch-07-the-energy-landscape.md:299` — "Building off the result in Problem 2, **calculate** the percentages…**?**"
- `chapters/ch-12-wind-energy.md:443` — "**Provide** a clear explanation of why…**?**"
- `chapters/ch-13-solar-energy.md:825` — "**Explain** how both things can be true**?**"

A few similar cases end with a period where a question mark is wanted, e.g.
`chapters/ch-20-adaptation-strategies.md:577` ("And how bad would it be if we
'built some character' along the way for no reason**.**") and
`appendices/app-a-math-and-equations.md:18` ("so why carry extra digits**.**").

### 4.5 Dash and hyphen misuse

Five places use an en dash where an em dash or a hyphen belongs:

- `chapters/ch-14-biological-energy.md:230` — "5 came out**–**only 1 of the 5" (em dash)
- `chapters/ch-14-biological-energy.md:434` — "our demand**–**not just 5 times" (em dash)
- `chapters/ch-15-nuclear-energy.md:568` — "energy**–**dense" (hyphen)
- `appendices/app-a-math-and-equations.md:562` — "complicated**–**looking" (hyphen)
- `appendices/app-d-alluring-tangents.md:212` — "hardest**–**to**–**easiest" (hyphens)

### 4.6 Minor style inconsistencies

- `chapters/ch-02-economic-growth-limits.md:177` "transatlantic" vs.
  `chapters/ch-04-space-colonization.md:208` "trans-atlantic".
- `front/preface.md:31` "off-putting" vs. `chapters/ch-18-human-factors.md:156`
  "offputting".
- `chapters/ch-18-human-factors.md:64` "over-representation" vs. `:71`
  "underrepresentation".
- `back/notation.md:31` "Stefan-Boltzmann" (hyphen) vs. everywhere else
  "Stefan–Boltzmann" (en dash).
- `chapters/ch-01-exponential-growth.md:210` — "ln 2 $\approx 0.693 \approx
  **.70**$" — leading zero dropped.
- `chapters/ch-08-fossil-fuels.md:449` — "the mid **80s**" → "mid-1980s".
- `index.md:36` uses British "labelled" in an otherwise US-spelling edition.

---

## 5. Broken mathematics (conversion defects)

The conversion pipeline reconstructs fractions and radicals from glyph
geometry. In the following places it failed, and the equation as published is
either wrong or unreadable. This is the most serious class of defect in this
edition.

### 5.1 Equations with pieces lost or relocated

| Equation | Location | As printed | Should be |
| --- | --- | --- | --- |
| Eq. 3.2 | `ch-03-population.md:93` | `t - t_{0}= lnln (1 (+ ^{\frac{P}{P_{0}}} p))` | $t-t_0=\dfrac{\ln(P/P_0)}{\ln(1+p)}$ |
| Eq. 3.6 | `ch-03-population.md:238` | `P(t) = 1 + e^{-r(t-t_{0})}.Q` | $P(t)=\dfrac{Q}{1+e^{-r(t-t_0)}}$ |
| Eq. 5.4 | `ch-05-energy-and-power-units.md:611` | `E = h\nu = hc` followed by a separate math block containing `\lambda,` | $E=h\nu=\dfrac{hc}{\lambda}$ |
| Eq. 5.5 | `ch-05-energy-and-power-units.md:641` | `E_{\mathrm{eV}}= \lambda (\mu \mathrm{m}) eV .1.24` | $E_\mathrm{eV}=\dfrac{1.24}{\lambda(\mu\mathrm{m})}$ |
| Eq. 6.10 | `ch-06-putting-thermal-energy-to-work.md:535` | `\epsilon_{cool}\le \frac{}{} = \frac{T_c}{\Delta T}` plus a spurious 3-row table holding $T_\mathrm{c}$, $T_\mathrm{h}-T_\mathrm{c}$, $T_\mathrm{h}$ | $\epsilon_\mathrm{cool}\le\dfrac{T_\mathrm{c}}{T_\mathrm{h}-T_\mathrm{c}}$ |
| Eq. 6.11 | `ch-06-putting-thermal-energy-to-work.md:558` | `\epsilon_{heat}\le \frac{}{T_h-T_c}` — empty numerator | $\epsilon_\mathrm{heat}\le\dfrac{T_\mathrm{h}}{T_\mathrm{h}-T_\mathrm{c}}$ |
| Eq. 6.13, 6.15 | `ch-06…:666`, `:702` | `\mathrm{EER}[\frac{Btu}{Wh}] 3600\mathrm{J/Wh} = \mathrm{EER}\cdot 0.293,1055\mathrm{J/Btu}` | EER × (1055 J/Btu)/(3600 J/Wh) = EER × 0.293 |
| Eq. 9.4 | `ch-09-climate-change.md:310` | `T = [\frac{RF_{\odot}}{\sigma}]0.25 + 33` — exponent lost its superscript | $T=\left[\frac{RF_\odot}{\sigma}\right]^{0.25}+33$ (Eq. 9.6 has it right) |
| Eq. 12.3 | `ch-12-wind-energy.md:225` | `\frac{\epsilon\rho\pi R^2 v^3}{ ^{\frac{1}{2}} 480R^2}` — the ½ landed in the denominator | $\dfrac{\frac{1}{2}\epsilon\rho\pi R^2v^3}{480R^2}$ |
| Eq. 13.1 | `ch-13-solar-energy.md:39` | `= ^{\frac{hc}{\lambda}} \approx … = \lambda 1(.\mathrm{i}2\mathrm{n}4\mu \mathrm{emV})` — the last term is character-interleaved gibberish | …$=\dfrac{1.24}{\lambda(\mathrm{in}\ \mu\mathrm{m})}$ eV |
| Eq. 13.4 | `ch-13-solar-energy.md:92` | `B_\lambda = \frac{2\pi hc^2}{\lambda^5}\frac{}{}\frac{W/m^2}{m}]` plus a spurious table holding `[`, `1`, `e^{hc/\lambda k_B T}-1` | $B_\lambda=\frac{2\pi hc^2}{\lambda^5}\frac{1}{e^{hc/\lambda k_\mathrm{B}T}-1}$ |
| Eq. 16.2 | `ch-16-small-players.md:184` | `\frac{\epsilon mg}{\Delta t ^{\frac{h}{2}}}` — the $h/2$ landed in the denominator | $\dfrac{\epsilon mg\frac{h}{2}}{\Delta t}$ |
| Eq. 16.5 | `ch-16-small-players.md:282` | `\frac{\rho\lambda\ell gA^2}{}` plus a spurious table holding `16\Delta t`, `8`, `= \rho gA^2 v` | $\dfrac{\rho\lambda\ell gA^2}{16\Delta t}$ |
| Eq. 16.6 | `ch-16-small-players.md:295` | `P_{tot} = \frac{\rho\ell gA^2v}{}` — empty denominator; also numbered as literal text "(16.6)" so it carries no label | $\dfrac{\rho\ell gA^2v}{8}$ |
| Eq. 16.7 | `ch-16-small-players.md:303` | `\frac{P_{tot}}{\ell} 8` — the whole right-hand side is missing; also literal "(16.7)" | $\dfrac{P_\mathrm{tot}}{\ell}=\dfrac{\rho gA^2v}{8}$ (which is what yields the text's 3,750 W/m) |
| Eq. A.2 | `appendices/app-a…:159` | `b \cdot ^{\frac{x}{y}} = ^{\frac{?}{?}}` plus an orphan `\frac{a}{}` block and literal "(A.2)" | $\frac{a}{b}\cdot\frac{x}{y}=\frac{?}{?}$ |
| Eq. A.3 | `appendices/app-a…:170–174` | "In math terms: 1 1 3 / 2 $\cdot ^{\frac{1}{2}} = ^{\frac{1}{4}}$…" then `\frac{}{3} = 1.` | $\frac12\cdot\frac12=\frac14$; $\frac12\cdot\frac45=\frac25$; $\frac13\cdot\frac33=1$ |
| Eq. A.4 | `appendices/app-a…:181` | `^{\frac{a}{b}} \cdot ^{\frac{x}{y}} = …`; literal "(A.4)" | $\frac{a}{b}\cdot\frac{x}{y}=\frac{a\cdot x}{b\cdot y}$ |
| Eq. A.5 | `appendices/app-a…:200–206` | "1 1 3 / 2 $+ 1 2 + ^{\frac14}=^{\frac34}$; 4 $<^{\frac12}+1$" then `\frac{}{2} = 1; \frac{}{} \frac{}{} \frac{}{} \frac{}{} \frac{}{} \frac{}{3} < 1` | $\frac12+\frac12=1$; $\frac12+\frac14=\frac34$; $\frac12+\frac13<1$ |
| Eq. A.6 | `appendices/app-a…:246` | `x^{n}= ?1` (third clause) | $\frac{1}{x^n}=?$ |
| Eq. A.9 | `appendices/app-a…:279` | `x^{n}= x^{-n}.1` | $\frac{1}{x^n}=x^{-n}$ |
| Eq. A.12 | `appendices/app-a…:393` | `= \sqrt{c^{2}}- b^{2}` — the radical does not cover the subtraction | $\sqrt{c^2-b^2}$ |
| Eq. B.1 | `appendices/app-b…:144` | `10012c + h + 16o + 14n kcal /\mathrm{g}.c + 0.3h - 0.5o` | $\dfrac{100(c+0.3h-0.5o)}{12c+h+16o+14n}$ kcal/g — confirmed by the worked sucrose example (13.1/342 = 3.8) and by all six rows of Table B.1 |
| Eq. B.3 | `appendices/app-b…:203` | `R = 8.314 mol \cdot \mathrm{K.J}` | $R=8.314\ \mathrm{J/(mol\cdot K)}$ |
| Eq. B.5 | `appendices/app-b…:235` | `k_B = 1.3806\times10^{-23} J` then a separate math block `\mathrm{K}.` | $1.3806\times10^{-23}$ J/K |

### 5.2 Other broken math and math-adjacent text

- `chapters/ch-16-small-players.md:455` — footnote 26: "$(v = **pgd**)$" — the
  radical sign became the letter `p`; should be $v=\sqrt{gd}$.
- `appendices/app-a-math-and-equations.md:120` — "throw in a **$pi/3$** factor" —
  the LaTeX command lost its backslash; should be `$\pi/3$`.
- `appendices/app-a-math-and-equations.md:434` — the drag-force dimension check
  has `(\frac{\mathrm{m}}{\mathrm{s}})**2**` — exponent lost its superscript.
- `appendices/app-a-math-and-equations.md:447–461` — Example A.10.2's
  unit-conversion chains are unreadable: `person $=10^{4}\mathrm{J/s}$ person
  $\cdot$ s $,10^{4}$ J`, then `person $\cdot$ s $\cdot 60 \mathrm{s}10^{4}$ J 1
  $\min \cdot 60$ min1 hour $\cdot 24$ hour1 day $\cdot 365$ day1 year`, then
  `$3.15 \times 10^{11}$ year $\cdot$ person$.\mathrm{J}$`.
- `appendices/app-a-math-and-equations.md:473` — Example A.10.3 likewise:
  `$1.04 \times 10^{20}$ year $\cdot 1$ BtuJ $1,$ 055 J $\cdot 1$
  quadrillion$10^{15}\approx 100$ quadrillion $\mathrm{Btu}/$year$.$`
- `appendices/app-a-math-and-equations.md:413` — Example A.10.1: `42 m s $=
  \frac{4}{2}\cdot$ m` followed by `\frac{}{\mathrm{s}} = 2\mathrm{m/s}`.
- `chapters/ch-09-climate-change.md:559`, `:580` — the two tables inside
  Examples 9.4.2 and 9.4.3 lost their structure entirely; the header
  ("component math depth (m)") and all rows run together on one line.
- `chapters/ch-14-biological-energy.md:380` — Problem 5: "**5 $\times 10^{1}4$
  kg**" — should be $5\times10^{14}$ kg. ("4kcal/g" in the same line is also
  missing a space.)
- `chapters/ch-15-nuclear-energy.md:1103` — Problem 24: "express the result in
  the notation $^{\mathrm{A}}$**.X**" — should be $^{A}$X.
- `chapters/ch-08-fossil-fuels.md:123–131` and
  `chapters/ch-15-nuclear-energy.md:928–932` — in each case a set of three
  reactions is given, but only the middle one is inside a numbered math block
  (Eq. 8.1, Eq. 15.3); the other two are inline text, so the equation label
  covers only one third of what it names.

### 5.3 Missing space after inline math

58 places where a closing `$` is followed immediately by an English word, e.g.
`ch-01:362` "$\sigma$is the Stefan–Boltzmann constant", `ch-05:215` "$m$is 10
kg", `ch-13:100` "$\lambda$and $T$ are variable", `ch-15:173` "$A$by 4",
`ch-16:184` "$\epsilon$is the efficiency". Concentrated in
`ch-13-solar-energy.md` (37) and `ch-09-climate-change.md` (5).

---

## 6. Lost and scrambled text (conversion defects)

### 6.1 Text reordered across the print columns

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

**`appendices/app-c-selected-answers.md`** — the whole file; see §8.

### 6.2 Sentences truncated or lost outright

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

### 6.3 Isotope superscripts detached throughout Chapter 15

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

### 6.4 Isotope superscripts turned into *footnote references* — Chapter 15 boron

Three places where `$^{10}$B` / `$^{11}$B` became `[^10]` / `[^11]`, which is
worse than a lost character: MyST resolves them as links to real footnotes with
entirely unrelated content (footnote 10 in this chapter is about helium in
natural gas; footnote 11 is about neutrinos).

| Location | As printed | Should read |
| --- | --- | --- |
| `ch-15:84` | "19.9% of boron is found in the form of **[^10]**, while the other**B** 80.1% is **[^11].B**" | in the form of $^{10}$B, while the other 80.1% is $^{11}$B |
| `ch-15:478` | "Boron (**[^10]** ) is a**B** favorite choice" | Boron ($^{10}$B) is a favorite choice |
| `ch-15:1031` | "…tend to contain **[^10]**, which has**B** a high neutron absorption cross section" | contain $^{10}$B, which has a high… |

### 6.5 Words fused where a line break was removed

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

### 6.6 Dangling word fragments at page boundaries

Words split across a printed page were left split, so a paragraph begins with
half a word:

| Location | Fragment |
| --- | --- |
| `chapters/ch-02-economic-growth-limits.md:341` | "**sumed.** The real world is not partitioned…" (from "con-sumed") |
| `chapters/ch-04-space-colonization.md:298` | "**tation** as a *good* idea" (from "habi-tation"; `:296` ends "ocean floor habi-") |
| `chapters/ch-05-energy-and-power-units.md:761` | "**ence** is $10^{\circ}\mathrm{C}$" (from "differ-ence") |
| `chapters/ch-07-the-energy-landscape.md:144` | "**sured** by electrical *output*" (from "mea-sured"; `:142` ends "mea-") |

---

## 7. Structural and markup defects (conversion)

### 7.1 47 numbered margin notes lost

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

### 7.2 202 figure alt-texts damaged

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

### 7.3 Captions and titles split across block boundaries

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

### 7.4 Tables whose rows or columns were destroyed

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

### 7.5 Stray artefacts left in the body text

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

### 7.6 Cross-references and citations not converted

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

## 8. Appendix C is unusable

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

## 9. "rather then" for "rather than"

Four occurrences, plus one in the answer key:

- `chapters/ch-09-climate-change.md:593` — "concentrate heating in the upper layers **rather then** distributing uniformly"
- `chapters/ch-15-nuclear-energy.md:1203` — footnote 34: "gravity does the pulling **rather then** relying on some other drive force"
- `chapters/ch-20-adaptation-strategies.md:575` — "…when they come along, **rather then** being paralyzed by distress"
- `appendices/app-d-alluring-tangents.md:109` — "**Rather then** rely on external studies"
- `appendices/app-c-selected-answers.md:15` — "A smidge higher **then** boiling"

(`chapters/ch-06-putting-thermal-energy-to-work.md:127` also matches the
pattern — "This single number then indicates…" — but there "then" is correct.)

---

## 10. Edition-consistency notes

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
| Misspellings and wrong words | 23 |
| Doubled words | 12 |
| Subject–verb agreement faults | 21 |
| Other grammatical faults | 16 |
| Missing / doubled / stray punctuation | 17 |
| Quotation-mark faults | 6 |
| Imperatives punctuated as questions | 7 |
| Dash / hyphen misuse | 5 |
| "rather then" for "rather than" | 5 |
| Broken display equations | 25 |
| Other broken math | 10 |
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
