---
tags: [DWT, formula-sheet, exam]
source: "[[Lessons - DWT]]"
---
**Formula sheet — Digital Warehousing & Transportation**
All formulas from the lessons (Lesson 1–16), grouped by topic. Anything I added that is not in the notes is marked with ⚠️.

---

## 1. Primary transport (B2B) — own fleet costs

**Truck cost per km** $[€/km]$ = sum of all items, each expressed in €/km:

| Item | Formula | Typical values (lesson) |
|---|---|---|
| Driver | $c_{driver} = \dfrac{c_{hourly}}{\bar v}$ | $25\ €/h \,/\, 50\ km/h = 0.5$ |
| Fuel | $c_{fuel} = \dfrac{€/l}{km/l}$ | $1.6\,/\,3 = 0.54$ |
| Truck (investment) | $c_{truck} = \dfrac{I}{n_{years}\cdot km_{year}}$ | $160\,000/(5\cdot 250\,000)=0.13$ |
| Taxes + insurance | $c_{tax} = \dfrac{€/year}{km_{year}}$ | $4\,000/250\,000 = 0.02$ |
| Maintenance | $c_{mnt} = \dfrac{(4\div7\%)\cdot I}{km_{year}}$ | $5\%\cdot160\,000/250\,000 = 0.032$ |
| Highway | $c_{hw}\cdot\%_{highway}$ | $0.2\cdot 0.5 = 0.1$ |
| **Total** | $\sum$ | **≈ 1.4 €/km** |

**Cost of a trip**
$$C_{trip} = c_{km}\cdot d + \underbrace{(t_{loading}+t_{unloading})\cdot c_{driver,h}}_{\text{e.g. } 1.5h\cdot 25 = 37.5\ €}$$
- one way (the truck then does another job): $d$ = one way distance
- round trip with empty return: $d = 2\cdot$ one way
- **effective €/km** $= C_{trip}/d$ → grows when the distance decreases (loading/unloading weighs more)

**Temperature-controlled transport**: fresh ($2\div4°C$) **+10÷15 %**; frozen ($-25°C$) **+40÷50 %**

**Vehicle saturation** (articulated truck): weight **28 t**, volume **≈ 80 m³**
- goods density $< 400\ kg/m^3$ → **volume** saturates first
- density $\geq 400\ kg/m^3$ → **weight** saturates first

**Outsourcing (rates per trip)**: round trip ≈ **+60 %** (articulated truck) / **+54 %** (truck) vs one way.

**Truck / container loading**: articulated truck = **33 ISO1 pallets per layer** (15 rows × 2 + 3) → with 2 layers **66 UL/trip**.

---

## 2. Secondary transport (B2C, van deliveries)

**Maximum number of deliveries per vehicle**
$$N_{max} = \left\lfloor \frac{T - T_{A/R}}{t_{stop} + \dfrac{\bar d}{\bar v}} \right\rfloor \qquad T_{A/R} = \frac{2\cdot d_{WH\to area}}{v_{highway}}$$
($T_{A/R}$ = round-trip time WH ⇄ delivery area, notation of the lessons)
- $T$ = shift (8 h), $t_{stop}$ = time at the customer **in hours** (5÷15 min), $\bar d$ = average distance between customers, $\bar v$ = city speed
- **round down** (you cannot make 15.8 deliveries)

**Average distance between customers and total tour** (area $S$ [km²], $N$ customers)
$$\bar d = 0.9\,\frac{\sqrt S}{\sqrt N} \qquad D_T = 0.9\,\sqrt S\cdot\sqrt N$$

**Number of vehicles**: $N_{trucks} = \left\lceil \dfrac{N_{T,deliveries}}{N_{max}} \right\rceil$

**Daily km of a van** making $n$ deliveries
$$d_{van} = 2\cdot d_{WH\to area} + (n-1)\,\bar d$$
(if deliveries do not split evenly, some vans do $n$ and others $n-1$: compute them separately)

**Yearly costs**
$$C_{driver} = N_{van}\cdot T_{h/day}\cdot D_{days/year}\cdot c_{€/h} \qquad C_{fuel} = D_{T,year}\cdot\frac{l}{100\ km}\cdot\frac{1}{100}\cdot €/l$$
$$C_{highway} = D_{T,year}\cdot\%_{highway}\cdot c_{€/km}$$

