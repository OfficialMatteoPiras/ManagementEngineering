---
course: Smart Operations and Supply Chain Management
professor: Laura Macchion
chapter: 7
book: "Slack, Brandon-Jones, Burgess – Operations and Process Management (PDF in /pdf)"
tags: [SOSCM, summary, chapter7]
---
# Chapter 7 – Supply chain management

> [!abstract] In one breath (for the oral)
> **SCM** manages relationships and flows (products/services downstream, information both ways) along a *chain* of operations. A *network* contains many chains. SC objectives are the usual five plus **sustainability**, and errors **compound** along the chain (0.99⁷ = 93.2%). **Functional** products need **efficient (lean)** chains and **innovative** products need **responsive (agile)** chains (Fisher). Relationships range from **transactional** to **partnership**. Sourcing can be **multiple, single, delegated or parallel**. The **bullwhip (Forrester) effect** amplifies small demand changes upstream; it is reduced by channel alignment, operational efficiency, better forecasts and **information sharing**, including **blockchain**.

[[Ch06 - Process design 2 - Analysis-claude|← Ch 6]]

---

## 7.0 Introduction and executive summary (book)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=259|p.259–261]]
Chapter 4 dealt with the **structure and scope** of the network; this chapter covers how chains and networks are **managed on an ongoing basis**: performance objectives, relationships (transactional vs partnership), **sourcing strategies**, **supplier selection and negotiation**, day-to-day supply, **supplier development** and **supply chain dynamics**. These are usually the job of **purchasing/procurement**, the link between the operation's processes (whose requirements it must understand) and the capabilities of potential suppliers.
The book's six diagnostic questions: 7.1 nature of SCM · 7.2 relationships · 7.3 sourcing configuration (multiple/single/delegated/parallel × **non-critical, bottleneck, leverage, strategic**) · 7.4 **supplier selection and negotiation** (qualification, criteria, information, scoring, tactics) · 7.5 **running supply chains** (two-way information, SLAs, perception gaps, supplier development, **logistics** and IoT) · 7.6 **dynamics** (bullwhip and its four remedies, blockchain).

## 7.1 What is supply chain management?

*"Operations do not exist in isolation"*: an operation's performance is partly a function of its whole network. Think of disruptions from **factory fires, tsunamis, pandemics, trade disputes**. It is the whole network that determines the quality, speed, dependability, flexibility, cost and sustainability delivered to end customers ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=262|p.262]]).

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=262|p.262]]
> Supply chain management (SCM) is the management of the relationships and flows between the 'string' (or chain) of operations and processes that deliver value in the form of products and services to the ultimate consumer. It is a holistic approach to managing across the boundaries of companies and of processes. […] supply chains are technically different to supply networks. A supply network is all the operations that are linked together so as to provide products and services through to end customers. […] supply chain management is as much concerned with managing information flows (upstream and downstream) as it is with managing the flow of products and services.

![[Summary SOSCM - Macchion-1793008730335.webp|600]]

> [!info] 📖 Figure 7.2 – Supply chain vs supply network; flows of information and products · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=262|p.262]]
> - Each box is an operation with its own internal "flow between processes".
> - The **orange boxes** linked in a row form **one supply chain** (*"supply chain management concerns flow between a string of operations"*). **All the boxes together** form the **supply network** (*"supply network management concerns flow between all operations"*).
> - **Top arrow, upstream:** flow of **customer requirements**: long-term plans, market research, individual orders, payment, ideas for new products.
> - **Bottom arrow, downstream:** flow of **products and services**: new products, delivery information, payment requests/credit.
> Your note: **non-physical and physical flows**; **internal** relationships between processes and **external** relationships between operations.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=263|p.263]]
> OPERATIONS PRINCIPLE: Supply chain management applies equally to non-physical flows between operations and processes as well as physical flows.
>
> OPERATIONS PRINCIPLE: Supply chain management concepts apply to internal relationships between processes as well as the external relationships between operations.
>
> *(These two principles are exactly your note: "non-physical and physical flows; internal relationships between processes and external relationships between operations".)*

- **Non-physical flows** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=263|p.263]]): most literature focuses on material operations, but SCM applies equally to **financial services, malls, insurers, healthcare, consultants, universities**. They all buy services and choose how to deliver theirs, and every network has service elements.
- **Internal and external chains:** "organisations" in a chain need not have different owners. The network idea applies at organisation-to-organisation, **process-to-process** and even **resource-to-resource** level (internal customers and suppliers, Ch 1).
- A large network can contain **hundreds of supply chains** through a single operation. The terms *supply chain* and *supply network* are often (mistakenly) used interchangeably. The most visible failures are downstream, but **root causes are often failures in upstream information flows**.

### Case example: Zipline's drone-enabled supply network

![[Summary SOSCM - Macchion-1793009092506.webp|500]]

