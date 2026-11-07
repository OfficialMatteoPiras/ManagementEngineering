---
course: Smart Operations and Supply Chain Management
professor: Andrea Vinelli
chapter: 5
book: "Slack, Brandon-Jones, Burgess – Operations and Process Management (PDF in /pdf)"
tags: [SOSCM, summary, chapter5]
---
# Chapter 5 – Process design 1: Positioning

> [!abstract] In one breath (for the oral)
> Process design is in two parts: **positioning** (this chapter: broad choices about resources) and **analysis** ([[Ch06 - Process design 2 - Analysis-claude|Ch 6]]: detailed activities). Everything is governed by the **volume–variety** position. The **product–process matrix** shows that each process should sit on the **natural diagonal**; this gives the **process types** (project, jobbing, batch, mass, continuous / professional service, service shop, mass service). Off the diagonal you pay excess cost, either through excess flexibility or excess rigidity. The same logic sets **layout** (fixed-position, functional, cell, product), **technology** (automation, scale, coupling) and **job design** (division of labour). New digital technologies **bend the diagonal**.

[[Ch04 - Operations scope and structure-claude|← Ch 4]]

---

## 5.1 Does the operation understand the importance of how it positions its process resources?

- **Design** = *to conceive the looks, arrangement and workings of something before it is constructed*. It is conceptual, but it must work in practice. It works at **two levels of detail**: first the overall shape (positioning the resources), then the detail (analysis of activities). The two are **not strictly sequential**: detailed analysis may force a change in positioning ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=188|p.188]]).
- An operation's **resources are more than the balance sheet**: technology, equipment and facilities, **people** (skills, enthusiasm, creativity) and **intangibles** (knowledge, supply and customer relationships, culture). They also include resources it can **access** through its supply network: *"an operation's ability to access resources is a resource in itself."*
- **Positioning and analysis are related**, mutually supportive *and* mutually limiting. Inappropriate resources restrict what processes can do; conversely, a highly divided, repetitive design can **limit learning**. *"Processes are really the best source of learning that operations managers will ever have"*: thousands of transactions a minute, each an opportunity to learn.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=188|p.188]]
> OPERATIONS PRINCIPLE: Defining process resources (process positioning) and defining process activities (process analysis) are strongly related and ideally should be considered alongside one another.

## Process design: positioning vs analysis

![[Summary SOSCM - Vinelli-1791980573802.webp]]

> [!info] 📖 Figure 5.2 – Two parts of process design · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=189|p.189]]
> - **Left (blue), process positioning = defining process resources:** broadly position the resources by the volume and variety they must produce, then lay out the process, decide the technology and design the jobs. **This chapter.**
> - **Right (yellow), process analysis = defining process activities:** align with performance objectives, map the current design, configure tasks and capacity, include variability. **Chapter 6.**
> - **The two arrows:** resources limit what processes can do, and processes should build capabilities that improve resources. The two parts constantly **feed each other**.

---

## 5.2 Do processes match volume–variety requirements?

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=188|p.188]]
> Two factors are particularly important in process design: these are the volume and variety of the products and services that it processes. Moreover, volume and variety are related, in so much as low-volume operations processes often have a high variety of products and services, and high-volume operations processes often have a narrow variety of products and services. So, we can position processes on a continuum […]

> [!important] OPERATIONS PRINCIPLE
> The design of any process should be governed by the volume and variety it is required to produce. ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=189|p.189]])

### The product–process matrix

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=189|p.189]]
> The underlying idea of the product–process matrix is that many of the more important elements of process design are strongly related to the volume–variety position of the process. […] This means that most processes should lie close to the diagonal of the matrix that represents the 'fit' between the process and its volume–variety position. This is called the 'natural' diagonal.

![[Summary SOSCM - Vinelli-1791980537339.webp]]

> [!info] 📖 Figure 5.3 – The product–process matrix · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=190|p.190]]
> - **Horizontal (top arrow):** the volume–variety position, from **high variety / low volume** (left) to **low variety / high volume** (right).
> - **Vertical (left arrow):** the process design characteristics (performance objectives, tasks, flow, layout, technology, job design).
> - **The diagonal:** the "natural" line of fit. A process's design should change *together* with its volume–variety position.

