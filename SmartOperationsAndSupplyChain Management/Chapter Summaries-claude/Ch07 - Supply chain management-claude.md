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

## 7.1 What is supply chain management?

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

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=266|p.266]]
> OPERATIONS PRINCIPLE: 'Functional' products and services suit efficient (lean) supply chain management; 'innovative' products and services suit responsive (agile) supply chain management.

---

## 7.2 What type of supply chain relationship should be adopted?

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=267|p.267]]
> Transactional (or contractual) relationships involve purchasing products and services in a 'pure' market fashion, often seeking the 'best' supplier every time it is necessary to make a purchase. […] In contrast, partnership (or collaborative) relationships are longer term and involve a commitment to work together over time to gain mutual advantage. These relationships emphasise cooperation, frequent interaction, information sharing, joint problem solving and sometimes even profit sharing.

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

---

## 7.4 Are supply chain dynamics under control? The bullwhip (Forrester) effect

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

## 7.5 Blockchain in supply networks

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=284|p.284]]
> A blockchain is a decentralised, digitised, public ledger (list) of transactions (movements, authorisations, payments, etc.). A 'block' is a record of new transactions. When each block is completed (verified) it is added to the chain, thus creating a chain of blocks, or 'blockchain'.

**Five principles** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=284|p.284]]):
1. **Distributed database:** everyone has the whole history; no one controls it; verification without an intermediary.
2. **Peer-to-peer transmission:** nodes communicate directly; each stores and forwards to all others.
3. **Transparent, optionally anonymous:** every transaction is visible; users have alphanumeric addresses.
4. **Irreversible records:** each record is linked to all previous ones, so it can't be altered.
5. **Computational logic:** rules can automatically trigger transactions (e.g. **payment on delivery**, "smart contracts").

**Why it suits supply chains:** many nodes make it *more* secure; it handles huge numbers of transactions, especially cross-border (customs, certificates); it is very hard to hack (an attacker would need to control more than half the nodes); and it gives traceability.

![[Summary SOSCM - Macchion-1793614547604.webp]]

> [!info] 📖 Figure 7.10 – How blockchain records and verifies supply chain transactions · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=285|p.285]]
> Nodes: supplier, manufacturer, logistics operation, bank, end customer and other operations in the chain, **all connected to all**, each holding a copy of the ledger (the document icons). The numbered steps:
> 1. A transaction is **requested** by an operation in the chain.
> 2. It is **encrypted and broadcast** to the P2P network of nodes.
> 3. The nodes **validate** the transaction and the requester's status using known algorithms.
> 4. Once verified, it is **combined with other transactions into a new block** of data for the ledger.
> 5. The new block is **added to the existing chain**, permanent and unalterable.
> Book case: **TradeLens**, blockchain for global shipping documentation ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=285|p.285]]).

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
