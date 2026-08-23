---
title: "B. Chemistry Primer/Refresher"
short_title: "Appendix B"
label: app-b
---

# B. Chemistry Primer/Refresher

This book does not rely heavily on past knowledge of chemistry, but it is helpful to know a few basic elements that play a role in fossil fuels, biological energy, and climate change. This section could act as a refresher, or a first exposure to the fundamentals.

(sec-b-1)=
## B.1 Moles

Chemistry deals with atoms and molecules and the interactions between them. Atoms and molecules[^1] are irreducible nuggets of a substance—the minimum unit that carries the essential properties of that substance. Water, for instance, is comprised of two hydrogen atoms bonded to a single oxygen atom, which we denote as H$_{2}$O.

:::{figure} ../images/fig-b-1.svg
:label: fig-b-1
:enumerator: B.1
:alt: Periodic Table of the Elements. This version is too small to permit names, so that only symbols are given. The more familiar elements are hi

Periodic Table of the Elements. This version is too small to permit names, so that only symbols are given. The more familiar elements are highlighted. Numbers represent the number of protons in the nucleus of the associated atoms.
:::

[Figure B.1](#fig-b-1) presents a stripped-down version of the periodic table. Additional exploration of more fully-featured versions is encouraged.[^2]

It is natural to imagine that a first step in dealing with piles of atoms and/or molecules is being able to *count* them. But since individual atoms are fantastically small, the numbers can be overwhelmingly large. This is where the mole[^3] comes in. A mole is *just a number*, and that number is called Avogadro’s number, having a value of $N_{\mathrm{A}}= 6.022 \times 10^{23}$, or 602,214,076,000,000,000,000,000, if written out.[^4]

The way the mole is defined, essentially, is that 12.000000 grams of neutral carbon atoms (of the isotope having 6 protons and 6 neutrons in its nucleus) will constitute one mole of atoms. In this way, the masses of other elements—being comprised of an integer number of protons and neutrons[^5]—will tend to be close to an integer number of grams.[^6] For instance, a mole of hydrogen atoms is very close to 1.00 grams. A mole of helium is very nearly 4.00 grams, nitrogen 14, oxygen 16, etc.

So the concept of the mole is pretty straightforward: just a number— albeit a very large one.

::::{admonition} Box B.1: Moles to Mass
:class: tip
:label: box-b-1

Incidentally, the inverse of Avogadro’s number becomes the definition of the atomic mass unit (a.m.u.). The a.m.u. can be thought of as the average mass of an atom per nucleon.[^7] In other words, carbon-12 (6 protons, 6 neutrons) has a mass of 12 a.m.u. In fact, this is how the a.m.u. is defined. This means that hydrogen (a single proton) has a mass very close to 1.00 a.m.u., and oxygen-16 (8 protons, 8 neutrons) has a mass close to 16.00 a.m.u. [Chapter 15](#ch-15) delves into the subtle reason why these are not exactly 1.00000 and 16.00000 in these cases.

Since one mole of 12.00000 a.m.u. carbon-12 atoms is defined to have a mass of 12.00000 g, one mole of 1.000000 a.m.u. particles[^8] would have a mass of 1.000000 g. Therefore, a *single* 1.000000 a.m.u. particle would have a mass of 1.000000 g divided by Avogadro’s number, $N_{\mathrm{A}}= 6.02214076 \times 10^{23}$, which turns out to be $1.66053907 \times 10^{-24}$ g, or $1.66053907 \times 10^{-27}$ kg. This is the number you will find if looking up the atomic mass unit (also called a Dalton).

::::

(sec-b-2)=
## B.2 Stoichiometry

Chemistry starts by counting atoms and molecules. Since molecules are comprised of integer numbers of atoms of specific types, the counting fun does not stop there. When atoms and molecules react chemically, the atoms themselves are never created or destroyed—only rearranged. This means that an accurate count of how many of each atom type are present at the start, a proper count at the end should yield *exactly* the same results.

Before we get into balancing chemical reactions, we need to know something about the scheme for labeling chemical compounds. A compound is an arrangement of atoms (representing pure elements) into a molecule. For instance, water is made of three atoms drawn from two elements: hydrogen and oxygen. Two atoms of hydrogen are bonded to an atom of oxygen to make a molecule of water. We denote this as H$_{2}$O.

Examples of a few familiar atoms and molecules are presented in [Figure B.2](#fig-b-2). Each one is named at the top. Below each one appears the bond structure in the case of molecules and the chemical “formula” in all cases. Notice that hydrogen atoms always have a single bond (single

:::{figure} ../images/fig-b-2.svg
:label: fig-b-2
:enumerator: B.2
:alt: Representing atoms as colored spheres for schematic purposes, we can depict the general appearance of molecules as bonded collections of ato

Representing atoms as colored spheres for schematic purposes, we can depict the general appearance of molecules as bonded collections of atoms. Here, we have three elements—hydrogen, oxygen, and carbon—combined into familiar molecules. Oxygen in the air we breathe is self-bonded into a “diatomic” molecule. Two representations appear below each molecule: a diagram indicating bonds (including double-bonds in some cases), and the chemical formula.
:::

electron to share), oxygen has two (wants to “borrow” two electrons to feel good about itself), and carbon tends to have four (either donating four in the case of CO$_{2}$, or accepting four when bonding to hydrogen). The chemical formula for each uses elemental symbols to denote the participants and **subscripts** to *count how many are present*.[^9]

Now we come to a bedrock practice in chemistry called stoichiometry— which boils down to counting atoms in a reaction to make sure no atoms are missing or spontaneously appear. To get a sense of this, see [Figure B.3](#fig-b-3) for two examples. The graphical version captures the physical reality, so that simply counting the number of spheres of each color on the left and right had better match. Below each graphical reaction is the associated chemical formula. Each formula contains an arrow indicating the direction of the reaction (separating “before” and “after”). Numerical factors (coefficients, or prefactors) in front of a molecule indicate how many molecules are present in the reaction. To get the total number of atoms represented, we must multiply the subscript for that atom (implicitly 1 if not present) by the prefactor.[^10]

::::{admonition} Example B.2.1
:class: seealso
:label: ex-b-2-1

Let’s figure out a tougher formula, pertaining to the combustion of ethanol (depicted in [Figure B.2](#fig-b-2)). In this situation, we combine a $\mathrm{C}_{2}$H$_{6}$O molecule with some number of oxygen molecules (O$_{2})$, and the reaction products will be CO$_{2}$ and H$_{2}$O (carbon dioxide and water). Our job is to figure out how many molecules are needed to balance the reaction:

:::{math}
\mathrm{C}_{2} H _{6} O + ?O _{2}\rightarrow ?CO _{2}+ ?H _{2} O
:::

where question marks indicate what we need to figure out. Three unknowns and one equation? It may seem hopeless, but the formula is *not* the equation. The equations are that the total number of carbons on each side are equal, the total number of oxygens are equal, and the total number of hydrogens are equal. So we actually have three equations.[^11]

Start by noticing that the left side has 2 carbons and 6 hydrogens. We don’t know how many oxygens yet, but it’s good enough to start. On the right, carbon only shows up in CO$_{2}$, so getting 2 carbons on the right requires 2CO$_{2}$. Likewise, hydrogen only shows up in water, and ethanol has 6 hydrogen atoms to stuffinto water molecules that hold 2 hydrogens apiece. It will obviously take 3 water molecules to account for 6 hydrogens.[^12] So now the right side is hammered out:

:::{math}
\mathrm{C}_{2} H _{6} O + ?O _{2}\rightarrow 2CO _{2}+ 3H _{2} O
:::

The only thing left to figure out is how many oxygens are on the left. To balance the reaction, count the number of oxygen atoms on the right. Four come from the two CO$_{2}$ molecules, and 3 from the water for a total of 7. One oxygen was already present in the ethanol molecule on the left, so only need 6 in the form of O$_{2}$, thus requiring three of these:

:::{math}
\mathrm{C}_{2} H _{6} O + 3O _{2}\rightarrow 2CO _{2}+ 3H _{2} O
:::

The job is done: the reaction is now balanced. That’s stoichiometry.

::::

:::{figure} ../images/fig-b-3.svg
:label: fig-b-3
:enumerator: B.3
:alt: Two example fossil fuel reactions (combustion) are shown here. The first is coal and the second is natural gas (methane). Both cases simply

Two example fossil fuel reactions (combustion) are shown here. The first is coal and the second is natural gas (methane). Both cases simply rearrange the input atoms without creating or destroying any, so that the count is the same on both sides of the arrow (which denotes the direction of the reaction). In other words, four purple hydrogens on the left in the case of methane must all appear on the right somewhere. The formula version also just counts instances of each atom/molecule, in which pre-factors (coefficients) indicate how many molecules are present.
:::

The treatment above cast chemical reactions at the most fundamental level of individual molecules reacting. In practice, reactions involve great numbers of interacting particles, so it is often more convenient to think in moles. In fact, common practice is to look at the prefactors[^13] in chemical reaction formulas as specifying the number of *moles* rather than the number of individual molecules. Either way, the formula looks exactly the same,[^14] and it’s just a matter of interpretation.

Thinking of the chemical formulas in terms of moles makes assessment of the masses involved more intuitive. Recall that one mole of carbon atoms is exactly 12 grams, that hydrogen is 1 g, and oxygen is 16 g. That means one mole of water molecules (H$_{2}$O) will be 18 g (16 $+ 1 + 1)$, one mole of carbon dioxide (CO$_{2})$ is 44 g (12 $+ 16 + 16)$, and one mole of ethanol $(\mathrm{C}_{2}$H$_{6}$O) is 46 g (12 $+ 12 + 1 + 1 + 1 + 1 + 1 + 1 + 16)$. We refer to this figure as the molar mass, and standard periodic tables display the molar masses for each element: the mass of one mole of the substance. The unit is typically grams per mole, or g/mol.

::::{admonition} Example B.2.2
:class: seealso
:label: ex-b-2-2

How much mass of CO$_{2}$ will emerge from the burning of 1 kg of ethanol? We start with the formula we worked out in [Example B.2.1](#ex-b-2-1):

:::{math}
\mathrm{C}_{2} H _{6} O + 3O _{2}\rightarrow 2CO _{2}+ 3H _{2} O
:::

This problem can be approached in Two equivalent ways: either figure out how many moles of ethanol it takes to amount to 1 kg and then scale the formula accordingly; or just work it out for one mole to get a ratio and then apply to 1 kg. We’ll do it both ways.

Since ethanol has a molar mass of 46 g, one kilogram corresponds to 21.7 moles. So we could re-write the formula as:

:::{math}
21.7\mathrm{C}_{2} H _{6} O + 65.2 O _{2}\rightarrow 43.5 CO _{2}+ 65.2 H _{2} O
:::

where we have multiplied each prefactor (coefficient) by 21.7. CO$_{2}$ has a molar mass of 44 g/mol, so 43.5 moles will come to 1.91 kg.

The other approach is to note that 2 moles of CO$_{2}$ are produced for every one mole of ethanol combusted. So 88 g of CO$_{2}$ (44 g/mol) results for every 46 g of ethanol supplied. This ratio is 1.91. So 1 kg of ethanol input will make 1.91 kg of CO$_{2}$ out, as before.

::::

(sec-b-3)=
## B.3 Chemical Energy

Atoms (elements) can bond together to make molecules (compounds). The bond—formed by outer electrons within the atoms—can be strong or weak. It takes energy[^15] to pull apart bonded atoms. It stands to reason that when two atoms form a new bond, energy is released—usually as vibrations that we know as heat. In a typical reaction, some bonds are broken and other new ones formed. If the balance is that the new bonds are stronger than the broken bonds, energy will be released. Otherwise, energy will have to be put into the reaction to allow it to happen.

In the context of this book, chemical energy is typically associated with combustion (burning) a substance in the presence of oxygen. This is true for burning coal, oil, gas, biofuels, and firewood. In a chemistry class, one learns to look up the energetic properties of various compounds in tables, combining them according to the stoichiometric reaction formula to ascertain a net energy value. We’re going to take a shortcut to all that, by introducing the following *approximate* formula for combustion energy.

:::{margin}
This empirical formula can serve as a general guide, but should not be taken as a literal truth from some profound derivation. It captures the main energy features and produces a useful, approximate result.

:::

The *approximate* energy available from the compound $\mathrm{C}_{\mathrm{c}}$H$_{\mathrm{h}}$O$_{\mathrm{o}}\mathrm{N}_{\mathrm{n}}$— where the subscripts represent the number of each atom in the molecule to be burned—is:

:::{math}
:label: eq-b-1
:enumerator: B.1
\frac{100(c + 0.3h - 0.5o)}{12c + h + 16o + 14n}\ \mathrm{kcal/g}
:::

For instance, sucrose has the formula $\mathrm{C}_{12}$H$_{22}$O$_{11}$, so that $c = 12, h = 22$, $o = 11$, and $n = 0$. The denominator in the formula is just the molar mass,[^16] or 342 in this case. The numerator adds to 13.1, so that the result is 3.8 kcal/g—very close to the expected value around 4 kcal/g for a carbohydrate like sugar.

The numerator of [Eq. B.1](#eq-b-1) tells us that we get the most energy from each carbon atom, 30% as much from each hydrogen atom, and take a 50% hit (deduction) for each oxygen atom. Nitrogen is energetically inert and does not contribute to the numerator—while degrading the energy density by adding mass in the denominator. The negative coefficient for oxygen tells us something important. Since combustion is a process of joining oxygen to atoms in the fuel, the presence of oxygen *already* in the fuel means it is already partly “reacted” and has less to offer in the way of new oxygen bonds.

:::{margin}
This is a generically useful practice: it helps integrate new knowledge into your brain by validating the behavior in known contexts. Does it make sense? Can you accept it, or does it seem wrong/suspect? Experts often apply new tools first to familiar situations whose answers are known to build trust and competence using the new tool before applying it more broadly.
:::

We can explore the sensibility of [Eq. B.1](#eq-b-1) by testing it on some known

product at the end of the energy process. H$_{2}$O, as another commonboundary cases.$^{17}$CO$_{2}$, calculating for CO$_{2}$ should offer no energy to us, since it’s a “waste”Since one ubiquitous end-product of combustion is

:::{margin}
**Try it:** Try it out, using $c = 1$ and $o = 2$.

:::

combustion product, is likewise effectively neutralized in the formula (the result is at least made to be very small). [Table B.1](#tab-b-1) provides some examples of what [Eq. B.1](#eq-b-1) delivers for familiar carbon-based substances. Note that oxygen content (last column) drives energy down, while hydrogen offers a boost.

:::{margin}
**Try it:** Try this one, too, coming up with your own values for $h$ and $o$.

:::

:::{table} Example approximate chemical energies. The results of the approximate formula are compared to true values (favorably). Fractional mass in carbon, hydrogen, and oxygen also appear—emphasizing the penalty for molecules already carrying oxygen.
:label: tab-b-1
:enumerator: B.1

| substance | formula | Eq. B.1 kcal/g | true kcal/g | % C | % H | % O |
| --- | --- | --- | --- | --- | --- | --- |
| glucose | $\mathrm{C}_{6}$H$_{12}$O$_{6}$ | 3.7 | 3.7 | 40 | 7 | 53 |
| typ. protein | $\mathrm{C}_{5}$H$_{10}$O$_{3}\mathrm{N}_{2}$ | 4.4 | $\sim 4$ | 41 | 7 | 52 |
| coal | C | 8.3 | 7.8 | 100 | 0 | 0 |
| typ. fat | $\mathrm{C}_{58}$H$_{112}$O$_{6}$ | 9.8 | $\sim 9$ | 77 | 12 | 11 |
| octane | $\mathrm{C}_{8}$H$_{18}$ | 11.8 | 11.5 | 84 | 16 | 0 |
| methane | CH$_{4}$ | 13.8 | 13.3 | 75 | 25 | 0 |
:::

The resulting calculated energies are definitely in the right (expected) ranges. Notice that the “winners” have little or no oxygen as a percentage of the total molecular mass. The lower-energy entries in [Table B.1](#tab-b-1) are more than half oxygen, by mass.

(sec-b-4)=
## B.4 Ideal Gas Law

Another topic covered in chemistry classes that strongly overlaps physics is the ideal gas law. This relationship describes the interactions between pressure, volume and temperature of a gas. In chemistry class, it is learned as

:::{math}
:label: eq-b-2
:enumerator: B.2
PV = nRT,
:::

where $P$ stands for pressure (in Pascals[^18]), $V$ is volume (cubic meters), $n$ is the number of moles, $T$ is temperature (in Kelvin), and $R$ is called the gas constant, having the value

:::{math}
:label: eq-b-3
:enumerator: B.3
R = 8.314 mol \cdot \mathrm{K.J}
:::

To get degrees in Kelvin, add 273.15 (273 among friends) to the temperature in Celsius.[^19] Standard atmospheric pressure is about $10^{5}$ Pa.[^20]

::::{admonition} Example B.4.1
:class: seealso
:label: ex-b-4-1

Let’s say we have a gas at “standard temperature and pressure” (STP), meaning $0^{\circ}\mathrm{C}$ (273 K) and $1.013 \times 10^{5}$ Pa. How much volume would one mole of gas[^21] occupy?

We have everything we need to solve for volume, so

$V = nRTP = (1 \mathrm{mol})(8.314 \mathrm{J/K/mol})(273 \mathrm{K})1.013 \times 10^{5}$ Pa $\approx 0.0224 \mathrm{m}^{3}= 22.4 \mathrm{L}.$

Okay; lots going on here. After the three values in the numerator are multiplied, the only surviving unit is J (Joules of energy). The unit in the denominator is Pascals, but this is equivalent to Joules per cubic meter. So the answer emerges in cubic meters, as a volume should. Since a cubic meter is 1,000 liters, we find that a mole of gas at STP occupies 22.4 L—a number memorized by many a chemistry student!

::::

Physicists prefer a variant of the ideal gas law that derives from the study of “statistical mechanics,” which is practically synonymous with thermodynamics and relates to the study of interactions between large ensembles of particles. The form looks pretty familiar, still:

:::{math}
:label: eq-b-4
:enumerator: B.4
PV = Nk_{\mathrm{B}}T.
:::

Pressure, volume, and temperature are all unchanged, and expressed in the same units as before. Now, $N$ describes the *number* of particles (quite large, usually), and $k_{\mathrm{B}}$ is called the Boltzmann constant, having a value

:::{math}
:label: eq-b-5
:enumerator: B.5
k_{\mathrm{B}}= 1.3806 \times 10^{-23} J
:::

:::{math}
\mathrm{K}.
:::

Notice that $N$, the number of particles, and $n$, the number of moles, differs simply by a factor of Avogadro’s number, $N_{\mathrm{A}}= 6.022 \times 10^{23}$. Indeed, if we multiply $N_{\mathrm{A}}$ by $k_{\mathrm{B}}$, we get 8.314, and are back to $R$.[^22]

::::{admonition} Example B.4.2
:class: seealso
:label: ex-b-4-2

Gas is stored at high pressure at room temperature in a metal cylinder, at a pressure of about 200 atmospheres.[^23] The cylinder is designed to meet a safety factor of 2, meaning that it likely will not fail until pressure reaches 400 atmospheres. If a fire breaks out and the cylinder heats up, the pressure will rise. How hot must the gas get before the cylinder may no longer be able to hold the pressure (assuming no fire damage to the cylinder itself)?

We *could* start throwing numbers into the ideal gas law, but we don’t know the volume or number of moles (or particles). Heck, we’re not even given a temperature. Ack! Students hate this sort of problem, because it does not appear to be algorithmic in nature. No plug and chug (an activity that does not engage the brain heavily, and thus its appeal).

But we’re okay. What is room temperature? Something like 20–$25^{\circ}\mathrm{C}$, so that’s 293–298 K. Whatever the volume is, or the amount of gas in the cylinder, those things don’t change as the temperature rises.[^24] What we’re left with is a straightforward scaling between temperature and pressure (because the numerical factors are all constant for our problem). Therefore, if temperature doubles, pressure doubles.[^25]

Hey, it’s doubling pressure that we are interested in, which will happen if the temperature doubles. So if the temperature goes up to about 600 K, we may be in trouble. It is easy to imagine that a fire could create such conditions. Notice that we are not bothering to say 586–596 K, but just said about 600 K. Do you want a precise temperature when the thing will rupture? Good luck. The point at which it explodes may be 405 atmospheres or it may hold on until

453. Also, how likely is it that all the gas throughout the cylinder is at exactly the same temperature when being heated by a nearby fire? So let’s give ourselves a break and not pretend we’re totally dialed in. There’s a fire, after all.

::::

:::{margin}
This is an example where internalizing the ideal gas law for what it *means*, or what it *says* is more important than treating it like a recipe for cranking out problems. Don’t just treat equations as mechanical objects: learn what it is they have to *say*!

:::

[^1]: Molecules are made from a handful of atoms.
[^2]: Perhaps at least identifying the highlighted elements would be worthwhile.
[^3]: … the word *molecule* begins with *mole*.
[^4]: Unfortunately, it can be hard to remember if it is supposed to be $6.022 \times 10^{23}$ or $6.023 \times 10^{22}$. For this reason, it may be wise to forget about the 22 and just remember $6.0\times 10^{23}$, or even $6.023\times 10^{23}$ as something that is *very slightly* wrong but much better than being 10 times off!
[^5]: … and associated light-weight electrons equal in number to the protons
[^6]: Blends of different isotopes can mess up this convenient arrangement in natural (mixed) samples, however.
[^7]: A nucleon is either a proton or a neutron: the two types of particles that occupy the nucleus of an atom and are responsible for almost all of the atom’s mass.
[^8]: … if such a thing were to be found/created
[^9]: Two variants are shown for ethanol. The first is a no-nonsense census of the atoms, while the second pulls one of the H symbols to the end to call attention to the OH (hydroxyl) tagged onto the end of the molecule. In either case, the formula specifies 2 carbons, 6 hydrogens, and 1 oxygen, in total.
[^10]: For example, 2H$_{2}$O has a total of 4 hydrogen atoms and 2 oxygens.
[^11]: Equations are just statements of truth that we can create on our own. They are just a way to express what we know about a problem.
[^12]: What if the starting point had an odd number of hydrogens on the left? We’d need to double the number of hydrogen-containing molecules on the left to produce an even number and start over.
[^13]: … also called coefficients
[^14]: To be explicit, if a formula is balanced for individual molecules, then it should also be balanced if doubling the “recipe,” or tripling, multiplying by 10, or even by 6 $\times 10^{23}$.
[^15]: Recall that energy is a measure of work, or a force times a distance.
[^16]: The coefficients in the denominator reflect the fact that carbon is 12 units of mass, oxygen is 16, etc.
[^18]: A Pascal (Pa) is also a Newton of force per square meter, which reduces to more fundamental units of $\mathrm{J/m}^{3}$ (Joules of energy per cubic meter).
[^19]: And $T(^{\circ}$F$) = 1.8 \cdot T(^{\circ}\mathrm{C}) + 32$.
[^20]: 1 atmosphere is 101,325 Pa.
[^21]: It may be surprising, but the ideal gas law does not care what element or molecule we are considering!
[^22]: The units work, too, since $N_{\mathrm{A}}$ effectively has units of a number (of particles) per mole.
[^23]: … means 200 times atmospheric pressure
[^24]: The gas is not leaking out, and the cylinder does not change size—at least not significantly—as it warms.
[^25]: That’s one of the things [Eq. B.4](#eq-b-4) is trying to say, beneath all the bluster.