### Process types

![[Summary SOSCM - Vinelli-1791981164429.webp]]

> [!info] 📖 Figure 5.4 – Process types along the diagonal · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=191|p.191]]
> - **Left matrix (manufacturing):** project → jobbing → batch → mass → continuous, from top-left (high variety, low volume) to bottom-right.
> - **Right matrix (services):** professional services → service shops → mass services.
> - **Two side arrows:** process **tasks** go from diverse/complex to repeated/divided; process **flow** goes from intermittent to continuous.
> - **The boxes overlap:** the types are not sharp categories (batch in particular covers a wide range).

| Type | Volume / variety | Key traits | Examples |
|---|---|---|---|
| **Project** | Very low / very high | Discrete, highly customised, long timescale; resources dedicated to *one* product; ill-defined, changing activities | Shipbuilding (🎓 **Fincantieri**), construction, movies, oil wells |
| **Jobbing** | Low / very high | Each job *shares* resources with others; low repetition, many one-offs | Specialist toolmakers, furniture restorers, made-to-measure tailors |
| **Batch** | Medium / medium (widest range) | Several units at a time; repetition while the batch runs | Machine tools, gourmet frozen food, car components, most clothing |
| **Mass** | High / narrow *effective* variety | Repetitive, predictable; many variants that don't change the basic process | Car plants, frozen pizza, beer bottling |
| **Continuous** | Very high / very low | Endless flow, inflexible and capital-intensive technology | Refineries, electricity, steel, server farms |
| **Professional services** | Low / high | High customisation, staff discretion, people-based, focus on *how* the service is delivered | Consultants, lawyers, architects, doctors |
| **Service shops** | Medium | Mix of front and back office; standardised "product" with customised process | Banks, shops, hotels, restaurants, car rental, schools |
| **Mass services** | High / low | Many transactions, little customisation, equipment-based, value added in the back office | Supermarkets, rail networks, airports, call centres |

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=189|p.189]]
> OPERATIONS PRINCIPLE: Process types indicate the position of processes on the volume–variety spectrum.

### Moving off the natural diagonal

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=194|p.194]]
> A process lying on the natural diagonal of the matrix shown in Figure 5.3 will normally have lower operating costs than one with the same volume–variety position that lies off the diagonal. […] Processes that are on the right of the 'natural' diagonal […] are likely to be more flexible than seems to be warranted by their actual volume–variety position. […] Conversely, processes that are on the left of the diagonal […] will therefore be 'over-standardised' and probably too inflexible for their volume–variety position.

![[Summary SOSCM - Vinelli-1791982906967.webp]]

> [!info] 📖 Figure 5.5 – Product–process matrix for the meter-installation process · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=196|p.196]]
> - **Above/right of the diagonal = excess process flexibility:** too flexible for the volume–variety position, so **higher cost**.
> - **Below/left of the diagonal = excess process rigidity:** too standardised, so it **cannot change easily**, which also raises cost.
> - **The story:** **A** is the original position, on the diagonal. Volume rises and variety falls, so the process moves to **B** without its design changing: it is now **too flexible** for its new position. Redesigning the process (more standardisation and repetition) brings it down to **C**, back on the diagonal.
> - **Right axis:** flexibility performance. **Bottom axis:** cost performance.
> - **Caution (book):** a *conceptual* model. Moving off the diagonal clearly costs more, but by how much is hard to quantify.
> - **Why a process ends up off the diagonal:** its volume–variety position **changed without the design changing**, or design changes were introduced **without considering** their fit. The first step in examining any existing process is to check whether it sits on the diagonal ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=195|p.195]]).
> - Full story in the **meter installation worked example** at the end of the chapter.

**Layout, technology and jobs** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=195|p.195]]): moving along the diagonal changes the two ingredients of process resources (**technology and people**) and how they are arranged (**layout**). The rest of the chapter covers them in that order.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=195|p.195]]
> OPERATIONS PRINCIPLE: Moving off the 'natural diagonal' of the product–process matrix will incur excess costs.

---

