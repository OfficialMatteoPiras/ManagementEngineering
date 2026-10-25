## 1. What the assignment asks, in concrete terms

The assignment has three levels, from the most concrete to the most general:

1. **System example**: design a 45×30×20 m warehouse holding more than 4000 pallets, with 40 pallets/h inbound (24h a day) and 60 pallets/h outbound (16h a day), and 6 pallets per SKU. You must decide the **racks**, the **number and location of the lifts**, and the **number of shuttles**.
2. **Parametric model**: understand how the **best shape** of the warehouse and the **best lift locations** change with the position of the INBOUND and OUTBOUND bays.
3. **Field of application**: describe in general when this technology fits with respect to (a) ABC handling classes, (b) shuttle management between floors, (c) resilience, (d) energy consumption, (e) throughput, (f) future expansions.

The evaluation criteria reward **quantitative content**: you need numbers, not only descriptions. The paper by Tappia et al. (2016) is your theoretical reference: it provides the model (semi-open queuing networks) and the result “depth/width ratio ≈ 1.25”.

## 2. The available data, translated

### Geometry

| Data | Value | What it means for the model |
| --- | --- | --- |
| Pallet (system example slide) | 850 × 1250 × 1700 mm, 1000 kg | Euro pallet 800×1200 plus clearance: gives the pitch of one position |
| Shuttle | 1045 × 890 × 197 mm, 260 kg, capacity 1000 kg | Drives under the pallet; the 197 mm height affects the vertical pitch |
| Warehouse | 45 × 30 m, height 20 m | Limits lanes, levels and number of tiers |
| SKU | 6 pallets each | Natural lane depth = 6 positions |

### Kinematics

|  | Shuttle | Lift |
| --- | --- | --- |
| Maximum speed | 1.4 m/s | 1 m/s |
| Acceleration / deceleration | 0.5 m/s² | 0.7 m/s² |
| Direction change | 4 s | n/a |
| Load/unload in rack | 25 s | n/a |
| Load/unload with shuttle | n/a | 25 s |
| Load/unload with chain conveyor | n/a | 7 s |
| Positioning | n/a | 1 s |
| Battery / power | 50 V/Ah, 8 h runtime | 16 kW installed, capacity 1800 kg |

The lift capacity (1800 kg) exceeds pallet + shuttle (1000 + 260 kg): a shuttle can therefore ride the lift to change floor.

### Flows

- Inbound 40 pallets/h × 24 h = **960 pallets/day**.
- Outbound 60 pallets/h × 16 h = **960 pallets/day** (the warehouse is balanced).
- **Peak hour**: 40 + 60 = **100 transactions/h** (during the 16 h); at night only 40/h.

### Assumptions I had to make (to confirm with the professor)

| # | Assumption | Why |
| --- | --- | --- |
| A1 | Position pitch: u\_d = 1.25 m (along the lane), u\_w = 0.85 m (across) | Pallet 800×1200 plus 50 mm clearance |
| A2 | Vertical pitch u\_h = 1.85 m (1700 + 150 mm) | I read the 150 mm of the “Geometric parameters” slide as rail/beam allowance |
| A3 | “Generic” shuttle in the paper’s sense (six-way, no transfer car) | It is an omnidirectional shuttle |
| A4 | Single-command cycles; the shuttle starts from and returns to the lift point | Conservative (as in the paper) |
| A5 | Honeycombing factor f = 0.2 | Conservative end of the paper’s range (tested 0–0.2) |
| A6 | Tier 1 at ground level, connected directly to the IN/OUT conveyors, no lift | As in the paper (the I/O point is at tier 1) |
| A7 | 1000 kg pallets (upper bound) for energy | Average weight not given |

## 3. How it is modeled (simple version)

Each tier has a **cross-aisle** with **storage lanes** N\_C positions deep on both sides. Shuttles travel along the cross-aisle to the right lane, enter it, store or retrieve the pallet and return to the **lift**, which moves pallets between ground and tier. The paper models each tier as a semi-open queuing network (open for requests, closed for shuttles).

**Travel time** with acceleration (trapezoidal profile):