> [!info] 📖 Case example – Zipline · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=263|p.263–264]]
> - **Context:** in **Rwanda** over 80% of roads were unsurfaced, so road delivery of urgent **blood and medical supplies** was slow, especially in the rainy season.
> - **Solution:** autonomous drones carrying **1.5 kg** each (3 × 500 ml of blood) over a **22,500 km²** area, reaching over half of the 12 million population.
> - **Speed:** GPS moved into the battery (signal ready before launch), a **modular** fuselage/wing/battery, and pre-flight checks done by app and computer vision. Order-to-launch time is **5 minutes**, with a launcher reaching 100 km/h in 0.3 s. The photo shows staff mounting a drone on the launcher.
> - **Dependability:** back-up for every critical component. Delivery is by **wax-paper parachute**, so no infrastructure is needed at the destination.
> - **Business models:** **cross-docking** (clients' packages are consolidated at Zipline DCs and scheduled) or **3PL** (Zipline holds client inventory and ships on order).
> - **Strategy:** **lean when it can be, agile when it needs to be**. Drone delivery costs more, partly offset by **less inventory and obsolescence**, with big gains in speed, dependability and patient health.

![[Summary SOSCM - Macchion-1793009598482.webp|600]]

> [!example] 🎓 Lecture slide – "Responsible Operations Challenge" (not in the book)
> A class discussion slide. **Your challenge: "What should the company change first?"** Four responsible-operations priorities:
> - **People:** safe work and fair treatment.
> - **Planet:** less energy, material and waste.
> - **Integrity:** traceable and ethical decisions.
> - **Resilience:** reliable quality and continuity.
> Bottom line: *"Responsible operations make these priorities part of everyday decisions."*
> **How to use it at the oral:** connect it to the **triple bottom line** ([[Ch01 - Operations and processes-claude#Triple bottom line (people, planet, profit)|Ch 1]]), to **sustainability** as a supply chain objective (below), and to **blockchain** for traceability/integrity (7.5).

### Supply chain objectives

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=264|p.264]]
> The objectives of supply chain management are similar to those for individual operations – to deliver services and products to end customers that meet their expectations in terms of quality, speed, dependability, flexibility, cost and sustainability.

| Objective | What changes at the *chain* level |
|---|---|
| **Quality** | Errors **multiply** along the chain: 7 stages with 1% errors each give 0.99⁷ = **93.2%** good output. Every stage must take responsibility for itself *and* its suppliers. |
| **Speed** | Two meanings: (1) **responsiveness** to customers (can be "bought" with excess stock or capacity), (2) **fast throughput** through the chain (less inventory and working capital). Balance the two. |
| **Dependability** | On-time delivery can also be "bought" with excess resources. Better: dependable **throughput time**, which reduces uncertainty. Unreliable suppliers make customers **over-order or order early**. Measured as **on-time, in-full (OTIF)**. |
| **Flexibility** | **Supply chain agility**: coping with changes in demand *and* in supply capabilities. |
| **Cost** | Besides each operation's own cost, **transaction costs**: finding suppliers, contracting, ordering, monitoring, invoicing, dealing with failures, exit costs. Partnerships and fewer suppliers aim to reduce them. |
| **Sustainability** | Buy from responsible suppliers: local sourcing, ethical practices, eco-friendly products, minimal packaging, ground rather than air transport. |

### Efficient vs responsive supply chains (Fisher)

![[Summary SOSCM - Macchion-1793010246137.webp]]

> [!example] 🎓 Lecture slide – "Efficient vs responsive supply networks" (adapted from Fisher, HBR 1997). The book's version is Figure 7.3, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=266|p.266]]
> A 2×2 matrix:
> - **Columns = nature of demand.** **Functional products:** predictable, few changes, low variety, stable price, long lead time, low margin. **Innovative products:** unpredictable, many changes, high variety, price markdowns, short lead time, high margin.
> - **Rows = supply chain objectives.** **Efficient:** low cost, high utilisation, minimal inventory, low-cost suppliers. **Responsive:** fast response, low throughput time, deployed inventory, flexible suppliers.
> - **The diagonal (circled in red on the slide):** functional + efficient = **lean supply chain management**; innovative + responsive = **agile supply chain management**. The other two cells are **mismatches** (underlined).
> **Book examples (Fig 7.3):** a bucket or bread (functional) vs a mobile phone or fashion bag (innovative).

**Book detail** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=265|p.265–267]]): functional demand is stable and predictable with low margins; innovative demand is uncertain with much higher margins. The same company can have both: **consultants** (standardised vs tailored work), **hospitals** (routine cataract removal vs emergency post-trauma surgery), **shoe makers** (classics vs one-season fashion).
- **Efficient (lean) policies:** low inventory and capacity, especially **downstream**; fast throughput and little working capital; **maximise utilisation**; fast information up and down so schedules can be adjusted efficiently.
- **Responsive (agile) policies:** high service levels; inventory or capacity **deployed close to the customer**, so supply continues even with dramatic demand changes; fast upstream throughput still needed to replenish.
- **Figure 7.3** data: time between new introductions (bucket 10 years+, bread 1–10+ years, phone 1 year–18 months, fashion bag 3–6 months); margins (tiny, small, very high, high).
- **Hybrids exist:** **Inditex** (Zara) is predominantly agile but lean in some activities. "Leagile" is in Ch 11.

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=266|p.266]]
> OPERATIONS PRINCIPLE: 'Functional' products and services suit efficient (lean) supply chain management; 'innovative' products and services suit responsive (agile) supply chain management.

---

## 7.2 What type of supply chain relationship should be adopted?

*"Managing supply networks is about managing relationships"*: the relationship is the basis on which products, services, information and money are exchanged. Two dimensions: **what** to outsource (Ch 4) and **who** supplies (how many suppliers, how close) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=267|p.267]]).

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=267|p.267]]
> Transactional (or contractual) relationships involve purchasing products and services in a 'pure' market fashion, often seeking the 'best' supplier every time it is necessary to make a purchase. […] In contrast, partnership (or collaborative) relationships are longer term and involve a commitment to work together over time to gain mutual advantage. These relationships emphasise cooperation, frequent interaction, information sharing, joint problem solving and sometimes even profit sharing.

- **Mutuality** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=268|p.268]]): *"A supplier does not become a 'partner' merely by being called one."* True partnerships imply **mutual benefit, and often mutual sacrifice**. A business unwilling to give up some freedom of action won't make partnerships work.
- **A portfolio of relationships:** firms rarely use only one type, and each relationship can be managed more or less transactionally. The question is **where on the spectrum** to put each relationship:
  - **Competing on price:** market-based contracts minimise the **price paid**; partnerships minimise **transaction costs**. Choose whichever saves more.
  - **Competing on innovation:** if innovation needs **close collaboration**, partnership. If suppliers compete to out-innovate each other in a **turbulent, fast-growing market** (software, internet), keep the **freedom to switch** (transactional).
  - Sometimes the **market structure** decides: with few potential suppliers there is little market leverage.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=268|p.268]]