**Cross docking (transit point)**: no WH→area trip for each van anymore
$$N_{max}^{XD} = \frac{T - 0}{t_{stop} + \bar d/\bar v}$$
- primary transport: 1 vehicle doing WH → XD → WH (XD = cross-dock) (check daily goods **volume and weight** vs vehicle capacity)
- comparison: $\text{Saving} = \Delta C_{driver} + \Delta C_{van} + \Delta C_{fuel} + \Delta C_{hw} - C_{XD\ (rent + handling)}$
- warehouse rent today ≈ **6÷8 €/(m²·month)**

| Item | Direct delivery | Cross docking |
|---|:-:|:-:|
| Delivery vans + drivers | ⬆ | ⬇ |
| Primary transport | 0 | ⬆ |
| Cross-dock cost + handling | 0 | ⬆ |

**Outsourcing per pallet (delivery spectrum)**
$$C_{provider} = \sum_{k} n_{deliveries,k}\cdot n_{pallets,k}\cdot p(n_{pallets,k})\quad[€/day]$$
with $p(\cdot)$ = €/pallet rate of the band (1, 2, 3, 4–5, 6–10, >10 pallets). You need the **spectrum**: how many deliveries of 1, 2, 3… pallets per day.

---

## 3. Routing — Savings (Clarke & Wright) and Extra Mile

**Rectilinear (Manhattan) distance**: $d(i,j) = |x_i-x_j| + |y_i-y_j|$

**Savings**
$$D_0 = \sum_i 2\,d(W,i) \qquad S_{ij} = d(W,i) + d(W,j) - d(i,j)$$
1. distance table W–customers and customer–customer
2. compute all $S_{ij}$, sort them in decreasing order
3. merge the pair with max $S$ if: $S>0$, both customers are **ends** of their routes, constraints hold ($N_{max}$, shift hours, capacity)
4. $D_{k} = D_{k-1} - S_{ij}$ ; repeat
- **route time** $= \dfrac{km}{\bar v} + n_{stop}\cdot t_{stop} \le T$ → determines **how many vehicles** are needed
- **daily cost** $= km\cdot c_{km} + n_{stop}\cdot t_{stop}\cdot c_{driver}$ (as in the exam: driver paid separately during stops)

**General objective function**: $F_0 = \beta\,d + (1-\beta)\,t$, $0\le\beta\le1$ ($\beta=1$ distance only, $\beta=0$ time only, typical $\beta = 0.2$)

**Extra mile**: start from the farthest customer $D_i = 2d(W,i)$, then add $j$ with
$$E = d(W,i)+d(i,j)+d(W,j) - 2d(W,i)\quad \to\ \min,\ E\le E_{target}$$

---

## 4. Packaging

**Secondary packaging modules** (sub-multiples of the 1200×800 pallet, no overhang):
800×600 · 600×400 · 400×300 · 300×200 · 200×150 · 150×100 (and 266×400, 266×300, 266×196, 133×150)

**Boxes per layer**: try both orientations
$$n_{layer} = \max\left\{\left\lfloor\tfrac{1200}{l}\right\rfloor\left\lfloor\tfrac{800}{b}\right\rfloor;\ \left\lfloor\tfrac{800}{l}\right\rfloor\left\lfloor\tfrac{1200}{b}\right\rfloor\right\}\qquad n_{layers} = \left\lfloor\frac{H_{max\,UL} - h_{pallet}}{h_{box}}\right\rfloor$$
**Penalty for missing saturation** = unused area / pallet area (e.g. $\frac{0.8\cdot0.2}{0.96}=16.6\%$ higher cost).

**Cardboard surface (blank) by box type** ($L>B$, $B$ = short side, $H$ = height)

![[p2-american-blank-claude.png|560]]