## 5.3 Are process layouts appropriate?

**Objective of layout** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=196|p.196–197]]): a well-sequenced process is useless if its activities are physically located so as to cause excessive movement. Usually the aim is to **minimise movement**. But in information processes, where distance hardly matters, other criteria can dominate (an international bank **groups its foreign-exchange dealers** to encourage discussion, even though trades are processed elsewhere), and high-visibility processes may fix the layout to shape **customer behaviour**.
Layout also follows volume–variety:
- **Very low volume, high variety:** flow is not a major issue (e.g. **telecom satellite manufacture**: each product is different and flows very rarely).
- **Higher volume, still high variety:** flow matters, but flow patterns vary. A **library** arranges categories to minimise the average distance for *most* customers, inconveniencing a minority.
- **A distinct category with similar needs emerges:** group the resources into a **cell**.
- **Low variety, high volume:** regular flow, a classic **flow line**.

![[Summary SOSCM - Vinelli-1791984429619.webp]]

> [!info] 📖 Figure 5.6 – Layouts along the volume–variety diagonal · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=197|p.197]]
> From top-left to bottom-right:
> - **Fixed-position:** the product stays still and the resources come to it (one circle with arrows pointing in).
> - **Functional:** similar resources are grouped together; items follow complex routes between them.
> - **Cell:** a group of mixed resources dedicated to a family of products, so flow is tidier inside small cells.
> - **Product:** resources in a line along the fixed sequence of the product.
> **Left arrow:** layout is *based around process resources* at high variety and *based around products/services* at high volume.

**The four basic layouts:**
- **Fixed-position:** the transformed thing is too large, delicate or immobile to move, so resources move to it. Book examples: power-generator construction (too large), open-heart surgery (too delicate), high-class restaurant (customers would object to moving) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=197|p.197]]).
- **Functional:** the needs and convenience of the **transforming resources** dominate. Similar activities and resources are located together (convenience or better utilisation), and items follow their own route, so flow is **complex**. Book examples: **hospitals** (radiography and labs used by many patient types); **aircraft-engine parts** (heat treatment needs fume extraction; machining centres share technical support; grinding gets high utilisation because all parts pass one section); **supermarkets** (tinned goods together for restocking, freezers share technology, fresh vegetables together to look attractive) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=199|p.199]]).
- **Cell:** items are **pre-selected** (or select themselves) to go to one *cell* that has all the resources for their immediate needs. Inside, the cell can be arranged in any way; afterwards items may go to another cell. It brings order to the complexity of functional layout. Book examples: **computer components** for one customer with special quality needs; the **"lunch" area** in a supermarket (sandwiches, snacks, drinks); a hospital's **maternity unit** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=199|p.199]]).
- **Product (flow/line):** people and equipment are located **entirely for the convenience of the transformed resources**, which follow a prearranged route in sequence. Flow is clear, predictable and easy to control. Examples: **car assembly** (almost all variants of a model follow the same sequence); **self-service cafeteria** (starter, main, dessert, drink; it also controls customer flow) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=200|p.200]]).

**Why layout matters** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=200|p.200]]): changing it is costly, difficult and disruptive (not something to repeat often); a wrong layout adds **cost every time an item is processed**; and a good layout gives **clarity and transparency** to the flow, so everyone sees they are part of one process.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=197|p.197]]
> OPERATIONS PRINCIPLE: Resources in low-volume, high-variety processes should be arranged to cope with irregular flow. · Resources in high-volume, low-variety processes should be arranged to cope with smooth, regular flow.

### Layout selection

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=200|p.200]]
> There is often some confusion between process types and layout types, but they are not the same thing. […] Layout is a narrower concept but is very clearly linked to process type. Just as process type is governed by volume and variety, so is layout. But for any given process type there are usually at least two alternative layouts.

![[Summary SOSCM - Vinelli-1792493139220.webp]]

> [!info] 📖 Table 5.1 – Alternative layouts for each process type · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=200|p.200]]
> | Manufacturing type | Possible layouts | Service type |
> |---|---|---|
> | Project | Fixed-position, functional (+ cell for services) | Professional service |
> | Jobbing / batch | Functional, cell | Service shop |
> | Mass / continuous | Cell, product (continuous: product only) | Mass service |
> **Takeaway:** each process type allows **2–3** layouts. The choice depends on the relative priority of **cost vs flexibility**.

