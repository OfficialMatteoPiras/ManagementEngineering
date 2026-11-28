---
tags: [anylogistix, MFSSCM, lab]
course: Material Flow Systems and Supply Chain Management – anyLogistix Lab
teacher: Niloofar Katiraee (niloofar.katiraee@unipd.it)
---

> [!IMPORTANT] How these notes are organised
> - One `# Lezione N` per lesson. Lezione 1–2 come from the PDF slides, Lezione 3–8 from the video recordings (+ the PDFs/Excel used in class).
> - ⏱ `h:mm:ss` = position in the video recording of that lesson (file in `anylogistic_lessons/`).
> - 📁 = file in the `lab/` folder used in that part of the lesson.
> - Screenshots are in `assets/anylogistic-claude/`.
> - At the end there is a **Project cheat-sheet** that collects all the "pay attention in your work project" warnings the teacher gave.

**Course structure (slide "anyLogistix Lab")**
- Introduction to anyLogistix · ALX Development Environment
- Section 1 – Facilities Location: GFA presentation + GFA example
- Section 2 – Supply Chain Design: Network Optimization (NO) presentation + NO example
- Section 3 – Dynamic Simulation (presentation + simple simulation model)
- Section 4 – Supply Chain Analysis: service level analysis, risk assessment
- Section 5 – Inventory Optimization: inventory optimization, safety stock estimation
- **Final evaluation: project assignment in groups of 4 → 11 out of 33 points**

**Files of the lab** (📁 `lab/`)

| Lesson | Folder | Files |
|---|---|---|
| L3–L4 (22 Oct) – Case 1 *Polarbear Bicycle* | [[lab/LECTURE 3-4 (OCT22-26)-20261022/Case 1 Level 1/Case 1_Level 1.pdf\|Case 1_Level 1.pdf]], [[lab/LECTURE 3-4 (OCT22-26)-20261022/Case 1 Level 1/Case 1 Level 1_Extended.pdf\|Case 1 Level 1_Extended.pdf]] (annotated copy in `Annoted/`) | `Exercise_01.xlsx`, `PB GFA Level 1.xlsx`, `PB NO Level 1.xlsx`, `PB NO Level 1_Constrained.xlsx`, `PB NO Advanced_Extended (n periods).xlsx`, `PB SIM Level 1.xlsx`, `PB SIM Level 1_Improved.xlsx`, theory: [[lab/LECTURE 3-4 (OCT22-26)-20261022/ALX_NO.pdf\|ALX_NO.pdf]] |
| L5–L6 (5 Nov) – Case 2 *Berlin Brewery* | [[lab/LECTURE 5-6 (NOV5-26)-20261105/Case study 2 Level 2.pdf\|Case study 2 Level 2.pdf]] (+ `noted` version) | `BR NO Level 1.xlsx`, `BR NO Level Solution.xlsx`, `BR GFA Solution.xlsx`, `BR SIM Level 1.xlsx`, `BR SIM Solution.xlsx`, `BR SIM Level 1 Disruption Risk 2 DC.xlsx`, `BR SIM Level 1 Disruption Risk with 1 DC.xlsx` |
| L7–L8 (19 Nov) – Case 2 completed: SIM, disruptions, comparison, variation + work-project tips | same files as L5–L6 | `BR SIM Level 1 Disruption Risk 2 DC.xlsx`, `BR SIM Level 1 Disruption Risk with 1 DC.xlsx` (also a copy in `lab/`) |

---

# Lezione 1 – Introduction to anyLogistix (8 Oct, PDF)
📄 [[anylogistic_lessons/LECTURE 1 (OCT8-26).pdf]]

### Before starting
- Download: https://www.anylogistix.com/downloads/ (PLE = Personal Learning Edition, free, non-commercial).
- **Required knowledge: basic Excel**, especially **VLOOKUP** and **PIVOT** tables (they are needed to prepare the raw project data).
  - VLOOKUP: https://www.youtube.com/watch?v=d3BYVQ6xIE4
  - PIVOT: https://www.youtube.com/watch?app=desktop&v=F9WgF1K_K2g&t=20
- Resources: *Supply Chain Simulation and Optimization with anyLogistix* (D. Ivanov), *Global Supply Chain and Operations Management* (Ivanov, Tsipoulanidis, Schönberger), *Exercises in Supply Chain Optimization and Simulation using anyLogistix*.

### Supply chain & supply network
- **Supply chain** = a system of organizations, processes, activities, information and resources involved in supplying a product or service to a consumer (example: Starbucks coffee, from bean to cup).
- **Supply network**: the real structure is a network (suppliers → producers → DCs → warehouses → supermarkets → customers), with material/energy flow in one direction and information/financial flow in the other.

![[L1-p07-claude.jpg|600]]

**Supply network challenges** (decision levels):

| Level | Decisions |
|---|---|
| **Strategic** | size and location of plants / DCs, structure of service networks, design of the supply chain |
| **Tactical** | production, transportation and inventory planning |
| **Operative** | production scheduling and control, inventory control, vehicle routing |

![[L1-p08-claude.jpg|600]]

**The supply chain is constantly evaluated** – typical questions: What should the SC design be? How much to produce and where to store? Which transportation policies? Which resources/capacity do we need? What if we introduce new products? What if workers go on strike / we lose a key supplier? Where is the SC susceptible to risk? Which service level can we provide? How to make it more sustainable? Make or buy? What if I change inventory, transportation or sourcing policies?

![[L1-p10-claude.jpg|600]]

### What is anyLogistix (ALX)
- Supply chain analytics software to **design, optimize and analyze** a company's supply chain. It combines **analytical optimization** with **simulation**.
- **Two engines**:
  1. **CPLEX – analytical LP/MIP solver** (IBM ILOG CPLEX built in) → GFA and Network Optimization (optimal SC sites, flows, multi-period).
  2. **AnyLogic – dynamic simulation modeling** → simulation of the SC behaviour over time, policies, risk, robustness.

![[L1-p12-claude.jpg|600]]

**What can we do in ALX?**
- Facility location planning; center-of-gravity method (single and multiple locations)
- Network optimization with Mixed-(Integer)-Linear Programming
- Capacity planning of DCs
- Inventory control policies and ordering rules
- Sourcing policies (single / multiple sourcing)
- Transportation policies (FTL = Full Truckload / LTL = Less-Than-Truckload)
- Batching in transportation, production and sales
- Bullwhip effect and ripple effect analysis

**Modelling logic:** scenarios → GFA / Analytical Network Optimization / Simulation → results → decision making.

![[L1-p15-claude.jpg|600]]

**Problem examples:** best locations for warehouses/DCs/plants; how to allocate demand and supply; best replenishment, sourcing and transportation policies; resilience to supplier disruptions; what happens if we change inventory policy, DC capacity, demand, add a product; what does an out-of-stock cost?

**Simulation vs optimization** (level of detail): optimization = high abstraction, static (locations, flows, aggregated parameters → *where to build DCs, master planning, fleet size*); simulation = dynamic, more detail (time, randomness, processes, resources → *inventory & sourcing policies, service level, bullwhip, risk*).

![[L1-p17-claude.jpg|600]]

