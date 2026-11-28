---
tags: [DWT, exercises, theory, exam]
source: "[[Lessons - DWT]]"
formula-sheet: "[[DWT - Formula Sheet-claude]]"
---
**Exam practice — Digital Warehousing & Transportation**
Built on the exams in `exams/` and on the exam exercises solved in class (Lesson 3, 9, 14, 16), limited to the topics of Lessons 1–16. Answers and solutions are in collapsible boxes: try first, then open.

**Contents**
- **PART A — THEORY**: A1 · 26 multiple-choice questions · A2 · 14 open questions (exam style "Illustrate…")
- **PART B — EXERCISES**: 42 numerical exercises in 3 blocks (T transport · P packaging · W warehouses), then exam simulations and the mistakes checklist

**How the exam is structured** (from the 8 papers): **1 numerical exercise + 1 theory question**. The exercises fall into 5 families:

| Family | Real exams | Exercises here |
|---|---|---|
| Transport costs, van deliveries, cross-dock | Lesson 3 | T1–T4, T7–T9, T11, T12, T14 |
| Routing with savings | Exam 9 (solved in Lesson 9) | T5, T6, T10, T13 |
| Packaging and single-use vs reusable | Exam 7, theory of Exam 2/6/ex.1 | P1–P12 |
| Bays, indexes, pallet AS/RS (FEM, dual, picking) | Exam 2, 3, 6 (solved in Lesson 14) | W1–W5, W8, W10–W12, W15, W16 |
| Shuttle/lift, miniload (BW) | Exam 8, Example 1 | W6, W7, W9, W13, W14 |

> [!tip] A method that always pays off at the exam
> 1. Write the **data** in a small table with units (min → h!). 2. Write the **general formula** before the numbers. 3. Round **down** deliveries and floors, **up** vehicles, machines and modules. 4. Close with a **one-line comment** (bottleneck, convenient/not convenient, U between 0.6 and 1).

---

# PART A — THEORY

Theory questions on Lessons 1–16. At the exam the theory part is usually **one open question** (e.g. "Illustrate…"); the multiple-choice questions are here to check that the concepts are solid. Model answers: [[DWT - Theory Summary-claude]].

## A1 · Multiple choice (26 questions)

**Q1.** Primary transport is:

- a) the sequence of deliveries from a warehouse to many customers
- b) B2B, large volumes, full truck, fixed origin → destination
- c) only rail and sea transport
- d) last-mile delivery with drones

> [!check]- Answer Q1
> **b** — e.g. plant → plant or plant → DC (distribution center). (a) is secondary transport.

**Q2.** Goods with density 250 kg/m³ are loaded on an articulated truck (28 t, ≈ 80 m³). Which saturation is reached first?

- a) weight
- b) volume
- c) both at the same time
- d) it depends on the distance

> [!check]- Answer Q2
> **b** — below 400 kg/m³ the volume saturates first (80 m³ × 250 = 20 t < 28 t).

**Q3.** The typical total internal cost of an articulated truck (own fleet) is about:

- a) 0.5 €/km
- b) 1.4 €/km
- c) 3 €/km
- d) 5 €/km

> [!check]- Answer Q3
> **b** — driver ≈ 0.5 + fuel ≈ 0.54 + truck 0.13 + taxes 0.02 + maintenance 0.03 + highway 0.1.

**Q4.** Which of these is an **external** cost of transport?

- a) fuel
- b) maintenance
- c) CO₂ emissions, noise, congestion
- d) highway tolls

> [!check]- Answer Q4
> **c** — external costs fall on society and the environment; the others are internal costs paid by the company.

**Q5.** When the trip distance decreases, the effective cost per km of a trip:

- a) decreases
- b) stays the same
- c) increases, because loading/unloading time is a fixed cost per trip
- d) becomes zero

> [!check]- Answer Q5
> **c** — e.g. 1.48 €/km at 500 km, 1.78 €/km at 100 km (Lesson 1).

**Q6.** Compared with ambient temperature, transporting frozen goods (−25 °C) costs about:

- a) +5 %
- b) +10÷15 %
- c) +40÷50 %
- d) +100 %

> [!check]- Answer Q6
> **c** — fresh goods (2÷4 °C) +10÷15 %.

**Q7.** With a cross-dock (XD) close to the customers, the maximum number of deliveries per van:

- a) decreases
- b) increases, because the time to reach the area ($T_{A/R}$) disappears
- c) does not change
- d) depends only on the stop time

> [!check]- Answer Q7
> **b** — $N_{max}=\frac{T-0}{t_{stop}+\bar d/\bar v}$ (Bologna: 13 → 24 deliveries/van).

**Q8.** The average distance between N customers in an area S is estimated as:

- a) $0.9\sqrt{S\cdot N}$
- b) $0.9\sqrt S/\sqrt N$
- c) $S/N$
- d) $0.9\,S/N$

> [!check]- Answer Q8
> **b** — (a) is the total tour length $D_T$.

**Q9.** In the Clarke & Wright method, the saving of joining customers i and j is:

- a) $d_{Wi}+d_{Wj}+d_{ij}$
- b) $d_{Wi}+d_{Wj}-d_{ij}$
- c) $2d_{Wi}-d_{ij}$
- d) $d_{ij}-d_{Wi}$

> [!check]- Answer Q9
> **b** — from $2d_{Wi}+2d_{Wj}-(d_{Wi}+d_{ij}+d_{Wj})$.

**Q10.** Savings are largest for customers that are:

- a) close to the depot and far from each other
- b) far from the depot and close to each other
- c) on opposite sides of the depot
- d) any pair, savings are always equal

> [!check]- Answer Q10
> **b** — customers on opposite sides of the depot give saving ≈ 0.

**Q11.** Two customers can be merged in the savings method only if:

- a) they are in the same city
- b) both are at the ends of their current routes and the constraints (capacity, shift time) are respected
- c) their saving is negative
- d) they have the same demand

> [!check]- Answer Q11
> **b**

**Q12.** The main advantage of the **consolidation method** is:

- a) it always gives the shortest distance
- b) little planning work and the same driver on the same route (learning effect)
- c) it needs routing software
- d) it eliminates stop times

> [!check]- Answer Q12
> **b** — its drawback is that longer distances can occur.

**Q13.** In the objective function $F_0=\beta d+(1-\beta)t$, the most common value of β is:

- a) 0
- b) 0.2
- c) 0.5
- d) 1

> [!check]- Answer Q13
> **b** — β = 1 distance only, β = 0 time only.

**Q14.** To choose between outsourced carriers with rates per pallet you need:

- a) only the total pallets per day
- b) the delivery spectrum (how many deliveries of 1, 2, 3… pallets)
- c) the €/km of your own truck
- d) the number of drivers

> [!check]- Answer Q14
> **b** — rates depend on the pallet band of each delivery.

**Q15.** How many 400×300 boxes fit in one layer of an ISO1 pallet (1200×800)?

- a) 6
- b) 8
- c) 9
- d) 10

> [!check]- Answer Q15
> **b** — (800/400)·(1200/300) = 2·4 = 8; the other orientation gives only 6.

**Q16.** The developed surface of an American box (FEFCO 0201) is:

- a) $(2L+2B)(H+2B)$
- b) $(2L+2B)(H+B)$
- c) $2(L+2H)(B+2H)$
- d) $L\cdot B\cdot H$

> [!check]- Answer Q16
> **b** — (a) fully overlapping flaps, (c) telescopic.

**Q17.** To minimize the cardboard of an American box with given internal dimensions, the dimension B should be:

- a) the largest
- b) the smallest
- c) equal to H
- d) irrelevant

> [!check]- Answer Q17
> **b** — B appears squared: $S=2LH+2BH+2LB+2B^2$. Optimal shape: L = H, B = L/2.

**Q18.** For the same L, B, H, which box uses the most cardboard?

- a) American
- b) half-overlapping flaps
- c) fully overlapping flaps
- d) telescopic

> [!check]- Answer Q18
> **d** — up to +150÷330 % vs American.

**Q19.** A typical cost of corrugated cardboard used to check box prices is:

- a) 0.12 €/m²
- b) 1.2 €/m²
- c) 12 €/m²
- d) 1.2 €/box

> [!check]- Answer Q19
> **b** — $C_{box}\approx1.2\cdot S$.

**Q20.** How many reusable boxes must be bought (minimum)?

- a) $N_{trip}$
- b) $2N_{trip}$
- c) $(I_c+2)\,N_{trip}$
- d) $I_c\cdot N_{trip}$

> [!check]- Answer Q20
> **c** — one set at the vendor, one travelling, one at the buyer + the empties going back.

**Q21.** With collapsible boxes $I_c=4$, the transport pattern is:

- a) always round trip
- b) every 4 trips: 3 one-way + 1 round trip
- c) always one way
- d) 2 one-way + 2 round trips

> [!check]- Answer Q21
> **b** — average trip cost $=\frac{3c_{dir}+c_{A/R}}{4}$.

**Q22.** The selectivity index of a double-deep rack is:

- a) 1
- b) 0.5
- c) 0.25
- d) 2

> [!check]- Answer Q22
> **b** — single deep = 1.

**Q23.** The access index $I_A$ is defined as … and an item with high $I_A$ should be placed …

- a) stock / movements, far from the I/O
- b) movements per day / average stock, close to the I/O
- c) movements / capacity of the warehouse, anywhere
- d) stock / capacity, close to the I/O

> [!check]- Answer Q23
> **b**

**Q24.** According to FEM 9.851, the reference points are:

- a) P1 (L/3; H/3), P2 (2L/3; 2H/3)
- b) P1 (L/5; 2H/3), P2 (2L/3; H/5)
- c) P1 (L/2; H/2) only
- d) P1 (L; H), P2 (0; 0)

> [!check]- Answer Q24
> **b**

**Q25.** The travel time of a stacker crane between two points is:

- a) $t_x+t_y$
- b) $\max(t_x;t_y)$
- c) $\min(t_x;t_y)$
- d) $(t_x+t_y)/2$

> [!check]- Answer Q25
> **b** — the two axes move simultaneously; each $t=l/v+v/a$.

**Q26.** The Bozer–White shape factor b indicates a good design when:

- a) b ≤ 0.3
- b) b ≈ 0.5
- c) b ≥ 0.8
- d) b > 2

> [!check]- Answer Q26
> **c** — b = 1 means the rack is "square in time"; b is always between 0 and 1.

---

## A2 · Open questions (14 questions)

Write the answer in 8–12 lines, then compare with the model answer.

**O1.** Illustrate the differences between primary and secondary transport (characteristics, modes, objectives).

> [!check]- Model answer O1
> - **Primary (B2B)**: large volumes, full truck/container, fixed routes from one origin to one destination (plant → plant, plant → DC). Road, rail, sea, air, intermodal. Objective: **saturate the vehicle** (weight 28 t or ≈ 80 m³; < 400 kg/m³ → volume first). Own fleet (road only) or outsourcing (any mode).
> - **Secondary**: sequence of deliveries from a warehouse to many customers (multi-drop), mostly vans; key parameters: deliveries per vehicle, stop time, distance between customers, routing.

**O2.** Which internal costs make up the cost of an own truck, and how do you obtain the €/km and the cost of a trip?