![[Summary SOSCM - Vinelli-1792493395029.webp]]

> [!info] 📖 Table 5.2 – Advantages and disadvantages of the basic layouts · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=201|p.201]]
> | Layout | ✅ | ❌ |
> |---|---|---|
> | **Fixed-position** | Very high mix and product flexibility; product/customer not moved; high task variety for staff | High unit costs; difficult scheduling of space and activities; lots of movement of plant and staff |
> | **Functional** | High mix flexibility; robust to disruption; easy supervision of equipment | Low utilisation; high WIP or customer queueing; complex flow hard to control |
> | **Cell** | Good cost–flexibility compromise; fast throughput; group work → motivation | Costly to rearrange; may need more equipment; lower plant utilisation |
> | **Product** | Low unit cost at high volume; equipment specialisation; convenient movement | Low mix flexibility; not robust to disruption; very repetitive work |

### Servicescape: the look and feel of a high-visibility process
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=201|p.201]]
In high-visibility processes the **look and feel** can matter as much as, or more than, "objective" criteria such as cost or distance moved. The **servicescape** is the environment of the operation: **ambient conditions, space factors, and signs and symbols** create an "environmental experience" for employees and customers that should support the **service concept**. Responses fall into three categories: **cognitive** (what people think), **emotional** (what they feel), **physiological** (the body's experience). A servicescape also includes **uncontrollable stimuli**, above all **other customers** (number, demographics, appearance), alongside controllable ones (colour, lighting, design, space, music).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=201|p.201]]
> OPERATIONS PRINCIPLE: Layout should include consideration of the look and feel of the operation to customers and/or staff.

---

## 5.4 Are process technologies appropriate?

Process technology means the machines, equipment and devices that transform materials, information and customers. It is distinct from **product technology** (what is embedded in the product) and includes **indirect process technology** (IT systems that run planning and control) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=203|p.203]]). Three dimensions vary with volume–variety: **automation**, **scale/scalability**, **coupling/connectivity**.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=203|p.203]]
> OPERATIONS PRINCIPLE: Process technology in high-volume, low-variety processes is relatively automated, large-scale and closely coupled when compared to that in low-volume, high-variety processes.

Few operations have been unaffected by technology advances, and the pace isn't slowing. Many businesses spend **more on the IT systems that run their processes** (indirect technology) than on direct process technology. High variety needs **general-purpose** technology; high volume can use **dedicated** technology ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=203|p.203]]).

**The three dimensions** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=203|p.203–204]]):
1. **Degree of automation:** how far the technology acts and decides by itself. All technology needs some human intervention: minimal in a **petrochemical refinery** (periodic maintenance), total in **keyhole surgery** (the surgeon is the "brain"). An **investment bank's** customised deals worth hundreds of millions are processed in the back office with **spreadsheets** and skilled staff deciding, while simple **equity trades** (tens of thousands a day, in milliseconds) are **automated**.
2. **Scale / scalability:** one large fast printer vs several small ones; one or two wide-bodied aircraft vs many small ones. **Large scale** is cheaper per item but needs high volume and low variety. **Small scale** is **nimble and flexible** (4 small machines make 4 different products at once; 1 big machine makes one product at a time) and **robust** (3 small machines: one breaks and 1/3 of capacity is lost; 1 big machine: capacity drops to zero). **Scalability** (for IT) = the ability to shift to a different level of useful capacity **quickly and cost-effectively**; it relies on a consistent IT architecture and high process standardisation.
3. **Coupling / connectivity:** linking separate activities in one integrated system. **Tight coupling** gives fast throughput, low inventory (no gaps between stages) and simple, predictable flow. But it is **expensive** (each connection costs capital), **vulnerable** (one failure stops the whole) and **constrains** products to a predetermined flow, so it suits low variety and high volume. High variety needs **open, unconstrained** coupling.