> OPERATIONS PRINCIPLE: All supply chain relationships can be described by the balance between their 'contractual' and 'partnership' elements.

![[Summary SOSCM - Macchion-1793011424974.webp|500]]

> [!info] 📖 Figure 7.4 – Types of supply network arrangement · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=267|p.267]]
> - **Y: what the operation outsources**, from *nothing* (top) through *relatively unimportant activities* to *everything* (bottom).
> - **X: who supplies the operation**, from *arm's length with many suppliers* (left) to *close, with few suppliers* (right).
> - **Bubbles:** **vertical integration** (outsource nothing; top-right) · **traditional market supply** (contracts, many suppliers, unimportant activities) · **'partnership' supply relationships** (few close suppliers, important activities) · **virtual spot trading** (outsource everything, arm's length).

![[Summary SOSCM - Macchion-1793010963414.webp]]

> [!info] 📖 Table 7.1 – Benefits of transactional vs partnership relationships · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=268|p.268]]
> | Transactional | Partnership |
> |---|---|
> | Keeps competition between suppliers | More loyalty to customers |
> | Easy to change the number and type of suppliers when demand changes | Less time and effort re-contracting; lower transaction costs |
> | Wider variety of innovation sources | Lower cost of compliance monitoring |
> | Useful to assess a supplier before a partnership | Fewer quality failures; earlier failure detection |
> | Good for one-off or irregular purchases | Joint problem-solving instead of blame; value from shared competences |

---

## 7.3 Has the sourcing configuration been determined?

The concepts are in the book ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=269|p.269–270]]). The four network icons in your notes come from the lecture slides.

| | Multiple | Single | Delegated | Parallel |
|---|---|---|---|---|
| **What** | One component from *several* suppliers | All of one component from *one* supplier | One supplier delivers a whole *package/sub-assembly* and manages its own sub-suppliers | Single source *per model*, but different models use different suppliers for the same component |
| **✅** | Competition, lower supply risk, flexibility, diverse knowledge, no dependence | Simplicity, lower transaction costs, commitment, higher quality, long-term view | Far fewer first-tier suppliers; focus on strategic partners | Combines the benefits of single and multiple sourcing: competition and the ability to switch |
| **❌** | Effort to keep quality consistent; low supplier commitment | Lock-in, upward price pressure, less bargaining power, vulnerable to disruption | Can create powerful **"mega-suppliers"** | Complex to manage |
| **Typical when** | Competitive markets, low switching costs, focus on price and dependability | High share of spend, strategic items | Complex products (e.g. automotive modules) | Several product models sharing components |

> [!example] 🎓 Lecture diagrams – the four sourcing structures
> ![[Summary SOSCM - Macchion-1793011578887.webp|200]] ![[Summary SOSCM - Macchion-1793011613051.webp|120]] ![[Summary SOSCM - Macchion-1793011634217.webp|150]]
> - **Multiple:** the buyer (dark circle) is linked to **four** suppliers of the same item.
> - **Single:** the buyer is linked to **one** supplier.
> - **Delegated:** the buyer is linked to **one** first-tier supplier, which in turn manages **two** second-tier suppliers (darker circles). This is the tiered approach.
>
> ![[Summary SOSCM - Macchion-1793011660570.webp|350]]
> - **Parallel:** the buyer makes **Model 1** and **Model 2**. Model 1 takes *component A* from supplier 2 and *component B* from supplier 4; Model 2 takes *component A* from supplier 1 and *component B* from supplier 3. The **dashed arrows** link the suppliers of the *same* component (2↔1 for A, 4↔3 for B): if one fails, the buyer can switch to the other, who already makes that component for the other model.

### Supply base reduction
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=270|p.270]]
A 25-year trend: **fewer, higher-quality relationships** with key suppliers (resources are limited). ✅ Big cuts in daily running costs (ordering, expediting, visits, failure interventions). ❌ **More supply risk** (some suppliers may act **opportunistically**) and **power shifts towards suppliers** as the buyer depends on fewer of them.

### Choosing the sourcing strategy: supply risk × criticality (Figure 7.5, smartphone maker)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=270|p.270–271]]
- **Supply market risk/complexity:** number of alternative suppliers, ease of switching, exit barriers, cost of bringing in-house.
- **Criticality:** % of total purchase cost, impact on business growth.

| Quadrant | Risk / criticality | Smartphone example | Favoured sourcing |
|---|---|---|---|
| **Non-critical** | Low / low | **Packaging, screws** | **Multiple sourcing** (sometimes single with short contracts, after supply base reduction) |
| **Bottleneck** | High / low | **Power pack** (cheap but few suppliers, high switching costs) | **Single sourcing** (no choice); try to **reduce the specificity** of requirements to widen the options |
| **Leverage** | Low / high | **Touch screen and display**, partly camera and speaker (high cost, many reliable suppliers) | Price competition (buyer power); **bundling → delegated sourcing** |
| **Strategic** | High / high | **Processor** (the "brain") | **Single sourcing**, moving towards **delegated or parallel** to reduce risk |

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=270|p.270]]
> OPERATIONS PRINCIPLE: Sourcing strategy is governed partly by the risk in the supply market, and partly by the criticality of the item to the business.

---

## 7.4 Has the approach to supplier selection and negotiation been determined?
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=272|p.272–274]]
Poor suppliers reduce the performance of every chain they belong to. Five steps:
1. **Initial qualification:** cut candidates to a manageable set, with minimum thresholds on **technical capability** (product/service knowledge for the spec), **operations capability** (process knowledge for consistent, responsive, dependable, reasonable-cost supply) and **financial capability** (strength in the short and long term).
2. **Measurement criteria:** set the **relative importance** of objectives (quality, speed, dependability, flexibility, cost, sustainability…) and **measurable criteria** for each. Cost: unit price, pricing terms (volume discounts), exchange rates. Delivery: average lead time, frequency, minimum order size, distance, verified % on time.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=272|p.272]]
> OPERATIONS PRINCIPLE: Measurement criteria for supplier selection should align with the overall performance objectives of the supply network.