> [!check]- Model answer O2
> Driver (€/h ÷ average speed), fuel (€/l ÷ km/l), truck depreciation (investment ÷ years ÷ km/year), taxes and insurance, maintenance (4÷7 % of investment/year), highway (€/km × % on highway) → ≈ 1.4 €/km. Trip cost = €/km × distance + loading/unloading time × driver cost (≈ 45 + 45 min). Distance depends on one-way vs empty return; €/km grows on short trips. +10÷15 % fresh, +40÷50 % frozen.

**O3.** What is a cross-docking point? When is it convenient compared with direct deliveries?

> [!check]- Model answer O3
> A facility without stock, close to the customers, where goods arrive with one primary vehicle and are immediately re-sorted onto delivery vans. Vans start inside the area → $N_{max}$ grows (no $T_{A/R}$), fewer vans/drivers, fewer km and highway costs. Extra costs: primary transport, rent of the facility (6÷8 €/m²·month), handling. Convenient when the area is far and has many deliveries: compare total yearly costs (Lesson 3: ≈ 10 % saving).

**O4.** Describe the methods to plan secondary transport routes with an own fleet (consolidation, savings, extra mile).

> [!check]- Model answer O4
> - **Consolidation**: fixed main routes towards important customers; daily customers are added to them. + little planning, same driver (learning effect); − longer distances.
> - **Heuristics (software, e.g. PTV)**: input = daily orders, addresses, time windows, road/unloading constraints, fleet.
>   - **Savings**: start with one round trip per customer; merge the pair with max $S_{ij}=d_{Wi}+d_{Wj}-d_{ij}$ if they are route ends and capacity/time constraints hold; repeat. Objective $F=\beta d+(1-\beta)t$.
>   - **Extra mile**: start from the farthest customer and add the customer with the minimum extra distance; good but worse than savings.

**O5.** Illustrate the integrated study of the product–packaging system, with attention to the optimization of secondary packaging. *(Exam 2, Example 1)*

> [!check]- Model answer O5
> Product, primary, secondary (box), tertiary (pallet/UL) and vehicle are one system: the best box minimizes **total cost** (packaging + handling + storage + transport + damages). Rules: box footprint = sub-module of the pallet (600×400, 400×300…) → no overhang, saturated pallet (otherwise e.g. +16.6 % cost); UL height to saturate the truck (66 UL/trip); box cost ≈ 1.2 €/m² × S; in the American box B is squared → B = smallest dimension, optimal L = H, B = L/2 (−14 % in the lesson case). Compare alternatives on packaging + transport (lesson: two boxes within 1 %). Check supplier prices against S × 1.2.

**O6.** Describe the types of commercial cardboard boxes and their relative cost.

> [!check]- Model answer O6
> FEFCO codes: 02xx slotted boxes (0201 American, flaps meeting; half- and fully-overlapping flaps), 03xx telescopic (tray + lid), 04xx folder boxes, 05xx slide boxes, 06xx rigid cases, 07xx ready-glued/automatic bottom. Surfaces: American $(2L+2B)(H+B)$; half overlap $(2L+2B)(H+1.5B)$ ≈ +16÷20 %; full overlap $(2L+2B)(H+2B)$ ≈ +33÷40 %; telescopic $2(L+2H)(B+2H)$ ≈ +150÷330 %.

**O7.** Why standardize packaging, and how do you do it?

> [!check]- Model answer O7
> Fewer codes → lower safety stock, fewer damaged/obsolete cartons, higher volume per code → lower price, easier automatic packing. Method: cluster analysis on (L, B, H) with the same grammage, Euclidean distance $d=\sqrt{\Delta L^2+\Delta B^2+\Delta H^2}$; merge the closest boxes; the standard box contains both (max of each dimension); check extra cardboard vs savings, weighting by yearly quantities.

**O8.** Briefly and quantitatively illustrate how to perform a cost–benefit analysis between single-use and reusable packaging. *(Exam 6)*

> [!check]- Model answer O8
> Single-use: $Q\cdot c_{box}$ + one-way transport (+ damages). Reusable: buy $N=(I_c+2)N_{trip}$ boxes; cycles/year $=Q/N$; life [years] = life cycles / cycles per year; yearly packaging = $N c_{box}$ / life (= $Q c_{box}/C_{life}$). Transport: $I_c=1$ always round trip; $I_c>1$ every $I_c$ trips $(I_c-1)$ one-way + 1 round. Compare totals; reusable wins with high volumes, short distances, frequent deliveries, high damages of single-use (Lesson 8: 165 k€ vs 119 k€ vs 114 k€).

**O9.** Classify warehouses (by unit handled, automation, function).

> [!check]- Model answer O9
> Unit handled: unit loads/pallets (tertiary), totes/boxes (secondary), single items (primary), special goods (bars, pipes, reels). Automation: automated, semi-automated, manual (forklifts and lifts still present). Function: stocking; stocking + picking (picker-to-goods, goods-to-picker); sorting (transit points, cross-docks). Big hubs integrate several types → consolidation, lower time to market.

**O10.** How do you size the number of loading/unloading bays?

> [!check]- Model answer O10
> Truck arrivals are Poisson: $P(x)=\frac{(\lambda T)^x e^{-\lambda T}}{x!}$ with λ trucks/h and T unloading time (≈ 45 min, in hours). The service level (90÷95 %) = probability that an arriving truck finds a free bay = cumulative $\sum_{0}^{n-1}P(x)$; bays = first n reaching LS. Each bay ≈ 4.5 m of wall → the number of bays also shapes the building (rear vs lateral unloading, in/out same side or opposite).

**O11.** Define selectivity and access indexes and explain how they guide the choice of the storage system.

> [!check]- Model answer O11
> $I_S$ = UL reachable without moving others / total UL (warehouse parameter): single deep 1, double deep 0.5, deeper systems lower but better surface saturation. $I_A$ = movements per day / average stock (item parameter): high $I_A$ close to the I/O. High movements + few UL per item → AS/RS single deep; high movements + several UL per item → double deep; many UL of the same item and high throughput → multi-deep/shuttle.

**O12.** Describe the steps to design a single-deep AS/RS for unit loads.

> [!check]- Model answer O12
> Input: UL dimensions/weight, capacity, max throughput (in+out/h), available height and surface. (1) Machines $N=\lceil Q\cdot T_{target}/3600\rceil$ (110 s simple, 100 s combined). (2) Usable height = available − 1 m (roof/sprinkler) − 0.8 m (floor); $H_F$ = UL + 0.1 gap + 0.15 beam → floors. (3) Capacity per machine → modules (3 UL, 2.95 m, 2 racks per aisle) → L; H = (floors − 1)·$H_F$. (4) FEM 9.851 cycle times and utilization $U=\frac{Q T}{N\cdot3600\cdot A}$ (0.6 < U < 1, A ≈ 0.96).

**O13.** Compare FEM 9.851 and Bozer–White for the evaluation of AS/RS cycle times.

> [!check]- Model answer O13
> FEM: standard with reference points P1 (L/5; 2H/3), P2 (2L/3; H/5), trapezoidal speed profile $t=l/v+v/a$, simultaneous axes $\max(t_x,t_y)$; $T_{CS}=2T(IO\!-\!P1)+2T(IO\!-\!P2)+4t_f$, $T_{CC}$ via P1 → P2. BW: analytical expected time with random storage on a rack normalized in time ($T$, shape factor b), average speeds; $T_{CS}=2T(1+b^2/3)+4t_f$, $T_{CC}=T(4/3+b^2/2-b^3/30)+4t_f$. They coincide for b = 1; BW is used where FEM does not apply (miniloads, multi-command). b ≥ 0.8 good design.

**O14.** Simple vs combined cycle, dual AS/RS and multi-deep (shuttle + lift) systems: how do they affect throughput?

> [!check]- Model answer O14
> Simple cycle: one storage or one retrieval per trip; combined cycle: storage + retrieval in one trip (picking: 1 combined cycle per order line) → less empty travel. Dual (capacity 2): 2 in + 2 out per trip → ≈ +35 % throughput. Multi-deep: one shuttle/push mover per level on x, separate IN/OUT lifts on y; system throughput = min(levels × shuttle throughput, lift throughput) → the lift is usually the bottleneck; good for many UL of the same item with high throughput.

---

# PART B — EXERCISES

## Block T — Transport

**T1 · Cost per km of an articulated truck (warm-up)**
A company owns an articulated truck: investment 150 000 €, life 6 years, 200 000 km/year; driver 28 €/h at an average speed of 60 km/h; diesel 1.75 €/l with consumption 3 km/l; taxes + insurance 5 000 €/year; maintenance 6 % of the investment per year; highway 0.18 €/km on 60 % of the route. Loading and unloading: 40 + 40 min.
1. Compute the cost in €/km.
2. Cost of a 400 km trip (a) one way, (b) round trip with empty return; and the cost per km in both cases.
3. €/km of a one-way trip of 150 km. Comment.
4. What if the goods were frozen? If the goods density were 250 kg/m³, which saturation do you reach first?

> [!success]- Solution T1
> **1.** $c_{driver}=28/60=0.467$ · $c_{fuel}=1.75/3=0.583$ · $c_{truck}=\frac{150\,000}{6\cdot200\,000}=0.125$ · $c_{tax}=\frac{5\,000}{200\,000}=0.025$ · $c_{mnt}=\frac{0.06\cdot150\,000}{200\,000}=0.045$ · $c_{hw}=0.18\cdot0.6=0.108$
> $$c_{km}=0.467+0.583+0.125+0.025+0.045+0.108\simeq \mathbf{1.35\ €/km}$$
> Loading + unloading: $\frac{80}{60}\cdot28 = 37.3\ €/trip$.
> **2.** (a) $1.353\cdot400+37.3 = \mathbf{578.5\ €}$ → $578.5/400=1.45\ €/km$
> (b) $1.353\cdot800+37.3 = \mathbf{1\,119.7\ €}$ → $1.40\ €/km$ travelled, but **2.80 €/km useful** (you also pay the empty return).
> **3.** $1.353\cdot150+37.3=240.3\ €$ → $\mathbf{1.60\ €/km}$: the shorter the trip, the more the fixed loading/unloading time weighs.
> **4.** Frozen: +40÷50 % → $578.5\cdot1.45\approx 839\ €$. Density $250<400\ kg/m^3$ → **volume** saturates first ($80\ m^3\cdot250 = 20\ t < 28\ t$).

---

**T2 · Van deliveries in two areas (Lesson 3 style)**
A warehouse serves two areas every day. Shift 8 h, stop at customer 8 min, highway speed 90 km/h, 220 days/year, driver 30 €/h, consumption 8 l/100 km, diesel 1.8 €/l.

| Area | Distance WH→area | Deliveries/day | $\bar d$ between customers | $\bar v$ in city |
|---|---|---|---|---|
| Turin | 120 km | 140 | 2.5 km | 20 km/h |
| Florence | 180 km | 70 | 4 km | 25 km/h |

![[t2-network-claude.png|560]]

1. $N_{max}$ deliveries per van and number of vans per area.
2. Yearly driver cost per area.
3. Daily km and yearly fuel cost per area.
4. (bonus) If for an area you only know the surface $S=400\ km^2$ and $N=100$ customers, what is $\bar d$? And $D_T$?