### New technology is changing the diagonal

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=204|p.204]]
> […] digitisation and the vastly increased computing power embedded in many new technologies has made it easier to achieve lower costs while not having to sacrifice the ability to provide variety. For example, the IT systems, databases and algorithms behind internet banking services allow customers to access a very wide variety of customised services, while retaining or enhancing back-office efficiency. Similarly, so-called 3D knitting machines can produce an entire garment […] The effect of this is to 'bend' what has hitherto been accepted as the 'natural' diagonal.

![[Summary SOSCM - Vinelli-1792493409185.webp]]

> [!info] 📖 Figure 5.8 – Technology dimensions and the bent diagonal · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=205|p.205]]
> - **Left arrows:** moving down (towards high volume), automation goes from low to high, scale from low to high, and coupling from broad/unconstrained to narrow/constrained.
> - **Matrix:** top-left = *manual, general-purpose, small-scale, flexible* technology; bottom-right = *automated, dedicated, large-scale, inflexible* technology.
> - **Yellow curve:** newer technologies "bend" the diagonal towards the top-right corner, giving **flexibility at lower cost**. The usual cost–flexibility trade-off is partly overcome. Think of it as the product–process version of *pushing out the efficient frontier* ([[Ch02 - Operations strategy-claude#Trade-offs and the 'efficient frontier'|Ch 2]]).

---

## 5.5 Are job designs appropriate?

**Job design** = how people carry out their tasks within a process. It positions expectations and perceptions of contribution, defines relations with colleagues and communication channels and, most importantly, **helps develop the culture** of the organisation (shared values, beliefs, assumptions). Badly designed jobs can destroy a process's potential whatever its layout or technology ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=205|p.205]]).

**Universal aspects (whatever the volume and variety):**
- **Safety:** protect everyone from physical or mental harm (the primary, universal objective).
- **Ethics:** no task that is illegal or (within limits) conflicts with strongly held ethical beliefs.
- **Work–life balance:** a healthy split between work time and time away from work.
These also improve performance, but they should be followed **for their own sake**.

**Aspects that depend on volume and variety** (Fig 5.9): an **architect** on major projects has wide, creative, undefined and intrinsically satisfying tasks; a clerk in the architect's accounts office **keying in invoices** has a repetitive, tightly defined job that can't rely on intrinsic interest. Three aspects vary: (1) **division of labour** (task allocation); (2) **job definition**; (3) **job commitment** methods ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=206|p.206]]).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=206|p.206]]
> OPERATIONS PRINCIPLE: Job designs in high-volume, low-variety processes are relatively closely defined with little decision-making discretion and needing action to encourage commitment when compared to those in low-volume, high-variety processes.

### The division of labour

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=206|p.206]]
> Separating tasks into smaller parts between individuals is called the division of labour. Perhaps its epitome is the assembly line […]

| ✅ Advantages of division of labour | ❌ Drawbacks |
|---|---|
| **Faster learning** (short, simple tasks) | **Monotony**, leading to absenteeism, staff turnover, errors |
| **Easier automation** | **Physical injury** (RSI, repetitive strain injury) |
| **Less non-productive work** (searching, positioning tools) | **Low flexibility** (product change → redesign the whole line) |
| | **Poor robustness** (one stage fails → the whole line stops) |

![[Summary SOSCM - Vinelli-1792494197095.webp]]

> [!info] 📖 Figure 5.9 – Job design along the diagonal · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=206|p.206]]
> - **Left arrows:** division of labour from broad → narrow; job definition from flexible → closely defined; job commitment from task-based → process-based.
> - **Top-left (low volume, high variety):** *broad, relatively undefined jobs with decision-making discretion and intrinsic job commitment* (e.g. a consultant).
> - **Bottom-right (high volume, low variety):** *narrow, closely defined jobs with little discretion, needing action to aid commitment* (e.g. an assembly operator, who needs job rotation, enlargement or empowerment to stay motivated).

### How far should jobs be defined?
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=207|p.207]]
High-variety jobs are hard to define except in general terms. They need **tacit knowledge** and **discretion**, so they are defined by **outcome** rather than activity (the architect: "achieve overall coordination, articulate the vision, keep stakeholders comfortable…"). Low-variety, high-volume jobs are defined **step by step**, with staff trained to follow them.