3. **Information collection:** **RFQs** (requests for quotes), **RFIs** (requests for information), supplier visits, **trial orders**. The effort depends on strategic importance and supply-base capability, and on the **type of purchase**: **routine re-buy** (low search) → **modified re-buy** (new service from a known supplier or known service from a new supplier: moderate) → **new buy** (unknown supplier, new product: extensive).
4. **Final selection:** rarely is one supplier clearly superior, so trade off attributes with **multi-criteria scoring**: the **weighted score method** (worked example below), **AHP** (analytical hierarchy process), or **TCO** (total cost of ownership: all costs, not just price).
5. **Negotiation:** shaped by the objectives, relationship type and sourcing configuration.

**Table 7.3, negotiation tactics** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=274|p.274]]):

| Tactic | Guidelines |
|---|---|
| **Emotion** | Frames the negotiation. **Anger** is the most common and most damaging; positive emotions support collaboration. Use early, be sincere, don't let emotions control you, use them to raise "perceived value" |
| **Logic** | Be credible; **one powerful argument** beats several weak ones; get yours in first; use it to counter emotion |
| **Threat** | Avoid if possible and be credible. Threaten the **business, not the person**; veiled threats are less risky; use **"if"** to leave room to manoeuvre |
| **Bargaining** | Don't expose your position too early; move in **small, decreasing steps** and get something back; don't appear too keen |
| **Compromise** | Use it **after** other tactics; start from an extreme (but credible) position; compromising too early **shuts down creative solutions** |

- **Advocacy approach** (fight for your own best outcome): risks short-termism, personal conflicts, a damaged relationship, even **lose–lose**.
- **Collaborative negotiation** (also called *principled negotiation* or *mutual gains bargaining*): meet **both parties' needs**, a transparent process, personal relationships, creative brainstorming (**grow the pie** instead of dividing a fixed one), long-term **win–win**.

---

## 7.5 Are supply chains run effectively?
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=274|p.274–280]]
**Two-way information flow:** choosing suppliers and then "leaving them to it" isn't enough. Customers may expect supply "under any circumstances", while suppliers may hide problems for fear of losing the relationship. In a partnership, **free information and mutual tolerance of occasional problems** are the basis of smooth supply. Watch for **internal inconsistencies** (one department asks the supplier for extra while another pays late).

**Service-level agreements (SLAs):** formal definitions of the dimensions of service and the relationship (response times, range, dependability, boundaries of responsibility, measures). Book example, an **internal SLA** between IS support and a research unit in a pharmaceutical company: standard services, special services by period, **minimum "up time"**, maximum and average **response time** to get the system operational, response time for special services. ⚠️ SLAs often fail because they are used only to **set up** the relationship and then to **resolve disputes**. They should be **working documents** that capture shared knowledge: *"Any SLA that stays unchanged over time is failing to encourage improvement."*

**Perception gaps (Figure 7.6)** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=275|p.275–276]]), from the customer's point of view (scenario A):
1. **Requirements perception gap:** what the customer really wants vs what the supplier thinks it wants.
2. **Fulfilment perception gap:** how the customer thinks the supplier performs vs how the supplier thinks it performs.
3. **Supplier improvement gap:** what the customer wants vs how it perceives the supplier's performance. This drives the customer's **development goals**.
4. **Supplier performance gap:** the supplier's view of needs vs its own assessment of performance. This drives the supplier's **self-improvement**.
Gaps 1 and 2 depend on **communication**. In scenario B (the supplier's point of view) the same model also asks whether customer demands are **reasonable**: a small change might not bother the customer but greatly help the supplier, and the customer may be **poor at measuring** performance, so good service goes unrecognised.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=276|p.276]]
> OPERATIONS PRINCIPLE: Unsatisfactory supply chain relationships can be caused by requirement, fulfilment, supplier improvement and supplier performance perception gaps.

**Multi-tiered relationships (Figure 7.7)** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=276|p.276–277]]): a formal contract between organisation A (buyer) and B (supplier) is interpreted at several levels: **procurement ↔ sales/account managers**, **line managers ↔ line managers**, **service users ↔ service providers** (professional relationships). Ideally attitudes and perceptions are consistent at every level, but often they aren't, and there are also gaps between what each organisation wants from its employees and what is delivered on the ground.

**Supplier development** (unless the relationship is purely transactional, it is in the customer's interest; some firms have dedicated teams) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=277|p.277–278]]). Four stages:
1. **Select the product/service and supplier:** typically the **strategic** quadrant; weak current performance but potential; important inputs; hard to switch.
2. **Form a project team and gain buy-in** from buyer, supplier and stakeholders (it takes time and sensitivity; the supplier's management may be defensive).
3. **Agree goals and measures:** scope, timeline, cost, deliverables, plus **risk evaluation** and mitigation (e.g. internal marketing of benefits, profit sharing).
4. **Implement, monitor and learn:** intervene if off target, celebrate success. The goal is for the supplier to **keep improving without the customer's intervention**; the lessons feed future projects.

**Logistics (distribution)** = moving products from suppliers to customers. Critical when distribution is a large share of costs ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=278|p.278–279]]).
| Level | Meaning |
|---|---|
| **1PL** | Logistics entirely **internal** (the manufacturer delivers, or the supermarket collects) |
| **2PL** | Outsource **one segment** (e.g. a shipping line from A to B, with storage if needed) |
| **3PL** | A logistics company **manages logistics more fully**, working with other carriers: transport, warehousing, inventory, (re)packaging |
| **4PL** | An **integrator** (term coined by Accenture) that assembles its own and others' resources to *"design, build and run comprehensive supply chain solutions"*; a single interface to many providers |
| **5PL** | Broadens 4PL to include **e-business** |