- t(L) = L/v + v/a if L ≥ v²/a
- t(L) = 2·√(L/a) otherwise

(threshold: 3.92 m for the shuttle, 1.43 m for the lift)

**Shuttle cycle** (single command, storage or retrieval):

T\_sh = 2·25 + 2·4 + 2·t(ā) + 2·t(d̄)

- ā = mean cross-aisle distance to the nearest lift (+1 m)
- d̄ = (N\_C − 1)·u\_d/2·(1 + f) + 1 m, mean distance inside the lane (with honeycombing)

**Lift cycle**, single command at tier i, with h\_i = (i − 1)·u\_h:

T\_lift,i = 7 + 25 + 2·t(h\_i) + 2·1 = 34 + 2·t(h\_i)

**Utilization**: ρ = λ·T / (3600·n). Size for ρ ≲ 70–75% (the paper validates 70–90%) and check **N+1 redundancy**.

## 4. Solution: sizing the 45×30×20 m case

### 4.1 Racks

- **Levels**: 20 / 1.85 = 10.8 → **10 tiers** (18.5 m, leaving 1.5 m for roof, sprinklers and lift head). 11 tiers would need 20.35 m: it does not fit.
- **Lane depth**: **N\_C = 6**. One lane = one SKU = 6 pallets: no LIFO reshuffling between different SKUs.
- **Lanes per side**: the floor plan allows a cross-aisle 44 × 0.85 = **37.4 m** long (along the 45 m side) and storage lanes along the 30 m side: 7.5 + 1.5 + 7.5 = 16.5 m.
- **Capacity**: 2 sides × 6 × 44 lanes × 10 tiers = 5280 gross positions. Each lift replaces about 3 lanes on one side: 3 lifts × 3 × 6 × 10 = 540. **Net: 4740 positions = 790 lanes**, i.e. 790 SKUs of 6 pallets. At 84% average fill this gives about 4000: the “> 4000” requirement is met with margin for honeycombing.
- **Footprint**: 37.4 × 16.5 m ≈ 617 m², 46% of the 1350 m². A free strip of 13.5 × 45 m remains for IN/OUT bays, conveyors, battery charging, maintenance and expansion.

Discarded alternative: two modules with lanes along the 45 m side (17 m cross-aisle). The shuttle cycle improves by about 7% (83.4 vs 89.5 s with one central lift), but it doubles cross-aisles, shuttles and lifts per tier and leaves no room to expand.

### 4.2 Shuttle cycle versus number of lifts ($N_C$ = 6, $N_L$ = 44, L = 37.4 m)

| Lifts | Mean cross-aisle distance ā | Cycle T\_sh | Capacity per shuttle |
| --- | --- | --- | --- |
| 1, at the aisle end | 19.7 m | 104.1 s | 34.6 tx/h |
| 1, at the centre | 10.4 m | 90.7 s | 39.7 tx/h |
| 2, equally spaced | 5.7 m | 84.0 s | 42.9 tx/h |
| 3, equally spaced | 4.1 m | 81.7 s | 44.1 tx/h |

More lifts distributed along the aisle shorten the shuttle path, with diminishing returns.

### 4.3 Number and location of lifts

Peak hour: 100 tx/h; tier 1 does not use the lift, so about 90 tx/h reach the lifts (uniform distribution across tiers). Mean single-command lift cycle 55.4 s, i.e. about 65 tx/h per lift.

| Scenario (100 tx/h at peak)                    | 1 lift | 2 lifts | 3 lifts |
| ---------------------------------------------- | ------ | ------- | ------- |
| Uniform, single command                        | 138%   | 69%     | **46%** |
| Uniform, with dual commands                    | 123%   | 61%     | 41%     |
| ABC (see §6)                                   | 74%    | 37%     | 25%     |
| Uniform with chain conveyor at each tier (7 s) | 93%    | 47%     | 31%     |

**Choice: 3 lifts.** With 3 lifts normal utilization is 46%, and if one lift fails the remaining 2 run at 69%: still below 100%. At 125 tx/h (+25% margin) the 3 lifts run at 58%, while 2 lifts would be at 87%. With guaranteed ABC 2 lifts would be enough (37%, 74% with one failure), but 3 also cover an imperfect ABC classification and future expansion.