> [!success]- Solution T2
> **1.** Turin: $T_{A/R}=\frac{2\cdot120}{90}=2.67\ h$
> $$N_{max}=\frac{8-2.67}{\frac{8}{60}+\frac{2.5}{20}}=\frac{5.33}{0.258}=20.6\to \mathbf{20}\qquad N_{van}=\lceil 140/20\rceil=\mathbf{7}$$
> Florence: $T_{A/R}=\frac{360}{90}=4\ h$
> $$N_{max}=\frac{8-4}{0.133+\frac{4}{25}}=\frac{4}{0.293}=13.6\to\mathbf{13}\qquad N_{van}=\lceil70/13\rceil=\lceil5.38\rceil=\mathbf{6}$$
> **2.** $C=N_{van}\cdot8\cdot220\cdot30$: Turin $\mathbf{369\,600\ €/year}$, Florence $\mathbf{316\,800\ €/year}$.
> **3.** Turin: 7 vans × 20 deliveries → $d=2\cdot120+19\cdot2.5=287.5\ km$ → $7\cdot287.5=2\,012.5\ km/day$ → $442\,750\ km/year$ → $442\,750\cdot\frac{8}{100}\cdot1.8=\mathbf{63\,756\ €}$
> Florence: 70/6 → 4 vans with 12 and 2 with 11 deliveries → $4(360+11\cdot4)+2(360+10\cdot4)=1\,616+800=2\,416\ km/day$ → $531\,520\ km/year$ → $\mathbf{76\,539\ €}$
> **4.** $\bar d=0.9\frac{\sqrt{400}}{\sqrt{100}}=\mathbf{1.8\ km}$ ; $D_T=0.9\sqrt{400\cdot100}=\mathbf{180\ km}$.

---

**T3 · Cross docking in Florence (continues T2)**
A cross docking point in Florence is evaluated: one van does WH→XD→WH every day (primary transport, XD = cross-dock); delivery vans start from the cross-dock. Each customer receives 1 tote 600×400×400 mm of 12 kg; the van has 12 m³ and 1 500 kg payload. Yearly cost of a van (excluding driver and fuel) 6 000 €. Highway: 0.1 €/km, today on 50 % of the km; in the to-be only the primary transport uses the highway (80 % of its km). The cross-dock takes 700 m² at 7 €/(m²·month) + 35 000 €/year of handling.

![[t3-crossdocking-claude.png|560]]
1. Vans needed for deliveries in the to-be.
2. Can primary transport be done with 1 van only?
3. Yearly savings (drivers, vans, fuel, highway) and net convenience.

> [!success]- Solution T3
> **1.** Without $T_{A/R}$: $N_{max}=\frac{8-0}{0.133+0.16}=27.3\to27$ → $N_{van}=\lceil70/27\rceil=\mathbf{3}$ (24+23+23 deliveries).
> **2.** Volume $70\cdot0.6\cdot0.4\cdot0.4=6.72\ m^3<12$; weight $70\cdot12=840\ kg<1\,500$ → **yes, 1 van**.
> **3.** Vans/drivers: as-is 6 → to-be 3+1 = 4 → −2
> - drivers: $2\cdot8\cdot220\cdot30=\mathbf{105\,600\ €}$ ; vans: $2\cdot6\,000=\mathbf{12\,000\ €}$
> - to-be km: secondary $(23+22+22)\cdot4=268$, primary $2\cdot180=360$ → $628\ km/day$ → $138\,160\ km/year$ (as-is 531 520)
> - fuel: $(531\,520-138\,160)\cdot0.08\cdot1.8=\mathbf{56\,644\ €}$
> - highway: as-is $531\,520\cdot0.5\cdot0.1=26\,576$; to-be $79\,200\cdot0.8\cdot0.1=6\,336$ → $\mathbf{20\,240\ €}$
> - **Total saving ≈ 194 484 €/year**; cross-dock cost $=700\cdot7\cdot12+35\,000=93\,800\ €/year$
> - **Net ≈ +100 700 €/year → cross docking is convenient.**

---

**T4 · Choosing the carrier (rates per pallet)**
Daily delivery spectrum (from Vicenza to Bologna):

| Pallets per delivery | 1 | 2 | 3 | 4 | 5 | 7 | 12 |
|---|---|---|---|---|---|---|---|
| N° deliveries/day | 12 | 8 | 5 | 6 | 4 | 3 | 2 |

Rates €/pallet — Provider 1: 1 pallet 32; 2 pallets 27; 3 pallets 22; 4–5 pallets 18; 6–10 pallets 15; >10 pallets 12. Provider 2: 1–2 pallets 29; 3–5 pallets 19; >5 pallets 13.
Which provider do you choose? How much do you save in a 220-day year?

> [!success]- Solution T4
>
> | Pallets/deliv. | Deliveries | Tot pallets | P1 | P2 |
> |---|---|---|---|---|
> | 1 | 12 | 12 | 12·32=384 | 12·29=348 |
> | 2 | 8 | 16 | 16·27=432 | 16·29=464 |
> | 3 | 5 | 15 | 15·22=330 | 15·19=285 |
> | 4 | 6 | 24 | 24·18=432 | 24·19=456 |
> | 5 | 4 | 20 | 20·18=360 | 20·19=380 |
> | 7 | 3 | 21 | 21·15=315 | 21·13=273 |
> | 12 | 2 | 24 | 24·12=288 | 24·13=312 |
> | **Tot** | | **132** | **2 541 €/d** | **2 518 €/d** |
>
> **Provider 2**, saving $23\cdot220\approx\mathbf{5\,060\ €/year}$. Note: the choice depends on the spectrum (many 1-pallet deliveries favour P2).

---

**T5 · Savings — 1 vehicle (Exam 9 style)**
Warehouse W at (0;0); customers (coordinates in km): C1(−15;5), C2(−10;−10), C3(5;15), C4(10;10), C5(20;−5), C6(5;−15). Rectilinear (Manhattan) distances, $\bar v=50\ km/h$, stop 15 min, shift 8 h, vehicle 1.40 €/km, driver 30 €/h paid during stops.

![[t5-network-claude.png|560]]
Find the number of vehicles, the tour with the savings method and the daily cost.

> [!success]- Solution T5
> **Distances from W**: C1 20 · C2 20 · C3 20 · C4 20 · C5 25 · C6 20 → $D_0=2\cdot125=\mathbf{250\ km}$
> **Savings** ($S_{ij}=d_{Wi}+d_{Wj}-d_{ij}$), sorted: C3–C4 **30** (10) · C5–C6 20 · C4–C5 20 · C2–C6 20 · C1–C2 20 · C4–C6, C3–C6, C3–C5, C2–C5, C1–C4, C1–C3 = 10 · others 0.
> **Iterations**
> 1. C3–C4 → 250−30 = 220
> 2. C5–C6 → 200
> 3. C4–C5 (ends of C3-C4 and C5-C6) → C3-C4-C5-C6, 180
> 4. C2–C6 → C3-C4-C5-C6-C2, 160
> 5. C1–C2 → **W→C3→C4→C5→C6→C2→C1→W = 140 km**
>
> ![[t5-solution-claude.png|560]]
> Remaining savings: customers are no longer route ends or are on the same route → stop.
> **Vehicles**: time $=\frac{140}{50}+6\cdot0.25=2.8+1.5=4.3\ h\le8$ → **1 vehicle**.
> **Cost**: $140\cdot1.4+6\cdot0.25\cdot30=196+45=\mathbf{241\ €/day}$.

---

**T6 · Savings with a shift constraint — more vehicles**
W(0;0); customers (km): A(−25;20), B(−15;30), C(−30;5), D(20;25), E(30;15), F(25;−10), G(−10;−25), H(5;−30). Manhattan, $\bar v=50$ km/h, **stop 30 min**, shift 8 h, 1.40 €/km, driver 30 €/h during stops.

![[t6-network-claude.png|560]]
Apply the savings method respecting the shift: how many vehicles? Which tours? Daily cost?

> [!success]- Solution T6
> $d_W$: A 45, B 45, C 35, D 45, E 45, F 35, G 35, H 35 → $D_0=640\ km$
> Main savings: D–E 70 · A–B 70 · A–C 60 · G–H 50 · E–F 50 · B–D 50 · D–F 40 · B–C 40 · A–D 40 · F–H 30 · … · F–G 20 · C–G 20
> 1. D–E (70) → 570 2. A–B (70) → 500 3. A–C (60) → B-A-C, 440 4. G–H (50) → 390 5. E–F (50) → D-E-F, 340 6. B–D (50) → C-A-B-D-E-F, 290
> 7. F–H (30): route C-A-B-D-E-F-H-G = 260 km → time $260/50+8\cdot0.5=9.2\ h>8$ ❌ rejected (same for F–G, C–G)
> **Final tours**
> - Route 1: W→C→A→B→D→E→F→W = **200 km**, $4+6\cdot0.5=7.0\ h$
> - Route 2: W→G→H→W = **90 km**, $1.8+2\cdot0.5=2.8\ h$
>
> ![[t6-solution-claude.png|560]]
> Total 9.8 h > 8 h → **2 vehicles**. Cost $=290\cdot1.4+8\cdot0.5\cdot30=406+120=\mathbf{526\ €/day}$.
> 💡 At the exam: always write the time check when merging two routes.

---

**T7 · Own truck vs outsourced carrier**
Vicenza → Turin is 360 km. Your own articulated truck costs 1.4 €/km + 37.5 €/trip (loading + unloading). An outsourced carrier quotes 450 € one way and 720 € round trip (lesson table).
1. Cost with your own truck if (a) the truck finds another job at destination, (b) it comes back empty.
2. Which solution do you choose in each case?
3. Below which €/km would your own truck become convenient in case (a)? And in case (b)?

> [!success]- Solution T7
> **1.** (a) $1.4\cdot360+37.5=\mathbf{541.5\ €}$ ; (b) $1.4\cdot720+37.5=\mathbf{1\,045.5\ €}$
> **2.** Outsourcing in both cases (450 < 541.5; 720 < 1 045.5): the carrier saturates its vehicles with other customers' loads, especially on the return.
> **3.** (a) $c_{km}<\frac{450-37.5}{360}=\mathbf{1.15\ €/km}$ ; (b) $c_{km}<\frac{720-37.5}{720}=\mathbf{0.95\ €/km}$ → not realistic: own fleet makes sense only with return loads (saturation of the return trip).

---

**T8 · Van fleet sizing from the area surface**
A delivery area of **900 km²** has **144 deliveries/day**; the warehouse is 60 km away (highway 80 km/h). Stop 10 min, city speed 25 km/h, shift 8 h, 250 days/year. Driver 28 €/h, fuel 9 l/100 km at 1.7 €/l, van lease 7 000 €/year.
1. Average distance between customers.
2. $N_{max}$, number of vans, daily km.
3. Yearly total cost (drivers + fuel + lease).