| Type | Surface $S$ | vs American |
|---|---|---|
| (a) **American** 0201 (flaps meet) | $(2L+2B)(H+B)$ | — |
| (b) outer flaps half overlapping | $(2L+2B)(H+1.5B)$ | ≈ +16÷20 % |
| (c) flaps fully overlapping | $(2L+2B)(H+2B)$ | ≈ +33÷40 % |
| (d) **Telescopic** (tray + lid) | $2\,(L+2H)(B+2H)$ | ≈ +150÷330 % |

$$C_{box} \approx \bar c\cdot S \qquad \bar c \approx 1.2\ €/m^2\ (\text{typical corrugated cardboard})$$
- **$B$ enters squared** ($S = 2LH+2BH+2LB+2B^2$) → use the **smallest** dimension as $B$
- **optimal American shape**: $L = H$, $B = L/2$
- **price check**: $C_{expected} = S\cdot\bar c$ vs supplier price → if price > expected, price not correct (yearly overprice $= (c - C_{expected})\cdot Q$)

**Integrated product–packaging study**: for each alternative
$$n_{box} = \frac{Q_{products}}{prod/box} \quad C_{pack} = n_{box}\, C_{box} \quad n_{UL} = \frac{n_{box}}{box/UL} \quad n_{trips} = \frac{n_{UL}}{66} \quad C_{tr} = n_{trips}\, C_{trip}$$
$$C_{TOT} = C_{pack} + C_{tr}\ (+\ \text{damages})$$

**Standardization — cluster analysis** (same cardboard/grammage)
$$d_{ab} = \sqrt{(L_a-L_b)^2+(B_a-B_b)^2+(H_a-H_b)^2}$$
merge the closest pairs; ⚠️ the standard box of the cluster must contain both → take the **maximum of each dimension**, then check cost (more cardboard) vs benefits (higher volumes → lower price, less stock, fewer codes).

**Single-use vs reusable**

$N_{trip}$ = boxes per trip, $Q$ = boxes/year, $I_c$ = collapsibility index (empty folded boxes fitting in the volume of a full one; not collapsible $I_c = 1$)

| | Single-use | Reusable |
|---|---|---|
| Boxes to buy | $Q$ per year | $N_{box} = (I_c+2)\,N_{trip}$ (once) |
| Yearly packaging cost | $Q\cdot c_{box}$ | $\dfrac{N_{box}\,c_{box}}{N_{years\,life}}$ |
| Transport | one way only | $I_c = 1$: always round trip · $I_c>1$: every $I_c$ trips → $(I_c-1)$ one way + 1 round trip |

$$\text{cycles/year} = \frac{Q}{N_{box}} \qquad N_{years\,life} = \frac{C_{life}\,[cycles]}{\text{cycles/year}} \qquad c_{trip,avg} = \frac{(I_c-1)\,c_{dir} + c_{RT}}{I_c}$$

![[reusable-loop-claude.png|560]]
💡 shortcut: reusable yearly packaging cost $= \dfrac{Q\cdot c_{box}}{C_{life}}$ (same result).
Single-use **damages**, if any: $Q_{products}\cdot\%_{damage}\cdot\text{value}$.

---

## 5. Warehouse design — bays and indexes

**Loading/unloading bays — Poisson**
$$P(x) = \frac{(\lambda T)^x e^{-\lambda T}}{x!}\qquad LS = \sum_{x=0}^{n-1}P(x)\ \geq\ 90\%\ (95\%)$$
$\lambda$ = trucks/h, $T$ = unloading time **in hours** (≈ 45 min) → $N_{bays}$ = first $n$ with cumulative ≥ LS (with $x$ arrivals you need $x+1$ bays). Each bay ≈ **4.5 m** of wall.

**Selectivity index** (warehouse parameter): $I_S = \dfrac{UL\ directly\ reachable}{total\ UL}$, $0\le I_S\le1$ (single deep = 1, double deep = 0.5)

**Access index** (item parameter): $I_A = \dfrac{M\ [UL\ moved/day]}{C\ [average\ UL\ in\ stock]}$ → high $I_A$ = closer to the I/O

---

## 6. AS/RS for unit loads (single deep) — sizing