### How to encourage job commitment
Commitment depends on job history, co-workers and personal circumstances, but also on volume and variety. In **high-variety** jobs it comes from the **task itself** (skill, decisions). In **low-variety, high-volume** jobs (high division of labour, little discretion) work can be **alienating**, so satisfaction must be **designed in** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=208|p.208]]):

| Approach | What it is | Example / note |
|---|---|---|
| **Job enlargement** | More tasks *of the same type* (horizontal) | A 10-person line becomes 2 parallel lines of 5, so each person does twice as many tasks |
| **Job enrichment** | More tasks **plus more decision-making and autonomy** (vertical) | Operators also do routine maintenance, record-keeping, material supply, quality monitoring |
| **Job rotation** | Move people periodically between task sets | Builds skill flexibility, slightly less monotony; can **disrupt flow** and workers' **rhythm** |
| **Empowerment** | More ability and authority to change *how* the job is done | Limited in technology-constrained processes (chemical plants), wider in less-defined ones |
| **Team working** | Self-managed teams with overlapping skills and discretion | Teams may control task allocation, scheduling, quality, even hiring |
| **Work–life balance** | Harder today (no clear working hours, shared work/personal devices, home working) | Benefits: retention, reputation in the jobs market, fewer health problems, more effective staff |

### Critical commentary
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=209|p.209]]
1. Splitting process design into **positioning vs analysis is artificial**: they are interrelated, and one could treat layout and process mapping together.
2. The core assumption that **volume and variety govern design** is conventional for layout and technology, less so for **job design**: many argue most job-design decisions don't vary with volume and variety.
3. The treatment of job design is said to be over-influenced by the (to some, discredited) **"scientific management"** tradition (work study, time and motion).

### Summary checklist (book)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=209|p.209]]: Are process types understood and matched to volume–variety? Are processes on the diagonal, and are the consequences of moving off it understood? Are layout choices (flexibility vs cost) understood? Which of the four basic layouts fits? Are the three technology dimensions understood? Are jobs safe, ethical, with good work–life balance? Are division of labour, job definition and commitment mechanisms appropriate for each process's volume–variety?

---

## 📚 Case examples and worked examples (Chapter 5)

> [!example] Case – **Dishang and Sands Films**: opposite ends of the volume–variety spectrum · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=190|p.190–191]]
> **Context:** the world garment market is worth about **€1.3 trillion** and employs up to **75 million** people.
> - **Dishang Group (China):** founded 1993, **$1.5 billion** turnover; makes garments for **Zara, Matalan, Adidas**. When Chinese labour costs rose it expanded to **Cambodia, Myanmar, Bangladesh**. **73 million garments a year**, **80 wholly-owned factories in 12 locations**; automated technology, in-line and end-of-line quality control, **AQL** inspection levels per customer; a digital library of **50,000 fabrics** with image-based search for similar styles. Chairman Lihua Zhu's three success factors: (1) **volume strength**, which gives buying power; (2) in-house design and specialised factories, so brands get "everything" in one place; (3) its own international offices, **cutting out the middleman** (disintermediation, Ch 4). → **High volume, low variety: mass process.**
> - **Sands Films (London):** costume workshop for film, stage and TV, an "**Aladdin's cave**". From a single outfit to a wide range of specially designed costumes over a long production. Cutting, dyeing, printing, **corset and crinoline making, millinery**; actors visit and meet their character for the first time; work starts only once the project is approved and a designer appointed; **each costume needs different skills and a different route** through the stages. → **Low volume, high variety: jobbing process.**
> **Oral use:** an example of both ends of the product–process matrix in the same industry.