**Choosing transport:** consider **volume, size and value**. Small, high-value volumes go by **air**; high-volume, bulky, low-value goods go by **sea**. Typical cost order, from highest to lowest: **air > road > rail > water > pipeline**. Also consider **vertical trade-offs** (benefits that change over time, e.g. a new high-speed rail link or better ship fuel economy) and **lateral trade-offs** (the cost of a mode vs benefits elsewhere: **Zara** uses costly **air freight** but gains speed and **much lower inventories**).

**Logistics and the Internet of Things (IoT)** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=280|p.280]]): networks of physical objects (products, equipment, handling devices, trucks) with electronics, software and sensors that collect and exchange data. With **GPS**: instant tracking of trucks, materials and people, better coordination, cost savings. Examples: **back-loading** (finding a load for the return trip B → A so trucks don't return empty) and **track-and-trace** for parcel customers.

---

## 7.6 Are supply chain dynamics under control? The bullwhip (Forrester) effect

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=280|p.280]]
> There are dynamics that exist between firms in supply chains that cause errors, inaccuracies and volatility, and these increase for operations further upstream in the supply chain. This is known as the bullwhip effect, so called because a small disturbance at one end of the chain causes increasingly large disturbances as it works its way 'upstream'. Its main cause is a perfectly understandable and rational desire by the different links in the supply chain to manage their levels of activity or inventory sensibly.

![[Summary SOSCM - Macchion-1793613481804.webp|600]]

> [!example] 🎓 Lecture slide – "Forrester effect" (not in the book)
> A five-stage chain drawn **right to left**: **1 customer → 2 retailer → 3 wholesaler → 4 manufacturer → 5 raw material**. Above it, a wave labelled **"orders"**: on the right (customer) the oscillation is a ripple, *"small changes in demand"*; moving left (upstream) the swings get bigger and bigger.
> **Message:** each stage sees only its immediate customer's orders, so it **amplifies** the variation it receives. Jay **Forrester** first described this "demand amplification" (in industrial dynamics); "bullwhip" is the popular name.

![[Summary SOSCM - Macchion-1793613575424.webp]]

> [!info] 📖 Table 7.4 – Production fluctuations after a small demand change · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=281|p.281]]
> **Rule:** every stage keeps **one period's demand in stock**, so *production = demand + (target final stock − starting stock)*.
> Demand drops **100 → 95** in period 2:
> - **Focal firm:** starts with 100 in stock and must end with 95, so it produces **90** (then 95).
> - **1st tier:** sees an order of 90, so it produces **80** → 100 → 95.
> - **2nd tier:** 60 → 120 → 90 → 95.
> - **3rd tier:** **20 → 180 → 60 → 100 → 95**.
> A 5% change at the market becomes a swing from 20 to 180 three tiers up.
> Even the focal firm turns a **5-unit** demand change into a **10-unit** production change.

**Factors that make it even worse** (ignored in the simple example) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=281|p.281]]): no forecasting or forecasting errors; **quantity discounts** (fewer, larger orders); **price fluctuations**; **time lags** between information (orders) and materials (deliveries); variable delivery times; **panic ordering** before or after shortages.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=281|p.281]]
> OPERATIONS PRINCIPLE: Demand fluctuations become progressively amplified as their effects work back up the supply chain.

**Harmful impacts:** outsized facilities and **excess inventory** (then under-used); capacity swinging between under- and over-utilisation; **hire, fire, re-hire**; inefficiency, delays, **expediting costs**, unhappy customers.

![[Summary SOSCM - Macchion-1793613755020.webp]]

> [!example] 🎓 Lecture slide – "Management of materials in supply networks" (the same table, annotated in class)
> Same numbers as Table 7.4. The slide highlights each tier's **production column** (yellow boxes) and the **market demand** column (blue box), and adds the notation:
> - $S_f$ = inventory at the **end** of the period; $S_i$ = inventory at the **start**.
> - Policy: each actor holds stock equal to one period's demand of its customer ($S_f$ = market demand).
> - **A (purchases) = P (production) = $S_f - S_i$ + market demand.**
> Use it as the formula for the exercise below.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=280|p.280–281]]
> At the beginning of period 2, the focal firm has 100 units in stock (that being the rate of demand up to period 2). Demand in period 2 is 95 and so it knows that it would need to produce sufficient items to finish up at the end of the period with 95 in stock (this being the new demand rate). To do this, it need only manufacture 90 items; these, together with five items taken out of the starting stock, will supply demand and leave a finished stock of 95 items.

![[Summary SOSCM - Macchion-1793614736740.webp|600]]

> [!example] 🎓 Lecture exercise – "Complete the production table" (not in the book), solved with the same rule
> Market demand: period 1 = 160, then **156** from period 2 on. Tip from the slide: *"the production of one stage becomes the demand of the next upstream stage."*
>
> | Period | Market | Focal | 1st tier | 2nd tier | 3rd tier |
> |---|---|---|---|---|---|
> | 1 | 160 | 160 | 160 | 160 | 160 |
> | 2 | 156 | **152** | **144** | **128** | **96** |
> | 3 | 156 | 156 | 160 | 176 | 224 |
> | 4 | 156 | 156 | 156 | 152 | 128 |
> | 5 | 156 | 156 | 156 | 156 | 160 |
> | 6 | 156 | 156 | 156 | 156 | 156 |
>
> Check for period 2 at the focal firm: 156 + (156 − 160) = 152. At the 1st tier: 152 + (152 − 160) = 144. A −4 change (−2.5%) at the market becomes swings between 96 and 224 at the 3rd tier.

![[Summary SOSCM - Macchion-1793614073188.webp]]