**Usable height and floors**
$$H_{usable} = H_{avail} - 1\ (roof/sprinkler) - 0.8\ (ground)$$
$$H_F = h_{UL} + g_V\ (0.1) + s_{rack}\ (0.15) \qquad N_F = \left\lfloor \frac{H_{usable}}{H_F}\right\rfloor$$
With 2 UL types: $\bar H_F = w_a H_{F,a} + w_b H_{F,b}$ (weights = share of UL of each type).

**Number of stacker cranes (estimate)**
$$N^* = \frac{Q\cdot T_{target}}{3600}\qquad N = \lceil N^*\rceil$$
$Q$ = pairs (UL in + UL out)/h; $T_{target}$ = **110 s** simple cycle, **100 s** combined cycle.

**Rack module and length**
$$L_{module} = n\cdot l_{UL} + (n+1)\,g_H\ (0.1) + s_V\ (0.15)\qquad(3\ \text{europallets: } 3\cdot0.8+4\cdot0.1+0.15 = 2.95\ m)$$
$$C_{machine} = \frac{C_{tot}}{N}\qquad N_{modules} = \left\lceil\frac{C_{machine}}{UL_{module}\cdot 2\ (\text{2 racks/aisle})\cdot N_F}\right\rceil$$
$$L = N_{modules}\cdot L_{module}\qquad H = (N_F - 1)\cdot H_F$$

![[floor-height-claude.png|560]]

---

## 7. Cycle times — FEM 9.851

**Reference points** (I/O at $(0;y_{I/O})$)
$$P_1 = \left(\tfrac15 L\ ;\ \tfrac23 H + \tfrac13 y_{I/O}\right)\qquad P_2 = \left(\tfrac23 L\ ;\ \tfrac15 H + \tfrac13 y_{I/O}\right)$$
⚠️ Lesson 13 says $\tfrac13 L$ and $\tfrac13 H$, but the exam exercise (Lesson 14) uses $\tfrac15$: **use $\tfrac15$** (it is the standard).

![[fem-rack-generic-claude.png|560]]

**Time of one move** (trapezoidal profile, independent axes)
$$t = \frac{l}{v} + \frac{v}{a}\quad(\text{valid if } l\geq v^2/a)\qquad T(A\!-\!B) = \max\{t_x;\ t_y\}$$
⚠️ if $l < v^2/a$ the machine does not reach $v_{max}$: $t = 2\sqrt{l/a}$ (happens on short moves: miniload, lift, shuttle).

**Cycles** ($t_f$ = fork time for each pick/deposit)
$$T_{CS} = 2T(I/O\!-\!P_1) + 2T(I/O\!-\!P_2) + 4t_f\quad[s\ \text{per } 1\ UL_{in} + 1\ UL_{out}]$$
$$T_{CC} = T(I/O\!-\!P_1) + T(P_1\!-\!P_2) + T(P_2\!-\!I/O) + 4t_f\quad[s\ \text{per } 1\ UL_{in} + 1\ UL_{out}]$$

**Utilization and availability**
$$U = \frac{Q_{CS}\,T_{CS} + Q_{CC}\,T_{CC}}{N\cdot3600\cdot A}\qquad A = \frac{\sum UT}{\sum UT+\sum DT}\approx 0.96$$
- $U>1$ → add a machine; $U<0.6$ → remove a machine
- **throughput** of one machine: $Q_1 = \dfrac{3600}{T}$ cycles/h; real $= Q_1\cdot A\cdot U$; total $= N\cdot Q_1\cdot A\cdot U$

**Dual stacker crane (capacity 2 UL)** — simple cycle 2 in + 2 out
$$T_{CS}(2\,UL) = 2T(I/O\!-\!P_1) + 2T(P_1\!-\!P_2) + 2T(P_2\!-\!I/O) + 6t_f$$
$$T_{CS}\ \text{per } (1\,UL_{in}+1\,UL_{out}) = T(I/O\!-\!P_1) + T(P_1\!-\!P_2) + T(P_2\!-\!I/O) + 3t_f$$
Productivity increase $= \dfrac{Q_2}{Q_1} = \dfrac{T_{CS,1}}{T_{CS,2}}$ (lesson: 99 → 72.7 s = **+36 %**)