> [!success]- Solution T8
> **1.** $\bar d=0.9\frac{\sqrt{900}}{\sqrt{144}}=0.9\cdot\frac{30}{12}=\mathbf{2.25\ km}$
> **2.** $T_{A/R}=\frac{120}{80}=1.5\ h$ ; $N_{max}=\frac{8-1.5}{\frac{10}{60}+\frac{2.25}{25}}=\frac{6.5}{0.2567}=25.3\to\mathbf{25}$ ; $N_{van}=\lceil144/25\rceil=\mathbf{6}$ (24 deliveries each)
> km/van $=120+23\cdot2.25=171.75$ → $6\cdot171.75=\mathbf{1\,030.5\ km/day}$ → $257\,625\ km/year$
> **3.** Drivers $6\cdot8\cdot250\cdot28=336\,000$ · fuel $257\,625\cdot0.09\cdot1.7=39\,417$ · lease $6\cdot7\,000=42\,000$ → **≈ 417 400 €/year**

---

**T9 · How much can a cross-dock cost? (break-even)**
Same data as T2, area **Turin** (7 vans today, 442 750 km/year, 50 % on highway at 0.1 €/km). A cross-dock (XD) in Turin is evaluated: 1 van does WH→XD→WH (240 km/day, 80 % highway); each customer gets 1 tote 600×400×300 of 10 kg; van 12 m³ / 1 500 kg; van cost 6 000 €/year; handling in the XD 35 000 €/year.
1. Vans needed in the to-be and check of the primary van.
2. Yearly savings.
3. Maximum rent you can accept, and the maximum surface at 7 €/(m²·month).

> [!success]- Solution T9
> **1.** $N_{max}=\frac{8}{0.133+0.125}=31.0\to30$ → $\lceil140/30\rceil=\mathbf{5}$ vans (28 deliveries each). Primary: $140\cdot0.072=10.1\ m^3<12$, $1\,400\ kg<1\,500$ → 1 van ✓ (tight!)
> **2.** Vans 7 → 5+1 = 6 (−1)
> - drivers $1\cdot8\cdot220\cdot30=52\,800$ · van $6\,000$
> - to-be km/day: $5\cdot27\cdot2.5=337.5$ + 240 = 577.5 → $127\,050\ km/year$ → fuel $(442\,750-127\,050)\cdot0.08\cdot1.8=45\,461$
> - highway: as-is $442\,750\cdot0.5\cdot0.1=22\,138$; to-be $240\cdot220\cdot0.8\cdot0.1=4\,224$ → $\mathbf{17\,914}$
> - **Total ≈ 122 175 €/year**
> **3.** Max rent $=122\,175-35\,000=\mathbf{87\,175\ €/year}$ → $\frac{87\,175}{7\cdot12}\approx\mathbf{1\,040\ m^2}$. Above this the cross-dock is not convenient.

---

**T10 · Savings with vehicle capacity**
Warehouse W and 5 customers; vans carry **10 pallets**. Distances [km] (not Manhattan):

| | W | A | B | C | D | E |
|---|---|---|---|---|---|---|
| **A** | 12 | – | 6 | 14 | 25 | 15 |
| **B** | 15 | | – | 8 | 22 | 20 |
| **C** | 20 | | | – | 12 | 25 |
| **D** | 18 | | | | – | 14 |
| **E** | 10 | | | | | – |
| **Demand [pallets]** | | 3 | 4 | 3 | 5 | 2 |

Build the routes with the savings method respecting capacity.

![[t10-network-claude.png|480]]

> [!success]- Solution T10
> $D_0=2(12+15+20+18+10)=\mathbf{150\ km}$
> Savings: B–C 27 · C–D 26 · A–B 21 · A–C 18 · D–E 14 · B–D 11 · A–E 7 · C–E 5 · B–E 5 · A–D 5
> 1. B–C (27): load 4+3 = 7 ✓ → 123
> 2. C–D (26): load 7+5 = 12 > 10 ❌
> 3. A–B (21): A-B-C, load 10 ✓ → 102
> 4. A–C: same route · D–E (14): load 7 ✓ → 88
> 5. A–E, C–E, A–D: load 17 ❌ → stop
> **Routes**: W-A-B-C-W = **46 km** (10 pallets) and W-D-E-W = **42 km** (7 pallets) → **88 km**, 2 vans (or 1 van doing 2 trips if time allows).

---

**T11 · Own fleet vs outsourced for the T6 deliveries**
Use the T6 solution (own fleet: 526 €/day variable cost, 2 vehicles with a fixed cost of 80 €/day each). Pallets per customer: A 2, B 1, C 3, D 4, E 2, F 1, G 5, H 2. Outsourced rates (Provider 1 of T4): 1 pallet 32; 2 → 27; 3 → 22; 4–5 → 18 €/pallet. Which is cheaper?

> [!success]- Solution T11
> Outsourced: A $2\cdot27$ + B $32$ + C $3\cdot22$ + D $4\cdot18$ + E $2\cdot27$ + F $32$ + G $5\cdot18$ + H $2\cdot27$ $=54+32+66+72+54+32+90+54=\mathbf{454\ €/day}$ (20 pallets)
> Own fleet: $526+2\cdot80=\mathbf{686\ €/day}$ → **outsourcing is cheaper** (−34 %). Own fleet wins only with denser routes / more volume per stop.

---

**T12 · Saturation: volume or weight?**
1. Washing machines (density ≈ 100 kg/m³), 1 500 m³/month from Shanghai to Rotterdam in 40 ft containers (≈ 67 m³, 26 t), 3 000 €/container. How many containers and what cost? Which saturation?
2. Frozen fish (700 kg/m³), 400 t/month by articulated truck (28 t, 80 m³), base rate 1 200 €/trip at ambient temperature. Trips and monthly cost (use +45 % for frozen).

> [!success]- Solution T12
> **1.** $100<400\ kg/m^3$ → **volume** saturates: $\lceil1\,500/67\rceil=\mathbf{23}$ containers → $\mathbf{69\,000\ €/month}$ (weight per container only $67\cdot100=6.7\ t\ll26\ t$).
> **2.** $700\ge400$ → **weight** saturates: $\lceil400/28\rceil=\mathbf{15}$ trips (volume used $28/0.7=40\ m^3$ of 80). Cost $15\cdot1\,200\cdot1.45=\mathbf{26\,100\ €/month}$.

---

**T13 · REAL EXAM — Exam 9 (savings)** · `exams/Exam 9 Saving.pdf`