**Other concepts in the slides**
- *Supply Chain Analytics*: descriptive/predictive analytics (performance visualization, analysis) ↔ prescriptive (planning, monitoring, control).
- *Digital Supply Chain Twin* – ALX model connected to real data (blog: https://www.anylogistix.com/resources/blog/building-a-digital-twin-with-anylogistix-api/).

![[L1-p19-claude.jpg|600]]

- *Supply chain stress-testing*: risk data (historical / real-time disruptions) → SC model (stress-testing of SC designs, recovery plan selection) → performance analysis (possible / real performance impact).

![[L1-p20-claude.jpg|600]]

- *Development cycle of a simulation model*: Reality → (analysis) → Conceptual model → (programming) → Computerized model → (computer simulation) → back to reality; with **model qualification, verification, validation**.

![[L1-p21-claude.jpg|400]]

---

# Lezione 2 – Greenfield Analysis (GFA) theory + ALX Development Environment (8 Oct, PDF)
📄 [[anylogistic_lessons/LECTURE 2 (OCT8-26).pdf]] · 📄 [[anylogistic_lessons/Development Environment_ALX.pdf]]

## 2.1 What is Greenfield Analysis
- Analytical experiment that uses the **center-of-gravity** approach to find optimal locations for **new site(s)** that will manage the given demand.
- **Objective:** find the **number** and potential **areas** to locate SC facilities.
- **Criterion:** minimize **"transportation flows"** = `<distance> × <product amount>`.
- **Assumption:** routes are **straight** (direct distance).
- GFA lets you:
  - find the optimal locations for a **specified number of sites** (DCs by default), or
  - calculate the **optimal number of sites** given a **maximum distance to a customer** (service distance).
- Data considered: products, demand, supply sources, customer locations, service distance constraints, number of potential facilities.

![[L2-p03-claude.jpg|500]] ![[L2-p04-claude.jpg|500]]

## 2.2 Center-of-gravity model
- Each customer i is a pair of coordinates (xᵢ; yᵢ) → **input data / parameters** (cannot be changed).
- The new warehouse coordinates (pₓ; p_y) are the **decision variables**.
- Assumption: transport cost is **linearly proportional to distance and volume (demand)**.

**Objective function**

$$Z(p_x,p_y)=\sum_{i=1}^{N} d\big((p_x,p_y),(x_i,y_i)\big)\cdot D_i \;\rightarrow\; \min$$

| Notation | Meaning |
|---|---|
| Z | total transportation costs |
| pₓ, p_y | X / Y coordinate of optimal location |
| xᵢ, yᵢ | X / Y coordinate of customer i |
| Dᵢ | demand of customer i |
| i | running index of customers |

**Distances**
- Euclidean: $d=\sqrt{(x_i-p_x)^2+(y_i-p_y)^2}$
- Rectilinear: $d=|x_i-p_x|+|y_i-p_y|$

![[L2-p09-claude.jpg|550]]

*References: Tompkins – Facilities Planning (ch. 10); Ivanov – Global SC and Operations Management (ch. 7).*

### Example – German customers of TT Profi

| i | Name | xᵢ | yᵢ | Dᵢ |
|---|---|---|---|---|
| 1 | Sport 1-2-3 KG | 10 | −80 | 3 t |
| 2 | TT direct | −45 | −30 | 1 t |
| 3 | Sports and Fun | 60 | 50 | 1.5 t |
| 4 | Leisure Outlet | 45 | −75 | 3.5 t |
| 5 | Rackets & More | −75 | 80 | 2 t |

**Euclidean case** – set the partial derivatives dZ/dpₓ and dZ/dp_y equal to 0.

![[L2-p11-claude.jpg|550]]

1. **Equal demand (Dᵢ = 1)** → simple average:
   - pₓ = Σxᵢ/N = (10−45+60+45−75)/5 = **−1**
   - p_y = Σyᵢ/N = (−80−30+50−75+80)/5 = **−11**
2. **With individual demand** → formulas (6)–(7): weights Dᵢ / dᵢ, but dᵢ depends on (pₓ,p_y) → circular.

![[L2-p13-claude.jpg|600]]

### Miehle algorithm (1958)
- Breaks the circularity with a **recursive approximation**: start from (a₀;b₀) = equal-demand solution (Eq. 4–5), then plug (aᵢ;bᵢ) in the right side of (6)–(7) to get (aᵢ₊₁;bᵢ₊₁).
- The sequence Z(a₀;b₀), Z(a₁;b₁)… **decreases and converges** to the minimum.
- **Stop** when the distance between two consecutive solutions < predefined threshold.

Start value: Z(−1;−11) = 897.3

| i | aᵢ | bᵢ | aᵢ₊₁ | bᵢ₊₁ | Distance | Z(aᵢ;bᵢ) |
|---|---|---|---|---|---|---|
| 0 | −1.00 | −11.00 | 8.78 | −36.16 | 26.99 | 897.38 |
| 1 | 8.78 | −36.16 | 14.69 | −50.10 | 15.14 | 808.37 |
| 2 | 14.69 | −50.10 | 18.05 | −58.14 | 8.71 | 771.93 |
| 3 | 18.05 | −58.14 | 19.64 | −62.48 | 4.62 | 757.29 |
| 4 | 19.64 | −62.48 | 20.28 | −64.57 | 2.18 | 752.67 |
| 5 | 20.28 | −64.57 | 20.49 | −65.48 | 0.94 | 751.58 |
| 6 | 20.49 | −65.48 | 20.53 | −65.87 | 0.39 | 751.37 |
| 7 | 20.53 | −65.87 | 20.52 | −66.03 | 0.16 | 751.33 |
| 8 | 20.52 | −66.03 | 20.50 | −66.10 | 0.07 | 751.32 |
| 9 | 20.50 | −66.10 | 20.49 | −66.14 | 0.04 | 751.32 |

![[L2-p16-claude.jpg|500]]

> [!tip] Try it in Excel
> The Miehle iteration is easy to rebuild in Excel: one row per iteration, columns dᵢ for each customer, then `SUMPRODUCT` for numerator/denominator of (6)–(7).

**Rectilinear case** (weighted): pₓ = ΣDᵢxᵢ/ΣDᵢ = (30−45+90+157.5−150)/11 = **7.5**; p_y = (−240−30+75−262.5+160)/11 = **−27**; Z = 55.5·3 + 55.5·1 + 129.5·1.5 + 85.5·3.5 + 189.5·2 = **1094.5 t·km**.

![[L2-p18-claude.jpg|550]]

## 2.3 GFA in anyLogistix
- Data to specify: customers, **locations of customers (latitude; longitude)**, products, demand per customer & product, direct distance customers ↔ DCs.
- ALX uses **GIS data from OpenStreetMap**: the map updates instantly when you create an element or change a connection.

![[L2-p20-claude.jpg|500]]

**GFA with roads**: plain GFA ignores roads, cities, geography → it can propose a DC on a mountain or in the sea. *GFA with roads* considers **actual roads and city population** → more realistic DC locations.

![[L2-p21-claude.jpg|500]]

> [!summary] GFA summary
> - Finds the **NUMBER and AREAS** of facilities.
> - Needs: customers/market locations, products, demand.
> - Criterion: min transportation flows = distance × product amount.
> - Results: areas for facilities, flows facilities→customers, customer center of gravity & service distances.
> - Options: direct distance or real roads; inbound supply nodes and flows can be considered.

## 2.4 ALX Development Environment
**Welcome screen**: create new scenario, getting-started help, help, list of examples, useful links.

![[DE-p03-claude.jpg|600]]

**Projects**
- Input data and experiments are organized in **projects**; a project contains any number of **scenarios** (input data) and **experiments**.
- Creating a project creates a **dedicated database** (DBMS: sqlite by default; also sqlserver, mysql, postgresql, hsqldb).
- **Only one project open at a time** → `File | Select Project…` to switch.

![[DE-p04-claude.jpg|500]] ![[DE-p07-claude.jpg|500]]

**Scenarios & experiments**: scenarios = initial data. Experiments are either **analytical (CPLEX)** – GFA, Network Optimization, Transportation Optimization – or **dynamic simulation (AnyLogic)** – Simulation, Risk analysis, Inventory optimization, What-if & visualization, Comparison… → results → enhanced business decisions.

![[DE-p05-claude.jpg|600]]

**Main screen**: project name, scenario type tabs (GFA/NO/SIM/TO), list of scenarios in the tab, list of actions for the selected scenario, table editor. **Map**: map toolbar to create objects (double-click on map to create a site of the selected type), filter options, switch between *map view* and *scenario structure view*.

![[DE-p08-claude.jpg|500]] ![[DE-p09-claude.jpg|500]]

**Table editor toolbar**
- **Add** – new record · **Remove** – delete selected record(s)
- **Expand…** – (some tables) expands a record into several separate records
- **Compact view** – only in *Product Flows*: hides 10 columns into a new *Constraints* column · **Detailed view** – moves them back
- **Generate** – only in Milk Runs, Customers, DCs and Factories (NO, SIM, TO) and Demand: generates data from parameters

![[DE-p10-claude.jpg|600]]

**Output tables** (results): sort, filter, reorder columns like any ALX table, and also:
- **Group data** – drag a column title into the grouping area (several columns → left-to-right order = top-to-bottom grouping)
- **Aggregate function** – right-click a column → Sum / Mean / Count / None (default upper level shows the number of records)
- **Hide columns**

![[DE-p13-claude.jpg|500]] ![[DE-p16-claude.jpg|500]]

**Menus**
- *File*: create new scenario, **import data from Excel**, **export data to Excel**, add external tables, change user, change project.
- *Extensions*: AnyLogic extensions editor, edit, extension manager.
- *Settings*: time/date/number format, min/max fraction digits, units, drop cache, icons, password protection, DB users, access rules.
- *Help*: **import examples from Excel**, welcome screen, open log file, ALX help, version/license, check for updates.

![[DE-p17-claude.jpg|500]] ![[DE-p18-claude.jpg|500]]

---

# Lezione 3 – First steps in ALX, GFA and Network Optimization setup (22 Oct, morning – video)
🎥 `anylogistic_lessons/Video recording lecture 3 OCT22-26 STEM.mp4` (1h24)
📁 [[lab/LECTURE 3-4 (OCT22-26)-20261022/Case 1 Level 1/Case 1_Level 1.pdf|Case 1_Level 1.pdf]] · [[lab/LECTURE 3-4 (OCT22-26)-20261022/Case 1 Level 1/Case 1 Level 1_Extended.pdf|Case 1 Level 1_Extended.pdf]] · [[lab/LECTURE 3-4 (OCT22-26)-20261022/ALX_NO.pdf|ALX_NO.pdf]]

## 3.1 Material of the lesson ⏱ 0:00:27
- Moodle → *anyLogistix Laboratory* → folder **LECTURE 3-4 (OCT22-26)** → download as zip.
- Folder **Case 1 Level 1** = the *Polarbear Bicycle* case:
  - 2 PDFs (`Case 1_Level 1.pdf`, `Case 1 Level 1_Extended.pdf`) = complete description of the case **with all results and screenshots** → use them to study at home.
  - The year in the Excel files was updated **2021 → 2025**, results are "more or less similar" to the PDF.
  - `Exercise_01.xlsx` + scenarios: **GFA**, **NO** (network optimization), **2 files for SIM** (simulation).
- `ALX_NO.pdf` = theory file (mathematical model behind network optimization).
- Order of work in ALX: **GFA → NO → SIM** (GFA is always the first step).

## 3.2 Welcome page & settings ⏱ 0:05:46
- Right side: **documentation, help** → the ALX help is "really rich": search by keywords when you don't know something.
- Three main parts: **Greenfield Analysis, Network Optimization, Simulation** (with links to videos/tutorials/help).

![[L3-01-welcome-screen-claude.jpg|700]]

- **Settings** ⏱ 0:06:30 → *Number format*: *System* or *User defined* (decimal point/comma depending on your PC: Italian, English, German…), min/max fraction digits. Also "skip feasibility check if NO scenario is infeasible", update charts during simulation, chart update frequency, language.
- **About** → check the version: everybody should use the same version as the teacher.

![[L3-02-settings-number-format-claude.jpg|700]]

## 3.3 Creating the project ⏱ 0:07:28
- **Create new** → project name (e.g. `Case 1 Level 1`).
- ⚠️ In this (PLE) version **we cannot have multiple projects** → all scenarios must be **created/imported in only one project**.
- In the project: *All types* filter → GFA / NO / SIM.
- **+** menu on the left ⏱ 0:08:54 has 3 options:
  1. **Create scenario** – build a scenario from scratch (what you will do in the **work project**).
  2. **Import scenario** – import a prepared Excel scenario (what we do in class).
  3. **Explore examples** – solved examples from companies (e.g. simulation examples).

![[L3-03-create-import-explore-claude.jpg|700]]

## 3.4 Case 1 – Polarbear Bicycle ⏱ 0:11:55
- Start-up in Germany, e-commerce, needs **a location for a new DC**.
- 4 customers: **Cologne, Bremen, Frankfurt am Main, Stuttgart**.
- 4 products (bicycle types): **x-cross, urban, all terrain, tour**.
- Demand per day per customer and product (deterministic) → **total 245 bicycles/day**.

| Customer | x-cross | urban | all terrain | tour |
|---|---|---|---|---|
| Cologne | 2 | 50 | 15 | 10 |
| Bremen | 7 | 30 | 20 | 20 |
| Frankfurt am Main | 6 | 5 | 4 | 5 |
| Stuttgart | 15 | 15 | 1 | 40 |

(Data also in 📁 `Exercise_01.xlsx` with coordinates: Cologne 50.834/6.855, Bremen 53.054/8.855, Stuttgart 48.778/9.294, Frankfurt 50.078/8.635; basic period 01/01/2025–31/12/2025.)

> [!note] Teacher's remark ⏱ 0:14:24
> Today we import **prepared scenarios**: "import, run and see the result". In the work project your data will be **raw** and you will have to transform it into the ALX format – that's the hard part.

## 3.5 Importing the GFA scenario ⏱ 0:15:27
- **+ → Import scenario → browse → `PB GFA Level 1.xlsx` → Import**.
- **Advanced settings** ⏱ 0:15:53: option **"Scenario contains formulas"** → enable it when your Excel scenario contains formulas (likely in the work project). Not needed here.

![[L3-04-import-scenarios-dialog-claude.jpg|600]]

- After import you see the map with 4 customers. Left panel tables: **Basic / All / In use** → always look at **IN USE** (the tables actually used by the scenario; e.g. the Locations table is not under *Basic*) ⏱ 0:18:47.

### Demand table ⏱ 0:20:36
![[L3-05-gfa-demand-table-claude.jpg|700]]

- Demand types: **Historic demand**, **Periodic demand**, (and others).
- Here we use **Periodic demand** because data are **deterministic** (known quantity per day). In the work project data will be **stochastic**, not this easy.
- **Order interval = 1 day** for every row because the table gives *demand per day* → each day customers place an order; the **quantity** changes per customer/product.
- **Historic demand** ⏱ 0:23:30: add a row → parameters = list of **date + quantity** (e.g. the orders of the last year). In real cases we often use historic demand to test the *as-is* situation; it shows also seasonality/backlogs (e.g. beverage companies sell more in summer). → likely option for the **work project**.

![[L3-06-historic-demand-row-claude.jpg|700]]

- **First occurrence** (parameters dialog) ⏱ 0:24:55:
  - **First day** → as soon as the customer orders, the company prepares and ships.
  - **Next day after interval** → the order is processed the day after it is placed.
  - **Random time within interval** → random day.
  - Here: *First day*.

![[L3-07-demand-parameters-dialog-claude.jpg|600]]

- **Time period = (All periods)** because there is only one period (1 year). Often you split into several periods (12 months, 4 seasons…) ⏱ 0:26:40.
- **Locations** ⏱ 0:27:11: only **latitude and longitude** are needed (input data) – or pick the point on the map and ALX assigns them.
- **Products**: unit **pcs** (could be kg, litre, m³, tonne…).
- GFA uses **very few data (5–8 tables)** because it is a **long-term decision** and gives only an *estimated* location, not the final one ⏱ 0:28:09.

## 3.6 Running the GFA ⏱ 0:29:07
- Click **GFA experiment** → **always click Settings first** and check everything: product unit **pcs**, distance **km**.
- **Analyzed by**:
  - **Number of sites** → you decide how many DCs (case: 1).
  - **Service distance** → e.g. "no more than 200 km from customers" → ALX decides how many sites (1, 2, 3…).

![[L3-08-gfa-experiment-settings-claude.jpg|700]]

- Run with the **blue square/triangle** ⏱ 0:30:29.
- GFA and NO results should be **identical** on all PCs; in **simulation** results may differ slightly (different seeds/speed).

**Result with 1 DC** ⏱ 0:30:42: Flow = **89,425 pcs**, Distance = **2,754.119 km**, Flow cost estimation = **16,351,066.948 pcs·km**.

![[L3-09-gfa-result-1dc-claude.jpg|700]]

- **Structure view** (button next to the map) → "GFA DC → all customers"; **map view** shows the flows.
- **New sites** page ⏱ 0:31:51 → GFA DC at **lat 50.82, long 7.475** (near Cologne; PDF: max distance 266.11 km to Bremen, min 43.55 km to Cologne).

![[L3-10-gfa-new-sites-claude.jpg|600]]

- Why there? The GFA objective: minimize **flow cost = distance × product flow** (center of gravity) ⏱ 0:32:22.
- **Rename results**: right-click the result → *Edit* → e.g. `Result_1DC` ⏱ 0:33:28.

![[L3-11-rename-result-claude.jpg|600]]

**Result with 2 DCs** ⏱ 0:34:32 (set number of sites = 2 and rerun): three customers served by one DC, **Bremen** (far from the others) by the second one. Distance **1,287.003 km (−53.27%)**, flow cost **8,055,704.47 pcs·km (−50.73%)**. **Product flow stays 89,425** ⏱ 0:35:52: the number of products doesn't change, only distances.

![[L3-12-gfa-result-2dc-claude.jpg|700]]

> [!question] 1 or 2 DCs? ⏱ 0:37:08
> Flow cost decreases a lot with 2 DCs, and with 3, 4, … 100 DCs it would go towards 0 (distance → 0). But **GFA does not consider any facility cost**: no fixed costs, no vehicle types, no **initial cost** (= setup cost: building, renting), maintenance, energy, workers. → we cannot decide here. GFA only gives an **approximate location / an idea**; then we must go to **network optimization**.

> [!warning] Most repeated question in the work project ⏱ 0:40:23
> "GFA gave me this location: must I keep it in NO and SIM?" → **No.** GFA locations are only an indication that the area could work; in NO you decide based on **profit**, in SIM based on **other KPIs**.

## 3.7 Case 1 – Network optimization part ⏱ 0:42:55
- After GFA, Polarbear sells from the new DC (DC Germany = *Steimelhagen*). Then they decide to **produce their own bicycles**: factory in **Nuremberg**, **250 bikes/day**.
- Offer from a Polish company: rent a **DC in the Czech Republic** and a **factory in Warsaw (Poland)** – not part of the as-is, still under negotiation.
- 4 options to compare:
  1. DC Germany + Factory Germany
  2. DC Germany + Factory Poland
  3. DC Czech Rep. + Factory Poland
  4. DC Czech Rep. + Factory Germany
- With few data you could do it in Excel, with big data you need ALX: NO is solved by **CPLEX**.
- In the network figure the Polish factory is **dashed** = under negotiation; suppliers will be integrated next week.

## 3.8 Theory: what is behind Network Optimization ⏱ 0:48:58
- SC described as **echelons/entities**: suppliers → factories → DCs → customers; NO tests all **configurations/paths**.
- **Aim of NO: maximize profit** (≈ minimize costs). Compared to GFA it also considers **facility costs** (fixed, maintenance, carrying/inventory…).

![[L3-13-no-slide-annotated-claude.jpg|600]]

- **Boolean variable** yᵢ for each DC: **1 = open** (→ pay its **fixed cost** fᵢ + transport costs cᵢⱼ to customers j), **0 = closed** (no cost) ⏱ 0:51:36.
- If we don't know whether to open it, it is a **decision variable** → in ALX inclusion type **Consider**; *Include* = must be open, *Exclude* = not opened ⏱ 0:53:23.

![[L3-14-no-yi-open-close-claude.jpg|500]]

**Warehouse Location Problem (WLP)** (slide from 📁 `ALX_NO.pdf`): given potential locations S, markets M, links T = S·M, link costs c_sm, fixed costs f_s; variables y_s (open) and x_sm (link used); constraints x_sm ≤ y_s, Σ_s x_sm = 1 (single sourcing), binary; objective

$$\min Z=\sum_{s\in S} f_s\,y_s+\sum_{s\in S}\sum_{m\in M} c_{sm}\,x_{sm}$$

![[L3-15-no-wlp-model-claude.jpg|600]]

- You never see the CPLEX model in ALX – the software builds and solves it (with CPLEX directly – like the assembly line balancing in Prof. Battini's course – modelling a supply network would take a lot of time because of the many constraints) ⏱ 0:54:13.

![[ALXNO-p06-claude.jpg|550]]

### Hard vs soft constraints & penalties ⏱ 0:56:01
- **Hard constraint**: cannot be violated → with many hard constraints you may get **no feasible solution**.
- **Soft constraint**: can be violated **by paying extra** (money or time) → a solution is always found.
- Example ⏱ 0:57:46 – demand 1000, we can send only 800 (backlog 200):
  - Plan A (hard): D ≥ 1000 and a ≤ 800 → impossible to satisfy both → infeasible.
  - Plan B (soft): add **unmet demand u** → D + u ≥ 1000, a ≤ 800 → feasible, paying a **penalty**, e.g. 30 €/pc → 200 × 30 = 6,000 €.

![[L3-16-hard-soft-example-claude.jpg|500]]

- **Down penalty** = paid when you **fall below** the requested demand (e.g. need 245 bikes/day, send 200 → 45 × 30 €).
- **Up penalty** = paid when you **exceed** it (e.g. send 250 instead of 245).
- Penalties transform hard constraints into soft constraints → feasible solution ⏱ 1:02:16.

![[L3-17-penalties-slide-claude.jpg|500]]

From 📁 `ALX_NO.pdf`: penalties are also applicable to **sites/storages** (stock down penalty < min stock, safety stock penalty, stock up penalty > max stock) and **flows** (down penalty < min throughput, up penalty > max throughput), only if **Fixed** is disabled.

![[ALXNO-p10-claude.jpg|550]]

## 3.9 Importing `PB NO Level 1` ⏱ 1:04:17
📁 [[lab/LECTURE 3-4 (OCT22-26)-20261022/Case 1 Level 1/PB NO Level 1.xlsx|PB NO Level 1.xlsx]]
- NO needs much more data than GFA: fixed costs, carrying (inventory) costs, processing costs, transportation costs → all from Table 2 of the PDF.
- Import → map with 4 customers, 2 DCs, 2 factories. Look at **In use: 16 tables** (must be 16 for everybody) ⏱ 1:05:28.

![[L3-18-no-scenario-map-claude.jpg|700]]

**Input data (Table 2 of the case)**

| Cost | Value (USD) |
|---|---|
| Factory Nuremberg – fixed (other) costs / day | 15,000 |
| Factory Poland – fixed (other) costs / day | 5,000 |
| DC Germany – fixed (other) costs / day | 15,000 |
| DC Germany – carrying cost / bicycle | 3.00 |
| DC Czech Rep. – fixed (other) costs / day | 5,000 |
| DC Czech Rep. – carrying cost / bicycle | 2.00 |
| DC Germany – processing cost (in & outbound, per pc) | 2.00 |
| DC Czech Rep. – processing cost (in & outbound, per pc) | 1.00 |
| Production cost Nuremberg / bicycle | 250 |
| Production cost Poland / bicycle | 150 |
| Product purchasing cost (all bicycles) | 30 |
| Transport factory→DC and DC→customer | 0.01 × pcs × distance |
| Unit revenue | 499 |

Truck = **80 bicycles**, speed **80 km/h**. Rent of Polish factory / Czech DC is included in "other costs".

### Demand – down & up penalty ⏱ 1:06:07
- Same as GFA + **Revenue 499**, **Down penalty 5,000 USD**, **Up penalty 5,000 USD** (per unit).
- E.g. if instead of 245 we send 200 → pay 5,000 × 45.
- If set to 0 maybe nothing changes, but **with product backlog the software cannot give a feasible solution**.
- For the **work project you don't necessarily need up/down penalties** (the project is designed so you don't), but you can use them; they are useful when production capacity < demand.

![[L3-19-no-demand-penalties-claude.jpg|700]]

- **Inclusion type in Demand**: *Exclude* a row if e.g. a customer no longer wants x-cross; better than *Remove* because you can re-include it in another run ⏱ 1:08:11.

### Distribution centers ⏱ 1:09:30
| DC | Initially open | Inclusion type |
|---|---|---|
| Steimelhagen (Germany, found with GFA) | ✅ (already used) | Consider |
| Czech Rep. | ❌ (under negotiation) | Consider |

- **Consider** = the software decides (decision variable). **Include** = you force ALX to open it.
- NO = **medium-term** decision (GFA = long-term).
- In the work project: DCs you are sure about → **Include**; the others → **Consider** ⏱ 1:11:47.
- If an initially-open facility is closed, the company must pay the **closure cost** (not considered in this case).

![[L3-20-no-dc-consider-claude.jpg|700]]

### Facility expenses ⏱ 1:12:42
4 types of costs:
1. **Carrying cost** = inventory/holding cost; more related to the **product** (dimension → m³ needed) than to the facility. Unit: per **day** and per **product unit** (pcs, m³…). In reality usually per **m³**.
2. **Closure cost** – to close an already open facility.
3. **Initial cost** – building / setting up a new facility.
4. **Other costs** = **fixed costs**: maintenance, energy, electricity, rent… related to the facility (per day, no product unit).

![[L3-21-no-facility-expenses-claude.jpg|700]]

> [!warning] Work project ⏱ 1:16:57
> Costs are given to you as **input**. Carrying costs will be given **per year per m³** → divide to get the **daily** value (ALX has no yearly unit, only day/hour…).

📁 PB NO Level 1 – Facility Expenses

| Facility | Expense type | Value | Unit |
|---|---|---|---|
| Steimelhagen | Carrying cost | 3 | USD/day/pcs |
| Steimelhagen | Other costs | 15,000 | USD/day |
| Nuremberg | Other costs | 15,000 | USD/day |
| Czech Rep. | Other costs | 5,000 | USD/day |
| Czech Rep. | Carrying cost | 2 | USD/day/pcs |
| Poland | Other costs | 5,000 | USD/day |

### Factories ⏱ 1:17:38
Nuremberg (initially open, Consider), Poland (not initially open, Consider).

![[L3-22-no-factories-claude.jpg|700]]

### Groups ⏱ 1:18:09
- Create a group per echelon (customers, DCs, factories, suppliers) → **paths and product flows become much easier to write** (essential with ~100 customers).
- Here: `Customers 1` (4 customers), `DCs` (Czech Rep., Steimelhagen), `Factories` (Nuremberg, Poland).

![[L3-23-no-groups-claude.jpg|700]]

### Objective members ⏱ 1:19:20
Objective = **Revenue − all costs = profit** → results are sorted from the **most profitable** to the least profitable iteration. Members: Revenue (+), Total fixed (other) costs, inbound, outbound, penalties, production, storage (carrying), supply, transportation costs (−).

![[L3-24-no-objective-members-claude.jpg|700]]

### Overview of the other NO tables ⏱ 1:20:05
- **Paths** – "one of the most important parts": wrong paths are the most common error in the work project → define correctly **source → destination, product, cost calculation** (details in Lezione 4).
- **Periods** – 1 year. **Processing cost** – handling, loading/unloading = inbound & outbound logistics.
- **Product flows** – as important as paths. **Product storages**, **Production** (what each factory produces), **Vehicle types**.
- NO has many more data than GFA; SIM even more. Even after NO you can't see the final solution: you must **test it in simulation** ⏱ 1:22:23.

![[L3-25-no-paths-claude.jpg|700]]

![[L3-26-no-processing-cost-claude.jpg|500]] ![[L3-27-no-product-flows-claude.jpg|500]]
![[L3-28-no-production-claude.jpg|500]] ![[L3-29-no-vehicle-types-claude.jpg|500]]

---

# Lezione 4 – Network Optimization in detail, capacity constraint, first simulation (22 Oct, afternoon – video)
🎥 `anylogistic_lessons/Video recording lecture 4 OCT22-26 STEM.mp4` (1h32)
📁 `PB NO Level 1.xlsx`, `PB NO Level 1_Constrained.xlsx`, `PB SIM Level 1.xlsx`

## 4.1 Processing costs ⏱ 0:04:27
- Inbound & outbound logistics = cost of **loading/unloading** (handling). Here only for the 2 DCs (Steimelhagen 2 $/pc in & out, Czech Rep. 1 $/pc); factories and suppliers can also have processing costs.

![[L4-01-no-processing-cost-claude.jpg|700]]

## 4.2 Paths ⏱ 0:05:34
- Tell ALX **from which source to which destination** products are sent (here: factories → DCs, DCs → customers). With wrong paths you get "strange or incorrect numbers".
- **Groups** make paths short: `[Factories] → [DCs]`, `[DCs] → [Customers 1]`. Without groups you'd need one row for each pair.
- If costs differ between sources/destinations (e.g. Poland → Czech Rep. has a fixed cost) you **must add separate rows**; group only facilities with the same price ⏱ 0:09:45.

**Cost calculation** options ⏱ 0:07:04: cost per drop, distance-based with cost per stop, distance-based with fixed cost, **fixed delivery** (fixed price per shipment/truck), fixed delivery within distance range, **product & distance-based**, product & distance-based within distance range…

![[L4-02-path-cost-calculation-options-claude.jpg|700]]

- **Product & distance-based** (used here): cost depends on **product amount and distance** → typical of **LTL** shipments (truck not full: 70–80 %).
- With **FTL** you usually choose a **distance-based** cost (the truck leaves only when full → cost depends only on distance).
- **Cost calculation parameters**: here **cost per unit = 0.01** (0.01 × pcs × km).
- **CO₂ calculation parameter**: you can add CO₂ emissions → in the work project different vehicles with different CO₂ will be given: evaluate scenarios on **profit and CO₂** ⏱ 0:08:54.

![[L4-03-path-cost-parameters-claude.jpg|700]]

- **Distance = 0** in the table: it is **not** zero, it is computed by the software through **GIS** from the coordinates in *Locations* → leave it empty ⏱ 0:11:46.
- **Vehicle type** ⏱ 0:12:48: one truck, **capacity 80 bicycles, speed 80 km/h**. In reality speed is not constant (traffic, roads) → later we'll use **stochastic** values (triangular, uniform).

![[L4-04-vehicle-type-truck-claude.jpg|700]]

- **Transportation policy** ⏱ 0:14:01: **FTL** (ships only when the truck is full) or **LTL** (ships with a percentage of load). Here LTL. Inclusion type: include both paths.

![[L4-05-transportation-policy-ftl-ltl-claude.jpg|700]]

## 4.3 Product flows, storages, production, products ⏱ 0:14:52
- **Product flows**: which products can go from which source to which destination (factories → DCs, DCs → customers, vehicle Truck 1, *All products*). If factory 1 can only ship tour & x-cross, you must specify the products per source.

![[L4-06-product-flows-claude.jpg|700]]

- **Product storages** ⏱ 0:16:09: if you delete it, **no feasible solution** – ALX assumes the product cannot be stored anywhere. You must define storage in each facility (factories & DCs).

![[L4-07-product-storages-claude.jpg|700]]

- **Production** ⏱ 0:16:48: if missing, no results (factories produce nothing). Production cost per product: **Nuremberg 250, Poland 150** → expect NO to prefer Poland (objective = max profit).

![[L4-08-production-costs-claude.jpg|700]]

- **Products** ⏱ 0:19:23: compared to GFA there are **selling price (499)** and **cost (30)** → selling price is needed to compute **revenue** and therefore profit.

![[L4-09-products-price-cost-claude.jpg|700]]

> [!summary] Costs considered in NO (none in GFA) ⏱ 0:17:33
> - **Facility costs**: carrying cost (product/inventory) and other = fixed cost (facility: energy, maintenance, rent); **initial & closure** cost.
> - **Processing costs**: handling, loading/unloading.
> - **Production costs**.
> - (+ transportation costs in paths, product cost & selling price in products, penalties in demand)

> [!warning] ⏱ 0:21:00
> The lessons give fundamentals; in the work project you'll find new things you must **explore by yourself** – otherwise it couldn't be worth 11/33.

## 4.4 NO experiment settings ⏱ 0:22:26
- **Select demand variation type**:
  - **Exact demand** → all demand must be fulfilled exactly.
  - **95%–100%** → demand may be up to **5 % lower** without penalty; down penalty only for the part beyond 5 % (e.g. 7 % shortfall → penalty on 2 %). Used here (soft constraint).
  - **100%–105%** → up to 5 % over-delivery allowed; up penalty beyond.
- Other options are **CPLEX solver parameters** (search type *Find N best*, **number of best solutions = 10**, optimization time limit 600 s, relative MIP gap, threads, problem definition type…).
- ⚠️ Always check that **currency and units in the experiment settings match the input data** ⏱ 0:26:14 (PDF note: m³ vs pcs must be consistent, define unit conversions if needed).

![[L4-10-no-settings-demand-variation-claude.jpg|700]]

![[L4-11-no-settings-solver-claude.jpg|700]]

## 4.5 NO results – uncapacitated ⏱ 0:26:27
- 10 iterations sorted from best: **iteration 1 profit ≈ 26.17 M USD** (Flows amount 178,850 pcs, revenue 44,623,075 USD); last iteration has **negative profit**. 10 iterations is enough (huge drops after iteration 7–8).

![[L4-12-no-results-iterations-claude.jpg|700]]

- Click an iteration → **structure view**: Iteration 1 = **Poland factory → Czech Rep. DC → customers** (Nuremberg excluded) ⏱ 0:27:50.

![[L4-13-no-iteration1-structure-claude.jpg|700]]

> [!question] Should we choose iteration 1 just because it's the most profitable? ⏱ 0:29:48
> **No.** In NO the only KPI is **economic**: no service level, no network behaviour, no resilience (1 DC + 1 factory is not resilient – tested in SIM).
> Also economically: iteration 1 means opening 2 new facilities and closing the 2 German ones, but **initial and closure costs are not in the data** ⏱ 0:33:01; no info on **workers' skills**, agreements with Polish/Czech companies ⏱ 0:34:53.
> The **as-is** (Nuremberg → Steimelhagen → customers) is iteration 8 (or 10) with ≈ 10 M profit → too low. → Find a **balance between economic and other aspects**.

- Iteration 2: Poland factory + current German DC (no initial/closure cost for the DC). Iteration 3: Poland → Czech Rep. … ⏱ 0:36:05

![[L4-14-no-iteration-structure-view-claude.jpg|700]]

### Iteration 1 vs 4 – same facilities, −6 M profit? ⏱ 0:37:00
- Pages at the bottom: **Objective members**, **Overall stats** (all costs per iteration), **Flows details**, **Demand**, Sites…
- Overall stats ⏱ 0:39:23: revenue identical → total cost differs → the **fixed cost**: in iteration 4 ALX **opens Nuremberg too** but sends nothing from it (production cost 250 > 150) → you pay Nuremberg's fixed cost for nothing.
- Check with **Flows details** filtered by *Iteration = 4*, *From = Nuremberg* → nothing shipped ⏱ 0:42:14.
- NO gives every possible iteration; **you** must decide which one works for you.

![[L4-15-no-overall-stats-claude.jpg|700]]

![[L4-16-no-flow-details-iter4-claude.jpg|700]]

## 4.6 Capacity constraint of the Polish factory ⏱ 0:44:08
- After negotiation: Poland can produce per year **min 10,000 and max 25,000 units of each bicycle type** → *capacitated* facility.
- **Convert the scenario** ⏱ 0:46:12: right-click `PB NO Level 1` → **Convert** → name `PB NO Level 1_constrained`, scenario type **NO** → Convert (copy experiment settings / existing results).

![[L4-17-convert-scenario-dialog-claude.jpg|600]]

- Where to put the limits? Not in *Product storages* (min/max stock) but in **Production** → filter Site = Poland → columns **Min throughput = 10,000**, **Max throughput = 25,000** ⏱ 0:49:53.
- **Fill a whole column quickly**: select the cells with **Ctrl + click**, press **Space**, type the value ⏱ 0:50:28.
- Click **Check** on the scenario → "The scenario looks valid" ⏱ 0:51:41.
- Rename old result **`Result_incapacitated`**, new one **`Result_capacitated`**.
- (Or import the prepared 📁 `PB NO Level 1_Constrained.xlsx`.)

![[L4-18-production-min-max-throughput-claude.jpg|700]]

**Results** ⏱ 0:55:12: iteration 1 profit ≈ **19.34 M USD (−26 %)** → **both factories open** (Poland + Nuremberg) → Czech Rep. DC → customers. Poland can't cover everything, so the rest goes to Nuremberg.

![[L4-19-no-constrained-results-claude.jpg|700]]

- **Flows details** (iteration 1) ⏱ 0:58:48: Poland → Czech Rep. all products; Nuremberg → Czech Rep. only **tour** (2,375) and **urban** (11,500) because their demand exceeds Poland's 25,000 cap; x-cross and all terrain are fully from Poland. ALX assigns as much as possible to the cheaper factory.

![[L4-20-no-flow-details-constrained-claude.jpg|700]]

> [!warning] Flow details = basis of your inventory policy ⏱ 1:01:58
> In the work project you take the **flow details** (which product, from which source to which destination, how many) to **calculate the inventory policy**.

- **Overall stats** = most important page: all costs per iteration. **Total penalty = 0** in the first 3 iterations → demand fully satisfied: check page **Demand** (filter iteration 1 → *Satisfied* = demand, *Percentage* = 100 %) ⏱ 1:02:45.
- Without penalty costs in the input, ALX would assume you **must** satisfy all demand → iterations 4, 5, 6 (which pay penalties) wouldn't even appear ⏱ 1:03:42.

![[L4-21-no-demand-satisfaction-claude.jpg|700]]

### Why are flows 89,425 in GFA and 178,850 in NO? ⏱ 1:05:12
- NO flows are **aggregated over the echelons**: 89,425 factory→DC + 89,425 DC→customers = 178,850 (×2). With 3 levels (suppliers → factories → DCs → customers) ×3.
- GFA shows only the total amount of products. Because NO works with aggregated flows, **you can't see the real behaviour of the network**.

## 4.7 From NO to Simulation ⏱ 1:10:14
- NO doesn't show service level, lead time, resilience, sustainability → **simulation** (≈ **126 KPIs**: cost, profit, service level, resiliency…).
- Choice: iteration 1 of the capacitated scenario (2 factories + Czech DC).
- New data needed in SIM: **expected lead time**, **production time**, **sourcing policy**, **inventory policy** (Table 3 of the PDF).
- **Convert** `PB NO Level 1_constrained` → type **SIM** → `PB NO Level 1_SIM` ⏱ 1:14:01.

![[L4-22-convert-to-sim-claude.jpg|600]]

### Demand in SIM ⏱ 1:14:45
- **Expected lead time**: default **30 days** → set **5 days** (Table 3) – the lead time expected by the customer.

![[L4-23-sim-expected-lead-time-claude.jpg|700]]

- **Backorder policy** ⏱ 1:15:41:
  - **Allowed total** → if no inventory, the order stays **pending** and is shipped later (soft constraint, more flexibility).
  - **Not allowed** → no available inventory = **order cancelled**.

![[L4-24-backorder-policy-claude.jpg|700]]

### Facilities in SIM ⏱ 1:18:46
- In SIM you **cannot use "Consider"**: the facilities of the chosen NO iteration must be **Include**, the others **Exclude** (Steimelhagen excluded, Czech Rep. included; both factories included). If the network doesn't work you go back to NO and choose another iteration.
- Facility expenses: unchanged from NO.

![[L4-25-sim-dc-include-exclude-claude.jpg|700]]

- **Inventory** ⏱ 1:20:50 – "the most important parameter in simulation": when and how much to order. Linked to **pull system / Just-in-Time** (keep inventory low). Policy proposed by the case: **min-max, s = 50, S = 100** (explained in Lezione 5).

![[L4-26-sim-inventory-table-claude.jpg|700]]

- **Production** ⏱ 1:23:23: production **time** per unit (Table 3: Germany 0.1 day, Poland 0.07 day).

![[L4-27-sim-production-time-claude.jpg|700]]

**Homework given** ⏱ 1:23:41: using Table 3 of the PDF complete the SIM scenario: inventory policy (min/max), transportation time, production time, sourcing policy, transportation policy. Or import 📁 `PB SIM Level 1.xlsx`.

| Object | Inventory policy min / max | ELT (days) | Transp. time (days) | Prod. time / unit (days) | Sourcing | Transp. policy |
|---|---|---|---|---|---|---|
| Factory Germany | 50 / 100 | | 2 | 0.1 | | LTL |
| Factory Poland | 50 / 100 | | 2 | 0.07 | | LTL |
| DC Czech Rep. | 50 / 100 | | 2 | | Closest dynamic | LTL |
| Customers | | 5 | | | | |

## 4.8 First simulation run – `PB SIM Level 1` ⏱ 1:25:11
- Simulation experiment → blue square → you see the network **behaviour over time** (by month). Speed it up with the speed button.
- **Available daily inventory**, **ELT service level by products**: 100 % at the beginning, then **dropping** → the selected network doesn't work as is.

![[L4-28-sim-available-inventory-claude.jpg|600]] ![[L4-29-sim-elt-service-level-claude.jpg|600]]

- **Profit < 1 M USD** (936,291 USD) vs **19 M in NO** for the same configuration ⏱ 1:27:06.

![[L4-30-sim-financial-kpis-claude.jpg|700]]

> [!important] Huge gap NO ↔ SIM → first check the INVENTORY POLICY ⏱ 1:28:24
> s = 50 means you order only when 50 products are left → s/S too low/high = **wrong inventory policy**. Second suspect: **production time** (Production tab) → you can't fulfil the demand. (Explained in Lezione 5.)

![[L4-31-sim-inventory-minmax-50-100-claude.jpg|700]]

- The teacher will send **incomplete scenarios** as exercise (complete paths & product flows to see how parameters affect results) and will show how to **create a scenario from raw Excel data** ⏱ 1:30:11.

---

# Lezione 5 – Inventory management in SIM, improved scenario, KPIs, variation & comparison (5 Nov, morning – video)
🎥 `anylogistic_lessons/Video recording Lecture 5 NOV5-26 STEM.mp4` (1h21)
📁 `PB SIM Level 1.xlsx`, [[lab/LECTURE 3-4 (OCT22-26)-20261022/Case 1 Level 1/PB SIM Level 1_Improved.xlsx|PB SIM Level 1_Improved.xlsx]]

## 5.1 Recap ⏱ 0:00:13
Case 1: NO → 2 factories (Nuremberg already open + Poland) + new DC in Czech Rep., current German DC closed (opening/closure costs not considered). Tested in SIM → KPIs not satisfying: profit dropped a lot, service level ≈ 0 → the problem comes from **inventory management**.

## 5.2 The 3 key policies of simulation ⏱ 0:03:02
1. **Inventory policy**
2. **Shipping policy** – which vehicles/trucks and which policy: **FTL** or **LTL**.
3. **Sourcing policy** – if there are 2 possible sources (e.g. 2 DCs), which one: **closest**, **fastest**, **cheapest**…

![[L5-01-inventory-management-drawing-claude.jpg|700]]

## 5.3 Inventory management – brief theory ⏱ 0:04:41
(Full formulas in Prof. Battini's course; here just what is needed for ALX.)
- Goal: manage stock in warehouses to **prevent stock-out** situations, **without** keeping too much inventory (holding inventory costs money).
- **Safety stock (SS)**: margin of inventory to prevent stock-outs. It does **not always guarantee** no stock-out (demand and disruptions are not deterministic), but it helps keep a **higher service level** ⏱ 0:06:04.
- Inventory management answers **2 questions** ⏱ 0:07:32:
  1. **When should we order / replenish?** → **Reorder point**: $ROP = \bar d \times L + SS$ (average daily demand × lead time + safety stock). Example: supermarket shelves – when the operator sees 2 bottles left it's the signal to refill.
  2. **How much / how many should we order (send) or produce?** → **EOQ** (economic order quantity, for final products) $EOQ=\sqrt{\dfrac{2\cdot D_{annual}\cdot C_{order}}{C_{holding}}}$, or **EPQ** (economic production quantity, when you produce from raw material with a BOM).

![[L5-02-rop-eoq-formulas-claude.jpg|600]]

- In the saw-tooth graph: inventory is consumed → at the **ROP** level you reorder → during the lead time you consume the safety stock → you receive the quantity (EOQ / up to the **target level**) ⏱ 0:11:41.
- The drawing is deterministic (fixed interval, fixed demand). **Reality** is irregular: different lead times, **stock-outs** happen even with a "perfect" policy in your work project – **minimize them** ⏱ 0:13:38.
- 3 safety-stock formulas depending on whether **demand**, **lead time** or **both** vary (Battini's course).

> [!important] ⏱ 0:12:56
> If the **service level drops** in your work project, check shipping and sourcing policies too, but the policy with the **most significant impact on service level is the inventory policy** (reorder time and inventory level).

## 5.4 Inventory policy types in ALX ⏱ 0:17:08
Table **Inventory** → *Policy type*:

![[L5-03-inventory-policy-types-claude.jpg|700]]

| Policy | Notes from the lesson |
|---|---|
| **Min-max (s, S)** | s = minimum level = **when to reorder** (≈ ROP = d̄·L + SS); S = maximum = **target level** to replenish to |
| **Min-max with safety stock** | used when there is **variability** (stochastic demand/lead time). With deterministic demand (bicycle case: always 15, 16… "Value") you usually don't need SS; in reality you do |
| **RQ policy** | R ≈ ROP (reorder point), Q ≈ EOQ (order quantity) |
| **Order on demand** | replenish exactly what was ordered (10 orders received → replenish 10); works well only when you **know the demand** |
| Cross-docking, No replenishment, Regular policy (+ variants) | listed in the drop-down |
| **Unlimited inventory** | ⚠️ see below |

> [!danger] Never use "Unlimited inventory" in the work project ⏱ 0:20:18
> The software assumes facilities always have enough stock → service level perfect, but **factories don't need to produce → production cost is not counted** → profit very high and **not true**. "Once I see the profit I understand you used unlimited inventory."

![[L5-04-unlimited-inventory-option-claude.jpg|600]]

> [!warning] Inventory policy in the work project ⏱ 0:24:04
> One of the **most important parts** of the project: extract the data from the **product flows of the NO** and **calculate the policy yourself** (ALX could suggest numbers – don't use them).

## 5.5 Shipping & sourcing ⏱ 0:24:43
- **Shipping** table = like product flows in NO: from which sources to which destinations, which truck, **policy type** (FTL / LTL; other types exist but for this course only FTL/LTL).
- **Sourcing** table: delivery destination, sources, product, **type**: Cheapest (dynamic / fixed source), **Closest (dynamic / fixed source)**, Fastest (dynamic / fixed source), First (fixed source)… In the project you are **free to choose** the policy that gives better results.

![[L5-06-sourcing-policy-types-claude.jpg|700]]

- **Dynamic vs fixed** ⏱ 0:26:21 (e.g. *Closest*):
  - **Fixed** → always the same (closest) DC; if DC1 has no product, it can't use DC2 → service level goes down (like a hard constraint).
  - **Dynamic** → first DC1 (closest); if it has no available inventory, the remaining products are assigned to DC2. Usually better.
- Case 1: DCs sourced from **[Factories]** and customers from **[DCs]**, both *Closest (dynamic source)*.

## 5.6 Other SIM tables – recap ⏱ 0:28:18
- **Demand**: **backorder policy** exists only in SIM. *Not allowed* = hard constraint → no inventory = order **cancelled** = no revenue (not recommended); *Allowed total* = orders **pending** until stock is available ⏱ 0:29:43.
- **DCs**: in SIM use **Include** (and *Exclude*), **never Consider**: in NO you search the best iteration (Consider = boolean decision), in SIM you **test that specific network** (Czech Rep. DC + 2 factories). Not necessary to set *initially open* ⏱ 0:31:21.
- Facility expenses, groups, locations, paths, processing cost: as in NO.
- **Production** ⏱ 0:33:39: new in SIM = **production time** (input data): e.g. 0.1 day to produce one bicycle → type *Simple make policy*, time per unit. **Only factories** go in Production (not the Czech DC!).

![[L5-07-production-time-dialog-claude.jpg|600]]

- Products (price, cost), shipping, sourcing, unit conversions, vehicle types.

## 5.7 Why `PB SIM Level 1` fails ⏱ 0:35:56
Statistics: profit **936,291 USD** (< 1 M) vs **19 M** in NO; service level only 100 % on the first day then ≈ 0; **lead time** up to **280 days** for some products.

![[L5-08-sim-statistics-low-profit-claude.jpg|600]] ![[L5-09-lead-time-chart-claude.jpg|600]]

- Facility costs are the same as in NO → the problem is the **inventory policy**: it was defined for **all products** with the **same values (50/100) for all facilities**, but demand per product is very different (x-cross total 30/day ≠ urban…) ⏱ 0:39:54.
- → define a **different policy for each product and each facility**, and adjust the **production time** (it was too long: not enough bikes per day).

**Revised parameters (Table 4 of the PDF)** ⏱ 0:41:01 – min = daily demand of the product (e.g. x-cross 30), max = 2 × min (just an assumption here; in the project use the formulas):

| Object | Product | Min | Max | ELT | Transp. time | Prod. time/unit (days) | Sourcing | Transp. |
|---|---|---|---|---|---|---|---|---|
| Factory Germany | x-cross | 30 | 60 | 5 | 2 | 0.025 | | LTL |
| | urban | 100 | 200 | | | 0.0067 | | |
| | all terrain | 40 | 80 | | | 0.016 | | |
| | tour | 75 | 150 | | | 0.01 | | |
| Factory Poland | x-cross | 30 | 60 | 5 | 2 | 0.05 | | LTL |
| | urban | 100 | 200 | | | 0.02 | | |
| | all terrain | 40 | 80 | | | 0.05 | | |
| | tour | 75 | 150 | | | 0.02 | | |
| DC Czech Rep. | x-cross | 60 | 120 | | 2 | | Closest dynamic | LTL |
| | urban | 200 | 400 | | | | | |
| | all terrain | 80 | 160 | | | | | |
| | tour | 150 | 300 | | | | | |
| Customers | | | | 5 | | | Closest dynamic | |

![[L5-10-table4-improved-parameters-claude.jpg|500]]

## 5.8 Building the improved scenario ⏱ 0:43:19
- Right-click the scenario → **Convert** → name e.g. `PB SIM Level_revised` / *improved*, type **SIM**.
- ⚠️ **Save your scenarios**: if you delete a scenario from ALX it is gone. **Right-click → Export** to save the Excel on your PC (do it for the work project!) ⏱ 0:44:06.

![[L5-11-convert-revised-success-claude.jpg|600]]

- In *Inventory*: one row **per facility per product** (Czech Rep. × 4 products, Nuremberg × 4, Poland × 4), policy *Min-max*, set s and S in the parameters dialog (e.g. Czech Rep. all terrain 80/160, urban 200/400, tour 150/300, x-cross 60/120) ⏱ 0:45:17.

![[L5-12-inventory-edit-min-max-claude.jpg|600]]

- In *Production*: replace 0.1 / 0.07 with the new times ⏱ 0:49:09.
- Then import the prepared 📁 `PB SIM Level 1_Improved.xlsx` ⏱ 0:49:43.

> [!question] Student question ⏱ 0:50:46
> "In NO Nuremberg produced only tour & urban (Poland capacity limit): why define policies for all 4 products in Nuremberg?" → Here no capacity limitation was put in SIM. **In the work project you take the data from the NO product flows and must consider these aspects.**

## 5.9 Results of the improved scenario ⏱ 0:52:06
- **ELT service level = 100 %** (all products shipped within the expected lead time; "in reality you won't see it").
- **Profit ≈ 13.4 M USD** (13,407,086), revenue 44,623,075, production cost 20,628,187.5, total cost 31,215,988.8.

![[L5-13-improved-financial-kpis-claude.jpg|600]]

> [!question] Why 13 M in SIM vs 19 M in NO? ⏱ 0:53:21
> No delays (service level 100 %). The gap comes from **inventory**: to keep min/max levels (and service level) you **produce more than needed**; NO produces **exactly** the demand. Check NO → *Overall stats* → iteration 1: production cost ≈ **14.8 M** vs **20.6 M** in SIM → ≈ 6 M = exactly the profit gap.
> **In the work project it's normal to see differences between NO and SIM, but you must justify why and where they come from.**

![[L5-14-no-overall-stats-production-claude.jpg|600]]

## 5.10 Adding KPIs to the dashboard ⏱ 0:57:02
- ALX has **126 KPIs**. Simulation experiment → **Add KPI metrics** (square) or better **Add new chart** → *Add statistics* → categories: Finances, Distance, Products, **Ratio**, Time, Vehicles, Orders, Cash to Serve, CO₂ Emissions, Other, Preset.
- E.g. Ratio → **Service Level by Products** (also ELT service level by orders/products/revenue, production line utilization, service level by orders/revenue…).

![[L5-15-sim-dashboard-add-kpi-claude.jpg|600]] ![[L5-16-new-chart-statistics-ratio-claude.jpg|600]]

- Chart **settings** (gear): chart type **Table / Line / Histogram / Bar / B-M-W line**; show data **Daily / Accumulated**; filters on object, period, product, source.
- Use a **line** for ratios/service level → you see it **over time** (a table only gives an average, e.g. "90 %" without knowing when) ⏱ 0:59:00.

![[L5-17-chart-type-settings-claude.jpg|500]]

- **Available inventory** now oscillates between min and max as defined, with replenishment every ~2 days. In the work project you'll see high fluctuations: normal, but manage them to get the best service level and profit ⏱ 1:00:14.

![[L5-18-improved-available-inventory-claude.jpg|600]]

> [!tip] After the simulation ⏱ 1:01:22
> As a consultant: write **recommendations / managerial insights** – why the scenario works, **strengths and weaknesses** (e.g. only 1 DC: if it closes there is no alternative). Resiliency and CO₂ still to be tested. Then **verify and validate** the model.

## 5.11 Variation experiment (sensitivity analysis) ⏱ 1:02:23
- Like sensitivity analysis in operations research (changing the right-hand side), without maths: how does the network behave if a parameter changes?
- Simulation experiments list: **Variation experiment**, **Comparison experiment** (Last mile optimization is not part of the course).
- Variation experiment → **Settings → Add variable parameter**: object type **Demand** (could also be inventory, locations…), object = *Demand for customer Cologne, product bicycle "urban"*, parameter **Quantity**, variation **Number range**: **min 50, max 170, step 40** → results at **50, 90, 130, 170** (a step of 10 would produce too many results).

![[L5-19-variation-add-parameter-claude.jpg|600]] ![[L5-20-variation-number-range-claude.jpg|500]]

- **Experiment settings** → statistics configuration: search & enable the KPIs (profit, total cost, production cost, **service level by products**…). Add **only the KPIs that really matter**, otherwise the results table becomes a mess.
- ELT service level = expected-lead-time service level; all service levels = successful shipments / all shipments ⏱ 1:09:32.

![[L5-21-variation-experiment-settings-kpi-claude.jpg|600]]

- **Results** ⏱ 1:11:18: table with statistic name and **min / max / mean** columns. Service level by products: **1.0 (50) → 0.721 (90) → 0.448 (130) → 0.399 (170)**; profit increases (more demand, more revenue) but products are not shipped on time.

![[L5-22-variation-results-service-level-claude.jpg|600]]

> [!summary] Insight ⏱ 1:12:26
> The network is **sensitive to demand variation**: production capacity is not enough → increase capacity and revise the inventory policy. Managerial insight: "this network is useful but not for higher demand".

## 5.12 Comparison experiment ⏱ 1:17:20
- Not meaningful for Case 1 (only one network), but **very important for the work project**: you develop several networks and compare them – one best for finance (profit), one for service level, one for environment (CO₂), one more resilient.
- Comparison experiment → **Settings** → select the SIM scenarios to compare (not all) → add KPIs → run. Suggested KPIs: **profit, CO₂ emissions, service level** and other important ones. Take a screenshot to show which scenario has which priority ⏱ 1:18:18.

![[L5-23-comparison-experiment-claude.jpg|600]]

---

# Lezione 6 – Creating a scenario from raw Excel data + Case 2 Berlin Brewery (GFA, NO, SIM setup) (5 Nov, afternoon – video)
🎥 `anylogistic_lessons/Video recording Lecture 6 NOV5-26 STEM.mp4` (1h38)
📁 [[lab/LECTURE 3-4 (OCT22-26)-20261022/Case 1 Level 1/Exercise_01.xlsx|Exercise_01.xlsx]] · [[lab/LECTURE 5-6 (NOV5-26)-20261105/Case study 2 Level 2.pdf|Case study 2 Level 2.pdf]] · `BR GFA Solution.xlsx`, `BR NO Level 1.xlsx`, `BR NO Level Solution.xlsx`, `BR SIM Level 1.xlsx`, `BR SIM Solution.xlsx`

## 6.1 Variation experiment – clean result ⏱ 0:00:28
With only one variable parameter you get exactly **4 iterations** (step 40): quantity 50 → service level by products 100 %, then decreasing as demand increases; profit increases (more demand received) but production capacity is not enough (→ read it from the service level). Tabs in SIM: Simulation, **Variation**, **Comparison**.

![[L6-01-variation-results-recap-claude.jpg|600]]

## 6.2 From raw data to the ALX format ⏱ 0:02:53
- 📁 `Exercise_01.xlsx` (sheet *Demand_location_period*) = **raw data**: customer, bicycle type, demand per day + name/lat/long + basic period 1/1/2025–12/31/2025. It **cannot be imported directly**: an ALX Excel has its own format (sheets Agenda, Scenario settings, Customers, Demand, Locations, Periods, Products…, icons, IDs).
- You need Excel skills: **PIVOT** and **VLOOKUP** (links in Lezione 1).
- **Work project**: raw data are given every year; this year the **GFA will be given prepared**, while for the **inventory policy you must do everything** (a separate video will be recorded for it); raw data also for groups that want to work on them ⏱ 0:06:16 / 0:24:30.

![[L6-02-exercise01-raw-data-claude.jpg|600]]

### Procedure ⏱ 0:07:48
1. **+ → Create scenario** (not import) → name (e.g. `test`), type **GFA** (or NO/SIM), **start/end date** of the period (can be revised later).

![[L6-03-create-scenario-dialog-claude.jpg|500]]

2. Copy-paste row by row is impossible (thousands of demand rows in the project) → instead **add 1–2 dummy rows** in each needed table just to get the format: 2 customers (names; the location may end up in the sea – doesn't matter), 2 demand rows (*Periodic demand* here – **Historic demand in the work project**), 2 products (e.g. urban, tour) ⏱ 0:09:38.

![[L6-04-test-scenario-customers-claude.jpg|600]]

3. **Export** the scenario (right-click → Export) and open the exported Excel ⏱ 0:12:39.

![[L6-05-export-test-scenario-claude.jpg|600]]

4. **Paste your data into the exported file respecting the format** ⏱ 0:14:36:
   - **Customers** sheet: IDs (`Customer 1…4`, generated by ALX – keep the same style/numbers as in your file), Name (paste **as values** so the format doesn't change), Type = `Customer`, Inclusion type = `Include`, Icon = same number (e.g. 821).

![[L6-06-paste-customers-excel-claude.jpg|600]]

   - **Location** column must be `<Name> Location` → use `=CONCAT(B2," ","Location")` ⏱ 0:17:20.

![[L6-07-concat-location-formula-claude.jpg|600]]

   - **Locations** sheet ⏱ 0:21:02: ID and Name = the same location names as in Customers (copy-paste as values) → **they must match exactly** (a small difference in capital letters or spaces and ALX can't connect customer and location) + **Latitude, Longitude** from your data; Autofill coordinates = FALSE.

![[L6-08-locations-lat-long-claude.jpg|600]]

   - **Products** sheet: paste the exact product names (x-cross, urban, all terrain, tour); unit (m³ by default → change if needed) ⏱ 0:23:17.

![[L6-09-products-sheet-claude.jpg|500]]

   - **Demand** sheet ⏱ 0:24:47 – usually the hardest (especially with historic demand): IDs `Demand 1…16` (16 rows = 4 customers × 4 products), paste customer + product columns, then fill all rows with the same values: Periodic demand, *First occurrence = First day*, *Order interval, days = Value 1*, *Quantity = Value* + the daily quantity (Col 10), time period (All periods), Include.

![[L6-10-demand-sheet-filled-claude.jpg|600]]

5. **Import** the file ⏱ 0:28:49 (close the Excel first – an open file gives errors). First attempt → warnings *"Cannot process value … CONCAT(…)"* = the location formula was not read.

![[L6-11-import-warnings-formulas-claude.jpg|600]]

6. Re-import with **Advanced settings → "Scenario contains formulas"** ✅ → imported without errors; running GFA with 1 DC gives the same German DC as in Lezione 3 ⏱ 0:30:10.

![[L6-12-import-contains-formulas-claude.jpg|500]] ![[L6-13-test3-imported-ok-claude.jpg|500]]

> [!note]
> Without a license (PLE) data must be updated **manually**; with a license ALX can be connected through an **API** and updated automatically ⏱ 0:14:53. The exported Excel and the scenario in ALX are not linked: changing a value in ALX doesn't change your Excel until you export again ⏱ 0:45:56.

## 6.3 Summary GFA → NO → SIM ⏱ 0:35:19
![[L6-14-summary-gfa-no-sim-claude.jpg|600]]

| | GFA | NO | SIM |
|---|---|---|---|
| Behind it | gravity analysis (center of gravity) | MILP (CPLEX) | dynamic simulation (AnyLogic) |
| Objective | **min transportation flows/cost** (demand × distance) | **max profit** (min costs) | test the network on many KPIs (service level, lead time, CO₂, resiliency, profit…) |
| Data | products, demand, customers, locations | + **storage**, facility costs, processing costs, production costs, **paths**, **product flows** | + **inventory**, **shipping**, **sourcing** policies, production time (and more you'll discover) |
| Output | possible locations (not 100 % usable) | iterations from most to least profitable; flows **aggregated** among levels; no behaviour/service level/resilience | behaviour over time, 126 KPIs |

> [!warning] Don't forget in NO ⏱ 0:40:04
> **Paths**, **product flows**, **storages** and **production**: if one is missing the network doesn't work.

- ALX helps you design the best network on several KPIs, test it (also resiliency) and give **recommendations as a consultant**. Internal problems (production line, assembly line) → extend to **AnyLogic** (e.g. for a thesis) ⏱ 0:44:07.
- Close unused scenario tabs to keep the screen clean; scenarios are deleted only if you delete the **project** ⏱ 0:45:14.

## 6.4 Case 2 – Berlin Brewery ⏱ 0:46:36
Food & beverage networks are more complex: many **BOMs / ingredients**, vehicles with **fridges**, very important **service level**.
- Berlin craft-beer brand: **1 factory + 1 DC in Berlin**, **50 customers in 8 countries** (Germany, Switzerland, Austria, Sweden, Norway, France, Italy, Spain). Wants to **expand** the market/distribution network.
- **3 suppliers** of ingredients: crates (near **Nuremberg**), hops (**Koblenz**), malt (near **Dresden**) → factory → DCs → customers. Ingredients arrive **JIT / on demand**.
- **BOM** (also in your work project, since you'll have suppliers): product "Beer" = **1 crate = 20 bottles** (0.33 l each).

| BOM | Usage per crate | Measure in ALX | Cost per crate ($) |
|---|---|---|---|
| Hops | 7.92 g | 1 piece | 0.32 |
| Malt | 1390 g | 1 piece | 2.22 |
| Crate | 20 bottles | 1 piece | 6.00 |
| Production processing costs | | | 1.46 |
| **Total** | | | **10.00** |

![[L6-16-br-bom-table-claude.jpg|500]]

- **Unit conversions** are more complex (grams, pieces, pallets): 1 pallet = 40 crates = 800 bottles; hops/malt in 1 kg packages, 1 pallet = 40 packages ⏱ 0:50:20. (Costs in the PDF are some years old → cheap.)
- Other data from the PDF: price per crate **$60**; truck 80 km/h, **1,320 crates = 33 pallets**; carrying cost $0.005/crate/day ($0.2/pallet); transport factory→DCs $0.00175 per km/crate ($0.07/pallet); outbound at factory $0.66/pallet, inbound $40/pallet; factory maintenance $2,630/day; orders every 7 days.
- **Two periods** ⏱ 0:51:08: **Summer** 01/05–31/10 (demand coefficient **1.2** → +20 %) and **Winter** 01/11–30/04 (1.0).

## 6.5 GFA – `BR GFA Solution` ⏱ 0:51:41
- 50 customers on the map, periods summer/winter, **product groups** (Beer = final product; Ingredients = crate, hops, malt), unit conversions.

![[L6-17-br-gfa-periods-claude.jpg|600]]

- GFA experiment → Settings → **Number of sites = 7** (only customers are present, so sites are found from customers' locations) → run → e.g. the Italian DC serves only 3 customers. Flow 260,364 m³, flow cost estimation **37,187,015.579 m³·km**. Rename result `Result_7DCs` ⏱ 0:55:20.

![[L6-18-br-gfa-7dc-claude.jpg|600]]

- With **2 DCs**: distance +104 %, flow cost **99,490,415 (+167.5 %)** → fewer DCs = longer distances. But **7 DCs is not the answer**: GFA has no facility, processing or production costs (in use: only products, locations, unit conversions…) ⏱ 0:57:20.

![[L6-19-br-gfa-2dc-claude.jpg|600]]

- Demand: **periodic, order interval 7 days (weekly)** (Case 1 was daily), different quantity per period (+20 % in summer); first occurrence *Next day after interval* ⏱ 0:58:58.

![[L6-20-br-demand-weekly-claude.jpg|600]]

PDF answers: max distance from a DC to a customer 603.39 km (Marseille); total cost $37,187,015.579; all demand satisfied; not considered: fixed facility, inventory holding and processing costs.

## 6.6 NO – `BR NO Level 1` (incomplete on purpose) ⏱ 1:00:33
- DCs from GFA (some moved by the SC manager for availability of warehouses to rent, construction/fixed costs, infrastructure, future demand): Spain, Sweden, Austria, Bochum, Switzerland, Italy → **Consider**; **DC Berlin** (as-is) → initially open, **Include**. Suppliers = green icons ⏱ 1:01:07.

![[L6-21-br-no-dcs-consider-claude.jpg|600]]

**Cost structure per site (Table 3 of the PDF)**

| Site | Other costs / day | Carrying / day / pallet | Outbound / pallet | Inbound / pallet | Transport / pallet |
|---|---|---|---|---|---|
| DC Austria | 120 | 0.20 | 0.66 | 1.00 | 0.07 |
| DC Spain | 70 | 0.10 | 0.33 | 0.5 | 0.035 |
| DC Sweden | 310 | 0.40 | 1.02 | 1.55 | 0.108 |
| DC Bochum | 120 | 0.20 | 0.68 | 1.07 | 0.07 |
| DC Switzerland | 146 | 0.20 | 0.96 | 1.46 | 0.102 |
| DC Italy | 90 | 0.20 | 0.33 | 0.5 | 0.05 |
| DC Berlin | 100 | 0.20 | 0.66 | 1.00 | 0.07 |
| Factory Berlin | 2,630 | 0.005 | 0.66 (beer) | 40.00 (ingredients) | 0.07 |

DC inventory capacity min 5,800 – max 11,600 crates (one-week range); brewery max 10,000, at least 5,000 crates. Production cost $1.46, revenue $60.

- **Run → negative profit (−1.45 bn), Flows amount N/A, revenue 0, no customers on the map** → information is missing ⏱ 1:02:41. "Even by the type of output you can understand which information is missing."

![[L6-22-br-no-negative-profit-claude.jpg|600]]

### Missing piece 1 – Product flows ⏱ 1:05:46
- Paths were already there (from Factory Berlin → [DC], [Suppliers] → Factory Berlin *fixed delivery*, each DC → [Customer] with its own cost) but **without product flows ALX doesn't know which product goes from which facility to which destination**.

![[L6-23-br-no-paths-claude.jpg|600]]

- Add 3 rows ⏱ 1:07:13:
  1. **[Suppliers] → Factory Berlin**, product **[Ingredients]** (raw materials: hops, malt, crates – *not* beer!), vehicle Truck. (Type "Berlin" in the destination to find *Factory Berlin*.)
  2. **Factory Berlin → [DC]**, product **Beer**.
  3. **[DC] → [Customer]**, product **Beer**.
- **Product groups**: group your ingredients (row `Ingredients` → products Crate, Hops, Malt) – do it in the project too ⏱ 1:09:51.

![[L6-24-br-product-flow-suppliers-claude.jpg|500]] ![[L6-25-br-product-groups-ingredients-claude.jpg|500]]

![[L6-26-br-product-flows-3rows-claude.jpg|600]]

> [!warning] Vehicles in the work project ⏱ 1:11:21
> In paths and product flows you'll have **different vehicle types** in different parts (e.g. truck 1 suppliers→factory, truck 2 factory→DC): choose the correct one, each has its **own capacity and speed**.

### Missing piece 2 – Production ⏱ 1:13:01
- Production table empty → the factory produces nothing. Add: site = **Factory Berlin** only (only sites in the Factories tab; not "All sites"), product = **Beer** (the factory doesn't produce hops/malt), **BOM = BOM Beer**, production cost **1.46** ⏱ 1:14:25.
- **BOM** table: `BOM Beer` → end product Beer, quantity 1, components **Crate 1, Hops 1, Malt 1** (1 piece each thanks to the unit conversion). If beer is not linked to the BOM, ALX doesn't understand that beer depends on these ingredients ⏱ 1:15:10.

![[L6-27-br-production-site-claude.jpg|500]] ![[L6-28-br-bom-beer-claude.jpg|500]]

![[L6-29-br-production-bom-cost-claude.jpg|600]]

- Periods: summer (coefficient 1.2) and winter; the period group is extra and can be removed ⏱ 1:17:38.

### Missing piece 3 – Product storages ⏱ 1:18:44
- Without storage ALX assumes nothing is stored/on hand. Add: **Factory Berlin → [Ingredients] and Beer** (the factory stores both), **DCs → Beer** only ⏱ 1:19:11.
- After that the structure view is connected: **Suppliers → Factory Berlin → DC → Customers** and NO works ⏱ 1:20:28.

![[L6-30-br-product-storages-claude.jpg|600]]

![[L6-31-br-no-structure-connected-claude.jpg|600]]

> [!summary] Only 3 things were missing: **storage, product flow, production** ⏱ 1:21:03
> The other challenging part is **paths** (given here): source → destination and cost calculation (*product & distance-based*). Path costs are **input data** given to you, not assumptions.

### Paths with different costs ⏱ 1:21:58
Why one row per DC → customers instead of `[DC] → [Customer]`? Because **costs are different** (e.g. DC Switzerland 0.102, Sweden 0.108, Spain 0.035, Italy 0.05 × product). Group only if all costs are the same. **CO₂ emissions** for the project also go in the **paths** (CO₂ calculation param) ⏱ 1:22:47.

![[L6-33-br-paths-different-costs-claude.jpg|600]]

### Results ⏱ 1:23:08
- Iteration 1 (profit **12,425,609 USD**, flows 1,452,334 pcs, revenue 17,428,008 USD) = **as-is**: factory + DC in Berlin → but the company wants to **expand** → not chosen.
- Iteration 2 (12,413,398 USD) = **Berlin + Spain**; iteration 3 = Berlin + Italy; iteration 4 = same as 1 but another facility opened without flows (like Case 1).
- Decision: **DC Berlin + DC Spain** → to be tested in simulation (small profit difference, more flexibility & resilience). *(PDF: "fifth-best alternative", profit 12,276,719.782 – numbers differ slightly from the class run.)*

![[L6-32-br-no-results-claude.jpg|600]]

![[L6-34-br-iteration1-asis-claude.jpg|500]] ![[L6-35-br-iteration2-spain-claude.jpg|500]]

## 6.7 SIM – `BR SIM Level 1` (homework) ⏱ 1:26:03
- DC Berlin and DC Spain: **initially open + Include** (we test exactly this network). Demand: backorder policy *Allowed total*, expected lead time 5 days. Initial/closure costs not considered. Production present but **production time = 0** ⏱ 1:28:24.
- **Missing**: **inventory policy**, **sourcing**, **shipping** → fill them from **Table 4 (page 38 of the PDF)**; otherwise import 📁 `BR SIM Solution.xlsx` (ignore the warning "Post Processor was skipped…").

![[L6-36-br-sim-level1-claude.jpg|600]]

| Object | Inventory policy min | max | Sourcing | Transport |
|---|---|---|---|---|
| Factory Germany (beer) | 2000 | 5000 | Closest dynamic | LTL |
| Factory Germany (ingredients) | **On demand** | | | LTL |
| DC Germany | 1800 | 11600 | Closest dynamic | LTL |
| DC Spain | 1800 | 11600 | Closest dynamic | LTL |
| Customers | | | Closest dynamic | LTL |

![[L6-37-br-table4-sim-params-claude.jpg|500]]

- Inventory ⏱ 1:30:23: row Factory Berlin – Beer – Min-max s = 2000, S = 5000; DC Berlin – Beer – 1800/11600; DC Spain – Beer – 1800/11600; Factory Berlin – **[Ingredients] – Order on demand** (ingredients arrive based on the orders the factory sends to the suppliers).

![[L6-38-br-inventory-factory-minmax-claude.jpg|500]] ![[L6-39-br-inventory-order-on-demand-claude.jpg|500]]

- Add some KPIs and look at the results. Next lesson: results, **resiliency**, **disruptions** (closing a DC), then the **work project presentation** ⏱ 1:34:07.
- Student question: shouldn't the factory have a capacity? → yes, with capacity problems you must define it; it will be done next week ⏱ 1:36:32.
- Problems with group members for the work project → write directly to the teacher (niloofar.katiraee@unipd.it) ⏱ 1:35:49.

> [!note] Continues in Lezione 7–8
> Completion of the SIM (shipping & sourcing), risk analysis with events (2-month closure of DC Berlin, 1 DC vs 2 DCs), comparison and variation of Case 2.

---

# Lezione 7 – Case 2: completing the SIM (shipping & sourcing), NO vs SIM, resilience with events (19 Nov, morning – video)
🎥 `anylogistic_lessons/Video recording Lecture 7 NOV19-26 STEM.mp4` (1h24)
📁 `BR NO Level 1.xlsx`, `BR NO Level Solution.xlsx`, `BR SIM Level 1.xlsx`, `BR SIM Solution.xlsx`, [[lab/LECTURE 5-6 (NOV5-26)-20261105/BR SIM Level 1 Disruption Risk with 1 DC.xlsx|BR SIM Level 1 Disruption Risk with 1 DC.xlsx]], [[lab/LECTURE 5-6 (NOV5-26)-20261105/BR SIM Level 1 Disruption Risk 2 DC.xlsx|BR SIM Level 1 Disruption Risk 2 DC.xlsx]]

## 7.1 Organisation of the work project ⏱ 0:00:14
- Groups: no groups of 2 accepted → the online team of 2 is merged into teams of 3 (team 2 confirmed).
- **Work project presentation: 26 November** (in Prof. Battini's hours; all data and material given then). Come in person if possible.
- Teacher present on **10 and 17 December** (from 10:00, ~4 h) for questions; in between → online or by email.
- **Deadline: 15 January** – never extended. Another online Zoom Q&A after 6 January ⏱ 0:08:21.

## 7.2 Recap Case 2 ⏱ 0:10:52
GFA → candidate DCs; NO (`BR NO Level 1`, completed with product storage, production…) → iterations from ≈ 12 M down; chosen iteration = **DC Berlin + DC Spain**. Homework: complete `BR SIM Level 1` (a student completing it in class gets **+1 extra point** on the work project ⏱ 0:13:03).

## 7.3 What is missing in `BR SIM Level 1` ⏱ 0:14:03
- Running it gives a warning: *"No sourcing found for BOM component Malt for site Factory…"*.
- Checklist for any SIM (student's answer): **inventory ✓**, **shipping ✗**, **sourcing ✗** (+ production time).

![[L7-01-br-sim-warning-no-sourcing-claude.jpg|600]]

- "Without sourcing and shipping the echelons are not connected: how can the software know from which source to which destination which product is shipped?" ⏱ 0:19:04

![[L7-02-br-shipping-empty-claude.jpg|600]]

### Shipping ⏱ 0:26:02
Like *paths/product flows* in NO, the paths are already there; shipping must define:

| Sources | Destinations | Product | Vehicle | Type |
|---|---|---|---|---|
| [DC] | [Customer] | Beer | Truck | LTL |
| Factory Berlin | [DC] | Beer | Truck | LTL |
| [Suppliers] | Factory Berlin | [Ingredients] | Truck | LTL |

- Other columns: parameters *Partial delivery*, priority *FIFO*.
- **Work project**: you'll have **2 vehicle types** → choose the right one for each path/shipping ⏱ 0:28:13.
- **Days of week** ⏱ 0:28:45 (not needed for the case, **needed in the project**): e.g. only Mon–Fri. It impacts lead time: with 5 days lead time, an order placed on Monday arrives the next Monday; without it ALX would deliver on Saturday.
- **Start / end time**: not input data; usually 8 a.m.–5 p.m. (8–9 h/day). Less impactful than the days of week ⏱ 0:30:03.

![[L7-03-shipping-days-of-week-claude.jpg|700]]

### Sourcing – the real error ⏱ 0:31:08
- The customers' row was **[Customer] ← Factory Berlin** → the profit was **negative** because **no products arrived to customers**. Correct: customers are sourced by **[DC]**.
- Check the *Sources* drop-down: by default it may be **All sites** → select **only the echelon you want** (don't source customers from all sites) ⏱ 0:32:27.

![[L7-04-sourcing-wrong-factory-customer-claude.jpg|600]] ![[L7-05-sourcing-fixed-dc-customer-claude.jpg|600]]

| Delivery destination | Sources | Product | Type |
|---|---|---|---|
| [DC] | Factory Berlin | Beer | Closest |
| Factory Berlin | [Suppliers] | [Ingredients] | Closest |
| [Customer] | [DC] | Beer | Closest |

> [!tip] Negative / strange results in SIM ⏱ 0:31:45
> Look first at **paths, sourcing and shipping** (and inventory policy).

- **Sourcing policies** ⏱ 0:32:57: Cheapest / Closest / Fastest (dynamic sources or fixed source), First (fixed source) – free choice in the project.
  - **Fixed source**: if DC Berlin can't serve the customer, the customer **cannot** be assigned to DC Spain. **Dynamic**: it can → less of a hard constraint, the teacher suggests dynamic (but it depends on the company's strategy).
  - **Closest** = ship from the closest DC (e.g. Berlin for a German customer). **Cheapest** = not only transport: also **facility costs** of the DC → e.g. Spain (cheaper fixed costs) could serve German customers ⏱ 0:35:57.

![[L7-06-sourcing-policy-list-claude.jpg|600]]

## 7.4 Results of the completed SIM ⏱ 0:37:46
- Speed up by dragging the speed slider to max. Profit positive (**≈ 12.06 M USD**).
- Service level: high at the beginning then slightly decreasing; to see the **exact value** set the chart (gear) to **Table** → **0.963 = 96.3 %** of products shipped successfully on time ("100 % in reality is not meaningful") ⏱ 0:38:56.

![[L7-07-br-sim-results-positive-claude.jpg|600]] ![[L7-08-br-service-level-table-claude.jpg|500]]

- Exercise: **Add new chart → Add statistics → Finances → Production cost, Transportation cost** (also inventory carrying cost…) as tables ⏱ 0:42:06.

![[L7-09-add-statistics-finance-claude.jpg|600]]

## 7.5 Why NO and SIM profits differ ⏱ 0:43:17
- NO (chosen iteration "5", ≈ 12.28 M) vs SIM: ≈ 100–200 k USD less.
- NO uses **exact demand** (setting *demand variation type*) → produces/ships **exactly** the demand in the Demand table (sum ≈ 10,014 per order cycle in the Excel). SIM adds the **inventory policy** (safety stock, min/max) → **produces more** to prevent stock-outs → higher production cost → lower profit ⏱ 0:46:08.
- 95–100 % = up to 5 % less is allowed; 100–105 % = up to 5 % more is allowed ⏱ 0:51:33.

![[L7-10-br-demand-excel-claude.jpg|600]]

> [!warning] Work project ⏱ 0:48:48
> A **small** difference NO ↔ SIM is normal; a **huge** difference means something is wrong (e.g. over-production, too much initial stock). SIM can't really exceed NO's profit (NO = optimal: no inventory policy, no shipping…). Compare each SIM scenario with NO and **justify** the gap; if huge, reconsider the inventory policy.

- **Flow amounts** in NO must be **the same for all groups** (same dataset) even if profits differ → good validation check. They are aggregated (factory→DC + DC→customer + suppliers→factory ingredients) ⏱ 0:52:45.
- NO costs per iteration: **Overall stats** (+ objective members); **export to Excel** to read them better ⏱ 0:55:03.

![[L7-11-br-no-overall-stats-iter-claude.jpg|600]]

- Managerial insight on 2 DCs (Berlin + Spain): service level good, profit close to NO → useful scenario; in the project also evaluate **CO₂** ⏱ 0:57:16.

## 7.6 Resilience & disruptions ⏱ 0:58:13
- **Disruptions**: from small ones (rainy day → lower truck speed → longer lead time) to big ones (cyber-attack making fridges go to +40 °C in supermarkets, wars affecting oil & gas bottlenecks, natural disasters).
  - **External** (natural disasters, war): not controllable. **Internal**: more manageable.
- **Resilience** = ability to **deal with, recover from or adapt to** disruptions. In ALX we test it (not too deep, not superficial) by adding **events** (e.g. shutdown of a facility / production line, supplier backlog). Sensitivity analysis proper is done with the **variation** ⏱ 1:01:21.

### Scenario A – disruption with only 1 DC (as-is) ⏱ 1:02:43
1. Right-click the SIM scenario → **Convert** → name `BR SIM Level_Disruption_1DC`, type SIM (a copy, so the original stays untouched).

![[L7-12-convert-disruption-scenario-claude.jpg|500]]

2. Table **Events** → event types: **Additional expenses, Demand coefficient** (≈ sensitivity), **Facility state** (closure), **Fleet size**, **Path state** (e.g. a road closed for construction), **Production line state** (needs production lines defined in *Production*; not needed in the project) ⏱ 1:05:15.

![[L7-13-event-types-list-claude.jpg|500]] ![[L7-14-event-production-line-state-claude.jpg|500]]

3. Event 1: **Facility state** → parameters *Changes state to* **Temporarily closed**, object **DC Berlin**; occurrence type **Date** → **1 August** (time not important) ⏱ 1:07:03.

![[L7-15-event-temporarily-closed-claude.jpg|500]]

4. **Probability** = 1 → it surely happens (0.9 = 90 % probability) ⏱ 1:09:10.

![[L7-16-event-probability-claude.jpg|600]]

5. Event 2: Facility state → **Open**, DC Berlin, date **30 September**, **Trigger = Event 1** (otherwise the rows are not connected and the DC would stay closed forever) ⏱ 1:09:41.

![[L7-17-event-trigger-reopen-claude.jpg|600]]

6. To test the as-is: in *Distribution Centers* **Exclude DC Spain** (only Berlin) ⏱ 1:11:05.

![[L7-18-exclude-dc-spain-claude.jpg|600]]

- **Results** ⏱ 1:13:54: profit **9.69 M (−19.7 %)**, service level drops exactly when the DC closes and recovers after reopening → **0.707** overall (vs 0.963 without disruption). → the as-is with one DC **can't respond** to such a disruption: too risky.

![[L7-19-disruption-1dc-kpis-claude.jpg|600]] ![[L7-20-disruption-1dc-service-level-claude.jpg|500]]

### Scenario B – disruption with 2 DCs ⏱ 1:15:43
- Convert again → `…Disruption_2DC`; **no exclusion** in DCs; same 2 events (close Berlin 1 Aug, open 30 Sep with trigger Event 1).
- **Results** ⏱ 1:19:07: profit **≈ 11.79 M (−2.2 %)** vs 9.7 M with 1 DC; service level never below ~88 %, recovers to 93–94 % → **0.933** overall.

![[L7-21-disruption-2dc-kpis-claude.jpg|600]] ![[L7-22-disruption-2dc-service-level-claude.jpg|500]]

| Scenario | Profit | Service level by products |
|---|---|---|
| SIM, 2 DCs, no disruption | 12,058,386 | 0.963 |
| Disruption, 2 DCs | 11,793,927 | 0.933 |
| Disruption, 1 DC (as-is) | 9,687,687 | 0.707 |

> [!important] Work project ⏱ 1:21:26
> The project events will be **facility closures** (not production lines). You are a small **consulting company**: test the scenario under parameter changes (variation) and disruptions (events) to **convince** the company – the highest scores go to projects with **many analyses, tests and variations**, not just "this is my profit".

---

# Lezione 8 – Comparison & variation on Case 2, flow details, tips for the work project (19 Nov, afternoon – video)
🎥 `anylogistic_lessons/Video recording Lecture 8 NOV5-26 STEM.mp4` (1h26)

## 8.1 Comparison experiment ⏱ 0:01:07
- Purpose: compare scenarios on KPIs **without moving from one scenario to another**.
- On a SIM scenario **with solution** → *Comparison experiment* → **Settings → Select scenarios to compare** (list of all your SIM scenarios; select only the relevant ones, e.g. `BR SIM Level 1`, `…Disruption_1DC`, `…Disruption_2DC`) → KPIs in the dashboard (profit, demand/products backlog, service level; *Add new chart* for more) → run ⏱ 0:03:00.

![[L8-01-comparison-select-scenarios-claude.jpg|600]]

- Results (min / max / mean columns per scenario):

![[L8-02-comparison-service-level-claude.jpg|500]] ![[L8-03-comparison-profit-claude.jpg|500]]

| Scenario | Service level | Profit | Avg available inventory |
|---|---|---|---|
| BR SIM Level 1 (no disruption) | 0.963 | 12,058,385.9 | 504.975 |
| Disruption 2 DCs | 0.933 | 11,793,927.2 | 460.075 |
| Disruption 1 DC | 0.707 | 9,687,687.1 | 203.75 |

![[L8-04-comparison-available-inventory-claude.jpg|500]]

- In the final presentation: screenshot this table or build your own table/graphs (AI may help turn numbers into graphs, but don't do everything with AI) ⏱ 0:07:51.

> [!warning] Deliverables are checked one by one ⏱ 0:10:03
> The teacher asks for **all exported scenarios** as attachments and opens them **one by one** ("I'm very patient"): you can't be graded on the presentation alone. AI can help you check calculations, but do the work yourself.

## 8.2 Validation through variation ⏱ 0:11:28
- Disruption ≈ "what if something happens"; real sensitivity analysis = **variation** ("validation through variation": what if demand / inventory policy change?).
- PDF task: vary the **min (reorder point) of the DC inventory policy** from **900 to 2300, step 200** ⏱ 0:12:53.
- Variation experiment → Settings → **Add variable parameter**: object type **Inventory**, object *Inventory policy for facility DC Berlin, product Beer*, parameter **Min**, variation **Number range** 900 / 2300 / step 200 → results at 900, 1100, 1300, … ⏱ 0:16:25.
- Current DC policy: min **1,800** (= when to reorder), max **11,600** (= target level, not necessarily reached) ⏱ 0:15:24.

![[L8-05-variation-inventory-min-param-claude.jpg|500]]

- Result in class: service level constant **0.963** and profit unchanged for every min → here the min of the DC has **no impact**. Repeated on the **factory** min (current 2000/5000 → 1000–3000 step 200; delete the previous variable parameter first, otherwise both are run): still no change – also in the prepared scenario. "In reality, with your real data, it **will** change: different min levels at least impact production cost and profit." (PDF: best reorder point 1,300.) ⏱ 0:18:58

![[L8-06-variation-dc-min-results-claude.jpg|600]]

> [!tip] Variation in the project ⏱ 0:23:20
> Use it to find the **potential and the weaknesses** of your scenario for the managerial insights; each team must propose its own customised results.

## 8.3 Tips for the work project ⏱ 0:26:07
- **Safety stock estimation** experiment: **not available in the PLE version** anymore → you calculate safety stock yourself (ALX's estimates are not very precise anyway) ⏱ 0:26:27.

![[L8-07-safety-stock-estimation-not-available-claude.jpg|500]]

- **CO₂ emissions go in the Paths** (CO₂ calculation param, e.g. 0.5 × product per unit), next to the cost calculation ⏱ 0:27:28.

![[L8-08-path-co2-param-claude.jpg|600]]

- For anything new: use the ALX **Help** (search by keyword) ⏱ 0:28:47.

### Flow details → inventory policy ⏱ 0:29:20
- Min/max (s, S) are **not given**: you **calculate** them. A recorded video on the inventory policy will follow the project presentation.
- NO results → page **Flows details** → **export** to Excel → filter the chosen **iteration** (e.g. iteration 5 = Berlin + Spain): from which DC to which customer, which product, how much (+ distance, travel time…) ⏱ 0:30:53.

![[L8-09-no-flows-details-page-claude.jpg|500]] ![[L8-10-flows-details-excel-claude.jpg|600]]

- **s (min) = average daily demand × lead time (+ safety stock)**; average daily demand = flow ÷ **working days** (given). Organise data with **VLOOKUP / PIVOT** (AI only as a last resort) ⏱ 0:33:04.

### Project data preview ⏱ 0:34:50
- **98 customers** (case: 4), demand **> 35,000 rows** (case: ~1,300), **historic demand** (date, quantity pcs/day, customer, product family – same customer may order the same family several times a day) from **one year** of real (cleaned) company data; anonymised (names and locations changed).

![[L8-11-project-historic-demand-raw-claude.jpg|600]]

- This year the GFA scenario is **prepared**: only the **demand** is already in ALX format; you insert everything else ⏱ 0:36:37.
- **5 product families**, **5 semi-finished products** → BOM for each product; unit conversions (volume of each family), costs, **production time** per product family, CO₂, facility costs ⏱ 0:47:38.

![[L8-12-project-input-data-claude.jpg|600]]

- **As-is** ⏱ 1:07:18: **1 factory in north Italy**, **2 DCs (Poland and Belgium)**, **2 suppliers** – Italy (semi-finished 1, 2, 3) and Germany (4, 5); factory produces the 5 final products. Factory and suppliers **cannot be closed**; only DCs can be closed/opened (one of them "has a problem"); maximum **3–4 DCs** in total.
- "Forecast" part: use variation/tests on the as-is to forecast what happens if something changes ⏱ 0:40:18.

> [!warning] DC choices ⏱ 0:42:39
> Repeated mistake: **closing all existing DCs and opening many new ones** because GFA shows lower transport cost. Allowed, but you must justify it (initial & closure costs, agreements with new DCs…). Better: keep existing DCs, find other options with GFA, put them all as **Consider** in NO, then choose. Dedicate **1–2 slides of managerial insight** to justify the choice (profit + tests + variations).

- **Deliverables** ⏱ 0:45:47: (1) presentation, (2) Excel of the inventory-policy calculation, (3) exported file of the best SIM scenario, (4) exported file of the NO. **Export your scenarios** – deleting a project deletes them forever.
- Don't copy last year's projects: data and problems change every year, copying got very low scores ⏱ 0:49:58.

### Paths: choose the right cost calculation ⏱ 0:52:26
- The data won't say "product & distance-based": **interpret the units**. €/km with no product unit → depends only on distance → e.g. **Distance-based with fixed cost** (e.g. 0.7). €/km per product unit → **Product & distance-based** ⏱ 0:54:16.
- Strange results → always check **paths and product flows**. The **Check** button catches basic errors (e.g. *Vehicle type is not defined*) but not a wrong interpretation ⏱ 0:57:45.

![[L8-13-path-distance-based-fixed-cost-claude.jpg|600]]

- **Vehicle speed** may be **stochastic**: instead of *Value* choose **Triangular** (min, max, mode given in the data, e.g. 40 / 80 / 60) ⏱ 0:58:35.

![[L8-14-vehicle-speed-triangular-claude.jpg|600]]

- **Transportation time** in paths: 0 = computed from distance and speed; if the data give a transportation time (often **triangular**), insert it ⏱ 1:00:36.

![[L8-15-path-transportation-time-claude.jpg|600]]

### Planning advice ⏱ 1:02:02
- GFA: ~30 minutes → go **immediately to NO** (paths, product flows correct) → choose an iteration and go to **SIM** (the most challenging part). Don't spend weeks on NO.
- Have **one complete scenario (with inventory policy) by mid-December**; the second one is much faster. By the afternoon of **10 December** you should already be "struggling in simulation"; by **17 December** close the first SIM scenario. Write emails with exported file + screenshot before then ⏱ 1:03:26.
- Shipping & sourcing are easy once paths are right; the inventory policy gets a step-by-step video.
- In variation and comparison also consider **CO₂** and other KPIs, not only profit and service level ⏱ 1:09:52.

### Inventory policy calculation (example of a past year) ⏱ 1:11:11
Excel columns: **average daily demand** (from flow details, e.g. Belgium DC → customers) · **d × L** · **average lead time** · **std lead time** · **std demand** · **SS** · **K (= 1.65)** · **ROP** · selling price · **EOQ** · **S max** · S ALX · initial stock (with / without SS). A file with some formulas and a ~30 min video will be provided.

![[L8-16-inventory-policy-excel-example-claude.jpg|700]]

- **Policy choice is yours** (min-max with or without SS, RQ…) – look at your data ⏱ 1:13:53:
  - SS formula has 3 cases (lead time varies, demand varies, both). If **σ demand = 0 and σ lead time = 0 → SS = 0**.
  - Lead time fixed and order interval regular → σ_L = 0; lead time triangular → compute the **std of the triangular distribution**; demand not fixed → compute its std (Excel).
- **Help** → *Inventory* explains every policy (RQ: when inventory falls below the replenishment point R, order a fixed quantity Q; min-max…) ⏱ 1:17:26.

![[L8-17-help-rq-policy-claude.jpg|600]]

- **Suppliers / ingredients**: no inventory policy to compute → **Order on demand** for ingredients. **Production (factory)**: consider production time per product and use **EPQ** for the target level (S max); for finished products **EOQ**. Always **min = average daily demand × lead time + SS** (SS = 0 if no variability), **max = Q target** ⏱ 1:20:23.

---
# 🧰 Project cheat-sheet (everything the teacher flagged for the work project)

**Workflow**
1. **GFA** (given prepared this year) → only an indication of areas; don't feel bound to keep its locations (L3 ⏱ 0:40:23).
2. **NO** → candidate facilities = *Consider*, sure ones = *Include*; choose an iteration balancing profit with other aspects (initial/closure costs, workers, resilience) (L4 ⏱ 0:29:48).
3. **SIM** → chosen facilities *Include* (never *Consider*); add inventory, shipping, sourcing, production time (L4 ⏱ 1:18:46, L5 ⏱ 0:31:21).
4. **Variation** (sensitivity) and **Comparison** of your networks on profit, CO₂, service level, resilience (L5 ⏱ 1:02:23, 1:17:20).
5. Write **recommendations / managerial insights**: strengths, weaknesses (L5 ⏱ 1:01:22).

**Data preparation**
- Raw data → ALX format: create scenario, add dummy rows, export, paste as values, `CONCAT(name," ","Location")`, import with **"Scenario contains formulas"** (L6 ⏱ 0:07:48).
- Excel skills: **PIVOT, VLOOKUP**. Demand will be **historic demand** (L3 ⏱ 0:23:30, L6 ⏱ 0:10:48).
- Names in Customers ↔ Locations must match exactly (case, spaces) (L6 ⏱ 0:22:46).
- Use **groups** for every echelon (customers, DCs, factories, suppliers, ingredients) (L3 ⏱ 1:18:09).
- Carrying costs are given per **year per m³** → convert to **per day** (L3 ⏱ 1:16:57).
- **Export** your scenarios to save them; only one project in PLE (L5 ⏱ 0:44:06, L3 ⏱ 0:07:35).

**NO checklist** – paths (correct source/destination/cost calculation, separate rows when costs differ, **CO₂ in paths**), **product flows**, **product storages**, **production** (+ BOM), products with selling price & cost, vehicle types (different trucks per leg!), check units & currency in experiment settings, *Check* the scenario (L4 ⏱ 0:05:34–0:26:14, L6 ⏱ 1:21:03).
- Up/down penalties not necessarily needed in the project (L3 ⏱ 1:07:24).
- NO flows are aggregated across levels (L4 ⏱ 1:05:12).
- **Flow details** = source of data to compute your inventory policy (L4 ⏱ 1:01:58).

**SIM checklist**
- **Inventory policy**: compute it yourself from NO product flows (s = ROP = d̄·L + SS; S = target), **per product and per facility**; never *Unlimited inventory*; ingredients usually *Order on demand* (L5 ⏱ 0:20:18, 0:24:04, L6 ⏱ 1:33:04).
- Low service level → first check the inventory policy, then shipping/sourcing (L5 ⏱ 0:12:56).
- Big NO↔SIM profit gap → check inventory policy & production time; a residual gap (extra production to keep stock) is normal but **must be justified** (L4 ⏱ 1:28:24, L5 ⏱ 0:53:21).
- Backorder *Allowed total* recommended; *Not allowed* cancels orders (L5 ⏱ 0:29:43).
- Sourcing *dynamic* is usually better than *fixed* (L5 ⏱ 0:26:21).
- Use line charts for service level over time; add only meaningful KPIs (L5 ⏱ 0:59:00, 1:15:53).

**SIM – shipping & sourcing (L7)**
- Shipping: sources/destinations/product/vehicle (2 vehicle types in the project), **days of week Mon–Fri** (affects lead time), start/end time ~8–17 (L7 ⏱ 0:28:13).
- Sourcing: customers ← **[DC]** (not factory, not *All sites*); negative profit = products never reach customers (L7 ⏱ 0:31:08).
- Cheapest sourcing also considers DC facility costs, not only transport (L7 ⏱ 0:35:57).

**Analyses that raise the grade (L7–L8)**
- Resilience: Events → Facility state *Temporarily closed* + *Open* with **Trigger**, probability; compare 1 DC vs 2 DCs (L7 ⏱ 1:02:43).
- Comparison experiment table of all scenarios; variation on inventory min/max, demand… also on **CO₂** (L8 ⏱ 0:01:07, 1:09:52).
- Same dataset → **NO flow amounts must be identical for all groups** (validation check) (L7 ⏱ 0:52:45).

**Data interpretation (L8)**
- €/km without product unit → *Distance-based with fixed cost*; €/km/unit → *Product & distance-based* (L8 ⏱ 0:54:16).
- Speeds / transportation times may be **triangular** (min, max, mode) (L8 ⏱ 0:58:35).
- CO₂ in **Paths** (L8 ⏱ 0:27:28). Safety stock estimation not available in PLE → compute SS yourself (L8 ⏱ 0:26:27).
- As-is: 1 factory (N. Italy), DCs Poland + Belgium, suppliers Italy + Germany; only DCs can change, max 3–4 DCs; don't close everything and reopen from scratch without justification (L8 ⏱ 0:42:39, 1:07:18).

**Inventory policy recipe (L8 ⏱ 1:11:11, 1:20:23)**: NO *Flows details* → export → filter iteration → average daily demand (÷ working days) → σ demand, σ lead time (triangular!) → SS (K = 1.65; 0 if no variability) → **s = d̄·L + SS**, **S = EOQ** (finished products) / **EPQ** (factory) → ingredients *Order on demand*.

**Timeline**: presentation 26 Nov · Q&A 10 & 17 Dec · one full SIM scenario by mid-December · **deadline 15 January (no extensions)** (L7 ⏱ 0:08:21, L8 ⏱ 1:02:02).
**Deliverables**: presentation + inventory Excel + exported best SIM + exported NO; scenarios are opened one by one (L8 ⏱ 0:45:47, 0:10:03).

**Evaluation**: project in groups of 4 → **11/33**; you'll have to discover things not shown in class (L1, L4 ⏱ 0:21:00).