> [!example] Case – **Legal & General's modular homes** (mass process in construction) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=193|p.193]]
> **Facts:** a financial services group (more than **£19 billion** invested in homebuilding, regeneration and clean energy) builds houses **like cars**: modules made **off-site in a factory** and transported to site. Managers came from **Rolls-Royce** (CEO Rosie Toogood) and **automotive** (Ops Director Stuart Lord). "**Everything new, but nothing new**": an assembly line with **4 large and 4 smaller computer-controlled cutting and milling machines** cutting timber panels more precisely than on site. Modules leave with wiring, plumbing, decoration, carpets, kitchens and bathrooms; a home has one or more modules. Every millimetre is **digitally modelled** before production; processes are **standardised and simplified**; **continuous improvement** almost **halved delivery time**. Environmental benefits: **less water and site waste** (fewer skips, a tidier and safer site), more energy-efficient homes (Ellen MacArthur Foundation).
> **Exercise 5 in the book:** does it invalidate the volume–variety idea? **No.** L&G *reduced variety* (standard modules) to reach mass volumes, so it moved *down the diagonal* together with its process design. It **confirms** the model.

> [!example] Worked example – **Meter installation at a water utility** (moving off the diagonal) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=195|p.195–196]] → Fig 5.5 above
> - **Before (A):** installing and repairing a wide variety of meters in very different pipe systems. A supervisor **surveys** first, then **skilled plumbers** install on an agreed date: a **jobbing** process.
> - **The change:** the company installs **free** a new **standard remote-reading meter** (read via the phone line, which saves reading costs) with **universal quick-fit joints**. More plumbers are hired. Pilot: start with the customers who have the **oldest meters**, *leaving every other aspect of the process as it was*.
> - **Result (B): failure.** Old meters were scattered, so there was **long travel**. Customers hadn't asked for the visit, so they **forgot appointments**. Costs were far higher than forecast and plumbers were **frustrated** by a now standardised job. Variety fell and volume rose, but the process was still designed for jobbing: **excess flexibility and high cost**.
> - **Redesign (C):** target **small geographic areas**, **drop the survey** (98% of installations done in one visit), use **less expensive, less skilled labour**. Back on the diagonal: efficient.

> [!example] Case – **Reconciling quiet and interaction in laboratory layout** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=198|p.198–199]] (Fig 5.7)
> Labs have different service needs (temperature, extraction, no vibration) and two kinds of work: **active experimentation and conversation** vs **quiet reflection and writing up**. At the **Francis Crick Institute** (London), some complain the open plan makes concentration hard, but it has promoted ad hoc meetings and **new collaborations**. Prof. **Alan Penn**: busy circulation spaces let groups share ideas (people stop and join conversations in doorways). **Fig 5.7:** in the original layout conversations happen next to the **quiet writing area**; in the improved layout, a small change moves scientists' circulation (and their conversations) **towards the entrance**, away from the quiet area, so there is no interference.
> **Oral use:** layout isn't only about movement cost but about the **look, feel and behaviour** of people (servicescape).

> [!example] Case – **Ducati factory and Google offices: they have to look good** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=202|p.202]]
> - **Ducati (Bologna, since 1946):** **350 bikes a day** in the busy season. Assembly starts in a **"supermarket"** zone for each model, where **kits** with exactly the right parts are put together for every stage. *A part left in the tray means something went wrong.* **Just-in-time**, learned from **Porsche** engineers who learned it from **Toyota**: **−85% defects**. The factory is also a **tourist attraction** (tours and museum), so it is designed for visitors too, as a marketing and customer-relations device. Ducati riders park inside the gates; others park outside.
> - **Google offices:** **more than 70% of UK GDP** is reportedly generated by people at desks, so office layout matters as much as factory layout. Google designs for **creativity and collaboration**: nobody is more than **100 metres from food**; eco-friendly kitchens; quiet areas (libraries, aquariums); spaces for relaxing (even football). Design considers **culture, etiquette and rituals** and **observes behaviour** (where people spend time, where productive meetings happen, when the office is empty or noisy).