> [!info] 📖 Figure 7.9 – Supply chain dynamics with stable vs unstable demand · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=282|p.282]]
> - **Bottom:** the chain *supplier → manufacturer → wholesaler → retail store → consumers*. Deliveries go right, orders go left (dotted).
> - **(a) Stable end demand:** store sales are almost flat, but orders become increasingly **spiky** moving left (manufacturer's orders to its suppliers are the wildest).
> - **(b) Unstable demand** (promotions, panic buying as in COVID-19): the amplification is even more extreme, with huge spikes upstream.
> Consequences: hiring and firing, inefficiency, expediting costs, customer dissatisfaction.

Your lecture note: *we don't know future demand because it depends on customers' lives. Forrester showed that a small demand variation creates large inventory swings along the chain, pushing suppliers to hold big stocks for a demand they can't see. It can be avoided with **visibility** along the chain: a platform that reads sales and communicates them to the whole chain.*

### Controlling supply chain dynamics (the four remedies)

[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=282|p.282–283]]
1. **Align all the channels of information and supply:** harmonise scheduling, stock levels, pricing and planning methods across the chain. Example: **vendor-managed inventory (VMI)**, where the supplier manages the customer's stock.
2. **Increase operational efficiency throughout the chain:** fewer defects, shorter and more reliable lead times, so less replanning and lower safety stocks.
3. **Improve forecasts:** better accuracy means less inventory or excess capacity. Shorter lead times mean you forecast less far ahead ([[Ch04S - Forecasting-claude|Supplement Ch 4]]).
4. **Share information throughout the chain:** make **end-customer demand** visible upstream (**EPOS** point-of-sale data, **EDI**, **blockchain**).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=283|p.283]]
> OPERATIONS PRINCIPLE: Supply chain dynamics (the bullwhip effect) can be reduced by aligning planning and control decisions, improving flow efficiency, better forecasting and information sharing.

---

## 7.7 Blockchain in supply networks

Technically called **distributed ledger technology (DLT)**. Unlike technologies made for one use (robots, face recognition), it evolved from its first application, the accounting method of **Bitcoin**, into many domains including SCM ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=283|p.283]]).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=284|p.284]]
> A blockchain is a decentralised, digitised, public ledger (list) of transactions (movements, authorisations, payments, etc.). A 'block' is a record of new transactions. When each block is completed (verified) it is added to the chain, thus creating a chain of blocks, or 'blockchain'.

**Five principles** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=284|p.284]]):
1. **Distributed database:** everyone has the whole history; no one controls it; verification without an intermediary.
2. **Peer-to-peer transmission:** nodes communicate directly; each stores and forwards to all others.
3. **Transparent, optionally anonymous:** every transaction is visible; users have alphanumeric addresses.
4. **Irreversible records:** each record is linked to all previous ones, so it can't be altered.
5. **Computational logic:** rules can automatically trigger transactions (e.g. **payment on delivery**, "smart contracts").

**Why it suits supply chains** (5 reasons, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=284|p.284]]):
1. Networks are **complex with many operations**, and *the more nodes, the more secure* the ledger, so complexity **strengthens** it.
2. **Huge numbers of transactions**, especially **cross-border** (customs, certifications, regulatory documents).
3. **Security:** cryptography makes tampering practically impossible; a hacker would need **more than half of the nodes**.
4. **Provenance (history) can be trusted:** vital for **food**, **luxury goods** (often forged) and **ethical goods** (avoiding "blood diamonds").
5. It is **distributed**, like supply *networks* themselves.

![[Summary SOSCM - Macchion-1793614547604.webp]]

> [!info] 📖 Figure 7.10 – How blockchain records and verifies supply chain transactions · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=285|p.285]]
> Nodes: supplier, manufacturer, logistics operation, bank, end customer and other operations in the chain, **all connected to all**, each holding a copy of the ledger (the document icons). The numbered steps:
> 1. A transaction is **requested** by an operation in the chain.
> 2. It is **encrypted and broadcast** to the P2P network of nodes.
> 3. The nodes **validate** the transaction and the requester's status using known algorithms.
> 4. Once verified, it is **combined with other transactions into a new block** of data for the ledger.
> 5. The new block is **added to the existing chain**, permanent and unalterable.
> Book case: **TradeLens**, blockchain for global shipping documentation ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=285|p.285]]).

### Critical commentary
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=286|p.286–287]]
- **"Demand chain" rather than "supply chain":** "supply" suggests a **push** mentality (customers consume what suppliers decide to deliver); "demand" stresses customers **pulling** through the chain. Yet "supply chain" is still the common term.
- **Supplier development "imposed" by the customer** has two limits: (1) suppliers have many customers with **conflicting demands**, which can push them to mislead about changes and erode trust; (2) it assumes the **customer's ideas are better**, though suppliers are often as knowledgeable or more. Alternatives: **mutual development**, or **network development** (quality assurance programmes, network-wide technology initiatives such as TradeLens, stakeholder suggestion schemes, supply network councils).
- **Technology** isn't universally welcome: it can **hinder close partnerships**; firms underestimate the difficulty of adoption, so expected returns fail to materialise; there are threats to **employment, privacy and security** (IoT can be hacked: *"we no longer have objects with computers embedded in them: we have computers with objects attached to them"*). Supply chain **security** gets too little attention.

### Summary checklist (book)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=287|p.287]]: Is SCM understood as information *and* product flows, and as dependent on the whole network, applied internally too? Are objectives set for the whole network? Which products are functional or innovative, and so need lean or agile? Where is each relationship on the transactional–partnership spectrum, and are "partnerships" real? Which sourcing approach, and has **category analysis** (the four quadrants) been done? Is supplier selection rigorous and transparent? Do negotiators know the tactics and their risks? Is there two-way information, are SLAs used and evolving, are perception gaps monitored, is there enough supplier development? Is logistics managed? Have IoT and blockchain been considered? What bullwhip-reduction mechanisms are in place?

---

## 📚 Case examples and worked examples (Chapter 7)

> [!example] Case – **Zipline** → see 7.1 above · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=263|p.263–264]]. Key message: **lean when it can be, agile when it needs to be**. Higher transport cost offset by less inventory and obsolescence.