**Dual in combined cycle** (4 points): $P_1(\tfrac15L;\tfrac23H)$, $P_2(0.44L;0.46H)$, $P_3(L;0.87H)$, $P_4(\tfrac23L;\tfrac15H)$; path I/O→P1→P2→P3→P4→I/O.

**Target**: capacity-1 machine with $I_S=0.5$ (double deep) → $T_{CS} \approx 120\div130$ s.

**Picking fed by AS/RS**: 1 order line = 1 combined cycle (the picked UL goes back in, the next one comes out) + full UL inbound $= \dfrac{pieces/h}{pieces/UL}$ (inbound only ≈ $T_{CS}/2$).

---

## 8. Multi-deep warehouses (push/shuttle per level + lift)

**Level vehicle** ($x$ axis only, $P_1 = \tfrac15L$, $P_2=\tfrac23L$)
$$T_{CS} = 2T(I/O\!-\!P_1)_x + 2T(I/O\!-\!P_2)_x + 2t_{f,chain} + 2t_{f,shuttle}$$
$$Q_{1} = \frac{3600}{T_{CS}}\qquad Q_{vehicles} = Q_1\cdot N_{levels}$$

**Lift** ($y$ axis only, $P_1 = \tfrac23H + \tfrac13y_{I/O}$, $P_2 = \tfrac15H+\tfrac13y_{I/O}$)
$$T_{CS,y} = 2T(I/O\!-\!P_1)_y + 2T(I/O\!-\!P_2)_y + 4t_f$$
separate IN and OUT lifts → each $\dfrac{T_{CS,y}}{2}$ per UL → $Q_{lift} = \dfrac{3600}{T_{CS,y}/2}$ (often the **bottleneck**)

**System throughput** $= \min\{Q_{vehicles};\ Q_{lift}\}$; utilization of each component $= \dfrac{Q_{system}}{Q_{component}}$.
With capacity $k$ (e.g. shuttle 2 boxes, lift 4 boxes): multiply the UL per cycle.

---

## 9. Bozer–White (BW)

$$T_l = \frac{L}{\bar v_x}\quad T_h = \frac{H}{\bar v_y}\quad T = \max\{T_l;T_h\}\quad b = \min\left\{\frac{T_l}{T};\frac{T_h}{T}\right\}$$
- $b$ = **shape factor**: $b\ge0.8$ good design (warehouse "square in time"), $b\approx0.5$ bad

$$T_{CS} = 2T\left(1+\frac{b^2}{3}\right) + 4t_f\qquad T_{CC} = T\left(\frac43+\frac{b^2}{2}-\frac{b^3}{30}\right) + 4t_f$$
$$T_{internal}(P_1\!\to\!P_2) = T\left(\frac13+\frac{b^2}{6}-\frac{b^3}{30}\right)\qquad T_{CC} = \frac{T_{CS}}{2} + T_{internal}$$

**Comparison** (without $t_f$): $T_{CS,FEM} \approx \tfrac43T(1+b)$; $T_{CS,BW} = 2T(1+\tfrac{b^2}{3})$ → equal for $b = 1$ ($\tfrac83T$).
BW is used when FEM does not apply: **miniload / tote warehouses** (capacity 2–6 boxes per cycle).

**Typical values**: miniload $v_x=6$, $a_x=4$, $v_y=4$, $a_y=3$, $t_f = 5\div6$ s, ≈ **150 boxes(in+out)/h**; AS/RS investment for pallets **300÷400 €/UL**, for totes **30÷50 €/box**.

---

**Default values to remember**

| Parameter | Value |
|---|---|
| Driver shift | 8 h |
| Driver cost | 25÷30 €/h |
| Truck cost | ≈ 1.4 €/km |
| Loading + unloading | 45 + 45 min |
| Corrugated cardboard | 1.2 €/m² |
| UL per articulated truck | 33 × 2 = 66 |
| Roof / ground gap | 1 m / 0.8 m |
| $g_V$, $g_H$, rack thickness | 0.1 / 0.1 / 0.15 m |
| FEM kinematics | $v_x=4$, $a_x=1.2$, $v_y=1$, $a_y=0.9$ |
| Availability $A$ | 0.96 |
| $T_{target}$ CS / CC | 110 s / 100 s |
