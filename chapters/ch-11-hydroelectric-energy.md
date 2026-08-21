---
title: "11. Hydroelectric Energy"
short_title: "Chapter 11"
label: ch-11
---

:::{figure} ../images/art-p202-1.jpg
:alt: Chapter opening illustration

Boulder Dam. Photo Credit: Tom Murphy
:::

# 11. Hydroelectric Energy

Energy has been harnessed from flowing water for ages. Milling operations were often located on streams so that water could turn a wheel attached to grinding machinery. Today, captured water flow is a significant contributor to electricity worldwide in the form of hydroelectricity. The U.S. gets about 2.8% of its current energy (and 7% of electricity) from hydropower. Globally, hydropower accounts for about 9% of energy, or 16% of electrical production ([Table 7.2](#tab-7-2); p. 112).

Hydroelectricity taps into the solar-driven evaporation cycle, relying on the gravitational energy embodied in water lifted onto the land from lower bodies of water. In other words, solar energy lifts water, giving it gravitational potential energy, which is captured and converted to electrical energy.

While hydroelectric power is a simple and low-tech form of renewable energy that has been heavily exploited for over a hundred years, it is not one that is easy to expand beyond its current level of usage. This chapter will provide a better understanding of this mainstay of the renewable portfolio and its likely role in our future.

:::{margin}
Tidal power works in exactly the same way as hydroelectricity, but is a niche player and will be deferred to [Section 16.2](#sec-16-2).

:::

(sec-11-1)=
## 11.1 Gravitational Potential Energy

Gravitational force is incredibly weak. It may not seem so from daily experience, but consider the fact that a magnet held in your hand can lift a paperclip—overwhelming the gravitational pull of the *entire* earth! By comparison, electromagnetic forces are forty orders-of-magnitude stronger than gravitational force. We don’t tend to notice because electric charges tend to balance out so that gravity is the most obvious force in our daily lives.[^1]

We know intuitively that lifting a massive object requires work, and thus energy. In fact, since work is defined as a force times distance,[^2] and the force of gravity on an object follows Newton’s second law, $F = ma$,[^3] the force we need to exert on an object to lift it against gravity is called its weight, and is $W = mg$, where $g = 9.8 \mathrm{m/s}^{2}\approx 10 \mathrm{m/s}^{2}$ is the acceleration due to gravity on the surface of the earth. Thus, to lift an object through height, $h$, requires an energy input of this force, $W$, times the height, $h$. We call this gravitational potential energy since the energy put in to lift something can be released later if the mass is allowed to fall or be lowered. An early use of gravitational potential energy was in the form of weights on chains in old clocks.

::::{admonition} Definition 11.1.1 — gravitational potential energy
:class: important
:label: def-11-1-1

is computed as

:::{math}
:label: eq-11-1
:enumerator: 11.1
G .\mathrm{P.E}. = mgh,
:::

where $m$ is the mass in kg, $g \approx 10 \mathrm{m/s}^{2}$ is the acceleration due to gravity,[^4] and $h$ is the height to which the mass is raised, in meters. The result is in Joules.

::::

Most commonly, gravitational potential energy is converted to kinetic energy as an object falls: slowly at first but accelerating as more potential energy is converted to kinetic energy while the object gains speed (see [Fig. 5.1](#fig-5-1); p. 75). Only the vertical distance matters in computing gravitational potential energy: sideways motion does not operate against the gravitational force. Sliding a crate across a flat, level floor does take work to overcome friction, but that energy is converted to heat and cannot be later returned in useful form.[^5] In this case, the crate has gained no gravitational potential energy, since its height never changed.

::::{admonition} Example 11.1.1
:class: seealso
:label: ex-11-1-1

Lifting a 20 kg box of books, whose weight is therefore $W = mg \approx 200$ N,[^6] from the floor to a high shelf through a vertical distance of 2 m involves an energy expenditure of $mgh \approx 400$ J ([Figure 11.1](#fig-11-1)). We would say the box gained 400 J of potential energy.

If the person doing the work is exerting energy at a rate of 200 W (200 J/s), it will take two seconds to complete the action.

If the box later falls off the shelf and hits a 1.5 m tall person on the head, the box has *lost* 100 J (20 kg $\times 10 \mathrm{m/s}^{2}\times 0.5$ m) of potential energy (now kinetic) by the time it hits the person’s head.

::::

(sec-11-1-1)=
### 11.1.1 Comparison to Other Forms

:::{figure} ../images/fig-11-1.svg
:label: fig-11-1
:enumerator: 11.1
:alt: Diagram for Example 11.1.1.

Diagram for [Example 11.1.1](#ex-11-1-1).
:::

To give a flavor of how weak gravitational potential energy is compared to other familiar forms of energy storage, we will consider the energy content in a standard AA alkaline battery and in a similar volume of gasoline. So we’re talking about something approximately the size of a small finger. We want to know how much mass must be lifted to yield the same amount of gravitational potential energy as is contained in a battery or equivalent volume of gasoline. In the comparison, we will imagine having a hoist that can lift a large mass[^7] 4 m high—about house-height.

A standard AA battery cell has a charge rating of 2.5 Ah[^8] and operates at about 1.5 V. Following the development in [Sec. 5.8](#sec-5-8) (p. 81), we multiply these two numbers to get 3.75 Wh, translating to 13.5 kJ. Equating this to $mgh$, where we know $g \approx 10 \mathrm{m/s}^{2}$ and $h = 4$ m, we find that $m \approx 340$ kg. That’s really heavy—about the mass of 4–5 people.[^9] Meanwhile, the AA battery is a puny 0.023 kg. Reflect for a moment on this comparison, visualizing 340 kg lifted 4 m above the ground providing the same amount of energy as a AA battery held in your hand.

Gasoline is even more extreme. At an energy density around 34 kJ per mL of volume, filling a AA-sized cup[^10] with gasoline yields about 250 kJ of energy.[^11] Performing the same computation, we would need to lift over 6,000 kg (6 metric tons) to a height of 4 m to get the same energy content. Typical cars have masses in the 1,000–2,000 kg range, so we’re talking about something like 4 cars! One caveat is that we are not typically able to convert the thermal energy in gasoline[^12] into useful work at much better than 25%, while gravitational potential energy can be converted at nearly 100%. Still, being able to lift 1,500 $\mathrm{kg}^{13}$ to a height of 4 m using the energy in 7 mL of gasoline is rather impressive, again emphasizing that gravitational potential energy is pretty weak. It only amounts to significance when the masses (volumes) of water are rather large.

:::{margin}
… now just one car, rather than four; it means this small volume of gasoline can propel a car up a 4 m hill
:::

(sec-11-2)=
## 11.2 Hydroelectric Energy

The basic idea behind hydroelectricity is that water in a reservoir behind a dam ([Figure 11.2](#fig-11-2)) creates pressure at the base of the dam that can force water to flow through a turbine that drives a generator to make electricity—sharing elements of [Fig. 6.2](#fig-6-2) (p. 95) but spinning the turbine by water flow instead. The amount of energy available works out to be the gravitational potential energy corresponding to the height of water at the lake’s surface relative to the water level on the other side. It’s as if dropping the water from the surface to the turbine and asking how much potential energy it gave up in the process. In reality, water is not dropping from the lake surface, but the force on the water at the turbine is determined by the height of water above it: the “pressure head,” as it is called. The process is highly efficient, approaching 90% capture of the potential energy in the water delivered as electrical power from the generator.

:::{figure} ../images/fig-11-2.svg
:label: fig-11-2
:enumerator: 11.2
:alt: Cross section of a dam, holding back a reservoir of water at height, , over the downstream river.

Cross section of a dam, holding back a reservoir of water at height, $h$, over the downstream river.
:::

::::{admonition} Box 11.1: Why So Efficient?
:class: tip
:label: box-11-1

Achieving 90% efficiency is superb! Electric motors and generators[^14] can be $> 90\%$ efficient in converting between mechanical energy (rotation) and electrical energy. When coupled with low-friction turbines, dams just have very little loss—unlike thermal sources where most of the energy is unavoidably lost (for reasons covered in [Sec. 6.4](#sec-6-4); p. 93).

::::

::::{admonition} Example 11.2.1
:class: seealso
:label: ex-11-2-1

To compute the power available from a hydroelectric plant, we need to know the *height* of the reservoir and the *flow rate* of water—usually measured in cubic meters per second. The density of water is, conveniently, 1,000 $\mathrm{kg/m}^{3}$ ([Figure 11.3](#fig-11-3)), so that if we consider a dam having a flow rate of 2,000 $\mathrm{m}^{3}/\mathrm{s}$ and a reservoir height of 50 m, we can see that every second of time will pass 2 $\times 10^{6}$ kg of water,[^15] and the associated potential energy is $mgh \approx 10^{9}$ J. If each second delivers 1 GJ of energy, the power available is 1 GJ/s, or 1 GW. At an efficiency of 90%, we get to keep 900 MW of electrical power.

::::

:::{figure} ../images/fig-11-3.svg
:label: fig-11-3
:enumerator: 11.3
:alt: One cubic meter of water has a mass of 1,000 kg.

One cubic meter of water has a mass of 1,000 kg.
:::

The largest hydroelectric facility in the world is the Three Gorges Dam in China, rated at an astounding 22.5 GW. The largest in the U.S. is the Grand Coulee on the Columbia River, producing a maximum of 6.8 GW. The iconic Boulder Dam (a.k.a. Hoover Dam) is just over 2 GW.

:::{margin}
**Try it:** Look at the Wikipedia page on largest hydroelectric power stations [[66](#ref-66)] for a complete list.

:::

Note that flow rates vary seasonally with rainfall, so that dams cannot always operate at full capacity. In fact, the U.S. has about 80 GW of *capacity* installed, but operates at an annual average of about 33 GW. This implies a typical “capacity factor” around 40%.

::::{admonition} Definition 11.2.1
:class: important
:label: def-11-2-1

A **capacity factor** is the ratio of actual performance over time to the peak possible performance—or average output divided by maximum output, expressed as a percentage.

::::

::::{admonition} Example 11.2.2
:class: seealso
:label: ex-11-2-2

Boulder (Hoover) Dam on the Colorado River is listed in [[66](#ref-66)] as having a capacity of 2,080 MW and an annual production of 4.2 TWh. What is its capacity factor?

We just need to turn the 4.2 TWh in a year into an average delivered power. Following the definition of a watt-hour, we note that all we really have to do is divide $4.2 \times 10^{12}\mathrm{Wh}^{16}$ by the number of hours in a year: 24 times 365, or 8760.

$4.2 \times 10^{12}\mathrm{Wh}/8760$ h $\approx 480$ MW average power. Dividing this by 2,080 MW (max capacity) gives a 23% capacity factor.

::::

:::{margin}
1 TWh is $10^{12}$ Wh.
:::

As we saw in [Fig. 7.5](#fig-7-5) (p. 113) and [Table 10.3](#tab-10-3) (p. 177), hydroelectricity in the U.S. accounts for 2.7% of the nation’s total energy consumption, corresponding to about 33 GW of production. Globally, hydroelectric production averaged 477 GW in 2017. By comparison, [Table 10.2](#tab-10-2) (p. 175) indicates that 44,000 TW of solar input goes into evaporation and the hydrological cycle. Why, then, are we only able to use 0.477 TW (0.001%) of this bounty? Is this a great, untapped renewable resource?

(sec-11-2-1)=
### 11.2.1 Theoretical Potential

To understand the giant mismatch between solar input and hydroelectric development, we first need to study evaporation.

::::{admonition} Definition 11.2.2
:class: important
:label: def-11-2-2

The **heat of vaporization** of water is about 2,250 J per gram, meaning that every gram of water that goes from liquid to gas (vapor) requires an energy input of $\sim 2,250$ J.

::::

::::{admonition} Box 11.2: Vaporization is Serious Energy
:class: tip
:label: box-11-2

To put this in perspective, it takes 100 calories (418 J) to bring one gram of water from freezing to boiling temperature. Then it takes another 2,250 J to evaporate the water, which is a far larger quantity. This is why water in a pot does not all flash into steam once the water reaches $100^{\circ}\mathrm{C}$, as it would if the evaporation energy was very small. Instead, a boiling pot will retain water for a good while as energy continues to be applied before all boiling away.

::::

:::{figure} ../images/fig-11-4.svg
:label: fig-11-4
:enumerator: 11.4
:alt: The hydrological cycle. Sunlight evaporates water from the surface, at a cost of 2,250 J per gram. Each kilometer of height the gram of wate

The hydrological cycle. Sunlight evaporates water from the surface, at a cost of 2,250 J per gram. Each kilometer of height the gram of water gains in forming clouds costs an additional 10 J. When rain falls on terrain, most of the gravitational potential energy is spent, but on average retains 8 J—based on an average land elevation of 800 m. The 2,250 J of evaporation energy is released as heat when the water condenses into clouds.
:::

So let’s follow the energetics of a gram of water[^17] on its journey to a hydroelectric dam—most of which is represented in [Figure 11.4](#fig-11-4). First, the sun injects 2,250 J to evaporate that gram. Then let’s say it gets lofted to 5 km.[^18] The gravitational potential energy, $mgh$, comes to $0.001 \times 10 \times 5000 = 50$ J. That’s only 2% of the amount that went into evaporation.[^19]

When the water condenses in the cloud, it *releases* 2,250 J of thermal energy into the cloud/air, then falls back to the ground as rain, offering 50 J of still-available energy. If it falls on the ocean, where it presumably started, it gives up all 50 J of gravitational potential energy into useless forms.[^20] But if it falls on land—higher than sea level—it retains some gravitational potential, based on how high that land is above sea level.

On average, terrain is about 800 m above sea level, so each gram that falls on land has an average of 8 J left as available energy. But only 29% of the earth’s surface is land, so that the gram of water we’re tracking preserves about 2 J of energy, on average.[^21]

We’re down to only 0.1% of the input solar energy—2 J out of 2,300 J input—so that the theoretical hydroelectric potential might be about 44 TW: reduced from the 44,000 TW input. But only a small fraction of rain flows into rivers suitable for damming. And once dammed, a typical dam height is in the neighborhood of 50 m, knocking us down even further. Much of the journey from terrain to reservoir involves losing elevation in streams too small to practically dam, or just seeping through the ground. In the end, perhaps it is not surprising that we end up in the sub-TW regime globally.

:::{margin}
The 90% efficiency of a hydroelectric dam is now contextualized a bit better. That last step is pretty efficient, but the overall process is extremely inefficient. Still, it takes relatively little effort to exploit, and provides real power. Efficiency is not everything.

:::

Detailed assessments [[67](#ref-67)] of hydroelectric potential globally estimate a *technically* feasible potential[^22] around 2 TW, but only half of this is deemed to be economically viable. Recall that 477 GW, or about 0.5 TW, is delivered globally, which is therefore about half of what we believe to be the practical limit of $\sim 1$ TW. Thus we might not expect more than a factor-of-two expansion of current hydroelectricity as possible/practical. The low-hanging fruit has been plucked already, capturing about half of the total practical resource.

:::{margin}
[[67](#ref-67)]: (1997), *Study on the Importance of Harnessing the Hydropower Resources of the World*

:::

Compared to the 18 TW global scale of energy use, hydroelectricity is not poised to assume a large share at this level, unless the overall scale of energy use is reduced substantially. Let’s say this more visibly: **hydroelectric power cannot possibly come close to satisfying present global power demand.**

(sec-11-3)=
## 11.3 Hydropower in the U.S.

Hydroelectric power is not available to the same degree everywhere. Geography and rainfall are key factors. This brief section serves to present a snapshot of the distribution and qualities of hydroelectric power generation in the United States. We start with [Figure 11.5](#fig-11-5), showing the average hydroelectric power generated in each state, the top four states being listed in [Table 11.1](#tab-11-1). These four states account for 56% of hydroelectricity in the U.S., and the next states on the ranked list drop to 1 GW or lower. Most of the California generation is in the northern part of the state, effectively as part of the Pacific Northwest region.

:::{table} Top hydroelectric states.
:label: tab-11-1
:enumerator: 11.1

| State | Production (GW) |
| --- | --- |
| Washington | 8.9 |
| Oregon | 3.8 |
| California | 3.0 |
| New York | 2.9 |
| U.S. Total | 33 |
:::

To get a sense for how concentrated different sources are, we will make a habit of examining power density for renewable resource implementations. [Figure 11.6](#fig-11-6) indicates the state-by-state density of hydroelectric power generation,[^23] just dividing generation by state area. No state exceeds 0.05 $\mathrm{W/m}^{2}$, which can be contrasted to insolation values (see Ex. 10.3.1; p. 174) of $\sim 200 \mathrm{W/m}^{2}$. Globally, total land area is about

:::{figure} ../images/fig-11-5.png
:label: fig-11-5
:enumerator: 11.5
:alt: Average U.S. hydroelectric power delivered for each state, showing strongly along the west-coast, plus New York. And yes, Alaska really is t

Average U.S. hydroelectric power delivered for each state, showing strongly along the west-coast, plus New York. And yes, Alaska really is that big.
:::

:::{margin}
This is higher than estimated potential developed resources, but mathematically convenient here.
:::

unusual, having *already developed* a generation capacity 2.5 times larger

:::{margin}
Washington’s hydroelectric dominance owes largely to the presence of the mighty Columbia River, rather than human factors.
:::

:::{figure} ../images/fig-11-6.png
:label: fig-11-6
:enumerator: 11.6
:alt: U.S. hydroelectric power per area delivered for each state, giving a sense of how concentrated the resource is. The units are milliwatts per

U.S. hydroelectric power per area delivered for each state, giving a sense of how concentrated the resource is. The units are milliwatts per square meter, peaking at 48 $\mathrm{mW/m}^{2}$ for Washington.
:::

Next, we look at hydroelectric generation per capita. [Figure 11.7](#fig-11-7) shows the result. In this view, the states of the Pacific Northwest really pop up, and New York dims relative to its by-area showing. The contrast between [Figure 11.6](#fig-11-6) and [Figure 11.7](#fig-11-7) is effectively reflecting population density: large, sparsely-populated states[^26] show up more prominently on the per-capita map than the per-area map.

Finally, for completeness, we look at the capacity factors of hydroelectric installations, by state. The total installed capacity in the database used for these plots is 77.6 GW spread among 1,317 dams, while producing an annual average of 28.1 GW—corresponding to an overall capacity factor of 0.36. [Figure 11.8](#fig-11-8) shows how this distributes around the country. Since the Pacific Northwest dominates in installed hydroelectric power, it largely determines the overall capacity factor. Iowa stands out as having a high capacity factor, but only has 0.153 GW of installed capacity.[^27] Contrast this to Washington, having an installation capacity of 20.7 GW.$^{28}$

:::{figure} ../images/fig-11-7.png
:label: fig-11-7
:enumerator: 11.7
:alt: U.S. hydroelectric power per population within each state, indicating which residents receive the most hydroelectric power. The Pacific Nort

U.S. hydroelectric power per population within each state, indicating which residents receive the most hydroelectric power. The Pacific Northwest wins.
:::

:::{figure} ../images/fig-11-8.png
:label: fig-11-8
:enumerator: 11.8
:alt: U.S. hydroelectric capacity factors by state. The national average (weighted by generation) is about 0.4, meaning that over the course of a

U.S. hydroelectric capacity factors by state. The national average (weighted by generation) is about 0.4, meaning that over the course of a year the dams deliver 40% of their rated capacity—subject to seasonal water flow.
:::

(sec-11-4)=
## 11.4 Global Hydropower

This section provides a brief snapshot of hydroelectric production globally, which we saw at the end of [Section 11.2.1](#sec-11-2-1) amounts to 477 GW. [Figure 11.9](#fig-11-9) shows which countries have the most hydroelectricity, the corresponding numbers appearing in [Table 11.2](#tab-11-2)—including the percentage of electricity derived from hydroelectric sources within the country. Notice that Norway, Venezuela, Brazil, and Canada derive more than half their electricity demand from hydroelectricity. Keep in mind that electricity is not the whole energy story for a country, as [Fig. 7.2](#fig-7-2) (p. 110) made clear.

:::{figure} ../images/fig-11-9.svg
:label: fig-11-9
:enumerator: 11.9
:alt: Global allocation of hydroelectric power.

Global allocation of hydroelectric power.
:::

:::{table} Top ten hydroelectric producers in the world, accounting for two-thirds of the hydroelectricity production worldwide.
:label: tab-11-2
:enumerator: 11.2

| Rank | Country | GW | % elec. | Rank | Country | GW | % elec. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1. | China | 122 | 19 | 6. | India | 15 | 10 |
| 2. | Canada | 44 | 58 | 7. | Norway | 15 | 96 |
| 3. | Brazil | 43 | 63 | 8. | Japan | 10 | 8 |
| 4. | U.S. | 33 | 6.5 | 9. | Venezuela | 10 | 68 |
| 5. | Russia | 20 | 17 | 10 | France | 8 | 12 |
:::

(sec-11-5)=
## 11.5 Upshot: Pros and Cons of Hydro

The two lists below provide some pros and cons to hydroelectric power that are relevant to our assessment of its value to our mix of renewable energy options. First, the positive attributes:

- Natural source, solar-driven, without waste products or pollution;[^29]

- Technologically simple, therefore straightforward to implement and maintain;

- High efficiency, turning 90% of available energy into useful electricity;

- Good baseline of steady power over daily timescales;[^30]
- Life-cycle CO$_{2}$ emissions only 4% that of traditional fossil fuel electricity [[68](#ref-68)];

- Facilities[^31] can last a century or longer;
- While not directly related to energy, dams can provide flood control and reliable water supplies.

And some of the downsides that may discourage further development:

- Silt can build up behind dams displacing the reservoir, eventually rendering them useless and dangerous;

- Requires the semi-permanent flooding of an ecological habitat, of varying quality and value;

- Seasonal variability of available power, often by a factor of ten;
- Defunct or poorly maintained facilities represent a dam-burst danger to downstream residents;

- Blocks salmon runs and impacts the health of both oceanic and forest ecosystems;

- As the distribution maps show, hydroelectric is not a viable option everywhere: the combination of terrain[^32] and rainfall is needed.

On balance, our society has embraced hydroelectricity as a clean and reliable resource. One can view it as nature’s low-hanging fruit, partly evidenced by how early it was adopted on a large scale. It is likely to remain an attractive form of energy as we face increasing pressures to migrate away from carbon-based fuels.[^33] It will not, however, be able to provide an avenue for wholesale replacement of fossil fuels given its limited scale and electric-only nature. Only if our overall energy demand is reduced substantially will it form a large fraction of our portfolio.

(sec-11-6)=
## 11.6 Problems

1. If a 70 kg person climbs 10 flights of stairs, each flight 3 m high, how much potential energy have they gained?

2. If an 80 kg person is capable of delivering external mechanical energy at a rate of 200 W sustained over several minutes,[^34] how high would they be able to climb in two minutes?

3. A 10 kg box is lifted 2 m off the floor and placed on a frictionless horizontal conveyor to take it 30 m across a warehouse. At the end of the conveyor, it is lowered 1 m where it ends up on a shelf.[^35]

   How much *net* gravitational potential energy was given to the box from the start to the end of the process?

4. A standard AA battery cell stores about 13.5 kJ of energy. At a mass of 23 g each, how high would you have to lift the battery to get the same amount of gravitational potential energy?

:::{margin}
ⓘ The result emphasizes how weak gravitational potential energy is.

:::

5. A gallon of gasoline contains about 130 MJ of chemical energy at a mass of around 3 kg. How high would you have to lift the gallon of gasoline to get the same amount of gravitational potential energy? Compare the result to the radius of the earth.

:::{margin}
ⓘ The result emphasizes how weak gravitational potential energy is.

:::

6. Problem 5 used one gallon of gasoline to compute the equivalent height for gravitational potential energy. Does the result depend on what volume of gasoline we selected? Make an airtight argument as to why or why not. Solving symbolically[^36] may be a helpful route—but not the only one.

:::{margin}
Hint: the energy density in MJ per kg is a property of the gasoline.

:::

7. A typical American household uses approximately 30 kWh per day of electricity. Convert this to Joules and then imagine building a water tank 10.8 m above the house[^37] to supply one day’s worth of electricity.[^38] How much mass of water is this, in kg? At a density of 1,000 $\mathrm{kg/m}^{3}$, what is the volume in cubic meters, and what is the side length of a cube[^39] having this volume? Take a moment to visualize (or sketch) this arrangement.

8. The biggest hydroelectric installation in the U.S. is the Grand Coulee dam on the Columbia River. The enormous flow rate reaches its maximum at 4,300 $\mathrm{m}^{3}/\mathrm{s}$, and the dam (reservoir) height is 168 m. At an efficiency of 90%, at what rate is this dam capable of producing hydroelectric power (in $\mathrm{GW}^{40})$? Don’t forget the density of water and that $g \approx 10 \mathrm{m/s}^{2}$.

:::{margin}
ⓘ For comparison, a large nuclear reactor typically produces about 1 GW of electrical power.
:::

9. The Hoover Dam (also called Boulder Dam) on the Colorado River is rated at 2.08 GW when the flow is at its maximum rate of 1,280 $\mathrm{m}^{3}/\mathrm{s}$. How high is the reservoir if the efficiency of the installation is 90%?

10. A dam 50 meters high is constructed on a river and is delivering 180 MW at some moment in time. What is the flow rate of water, in cubic meters per second, if the facility converts gravitational potential energy into electricity at 90% efficiency?

11. A hydroelectric facility is built to deliver a peak power of 1 GW, which it manages to do for three months of the year during the spring snow-melt. But for three months in summer, it drops to 700 MW, then 500 MW for three months in fall. In winter, it drops way down to 200 MW for three months. Using the concept of the capacity factor ([Definition 11.2.1](#def-11-2-1)), what is the annual average capacity factor for this facility?

:::{margin}
This stepwise behavior is not exactly realistic, but need not be to apply the concept correctly.

:::

12. While the Chief Joseph Dam on the Columbia River can generate as much as 2.62 GW $(2.62 \times 10^{9}$ W) of power at full flow, the river does not always run at full flow. The average annual production is 10.7 TWh per year $(10.7 \times 10^{12}$ Wh/yr). What is the capacity factor of the dam: the amount delivered vs. the amount if running at 100% capacity the whole year?

:::{margin}
Hint: Multiplying peak power by hours in a year will result in units similar to Wh/yr for direct comparison.

:::

13. The Robert Moses Niagara dam in New York is rated at 2,429 $\mathrm{MW}^{41}$ and has a high capacity factor of 0.633. How many kWh does it produce in an average day, and how many homes would this serve at the national average of 30 kWh/day?

:::{margin}
… peak power capacity
:::

:::{margin}
Hint: Convert average power to kW then multiply by hours.

:::

14. The Robert Moses Niagara dam from Problem 13 is 30 m high. What is the peak flow rate, in $\mathrm{m}^{3}/\mathrm{s}$, if it can produce full capacity power (2.43 GW electrical output) while converting gravitational potential energy to electricity at 90% efficiency?

15. It takes 2,250 J to evaporate each gram of water, while only taking about 330 J to raise the temperature of water from room temperature to the boiling point. If it takes 10 minutes to bring a pot of water from room temperature to boiling, how much additional time will it take to boil off (evaporate) all the water if injecting energy at the same rate the whole time?

16. Starting at 44,000 TW of solar input to the hydrologic cycle, parallel the development in [Section 11.2.1](#sec-11-2-1) by computing the power remaining at each stage[^42] if, for each gram of water:

   a) water is evaporated and lifted to 5 km height;[^43] b) 30% of the water falls on land where collection is possible; c) the typical land height is 800 m; d) only 20% of the water makes it to dammable locations; e) only 50 m of height (of the original 800 m average) is left for the dam.

   By this analysis, how much hydroelectric power is theoretically possible, globally?

17. [Fig. 10.1](#fig-10-1) (p. 174) indicated that about 44,000 TW globally goes into evaporating water. We can turn this into an estimate of how much rain we expect per year, on average. The simplest way to do this is to think of a single square meter of ocean surface, receiving an average evaporation input power of 120 W.[^44] Each millimeter of of water depth across our square meter has a volume of 1 L, or a mass of 1 kg. At a steady input of 120 W,[^45] how many millimeters of water are drawn off in a year? That same amount will come back down *somewhere* as precipitation.

[^1]: Somewhat ironically, we only *feel* gravity because of a much stronger electromagnetic force that prevents us from falling through the floor. Electrons in the atoms in the floor and our feet repel each other to prevent free-fall—a weightless state in which gravity can’t be felt!
[^2]: Recall Def. 5.1.1 (p. 73).
[^3]: Force is mass times acceleration.
[^4]: Some may remember it more pedantically as 9.8 $\mathrm{m/s}^{2}$, but for the purposes of this book, 10 $\mathrm{m}/s^{2}$ will do nicely. Note that choosing this number implies that we are concerned only with gravitational energy on the earth’s surface.
[^5]: We often say in this case that the energy is “lost.” But energy is strictly conserved— not created or destroyed—so it is never *really* lost, it just escapes into a non-useful form.
[^6]: … again using $g \approx 10 \mathrm{m/s}^{2}$
[^7]: … a rock, for instance
[^8]: The number is usually given as, e.g., 2,500 mAh (milli-amp-hours).
[^9]: Amuse yourself by picturing 4–5 people slung haphazardly into a net and hoisted to roof height—a very odd (and grumpy?) replacement for a AA battery.
[^10]: … just over 7 mL
[^11]: Thus, gasoline is nearly 20 times as energy-dense as a AA battery *by volume*. Usually, we will discuss energy density *by mass*, in which case the $\sim 5\times$ denser battery provides nearly $100\times$ less energy per gram than does gasoline.
[^12]: … via combustion; see [Sec. 6.4](#sec-6-4) (p. 93)
[^14]: Fundamentally, motors and generators are nearly identical in concept and construction.
[^15]: Flow rate times density gives mass per second: 2,000 $\mathrm{m}^{3}/\mathrm{s}$ times 1,000 $\mathrm{kg/m}^{3}=$ 2 $\times 10^{6}$ kg/s
[^17]: … one cubic centimeter
[^18]: … typical cloud height
[^19]: The sun must, in total, supply 2,300 J to evaporate and lift the gram of water, and only 50 J of the 2,300 J is kept as potential energy.
[^20]: … heat through air resistance and collision with the ocean surface
[^21]: … reduced from 8 J since most rain falls back onto ocean
[^22]: … if cost is no barrier
[^23]: … based on actual generation, not installed capacity
[^26]: Montana, Idaho, even Alaska
[^27]: … delivering an average of 0.114 GW in 8 dams, dominated by the 0.125 GW Keokuk dam 28: … delivering an average of 8.9 GW spread across 65 dams
[^29]: … aside from construction and decommissioning aspects
[^30]: … no imposed short-term fluctuations in available power, as happens for solar or wind
[^31]: … the dam itself, at least; turbines and generators will need periodic replacement
[^32]: … mountains or canyons to hold the reservoir
[^33]: … whether due to resource limits or climate change action
[^34]: It is hard to keep up 200 W for too long.
[^35]: The shelf is therefore 1 m off the same (original) floor.
[^36]: … using variables/symbols
[^37]: Pretend all the water is at this height.
[^38]: Assume 100% conversion efficiency for mathematical convenience.
[^39]: … cube root of volume
[^42]: Each stage will knock down the number further; report each in TW.
[^43]: This is the largest jump, keeping only 50 J out of every 2,300 J.
[^44]: $44,000\times 10^{12}$ W divided by $3.7\times 10^{14}\mathrm{m}^{2}$ of ocean surface is 120 $\mathrm{W/m}^{2}$.
[^45]: ⓘ The steady 120 W is already accounting for day/night: this is a time average.