> [!example] Case – **Donkeys: the unsung heroes of supply networks** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=268|p.268–269]]
> **Facts:** in 150 years transport has changed hugely (**containerisation** enabling globalisation, the Wright brothers' flight in **1903**, Benz's "motorwagen" patent in **1886**), but the **donkey** (with ponies, mules and horses, the "packhorses") is still the most widely used transport animal: sugar cane in **Peru**, crops in **Argentina**, flowers in **Jamaica**, maize in **Malawi**, snow sledges in the **USA**, rubbish in **Mexico**, a beach bar in **Brazil**, fish in **Mauritania**, water in **Senegal**, families in **Namibia**, mobile libraries in **Ethiopia**, building materials in **Kenya**, livestock in **Yemen**, **ambulances for women in labour in Afghanistan**, brick kilns in **India**, ploughing in **China**.
> **The logic:** choosing a donkey follows the **same process as any transport mode**: (1) identify the options (constrained by **terrain** and **infrastructure**); (2) judge relative performance (quality, speed, dependability, flexibility, cost, sustainability). Even when an alternative is technically possible, the donkey may give **the best balance**. Ethical issue: packhorses are among the **most mistreated** animals (malnutrition, beatings, overloading, badly fitting packs, extreme climates). Charities lobby for **codes of conduct** and provide veterinary care.
> **Oral use:** logistics mode selection (volume, size, value, terrain), plus ethics and sustainability in the supply chain.

> [!example] Worked example – **Weighted supplier selection: a Belgian commercial bank choosing legal services** · Table 7.2, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=273|p.273]]
> Three firms scored 1–10 on criteria weighted 1–10:
> | Criterion | Weight | Sullivan & Anderson | **Juris Civilis** | Altium Legal |
> |---|---|---|---|---|
> | Quality of service | 10 | 7 → 70 | 8 → 80 | 6 → 60 |
> | Range flexibility | 8 | 5 → 40 | 7 → 56 | 6 → 48 |
> | Volume flexibility | 4 | 8 → 32 | 3 → 12 | 7 → 28 |
> | Average service speed | 7 | 5 → 35 | 8 → 56 | 9 → 63 |
> | Record of dependability | 9 | 4 → 36 | 8 → 72 | 7 → 63 |
> | Sustainability | 4 | 5 → 20 | 6 → 24 | 7 → 28 |
> | Potential innovation | 3 | 5 → 15 | 7 → 21 | 7 → 21 |
> | Price of service | 6 | 9 → 54 | 6 → 36 | 5 → 30 |
> | **Total** | | **302** | **357** ✅ | **341** |
> **Juris Civilis** is preferred (subject to negotiation). Note that the **cheapest firm** (S&A, price score 9) comes **last**: price weighs only 6, while quality (10) and dependability (9) weigh most.

> [!example] Case – **Twice around the world for Wimbledon's tennis balls** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=279|p.279]] (Fig 7.8)
> **Slazenger**, Wimbledon's ball supplier **since 1902**: the balls and their materials travel **81,385 km**, across **11 countries and 4 continents**. Clay from **South Carolina (USA)**, silica from **Greece**, magnesium carbonate from **Japan**, zinc oxide from **Thailand**, sulphur from **South Korea**, rubber from **Malaysia** → **Bataan (Philippines)**, where the rubber is **vulcanised** and the balls made. **Wool from New Zealand → felt pressed in Stroud (UK)** (more technical expertise) **→ flown back** to Bataan. Naphthalene from **Zibo (China)**, glue from **Basilan (Philippines)**, tins from **Indonesia**, then to Wimbledon. Prof. Mark Johnson (Warwick): it looks "ludicrous", but it is **the most cost-effective way**, since production sits near the main materials and low-cost labour, while the best wool and felt expertise are kept.
> **Oral use:** global sourcing and location trade-offs, logistics costs vs quality; links to Ch 4 (offshoring, reshoring).

> [!example] Case – **TradeLens: blockchain revolutionises shipping** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=285|p.285–286]]
> In **January 2018** **Maersk** and **IBM** (an early **Hyperledger** member) formed a joint venture for a blockchain platform built on **open standards** for the whole shipping ecosystem. Context: **more than 80%** (over **$4 trillion**) of the goods consumers use daily travel by sea; Maersk operates ports and logistics in **130 countries**. Trade documentation could cost up to **one-fifth of the physical transport cost**, because the business was manual and error-prone. CEO Michael J. White: aim for *"a fully open platform"*. Named **TradeLens** at the end of 2018, it was adopted by carriers representing **more than 50% of global container cargo**, **including competitors** (CMA CGM, Hapag-Lloyd, MSC, Namsung, ONE). Hapag-Lloyd: *"…greater trust, transparency and collaboration across supply chains."*
> **Oral use:** blockchain principles in practice, **co-opetition** (Ch 4) and network development.