> [!quote]- Original exam text
> ![[Exam 9 Saving.pdf#height=550]]

Manhattan distances read from the grid (as solved in Lesson 9), $\bar v=50$ km/h, stop 15 min, shift 8 h, vehicle 1.40 €/km (driver excluded during stops), driver 30 €/h:

| From W | C1 17.5 | C2 20 | C3 27.5 | C4 10 | C5 17.5 | C6 20 |
|---|---|---|---|---|---|---|

Relevant pairs: C1–C2 7.5 · C1–C4 7.5 · C2–C4 10 · C3–C5 10 · C3–C6 7.5 · C5–C6 12.5 (all other pairs are on opposite sides of W → saving ≈ 0).
Fleet size, routes and daily cost.

> [!success]- Solution T13
> $D_0=2(17.5+20+27.5+10+17.5+20)=\mathbf{225\ km}$
> Savings: C3–C6 **40** · C3–C5 35 · C1–C2 30 · C5–C6 25 · C1–C4 20 · C2–C4 20
> 1. C3–C6 → 185 2. C5–C3 (35) → C5-C3-C6, 150 3. C1–C2 → 120 4. C4–C1 (20) → C4-C1-C2, 100 5. merging the two routes saves 0 → stop
> **Routes**: W→C5→C3→C6→W (**55 km**) and W→C4→C1→C2→W (**45 km**) = **100 km/day**
> **Fleet**: $\bar d=10$ km → $N_{max}=\frac{8}{0.25+10/50}=17.8\to17\ge6$; time $=100/50+6\cdot0.25=3.5\ h$ → **1 truck** doing both routes.
> **Cost**: $100\cdot1.4+6\cdot0.25\cdot30=140+45=\mathbf{185\ €/day}$

---

**T14 · REAL EXAM — Lesson 3 (Milan & Bologna, vans + cross-dock)**
Warehouse in Verona. Milan: 135 km, 120 deliveries/day, $\bar d$ = 3 km, $\bar v$ = 20 km/h. Bologna: 160 km, 85 deliveries/day, $\bar d$ = 5 km, $\bar v$ = 30 km/h. Highway 90 km/h, stop 10 min, shift 8 h, 220 days/year, driver 30 €/h, fuel 7 l/100 km at 1.2 €/l.
1. Vans per area. 2. Yearly driver and fuel cost per area. 3. With a cross-dock in Bologna: vans needed.

![[t14-network-claude.png|560]]

> [!success]- Solution T14
> **1.** Milan $N_{max}=\frac{8-270/90}{10/60+3/20}=\frac{5}{0.317}=15.8\to15$ → $\lceil120/15\rceil=\mathbf{8}$ vans; Bologna $N_{max}=\frac{8-3.56}{0.167+0.167}=13.3\to13$ → $\lceil85/13\rceil=\mathbf{7}$ vans
> **2.** Drivers: Milan $8\cdot8\cdot220\cdot30=\mathbf{422\,400}$; Bologna $\mathbf{369\,600}$ €/year
> Milan km/day $8\,(270+14\cdot3)=2\,496$ → fuel $2\,496\cdot220\cdot0.07\cdot1.2=\mathbf{46\,126\ €}$
> Bologna: 1 van × 13 + 6 vans × 12 → $(320+12\cdot5)+6(320+11\cdot5)=2\,630\ km/day$ → $\mathbf{48\,602\ €}$
> **3.** $N_{max}=\frac{8}{0.167+0.167}=24$ → $\lceil85/24\rceil=\mathbf{4}$ vans + 1 primary van (85 totes = 10.2 m³, 170 kg ✓) → saving of 2 drivers ≈ 105 600 €/year (full comparison in Lesson 3–4: net saving ≈ 100 000 €/year).

---

## Block P — Packaging

**P1 · Pallet saturation**
ISO1 pallet 1200×800, maximum UL height 1.35 m (wooden pallet 0.15 m).
1. Box 350×250×280 mm: how many boxes per layer (try both orientations), how many layers, how many per pallet? What % of the surface is empty?
2. Same for 400×300 and 300×190 (footprint). Which would you suggest?

> [!success]- Solution P1
> **1.** Orientation 1: $\lfloor1200/350\rfloor\cdot\lfloor800/250\rfloor=3\cdot3=9$ ; orientation 2: $\lfloor800/350\rfloor\cdot\lfloor1200/250\rfloor=2\cdot4=8$ → **9/layer**
> Layers: $\lfloor(1.35-0.15)/0.28\rfloor=4$ → **36 boxes/UL**. Used surface $9\cdot0.0875=0.7875\ m^2$ out of $0.96$ → **18 % empty** (≈ higher transport/storage costs).
> **2.** 400×300: $3\cdot2=6$ or $2\cdot4=$ **8** → 100 % saturation. 300×190: $4\cdot4=16$ (5 % empty).
> **Suggestion**: use a **module** (400×300 or 300×200) → saturated pallet with no overhang.
>
> ![[p1-pallet-layers-claude.png|560]]

---

**P2 · Box types and price check**
1. Box with L = 0.5, B = 0.3, H = 0.4 m. Compute surface and cost (1.2 €/m²) for: (a) American, (b) half-overlapping flaps, (c) fully overlapping flaps, (d) telescopic. % vs American?
2. The supplier quotes these prices; are they correct? How much do you pay more (or less) per year?

| Box | L×B×H [m] | Type | Q [box/year] | Price |
|---|---|---|---|---|
| 1 | 0.6×0.4×0.3 | American | 50 000 | 1.40 € |
| 2 | 0.4×0.3×0.25 | American | 120 000 | 0.95 € |
| 3 | 0.6×0.3×0.4 | half overlap | 80 000 | 1.80 € |

> [!success]- Solution P2
> **1.** $(2L+2B)=1.6$
>
> ![[p2-american-blank-claude.png|560]]
> - (a) $1.6\cdot(0.4+0.3)=1.12\ m^2$ → **1.34 €**
> - (b) $1.6\cdot(0.4+0.45)=1.36$ → **1.63 €** (+21 %)
> - (c) $1.6\cdot(0.4+0.6)=1.60$ → **1.92 €** (+43 %)
> - (d) $2(0.5+0.8)(0.3+0.8)=2.86$ → **3.43 €** (+155 %)
> **2.**
> - Box 1: $S=2.0\cdot0.7=1.40$ → expected 1.68 €; price 1.40 → **ok (even good)**
> - Box 2: $S=1.4\cdot0.55=0.77$ → expected 0.924 €; price 0.95 → **too high**: $(0.95-0.924)\cdot120\,000\approx\mathbf{3\,120\ €/year}$ to renegotiate
> - Box 3: $S=1.8\cdot(0.4+0.45)=1.53$ → expected 1.84 €; price 1.80 → **ok**

---

**P3 · Orienting the dimensions correctly (Lesson 6 style)**
The content requires an American box with internal dimensions 450, 350, 250 mm. Today it is made with L = 0.45, B = 0.35, H = 0.25. 25 000 boxes are used per month (1.2 €/m²).
Is there a better orientation? Yearly saving?

> [!success]- Solution P3
> $S=(2L+2B)(H+B)$: B appears twice → **B = smallest dimension**.
> - as-is: $(0.9+0.7)(0.25+0.35)=0.96\ m^2$ → $0.96\cdot1.2\cdot300\,000=345\,600\ €/year$
> - to-be: L = 0.45, B = 0.25, H = 0.35 → $(0.9+0.5)(0.35+0.25)=0.84\ m^2$ → $302\,400\ €/year$
> - **Saving 43 200 €/year (−12.5 %)**. (Remember: ideal shape L = H, B = L/2.)

---

**P4 · Integrated product–packaging study (Lesson 6 style, snacks)**
180 000 bags/month are shipped. Max UL 1.35 m (pallet 0.15 m), articulated truck 66 UL/trip at 1 400 €/trip, cardboard 1.2 €/m². Two American box alternatives:
- (a) 600×400×300 mm (L×B×H), 30 bags
- (b) 400×300×300 mm, 12 bags

Compare the monthly packaging + transport cost.

> [!success]- Solution P4
>
> | | (a) 600×400×300 | (b) 400×300×300 |
> |---|---|---|
> | $S$ | $(1.2+0.8)(0.3+0.4)=1.40$ | $(0.8+0.6)(0.3+0.3)=0.84$ |
> | €/box | 1.68 | 1.008 |
> | boxes/month | 180 000/30 = 6 000 | 180 000/12 = 15 000 |
> | Packaging | **10 080 €** | **15 120 €** |
> | boxes/UL | 4/layer × 4 layers = 16 | 8 × 4 = 32 |
> | UL/month | 375 | 468.75 |
> | trips/month | 5.68 | 7.10 |
> | Transport | **7 955 €** | **9 943 €** |
> | **Total** | **18 035 €/month** | **25 063 €/month** |
>
> **(a) is better (−28 %)**: less cardboard per bag and "fuller" UL. Comment: always evaluate both costs together (in Lesson 6 the totals differed by only 1 %).

---

**P5 · Standardization (cluster analysis)**

| Box | L | B | H | Q [box/year] |
|---|---|---|---|---|
| a | 0.40 | 0.30 | 0.20 | 80 000 |
| b | 0.40 | 0.30 | 0.22 | 40 000 |
| c | 0.60 | 0.40 | 0.30 | 60 000 |
| d | 0.58 | 0.40 | 0.30 | 30 000 |
| e | 0.30 | 0.20 | 0.15 | 100 000 |

Same cardboard, American boxes, 1.2 €/m².
1. Compute the distances and identify the clusters.
2. Yearly cost before and after standardization (cluster box = max of each dimension). And if, thanks to higher volumes, the supplier gives −8 % on all codes?

> [!success]- Solution P5
> **1.** $d_{ab}=0.02$, $d_{cd}=0.02$; all others ≥ 0.15 (e.g. $d_{ae}=0.150$, $d_{ad}=0.229$, $d_{ce}=0.391$) → clusters **{a,b}**, **{c,d}**, **{e}**.
> **2.** Before: a 0.70 m² → 67 200 · b 0.728 → 34 944 · c 1.40 → 100 800 · d 1.372 → 49 392 · e 0.35 → 42 000 → **294 336 €/year**
> After: ab = 0.40×0.30×0.22 (0.728 m², 120 000 boxes) · cd = 0.60×0.40×0.30 (1.40 m², 90 000 boxes) · e → **298 032 €/year** (+1.3 %: more cardboard)
> With −8 %: **274 189 €/year → saving ≈ 20 000 €/year**, plus the qualitative advantages (less safety stock, fewer codes, automated packing).

---

**P6 · REAL EXAM — Exam 7 (reusable packaging)** · `exams/exam 7 reusable packaging.pdf`

> [!quote]- Original exam text
> ![[exam 7 reusable packaging.pdf#height=550]]

Customers in Lyon (700 km) and Mestre (60 km) served from Vicenza. Primary packaging 100×100×100 mm, 1 product, 15 €/piece. Lyon: 1 delivery/week, 66 pallets/delivery, 980 € (direct) or 1 570 € (direct + reverse). Mestre: 5 deliveries/week, 66 pallets, 100 € or 160 €. 52 weeks.

![[p6-network-claude.png|560]]

| Packaging | L×B×H | Cost | Life [cycles] | Boxes/pallet |
|---|---|---|---|---|
| Single-use | 400×300×200 | 1.4 €/m² | 1 | 40 |
| Reusable, $I_c=1$ | 400×300×200 | 10 € | 50 | 40 |
| Collapsible, $I_c=4$ | 400×300×200 | 15 € | 30 | 40 |

1. Best solution for Mestre and for Lyon. 2. With 0.5 % damage on single-use, does anything change? 3. If you can change the shape of the single-use box (American), what do you suggest?

> [!success]- Solution P6
> **Common data**: $N_{trip}=66\cdot40=2\,640$ boxes/trip (24 products/box). Lyon $Q=52\cdot2\,640=137\,280$ boxes/year; Mestre $Q=260\cdot2\,640=686\,400$.
> Single-use: $S=(0.8+0.6)(0.2+0.3)=0.70\ m^2$ → $0.98\ €/box$.
>
> ![[reusable-loop-claude.png|560]]
>
> | **Lyon** | Single-use | $I_c=1$ | $I_c=4$ |
> |---|---|---|---|
> | Boxes to buy | — | $3\cdot2\,640=7\,920$ | $6\cdot2\,640=15\,840$ |
> | Investment | — | 79 200 | 237 600 |
> | cycles/year → life | — | 17.3 → 2.88 years | 8.67 → 3.46 years |
> | Packaging €/year | 134 534 | 27 456 | 68 640 |
> | €/trip | 980 | 1 570 | $(3\cdot980+1570)/4=1\,127.5$ |
> | Transport €/year | 50 960 | 81 640 | 58 630 |
> | **Total** | 185 494 | **109 096** ✅ | 127 270 |
>
> | **Mestre** | Single-use | $I_c=1$ | $I_c=4$ |
> |---|---|---|---|
> | cycles/year → life | — | 86.7 → 0.58 years | 43.3 → 0.69 years |
> | Packaging €/year | 672 672 | 137 280 | 343 200 |
> | €/trip | 100 | 160 | $(3\cdot100+160)/4=115$ |
> | Transport €/year | 26 000 | 41 600 | 29 900 |
> | **Total** | 698 672 | **178 880** ✅ | 373 100 |
>
> **1.** For both the best is the **reusable not collapsible ($I_c=1$)**. (The collapsible one saves transport, but has a short life and costs more.)
> **2.** Single-use damages: Lyon $137\,280\cdot24\cdot15\cdot0.5\%=247\,104\ €$; Mestre $1\,235\,520\ €$ → single-use gets even worse: **solutions unchanged**.
> **3.** American with **B = smallest dimension**: L = 0.4, B = 0.2, H = 0.3 → $S=(0.8+0.4)(0.5)=0.60\ m^2$ → 0.84 €/box (−14 %). Single-use totals: Lyon 166 275, Mestre 602 576 → **still not convenient**. (A 400×200 footprint is still a pallet module: 12 per layer.)
> 💡 For Lyon (700 km), in reality more boxes in circulation would be needed due to transit time: mention it as a comment.

---

**P7 · Single-use vs reusable — "neck and neck" variant**
2 deliveries/week (104 trips/year), 60 pallets/trip, 25 boxes/pallet. Transport 1 100 € one way, 1 800 € round trip. Compare: (a) single-use 0.85 €/box; (b) reusable $I_c=1$, 12 €, 60 cycles; (c) collapsible $I_c=3$, 20 €, 40 cycles; (d) collapsible $I_c=5$, 28 €, 50 cycles.

> [!success]- Solution P7
> $N_{trip}=60\cdot25=1\,500$, $Q=156\,000$ boxes/year.
>
> | | (a) | (b) $I_c=1$ | (c) $I_c=3$ | (d) $I_c=5$ |
> |---|---|---|---|---|
> | Boxes | — | 4 500 | 7 500 | 10 500 |
> | Investment | — | 54 000 | 150 000 | 294 000 |
> | cycles/year · life | — | 34.7 · 1.73 y | 20.8 · 1.92 y | 14.9 · 3.37 y |
> | Packaging | 132 600 | 31 200 | 78 000 | 87 360 |
> | €/trip | 1 100 | 1 800 | $(2\cdot1100+1800)/3=1\,333$ | $(4\cdot1100+1800)/5=1\,240$ |
> | Transport | 114 400 | 187 200 | 138 667 | 128 960 |
> | **Total** | 247 000 | 218 400 | 216 667 | **216 320** |
>
> (d) wins by a small margin, but (b), (c), (d) are within 1 %: the choice depends on qualitative factors (initial investment 54 k€ vs 294 k€, risk, space for empties). Single-use loses.

---

**P8 · Price check on four box types**
Cardboard 1.2 €/m². Check the supplier prices and the yearly over/under-price.

| Box | Type | L×B×H [m] | Q [box/year] | Price |
|---|---|---|---|---|
| 1 | American | 0.5×0.4×0.3 | 40 000 | 1.20 € |
| 2 | half-overlapping flaps | 0.4×0.3×0.3 | 60 000 | 1.05 € |
| 3 | fully overlapping flaps | 0.6×0.4×0.2 | 20 000 | 2.10 € |
| 4 | telescopic | 0.4×0.3×0.1 | 10 000 | 1.40 € |

> [!success]- Solution P8
> - Box 1: $S=(1.0+0.8)(0.3+0.4)=1.26$ → expected 1.51 € > 1.20 → ok
> - Box 2: $S=(0.8+0.6)(0.3+0.45)=1.05$ → expected 1.26 € > 1.05 → ok
> - Box 3: $S=(1.2+0.8)(0.2+0.8)=2.00$ → expected 2.40 € > 2.10 → ok
> - Box 4: $S=2(0.4+0.2)(0.3+0.2)=0.60$ → expected 0.72 € **< 1.40** → overpriced: $(1.40-0.72)\cdot10\,000=\mathbf{6\,800\ €/year}$ to renegotiate
> Comment: plot expected cost vs price (as in Lesson 7): points above the line are overpriced.

---

**P9 · Unit load height: the weight trap**
Boxes 400×300×250 mm, 18 kg each, 8 per layer on an ISO1 pallet (0.15 m, 25 kg). Truck: 33 UL places per layer, internal height 2.7 m, 28 t.
- Option A: UL max 1.35 m, 2 UL stacked (66 UL places)
- Option B: UL max 2.40 m, 1 UL per place (33 places)

Boxes per truck in both options? Which saturation do you reach?

![[p9-ul-options-claude.png|560]]

> [!success]- Solution P9
> Density of a box $=18/(0.4\cdot0.3\cdot0.25)=600\ kg/m^3\ge400$ → **weight saturates first**.
> **A**: layers $\lfloor1.2/0.25\rfloor=4$ → 32 boxes, UL weight $32\cdot18+25=601\ kg$; 66 UL would weigh 39.7 t > 28 t → max $\lfloor28\,000/601\rfloor=46$ UL → **1 472 boxes**
> **B**: layers $\lfloor2.25/0.25\rfloor=9$ → 72 boxes, UL weight 1 321 kg; 33 UL = 43.6 t > 28 t → max 21 UL → **1 512 boxes**
> Both are weight-limited (≈ 1 500 boxes/trip): the height choice matters for handling and stacking, not for transport.

---

**P10 · Break-even transport cost for reusable packaging**
Q = 100 000 boxes/year, 100 trips/year (1 000 boxes/trip). Single-use box 1.10 €. Reusable not collapsible ($I_c=1$) 9 €, 100 cycles. The round trip costs 1.6 × the direct trip $d$.
1. Write total yearly cost of both solutions as a function of $d$.
2. Below which direct trip cost is reusable convenient?

> [!success]- Solution P10
> **1.** Single-use: $100\,000\cdot1.10+100\,d=110\,000+100\,d$
> Reusable: boxes $3\cdot1\,000=3\,000$ (27 000 €), cycles/year $=33.3$, life $=3$ years → $9\,000\ €/year$ (= $Q\cdot c/C_{life}$); transport $100\cdot1.6\,d=160\,d$ → $9\,000+160\,d$
> **2.** $110\,000+100d=9\,000+160d$ → $d^*=\mathbf{1\,683\ €/trip}$. Reusable wins for $d<1\,683$ € (short/medium distances); beyond it single-use wins.

---

**P11 · Optimal American box for a given volume**
You need an American box with internal volume 0.032 m³.
1. Find L, B, H with the optimal shape rule and its surface.
2. Compare with a cube and with 0.4×0.4×0.2 placed with B = 0.4.

> [!success]- Solution P11
> **1.** $L=H$, $B=L/2$ → $V=L^3/2$ → $L=\sqrt[3]{0.064}=\mathbf{0.4}$ → **L = 0.4, B = 0.2, H = 0.4** → $S=(0.8+0.4)(0.4+0.2)=\mathbf{0.72\ m^2}$ (0.86 €)
> **2.** Cube 0.317 m: $S=(4\cdot0.317)(0.635)=0.81\ m^2$ (+12 %); 0.4×0.4×0.2 with B = 0.4: $S=(0.8+0.8)(0.2+0.4)=0.96\ m^2$ (+33 %). Footprint 400×200 is also a pallet module ✓.

---

**P12 · Packaging with damages**
200 000 products/year, value 40 €/product, 20 products per box, box surface 0.9 m² in both options.
- (a) single-wall cardboard 1.2 €/m², damage rate 1 %
- (b) double-wall cardboard 1.8 €/m², damage rate 0.1 %

Which box do you choose?

> [!success]- Solution P12
> Boxes/year $=10\,000$
> (a) $0.9\cdot1.2\cdot10\,000=10\,800$ + damages $200\,000\cdot1\%\cdot40=80\,000$ → **90 800 €/year**
> (b) $0.9\cdot1.8\cdot10\,000=16\,200$ + damages $8\,000$ → **24 200 €/year** ✅
> The cheapest box is not the cheapest system: include damages in the integrated product–packaging study.

---

## Block W — Warehouses

**W1 · Number of bays (Poisson)**
On average 4 trucks/h arrive; unloading takes 40 min. How many bays for a 90 % service level? And for 95 %? How much wall is needed?

> [!success]- Solution W1
> $\lambda T=4\cdot\frac{40}{60}=2.667$, $P(0)=e^{-2.667}=0.0695$, $P(x)=P(x-1)\cdot\frac{\lambda T}{x}$
>
> | x | bays | P(x) | cumulative |
> |---|---|---|---|
> | 0 | 1 | 0.0695 | 0.0695 |
> | 1 | 2 | 0.1853 | 0.2548 |
> | 2 | 3 | 0.2471 | 0.5018 |
> | 3 | 4 | 0.2196 | 0.7214 |
> | 4 | 5 | 0.1464 | 0.8678 |
> | 5 | 6 | 0.0781 | **0.9459** |
> | 6 | 7 | 0.0347 | **0.9806** |
>
> LS 90 % → **6 bays** (27 m of wall); LS 95 % → **7 bays** (31.5 m).
>
> ![[w1-poisson-claude.png|560]]

---

**W2 · Access and selectivity indexes (short question)**

| Item | P | Q | R | S | T | U |
|---|---|---|---|---|---|---|
| UL moved/day | 12 | 5 | 18 | 8 | 20 | 3 |
| Average stock [UL] | 4 | 10 | 3 | 8 | 5 | 6 |

1. Compute $I_A$ and rank the items from closest to farthest from the I/O.
2. What is $I_S$ for: single deep rack, double deep, drive-in 4 UL deep? When do you choose double deep?

> [!success]- Solution W2
> **1.** $I_A$: P 3 · Q 0.5 · R 6 · S 1 · T 4 · U 0.5 → order **R, T, P, S, Q/U**.
> **2.** Single deep $I_S=1$; double deep $0.5$; drive-in 4 deep $0.25$. Double deep when each item has ≥ 2 UL and surface saturation matters (with high movements → double deep AS/RS).

---

**W3 · Complete AS/RS design (Exam 6 / Lesson 14 style)**
Single deep AS/RS with two UL types: (a) 800×1200×1000 mm, 6 000 UL; (b) 800×1200×1400 mm, 6 000 UL. Available height 28 m (gaps 0.8 + 1 m), rack thickness 0.15 m, gaps 0.1 m, modules of 3 UL (2.95 m). Throughput 280 UL in + 280 UL out per hour, simple cycles. FEM kinematics: $v_x=4$, $a_x=1.2$, $v_y=1$, $a_y=0.9$, $t_f=10$ s, I/O (0;0), A = 0.96.
1. Number of machines, floors, modules, L and H.
2. $T_{CS}$ according to FEM 9.851 and real utilization.
3. With capacity-2 stacker cranes: new throughput and % increase.

![[asrs-plan-claude.png|560]]

> [!success]- Solution W3
> **1.** $N=\lceil280\cdot110/3600\rceil=\lceil8.56\rceil=\mathbf{9}$
> $H_{F,a}=1.0+0.1+0.15=1.25$; $H_{F,b}=1.4+0.1+0.15=1.65$; $\bar H_F=0.5\cdot1.25+0.5\cdot1.65=1.45\ m$
> $N_F=\lfloor(28-1.8)/1.45\rfloor=\lfloor18.07\rfloor=\mathbf{18}$
> $C_{machine}=12\,000/9=1\,333$ → $N_{mod}=\lceil1\,333/(3\cdot2\cdot18)\rceil=\lceil12.3\rceil=\mathbf{13}$
> $L=13\cdot2.95=\mathbf{38.35\ m}$ ; $H=17\cdot1.45=\mathbf{24.65\ m}$
>
> ![[floor-height-claude.png|560]]
> **2.** $P_1=(7.67;\,16.43)$, $P_2=(25.57;\,4.93)$; $v_x/a_x=3.33$, $v_y/a_y=1.11$
>
> ![[w3-rack-claude.png|560]]
> - I/O–P1: $7.67<v_x^2/a_x=13.3$ → $t_x=2\sqrt{7.67/1.2}=5.06$; $t_y=16.43+1.11=17.54$ → **17.54 s**
> - I/O–P2: $t_x=25.57/4+3.33=9.72$, $t_y=4.93+1.11=6.04$ → **9.72 s**
> $$T_{CS}=2\cdot17.54+2\cdot9.72+4\cdot10=\mathbf{94.5\ s}$$
> $$U=\frac{280\cdot94.5}{3600\cdot0.96\cdot9}=\mathbf{0.85}\quad(0.6<U<1\ ✓)$$
> **3.** P1–P2: $t_x=17.9/4+3.33=7.81$, $t_y=11.5+1.11=12.61$ → **12.61 s**
> $T_{CS,dual}$ per (1 in + 1 out) $=17.54+12.61+9.72+3\cdot10=\mathbf{69.9\ s}$
> $Q_1=3600/94.5=38.1$, $Q_2=3600/69.9=51.5$ cycles/h·machine → **+35 %**. With 9 machines $U$ would drop to 0.63: you could reduce the number of machines (but recompute L).

---

**W4 · REAL EXAM — Exam 2 (coils)** · `exams/exam 2 DW.pdf`

> [!quote]- Original exam text
> ![[exam 2 DW.pdf#height=550]]

UL type a (coil Ø1.3 on 0.8×1.2 pallet, total height 1.35 m): 1 200 pallets; type b (2 coils Ø0.6 on 0.8×1.2 pallet, height 0.75 m): 600 pallets. 3 AS/RS, single deep, module 2.95 m, upright/beam thickness 150 mm, height 24 m, gaps 1 m (ceiling) and 0.8 m (floor).

![[w4-coils-claude.png|560]]
1. Size the warehouse (L and H). 2. Performance in combined cycles/h with $t_f=12$ s, $v_x=3$, $a_x=1.0$, $v_y=0.9$, $a_y=0.8$; utilization 90 %, availability 96 %, I/O at the origin.

> [!success]- Solution W4
> **1.** $H_{F,a}=1.35+0.1+0.15=1.60$; $H_{F,b}=0.75+0.1+0.15=1.00$; weights $1200/1800=2/3$, $1/3$ → $\bar H_F=1.40\ m$
> $N_F=\lfloor22.2/1.40\rfloor=\lfloor15.86\rfloor=\mathbf{15}$ ; $C_{machine}=1\,800/3=600$ → $N_{mod}=\lceil600/(6\cdot15)\rceil=\lceil6.67\rceil=\mathbf{7}$
> $L=7\cdot2.95=\mathbf{20.65\ m}$ ; $H=14\cdot1.40=\mathbf{19.6\ m}$
> (more precise alternative: 10 floors of 1.6 m for type a + 5 floors of 1.0 m for type b = 21 m ≤ 22.2 → still 7 modules)
> **2.** $P_1=(4.13;\,13.07)$, $P_2=(13.77;\,3.92)$; $v_x/a_x=3$, $v_y/a_y=1.125$
>
> ![[w4-rack-claude.png|560]]
> - I/O–P1: $4.13<v_x^2/a_x=9$ → $t_x=2\sqrt{4.13/1}=4.06$; $t_y=13.07/0.9+1.125=15.64$ → **15.64 s**
> - P1–P2: $t_x=9.64/3+3=6.21$; $t_y=9.15/0.9+1.125=11.29$ → **11.29 s**
> - P2–I/O: $t_x=13.77/3+3=7.59$; $t_y=3.92/0.9+1.125=5.48$ → **7.59 s**
> $$T_{CC}=15.64+11.29+7.59+4\cdot12=\mathbf{82.5\ s}$$
> Per machine $3600/82.5=43.6$ theoretical CC/h → real $43.6\cdot0.9\cdot0.96=37.7$ → **warehouse ≈ 113 combined cycles/h** (≈ 113 UL in + 113 UL out).

---

**W5 · REAL EXAM — Exam 3 (AS/RS feeding picking)** · `exams/exam 3 DW.pdf`

> [!quote]- Original exam text
> ![[exam 3 DW.pdf#height=550]]

$Z_{ih}$/$Q_{ih}$ matrices for 1 hour: 30 orders, each with 2 lines → **60 lines/h**; sum of $Q_{ih}$ = **134 pieces/h**. UL 800×1200×1500 (pallet included) with 32 boxes (1 piece/box). Capacity 6 000 pallets, height 20 m, single deep, FEM; $v_x=4$, $a_x=1$, $v_y=1.2$, $a_y=1$, $t_f=10$ s; U = 92 %, A = 98 %; I/O (0;0). Also consider inbound full UL.
Size the warehouse.

> [!success]- Solution W5
> **Flows**: 60 lines → **60 combined cycles/h** (the picked UL goes back in, the next one comes out); inbound full UL $134/32=\mathbf{4.19}$ UL/h (inbound only ≈ $T_{CS}/2$).
> **Floors**: $H_F=1.5+0.1+0.15=1.75$; $\lfloor18.2/1.75\rfloor=\mathbf{10}$
> **Machine estimate**: $(60\cdot100+4.19\cdot55)/3600=1.73$ → **2**
> **Modules**: $3\,000/(6\cdot10)=\mathbf{50}$ → $L=147.5\ m$, $H=9\cdot1.75=15.75\ m$
> **FEM**: $P_1=(29.5;\,10.5)$, $P_2=(98.3;\,3.15)$; $v_x/a_x=4$, $v_y/a_y=1.2$
> - I/O–P1: $t_x=7.38+4=11.38$, $t_y=8.75+1.2=9.95$ → 11.38 s
> - P1–P2: $t_x=17.21+4=21.21$ → 21.21 s
> - P2–I/O: $t_x=24.58+4=28.58$ → 28.58 s
> $T_{CC}=11.38+21.21+28.58+40=\mathbf{101.2\ s}$ ; $T_{CS}=2\cdot11.38+2\cdot28.58+40=\mathbf{119.9\ s}$
> **Check**: work $=60\cdot101.2+4.19\cdot60.0=6\,321\ s/h$ → $U=\dfrac{6\,321}{3600\cdot0.98\cdot2}=\mathbf{0.90}\le0.92$ ✓
> With 3 machines: L = 100.3 m but $U=0.51<0.6$ → oversized. **Solution: 2 AS/RS, 10 floors, 50 modules/aisle, L = 147.5 m, H = 15.75 m.**

---

**W6 · Multi-deep with push mover per level + lift (Lesson 15 style)**
L = 60 m, H = 20 m, 10 levels, I/O (0;0). Push mover: $v_x=1.5$, $a_x=0.8$, $t_{f,chain}=8$ s, $t_{f,shuttle}=20$ s. Lift (one IN and one OUT): $v_y=1.2$, $a_y=1.0$, $t_f=10$ s.
Throughput of the push movers, of the lifts, of the system; utilization of the push movers.

![[w6-multideep-claude.png|560]]

> [!success]- Solution W6
> **Push mover**: $P_1=12$, $P_2=40$ m; $v/a=1.875$
> $t(12)=8+1.875=9.875$; $t(40)=26.67+1.875=28.54$
> $T_{CS}=2\cdot9.875+2\cdot28.54+2\cdot8+2\cdot20=\mathbf{132.8\ s}$ → $27.1$ cycles(in+out)/h per level → **271/h** with 10 levels
> **Lift**: $P_1=\tfrac23H=13.33$, $P_2=\tfrac15H=4$; $v/a=1.2$
> $T_{CS,y}=2(11.11+1.2)+2(3.33+1.2)+4\cdot10=\mathbf{73.7\ s}$ → each lift $73.7/2=36.8\ s/UL$ → **97.7 UL/h** inbound and 97.7 outbound
> **System** $=\min(271;\,97.7)=\mathbf{97.7}$ cycles (in+out)/h → **bottleneck: lift**. $U_{push}=97.7/271=36\ \%$.

---

**W7 · REAL EXAM — Exam 8 (AVS/R, shuttle + lift)** · `exams/exam 8 AVS R.pdf`

> [!quote]- Original exam text
> ![[exam 8 AVS R.pdf#height=550]]

1 aisle, 30 levels (level height 0.6 m), 1 shuttle per level (capacity 2 boxes), independent IN and OUT lift sections of 4 boxes. Shuttle $v_x=4$, $a_x=2$, $t_f$(2 boxes) = 4 s; lift $v_y=3$, $a_y=4$, $t_f$(4 boxes) = 5 s; L = 70 m, I/O (0;0).
1. Throughput in boxes/h. 2. Utilization of shuttles and lift.

![[w7-avsr-claude.png|560]]

> [!success]- Solution W7
> *Assumption (write it at the exam)*: the shuttle moves 2 boxes per trip to the same location ($t_f$ is given for 2 boxes); one-dimensional FEM as in Lesson 15.
> **Shuttle**: $P_1=70/5=14$, $P_2=\tfrac23\cdot70=46.7$; $v/a=2$ ($v^2/a=8\ m$ < distances ✓)
> $t(14)=3.5+2=5.5$; $t(46.7)=11.67+2=13.67$
> $T_{CS}=2\cdot5.5+2\cdot13.67+4\cdot4=\mathbf{54.3\ s}$ per 2 boxes in + 2 boxes out → $4\cdot3600/54.3=\mathbf{265}$ boxes/h per shuttle → **7 951 boxes/h** with 30 shuttles
> **Lift**: $H=29\cdot0.6=17.4$; $P_1=11.6$, $P_2=3.48$; $v/a=0.75$ ($v^2/a=2.25$ ✓)
> $t(11.6)=3.87+0.75=4.62$; $t(3.48)=1.16+0.75=1.91$
> $T_{CS,y}=2\cdot4.62+2\cdot1.91+4\cdot5=\mathbf{33.1\ s}$ → each section $16.5\ s$ per 4 boxes → **871 boxes/h** IN + 871 OUT = **1 742 boxes/h**
> **1.** Throughput $=\min(7\,951;\,1\,742)=\mathbf{1\,742\ boxes/h}$ (871 in + 871 out) — bottleneck: **lift**
> **2.** $U_{lift}=100\ \%$ ; $U_{shuttle}=1\,742/7\,951=\mathbf{22\ \%}$ → lift capacity could be increased, or fewer shuttles used (e.g. shuttles serving several levels).

---

**W8 · FEM vs Bozer–White (Lesson 16 style)**
Use the warehouse of W3 (L = 38.35 m, H = 24.65 m, $t_f=10$ s) with average speeds $\bar v_x=3$, $\bar v_y=0.9$ m/s.
1. $T$, $b$, $T_{CS}$ and $T_{CC}$ with BW. 2. Compare with FEM. 3. Is the design good?

> [!success]- Solution W8
> **1.** $T_l=38.35/3=12.78\ s$; $T_h=24.65/0.9=27.39\ s$ → $T=27.39$, $b=12.78/27.39=\mathbf{0.47}$
> $T_{CS}=2\cdot27.39\,(1+0.47^2/3)+40=\mathbf{98.8\ s}$ ; $T_{CC}=27.39\,(4/3+0.47^2/2-0.47^3/30)+40=\mathbf{79.4\ s}$
> **2.** FEM: $T_{CS}=94.5$, $T_{CC}=79.9$ → close values (BW ≈ +4 % on the simple cycle).
> **3.** $b=0.47<0.8$ → **not balanced**: in time the warehouse is "tall and short" (the vertical axis is slow). Better longer aisles and fewer machines (with 7 machines L ≈ 47 m → b ≈ 0.57) or, if possible, a higher $v_y$.

---

**W9 · REAL EXAM — Example 1 (double-deep miniload, BW/FEM)** · `exams/Exam DWT example 1.pdf`

> [!quote]- Original exam text
> ![[Exam DWT example 1.pdf#height=550]]

Miniload for odette totes 400×600×320 placed end-on (short side on the front), double deep, L = 60 m, 20 modules of 2.8 m with 6 files of totes, rack depth 1.4 m, aisle 1.5 m, pedestals 0.08 m, level pitch 0.5 m, 25 levels, 6 miniloads, capacity 2 totes, $t_f$ = 6 s for loading/unloading 1 or 2 totes. $v_x=6$, $a_x=5.3$, $v_y=3$, $a_y=4$; I/O at 6 m height. Cycle: picks 2 totes at the I/O, deposits them in 2 locations, retrieves 2 totes from 2 locations, returns to the I/O.
1. Capacity. 2. Throughput per miniload and total.

![[w9-miniload-module-claude.png|560]]

> [!success]- Solution W9
> **Checks**: 6 files × 0.4 = 2.4 ≤ 2.8 m ✓; double deep 2 × 0.6 = 1.2 ≤ 1.4 m ✓; 0.32 + 0.08 = 0.40 ≤ 0.5 m ✓
> **1.** Per aisle: $20\cdot6\cdot2\,(\text{deep})\cdot2\,(\text{sides})\cdot25=12\,000$ → × 6 = **72 000 totes**
> **2.** $H=24\cdot0.5=12\ m$, I/O (0;6). Points (as in the notes, with $y_{I/O}$): $P_1=(12;\ 8+2)=(12;10)$, $P_2=(40;\ 2.4+2)=(40;4.4)$
>
> ![[w9-miniload-rack-claude.png|560]]
> $v_x/a_x=1.13$ ($v_x^2/a_x=6.8\ m$), $v_y/a_y=0.75$ ($v_y^2/a_y=2.25\ m$)
> - I/O–P1: $t_x=2+1.13=3.13$; $t_y=4/3+0.75=2.08$ → **3.13 s**
> - P1–P2: $t_x=28/6+1.13=5.80$; $t_y=5.6/3+0.75=2.62$ → **5.80 s**
> - P2–I/O: $t_x=40/6+1.13=7.80$; $t_y$: $1.6<2.25$ → $2\sqrt{1.6/4}=1.26$ → **7.80 s**
> Forks: load at I/O, unload P1, unload P2, load P1, load P2, unload I/O = $6\cdot6=36\ s$
> $$T=2\,(3.13+5.80+7.80)+36=\mathbf{69.5\ s}\ \text{per 4 totes (2 in + 2 out)}$$
> Per miniload $4\cdot3600/69.5=\mathbf{207}$ totes/h → total $6\cdot207\approx\mathbf{1\,244}$ totes/h.

---

**W10 · Loading and unloading bays**
Inbound: 3 trucks/h, unloading 45 min. Outbound: 6 trucks/h, loading 30 min. Service level 90 % (then 95 %). How many bays in total and how much wall?

> [!success]- Solution W10
> **Inbound** $\lambda T=2.25$: cumulative 0.105, 0.343, 0.609, 0.809, **0.922** (x = 4) → **5 bays** (95 %: 0.973 at x = 5 → 6 bays)
> **Outbound** $\lambda T=3$: $P(0)=e^{-3}=0.0498$; cumulative 0.050, 0.199, 0.423, 0.647, 0.815, **0.916** (x = 5) → **6 bays** (95 %: 0.967 at x = 6 → 7 bays)
> **Total** LS 90 %: 11 bays → $11\cdot4.5=\mathbf{49.5\ m}$; LS 95 %: 13 bays → 58.5 m

---

**W11 · AS/RS for picking (combined cycles)**
One UL type 800×1200×1100 mm (pallet included), capacity 9 000 UL, single deep, height 25 m. The warehouse feeds picking: **200 order lines/h** (1 combined cycle each). FEM kinematics ($v_x=4$, $a_x=1.2$, $v_y=1$, $a_y=0.9$), $t_f=10$ s, A = 0.96, I/O (0;0), modules of 3 UL (2.95 m).
Size the warehouse and check the utilization.

> [!success]- Solution W11
> $N=\lceil200\cdot100/3600\rceil=\lceil5.56\rceil=\mathbf{6}$ ; $H_F=1.1+0.1+0.15=1.35$ ; $N_F=\lfloor23.2/1.35\rfloor=\mathbf{17}$
> $C_{machine}=1\,500$ → $N_{mod}=\lceil1\,500/(6\cdot17)\rceil=\mathbf{15}$ → $L=\mathbf{44.25\ m}$, $H=16\cdot1.35=\mathbf{21.6\ m}$
> $P_1=(8.85;14.4)$, $P_2=(29.5;4.32)$
> - I/O–P1: $t_x=2\sqrt{8.85/1.2}=5.43$ (8.85 < 13.3), $t_y=14.4+1.11=15.51$ → 15.51 s
> - P1–P2: $t_x=20.65/4+3.33=8.50$, $t_y=10.08+1.11=11.19$ → 11.19 s
> - P2–I/O: $t_x=29.5/4+3.33=10.71$, $t_y=4.32+1.11=5.43$ → 10.71 s
> $T_{CC}=15.51+11.19+10.71+40=\mathbf{77.4\ s}$ → $U=\frac{200\cdot77.4}{3600\cdot0.96\cdot6}=\mathbf{0.75}$ ✓

![[w11-rack-claude.png|520]]

---

**W12 · Dual AS/RS in combined cycle (4 points)**
Same warehouse as W11, but with capacity-2 machines doing combined cycles: I/O → P1 → P2 (store 2) → P3 → P4 (retrieve 2) → I/O, with $P_1(\tfrac15L;\tfrac23H)$, $P_2(0.44L;0.46H)$, $P_3(L;0.87H)$, $P_4(\tfrac23L;\tfrac15H)$. Fork operations: 6 per cycle.
Cycle time per (1 in + 1 out) and throughput increase vs W11.

![[w12-dual-cc-claude.png|520]]

> [!success]- Solution W12
> Points: P1 (8.85; 14.4), P2 (19.47; 9.94), P3 (44.25; 18.79), P4 (29.5; 4.32)
> - I/O–P1 15.51 s · P1–P2: $t_x=2\sqrt{10.62/1.2}=5.95$, $t_y=4.46+1.11=5.57$ → 5.95 s
> - P2–P3: $t_x=24.78/4+3.33=9.53$, $t_y=8.86+1.11=9.97$ → 9.97 s
> - P3–P4: $t_x=14.75/4+3.33=7.02$, $t_y=14.47+1.11=15.58$ → 15.58 s
> - P4–I/O 10.71 s
> $T=15.51+5.95+9.97+15.58+10.71+6\cdot10=\mathbf{117.7\ s}$ per 2 in + 2 out → **58.9 s** per (1 in + 1 out)
> vs single CC 77.4 s → $77.4/58.9=\mathbf{+31\ \%}$ throughput (with 6 machines U would drop to ≈ 0.57 → 5 machines could be enough, recomputing L).

---

**W13 · Bozer–White: redesign a badly shaped miniload**
Miniload aisle L = 50 m, H = 10 m, $\bar v_x=4$, $\bar v_y=2$ m/s, $t_f=5$ s.
1. $T$, $b$, $T_{CS}$, $T_{CC}$.
2. Keeping the same rack face (L·H = 500 m²), find L and H giving b = 1 and the new cycle times.

![[w13-bw-shape-claude.png|520]]

> [!success]- Solution W13
> **1.** $T_l=12.5$, $T_h=5$ → $T=12.5$, $b=\mathbf{0.4}$ (bad) ; $T_{CS}=2\cdot12.5(1+0.4^2/3)+20=\mathbf{46.3\ s}$ ; $T_{CC}=12.5(4/3+0.08-0.002)+20=\mathbf{37.6\ s}$
> **2.** $b=1$ ⇔ $L/4=H/2$ ⇔ $L=2H$; $2H^2=500$ → $H=\mathbf{15.8\ m}$, $L=\mathbf{31.6\ m}$, $T=7.9\ s$
> $T_{CS}=2\cdot7.9\cdot\frac43+20=\mathbf{41.1\ s}$ (−11 %) ; $T_{CC}=7.9\,(4/3+1/2-1/30)+20=\mathbf{34.2\ s}$ (−9 %)

---

**W14 · How many lifts? (multi-deep, continues W6)**
In W6 the system is limited to 97.7 cycles (in+out)/h by the lifts. The target is **200 cycles/h**.
1. How many IN/OUT lift pairs are needed with the current lift ($v_y=1.2$, $a_y=1$)?
2. Alternative: a faster lift ($v_y=2$, $a_y=1.5$, same $t_f$). How many pairs then?

> [!success]- Solution W14
> **1.** $200/97.7=2.05$ → **3 lift pairs** (2 pairs = 195.4 < 200)
> **2.** $t(13.33)=6.67+1.33=8.0$; $t(4)=2+1.33=3.33$ → $T_{CS,y}=2\cdot8.0+2\cdot3.33+40=62.7\ s$ → each lift $3600/31.3=\mathbf{114.9}$ UL/h → $200/114.9=1.74$ → **2 faster pairs**. Push movers (271/h) are still sufficient.

---

**W15 · REAL EXAM — Exam 6 (22 December 2025)** · `exams/exam 6 22 december 2025.pdf`

> [!quote]- Original exam text
> ![[exam 6 22 december 2025.pdf#height=550]]

UL a 800×1200×900 (10 000), UL b 800×1200×1300 (10 000); HW 30 m (gaps 0.8 + 1 m); single deep; capacity 1 UL; 350 UL in + 350 UL out per hour, simple cycles; $v_x=4$, $a_x=1.2$, $v_y=1$, $a_y=0.9$, $t_f=10$ s; rack 150 mm, gaps 100 mm; I/O (0;0); A = 0.96.
1. Machines, floors, length, L and H, real utilization. 2. Capacity-2 machines: throughput and % increase.

> [!success]- Solution W15
> **1.** $N=\lceil350\cdot110/3600\rceil=\lceil10.7\rceil=\mathbf{11}$ ; $\bar H_F=0.5\cdot1.15+0.5\cdot1.55=1.35$ ; $N_F=\lfloor28.2/1.35\rfloor=\mathbf{20}$
> $C_{machine}=20\,000/11=1\,819$ → $N_{mod}=\lceil1\,819/(6\cdot20)\rceil=\mathbf{16}$ → $L=\mathbf{47.2\ m}$, $H=19\cdot1.35=\mathbf{25.65\ m}$
> $P_1=(9.44;17.1)$, $P_2=(31.47;5.13)$ → $T(I/O\!-\!P_1)=18.2$ s, $T(I/O\!-\!P_2)=11.2$ s
> $T_{CS}=2\cdot18.2+2\cdot11.2+40=\mathbf{98.8\ s}$ → $U=\frac{350\cdot98.8}{3600\cdot0.96\cdot11}=\mathbf{0.91}$
> **2.** $T(P_1\!-\!P_2)=13.1$ s → $T_{CS,dual}=18.2+13.1+11.2+30=\mathbf{72.5\ s}$ ; $Q_1=36.4$, $Q_2=49.7$ cycles/h·machine → **+36 %** (Lesson 14: 99 s → 72.7 s).

---

**W16 · Availability and number of machines**
In one month a stacker crane worked 160 h and was down 8 h.
1. Availability A.
2. With $T_{CS}=105$ s and Q = 150 (in+out)/h, how many machines are needed if U must not exceed 0.9? What is the real U?

> [!success]- Solution W16
> **1.** $A=\frac{160}{160+8}=\mathbf{0.952}$
> **2.** $N\ge\frac{150\cdot105}{3600\cdot0.952\cdot0.9}=5.1$ → **6 machines** → $U=\frac{15\,750}{3600\cdot0.952\cdot6}=\mathbf{0.77}$ (between 0.6 and 1 ✓)

---

# PART C — EXAM SIMULATIONS

**Exam simulations (1 exercise + 1 theory question, 1 h 30)**

| Simulation | Exercise | Theory (answers in [[DWT - Theory Summary-claude]]) |
|---|---|---|
| **S1** | W3 (all points) | Quantitative cost–benefit of single-use vs reusable |
| **S2** | P6 without looking at the table | Integrated product–packaging system and secondary packaging optimization |
| **S3** | T6 + daily cost | Consolidation method vs savings vs extra mile |
| **S4** | W7 | FEM 9.851 vs Bozer–White: when to use each, shape factor b |
| **S5** | T2 + T3 together | Types of cardboard boxes and standardization |
| **S6** | W5 | $I_S$ and $I_A$ indexes and single/double deep choice |
| **S7** | W15 | Simple vs combined cycle, dual AS/RS |
| **S8** | T14 | Primary vs secondary transport, internal vs external costs |
| **S9** | P9 + P12 | Vehicle saturation (weight vs volume) and integrated packaging study |
| **S10** | W11 + W12 | Selectivity index and AS/RS design steps |

**Typical mistakes checklist**
- minutes not converted to hours in $N_{max}$ and in driver costs
- deliveries/floors rounded up (they must be rounded down)
- FEM $P_1$/$P_2$ with $\tfrac13$ instead of $\tfrac15$
- forgetting $\max(t_x;t_y)$ or the $v/a$ term
- forgetting availability $A$ or the number of machines in $U$
- forgetting $(I_c+2)$ or the empty return for reusable packaging
- in savings, merging customers that are not route ends, or not checking the shift hours