> [!example] End-of-chapter case study – **McPherson Charles solicitors** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=210|p.210–211]]
> Bristol law firm: **21 partners, ~400 staff, 15 teams**. Managing Partner **Grace Whelan** runs a meeting on improving operations ("Plans for the Future"). Positions: **Simon Reece** says the people and relationship skills matter most (raise revenue); **Hazel Lewis** says technology and systems (cut costs); **Kate Hutchinson** says clients are cost-conscious and the firm "over-engineers" its services, so non-qualified staff could do much of the work.
> - **Family Law (Simon):** **89 "high value" clients** (word of mouth, wealthy, personal touch, no standard procedures, travel worldwide) plus **~750 routine** divorce and counselling cases (about 1/3 of income). Work is mixed for each lawyer; empowerment; an **open-plan office** around a specialist library.
> - **Property (Kate):** up to **100 domestic clients a week**; one contact solicitor; a **4-stage specialised process** (land registry searches → bank and mortgage liaison → surveys → completion). Plus about **5 "specials" a week** (volume remortgages, complex one-offs, "plot sales" for two big builders) that go through the **same** process.
> - **Litigation (Hazel):** bulk **debt collection** for **17 clients (5 = 85% of volume)**; a **semi-automated** process (data input → standard letters → queries → court if needed); work in batches; about 7 new cases a week.
> **Questions and hints:**
> 1. *Services:* high-value family, routine family, domestic property, special property, bulk debt collection.
> 2. *Volume–variety:* high-value family = professional service (low volume, very high variety); routine family = service shop; domestic property = towards mass service; property "specials" = high variety pushed through a mass process (**off the diagonal: excess rigidity**); debt collection = mass service (high volume, low variety, automated).
> 3. *Layout, technology, jobs:* family = open plan, little technology, broad empowered jobs; property = product-like 4-stage flow, divided jobs; litigation = semi-automated, closely defined jobs.
> 4. *Matrix:* the mismatches are the **property specials** (variety too high for the line) and possibly **routine family** work done by highly skilled, high-discretion staff (**excess flexibility**, as in Kate's point). Each partner is right for their own service: the answer is a different process per service.

> [!note] Book exercises (p.212–213), with the logic of each answer
> - **Retail bank:** service categories (transactions, advice, mortgages, business) get separate processes (ATM/app vs advisor) with different objectives (cost and speed vs quality and flexibility).
> - **Educational kits (Figs 5.10–5.11):** compare the flow between departments. Put departments with the **heaviest flow next to each other**; reconfigure the layout for the new flow matrix (minimise load × distance).
> - **International Frozen Pizza Co.:** Market 2 (20,000 t, 12 varieties) suits **automation (APAS)**. Markets 1 (25,000 t, 20 varieties, frequent innovation) and 3 (10,000 t, premium, wide range) have high variety, so APAS would put them **off the diagonal** (excess rigidity). Market 2 should prove that APAS can handle variety (the "new technology bends the diagonal" argument).
> - **Kitchen-equipment direct marketing:** the DC is built for high volume and medium orders. **Web orders** (many customers, 1–2 items) need higher variety and smaller orders; **discount stores** need few large orders of a narrow range. Neither fits the current process: subcontract or redesign (separate processes per channel = operation-within-an-operation).
> - **Supermarket:** a conventional supermarket is a **functional layout**, but the *customer* moves and chooses their own route (unlike a factory); **customer tracking** data helps design the layout and servicescape.

---

> [!question] 🎤 Likely oral questions
> - *Draw and explain the product–process matrix.* Axes, diagonal, process types, and what happens off the diagonal (Fig 5.5: A → B → C).
> - *Manufacturing vs service process types, with examples.*
> - *Process type vs layout type: what is the difference?* Table 5.1, plus pros and cons in Table 5.2.
> - *How is technology changing the diagonal?* Internet banking, 3D knitting (Fig 5.8).
> - *Division of labour pros and cons; job design along the diagonal* (Fig 5.9).

Next → [[Ch06 - Process design 2 - Analysis-claude]]

---

## 🗺️ Concept map (Chapter 5)

![[Ch05 concept map-claude.png]]

> [!tip] How to read the map
> **Dark blue box** = the chapter; **coloured blocks** = its sections, each with its key concepts. **Red arrows** = links between concepts (with the relation written on them); **orange dashed boxes** = links to other chapters. **Thumbnails** (blue dashed line) = the book figure or slide that explains that concept, with its page.
>
> 🎤 **Oral storyline:** Positioning vs analysis → the product–process matrix and the process types on the diagonal → then show that the diagonal also drives layout, technology and job design (red arrows).