> [!example] End-of-chapter case study – **Supplier selection at Hinkley Point C (EDF)** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=288|p.288–291]]
> **Context:** a new UK nuclear power station (two reactors, turbine halls, substation in the South-West). **Stefano Moretto** (Commercial Director) and **Eva Glines** (Senior Supply Chain Engagement Manager) must source the **site operations services** (everything except construction): expected spend **over £500m** (later **over £1bn**); *"It'll be like a small town."* Five main categories:
> - **Catering:** food production, vending, bars, food waste, distribution, cleaning, hospitality, staff.
> - **Transport:** buses for park and ride, direct service, direct secure (a "fast gate" with no internal transfer), internal site buses.
> - **Accommodation management:** campuses at the site and in Bridgwater, hotel services, grounds and sport, security, 24/7 reception.
> - **Facilities management:** temporary buildings, office services, cleaning, waste and recycling, M&E maintenance, AV.
> - **Infrastructure operations and maintenance:** roads and infrastructure.
> **The dilemma: "big or small?"** One **MNC generalist** per category (tried and tested, a one-stop shop, experience; over **150 tier-1 contracts** to set up in a few months) or **local SMEs** (smaller "bite-size" contracts or **consortia**).
> - **For SMEs (Eva):** MNCs are hard work in negotiations and don't care much about service quality (too many customers); SMEs put the effort in; the services are **not capital- or technology-intensive**, so capability development is easier; local firms are keen (chamber of commerce); **economic and social value** for the region; the project is **controversial locally** (residents opposed, acceptance "fragile").
> - **Against (Stefano and service managers):** SMEs lack experience at this **scale**; they need a lot of **upskilling**; it adds complexity to a "BIG jigsaw"; there is the problem of **scaling** from 3,000–4,000 to **7,000–9,000 workers** at peak.
> Expressions of interest include MNC2 (international transport), MNC3 (hotels), MNC4 (FM and utilities), MNC5 (civil engineering), NC1 (national bus company), SME7 (local buses), SME8 (B&B), SME9 (laundry), SME10 (building trades).
> **Questions and hints:**
> 1. *Service characteristics:* use the **criticality × risk** matrix. Catering, cleaning and laundry are low-tech with many suppliers (non-critical or leverage), so they suit **SMEs and multiple sourcing**. Transport and accommodation at large scale and critical to the project lean towards **MNC/national players or consortia** (delegated sourcing).
> 2. *Other factors:* stakeholders and local politics (CSR, TBL), project risk, the time available, internal capacity to manage many contracts.
> 3. *Preferring SMEs:* (a) engage through supplier events, the chamber of commerce and simplified bidding; (b) configure **lots** or **consortia** (delegated sourcing with a local lead), with **parallel sourcing** across categories for resilience; (c) use **supplier development** (the four stages), with a partnership approach, shared goals and measures, and gradual growth in scale.

> [!note] Book exercises (p.292–293), with the logic of each answer
> - **Super Cycles** (Table 7.5): **inner tubes** (3%, many suppliers, switch in days) → **non-critical**, multiple sourcing. **Frame tubing** (15%, only one capable supplier) → **bottleneck**, single sourcing and develop or qualify an alternative over time, reduce specificity. **Carbon-fibre stem and bars** (32%, many suppliers, easy switch) → **leverage**, competitive tendering, bundling or delegated sourcing. **Fourth component** (35%, few capable suppliers, complex, quality risk) → **strategic**, single or parallel sourcing with **partnership** and supplier development.
> - **Lopez Industries** (retailer → small garment maker → large cloth makers): the bottleneck to flexibility is **cloth**, bought at the start of the season, and Lopez has no leverage over large suppliers. The retailer could **share information** (forecasts, POS data), **use its own leverage** with the cloth makers (aggregate purchases, buy cloth directly or reserve capacity), postpone dyeing or cutting, or split the order into a forecast part and a flexible part.
> - **Bullwhip variants (my calculations with the book's rule):**
>   - (a) Demand **alternating 100/95**: focal firm 100, 90, 105, 90, 105…; 1st tier 80, 120, 75, 120…; 2nd tier 60, 160, 30, 165…; 3rd tier 20, 260, **−100**, 300… A negative value is **impossible** (it means the supplier is left with too much stock and produces nothing), so in reality the chain explodes into **stop-and-go**.
>   - (b) Keeping **half** a period's stock (100 → 95 case): focal 92.5 → 95; 1st 88.8 → 96.2 → 95; 2nd 83.2 → 99.9 → 94.4; 3rd 74.8 → 108.3 → 91.7. **Amplification is much smaller.** Less stock means less buffer adjustment and less bullwhip.
>   - (c) Examples of remedies: VMI, EPOS sharing, EDI, collaborative forecasting (CPFR), smaller and more frequent orders, everyday low pricing instead of promotions.
> - **Small retail shop supplier criteria:** price and terms, reliability, minimum order, delivery frequency, quality, range, local/sustainable, flexibility. Compare with the 3-step qualification and weighted scoring.
> - **Ethical sourcing policy:** motivations are reputation, legal risk, customer and investor pressure, and the TBL. Add environmental impact, anti-corruption, traceability (blockchain), audits and the right to inspect.
> - **Airline catering (Northern Foods + DHL at Heathrow):** (a) airlines outsource to specialists with scale and expertise (non-core); (b) caterers need quality appropriate to the class, cost, **flexibility** (numbers fixed only **6 hours** before take-off, frequent menu changes), **speed and dependability** (turnaround **≤ 40 minutes**); (c) turnaround time = aircraft utilisation, so revenue; (d) the consortium combined **retail-scale food production** (economies of scale, outside the airport) with an already-present airside logistics provider, reconfiguring the network against traditional on-airport caterers.

---

> [!question] 🎤 Likely oral questions
> - *Supply chain vs supply network; which flows does SCM manage?* (Fig 7.2)
> - *SC objectives, and why quality compounds along the chain* (0.99⁷).
> - *Fisher's matrix: lean vs agile, functional vs innovative* (Zipline = lean when possible, agile when needed).
> - *Transactional vs partnership* (Table 7.1, Fig 7.4).
> - *Sourcing strategies and their trade-offs;* draw the parallel sourcing diagram.
> - *Explain the bullwhip effect with numbers* (Table 7.4 or the 160→156 exercise), *its causes and the four remedies.*
> - *How can blockchain help?* (five principles, Fig 7.10).

[[00 - SOSCM index-claude|↑ Index]]

---

## 🗺️ Concept map (Chapter 7)

![[Ch07 concept map-claude.png]]

**Figures A–D of the map, full size:**

![[Ch07 concept map figures-claude.png]]

> [!tip] How to read the map
> **Dark blue box** = the chapter; **coloured blocks** = its sections, each with its key concepts. **Red arrows** = links between concepts (with the relation written on them); **orange dashed boxes** = links to other chapters. **Thumbnails A–D** (blue dashed line) = the book figure or slide that explains that concept, with its page; they are shown full size below the map.
>
> 🎤 **Oral storyline:** What SCM is (flows, chain vs network, Fisher) → relationships → sourcing (risk × criticality) → selection and negotiation → running the chain (SLAs, gaps, development, logistics) → bullwhip and remedies → blockchain.