**Location**: equally spaced along the aisle at L/6, L/2, 5L/6, i.e. at **6.2 m, 18.7 m and 31.2 m** from the start of the aisle. The lifts sit at the aisle edge, in the lane row of one side, connected at ground level to the IN/OUT conveyors in the free strip.

### 4.4 Number of shuttles

The total workload is only 100 × 81.7 / 3600 = **2.3 shuttle-equivalents**. What sizes the fleet is not the load but the **coverage of the 10 tiers**.

- Uniform distribution: 10 tx/h per tier, so a single shuttle per tier works at **23%**.
- With ABC (§6): tiers 1 and 2 take 40 tx/h each, so a single shuttle would be at 91%. You need **2 shuttles on tiers 1 and 2**.
- Tiers 3–5 (class B, 5 tx/h): 1 shuttle each.
- Tiers 6–10 (class C, 1 tx/h each): **2 roaming shuttles** shared across tiers, changing floor via the lift.
- **2 spares** for failures and battery rotation (8 h runtime vs 24 h operation; with moving utilization of 12–45%, opportunistic charging is enough).

**Fleet: 4 + 3 + 2 + 2 = 11 shuttles** (12 if one shuttle is dedicated to each tier without ABC).

Why not a smaller, fully shared fleet: every floor change occupies a lift for about 54–69 s (25 s entry, travel, 25 s exit) and steals capacity from the bottleneck.

### 4.5 Summary

| Item             | Choice                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| Tiers            | 10 (u\_h = 1.85 $m, 1$8.5 m height)                                             |
| Lanes            | N\_C = 6 deep, N\_L = 44 per side, one cross-aisle per tier along the 45 m side |
| Positions        | 4740 net (790 SKUs), about 4000 at 84% fill                                     |
| Lifts            | 3, at 6.2 / 18.7 / 31.2 m along the aisle                                       |
| Shuttles         | 11 (4 on tiers 1–2, 3 on tiers 3–5, 2 roaming, 2 spare)                         |
| Shuttle cycle    | about 82 s, about 44 tx/h per shuttle                                           |
| Peak utilization | Lifts 46% (25% with ABC), shuttles 23% uniform                                  |

## 5. Parametric model (first expected result)

### 5.1 Best shape

With mean cross-aisle distance ā = κ·L (L = N\_L·u\_w) and capacity per tier fixed (N\_C·N\_L constant), the shuttle cycle is minimal when

**D/W\* = (N\_C·u\_d)/(N\_L·u\_w) = 2κ / (1 + f)**

The coefficient κ depends only on the lift positions: 1/2 with one lift at the aisle end, 1/4 with one lift at the centre, **1/(4n)** with n equally spaced lifts.

| Lift configuration | κ | Theoretical D/W\* (f = 0.2) | Minimum found numerically |
| --- | --- | --- | --- |
| 1 at the aisle end | 1/2 | 0.83 | about 0.9 |
| 1 at the centre | 1/4 | 0.42 | about 0.4 |
| 2 equally spaced | 1/8 | 0.21 | about 0.2 |
| 3 equally spaced | 1/12 | 0.14 | 0.1–0.2 |

**Sweep at constant capacity (480 positions per tier), shuttle cycle in seconds:**

| N\_C | N\_L | D/W | 1 lift at end | 1 lift at centre | 2 lifts | 3 lifts |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 80 | 0.06 | 122.5 | 98.2 | 86.1 | 82.0 |
| 6 | 40 | 0.22 | 101.7 | 89.5 | **83.4** | 81.3 |
| 12 | 20 | 0.88 | **95.9** | 89.8 | 86.6 | 85.5 |
| 16 | 15 | 1.57 | 97.2 | 92.5 | 90.1 | 89.0 |
| 24 | 10 | 3.53 | 102.6 | 99.5 | 97.6 | 97.0 |

Reading: the paper finds D/W ≈ 1.25 because it also includes queuing in the aisle; without queues the order of magnitude is the same (about 0.9 with one lift at the aisle end). The curve is flat near the optimum (a few percent). **More distributed lifts → best shape becomes “wider and shallower”**: with N\_C = 6 imposed by the SKU, D/W = 0.22 is already optimal for 2–3 lifts.

### 5.2 Position of the INBOUND and OUTBOUND bays and of the lifts

| Case | Lift position | Notes |
| --- | --- | --- |
| IN and OUT on the same side | Equally spaced, all bidirectional | Short ground conveyors; fits similar flows |
| IN and OUT on opposite sides | Lift near IN dedicated to inbound, lift near OUT dedicated to outbound, central lift shared | Fewer ground crossings; assign lifts in proportion to the 40:60 flows |
| Only one lift possible | At the centre of the aisle (κ = 1/4), not at the end | Halves the mean shuttle path |

In the shuttle-side model the bay position does not change D/W\*: it only changes where the lifts go and the length of the ground conveyors. The paper does not model the conveyors, so add a bay-to-lift distance term if you want to quantify this effect.

## 6. Field of application (second expected result)

**(a) A, B, C classes.** Vertical zoning with A in tiers 1–2 (20% of positions, 80% of transactions), B in tiers 3–5 (15%), C in tiers 6–10 (5%):

- transactions using the lift fall from 90 to 60 tx/h;
- mean lifting height falls from 8.3 to 2.2 m;
- lift utilization falls from 46% to 25%;
- trade-off: tiers 1–2 are loaded at 91% per shuttle, so a second shuttle is needed (§4.4).

The technology fits many SKUs with medium-low rotation and few pallets per SKU; it is less suited to very few, very fast SKUs (single access point per lane, LIFO).

**(b) Shuttles between floors.** Hybrid strategy: fixed shuttles where load is high, roaming shuttles where it is low. Each floor change costs about 54–69 s of lift time: it only pays off on low-load tiers (class C).

**(c) Resilience.** Three lifts give N+1 (69% with one failure). Two spare shuttles cover failures. Each tier is independent: a stopped tier removes about 10% of capacity. Weak points: a tier’s cross-aisle (if blocked, the tier stops) and the lifts in case of multiple failures.

**(d) Energy.** The kinetic energy per shuttle start is small (1260 kg × 1.4² / 2 ≈ 1.2 kJ). Consumption is dominated by lifting pallets: with 1920 movements/day at 1000 kg, about **43.6 kWh/day** with uniform distribution versus **11.6 kWh/day** with ABC (−73%). These are minimum values (potential energy only, no counterweight or efficiencies). The lift’s 16 kW installed power is used only in transients.

**(e) Throughput.** Lift capacity is about 195 tx/h (3 × 65) against a 100 tx/h peak: a margin of about 2×. Each shuttle does about 44 tx/h. The bottleneck is the lift (uniform) or the tier 1–2 shuttles (ABC). Throughput scales by adding shuttles, which are cheap, up to the lift limit; chain conveyors at each tier (7 s vs 25 s) raise lift capacity by about 50%.

**(f) Expansions.** Capacity can be raised by adding shuttles and lifts without building. In plan a free strip of 13.5 × 45 m remains: a **half module** (lanes on one side, 7.5 + 1.5 = 9 m) adds 44 × 6 × 10 = 2640 positions (+56%). Height (10 tiers) is already exhausted.

## 7. Limits and next steps

- My calculation is **deterministic** (single command, no queues). With utilization below 50% the waiting time is small, but the paper itself reports errors up to 10% for a single tier and about 27% for multitier with a discrete lift: use the results for **concept design** and state them as such.
- **To clarify with the professor**: meaning of the 150 mm, pallet orientation in the lane, whether the lift’s 25 s includes the shuttle entering, meaning of “50 V/Ah”, ABC percentages.
- **Next step**: an Excel sheet or Python script with these parameters (N\_C, N\_L, N\_T, number of lifts, f, ABC) to run the sweeps in the presentation, and a discrete-event simulation to validate the numbers. I can prepare either.
