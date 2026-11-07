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

## 5.1 Process design: positioning vs analysis

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

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=195|p.195]]
> OPERATIONS PRINCIPLE: Moving off the 'natural diagonal' of the product–process matrix will incur excess costs.

---

## 5.3 Are process layouts appropriate?

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
- **Functional:** similar activities and resources are located together; flow is complex (hospital radiography, a grinding section, supermarket aisles) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=199|p.199]]).
- **Cell:** items are pre-selected to go to one *cell* that has all the resources they need. It brings order to the complexity of functional layout ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=199|p.199]]).
- **Product (line):** resources are arranged in the sequence the product needs (assembly line, self-service canteen).

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

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=201|p.201]]
> OPERATIONS PRINCIPLE: Layout should include consideration of the look and feel of the operation to customers and/or staff.

---

## 5.4 Are process technologies appropriate?

Process technology means the machines, equipment and devices that transform materials, information and customers. It is distinct from **product technology** (what is embedded in the product) and includes **indirect process technology** (IT systems that run planning and control) ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=203|p.203]]). Three dimensions vary with volume–variety: **automation**, **scale/scalability**, **coupling/connectivity**.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=203|p.203]]
> OPERATIONS PRINCIPLE: Process technology in high-volume, low-variety processes is relatively automated, large-scale and closely coupled when compared to that in low-volume, high-variety processes.

### New technology is changing the diagonal

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=204|p.204]]
> […] digitisation and the vastly increased computing power embedded in many new technologies has made it easier to achieve lower costs while not having to sacrifice the ability to provide variety. For example, the IT systems, databases and algorithms behind internet banking services allow customers to access a very wide variety of customised services, while retaining or enhancing back-office efficiency. Similarly, so-called 3D knitting machines can produce an entire garment […] The effect of this is to 'bend' what has hitherto been accepted as the 'natural' diagonal.

![[Summary SOSCM - Vinelli-1792493409185.webp]]

> [!info] 📖 Figure 5.8 – Technology dimensions and the bent diagonal · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=205|p.205]]
> - **Left arrows:** moving down (towards high volume), automation goes from low to high, scale from low to high, and coupling from broad/unconstrained to narrow/constrained.
> - **Matrix:** top-left = *manual, general-purpose, small-scale, flexible* technology; bottom-right = *automated, dedicated, large-scale, inflexible* technology.
> - **Yellow curve:** newer technologies "bend" the diagonal towards the top-right corner, giving **flexibility at lower cost**. The usual cost–flexibility trade-off is partly overcome. Think of it as the product–process version of *pushing out the efficient frontier* ([[Ch02 - Operations strategy-claude#Trade-offs and the 'efficient frontier'|Ch 2]]).

---

## 5.5 Are job designs appropriate? The division of labour

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

---

> [!question] 🎤 Likely oral questions
> - *Draw and explain the product–process matrix.* Axes, diagonal, process types, and what happens off the diagonal (Fig 5.5: A → B → C).
> - *Manufacturing vs service process types, with examples.*
> - *Process type vs layout type: what is the difference?* Table 5.1, plus pros and cons in Table 5.2.
> - *How is technology changing the diagonal?* Internet banking, 3D knitting (Fig 5.8).
> - *Division of labour pros and cons; job design along the diagonal* (Fig 5.9).

Next → [[Ch06 - Process design 2 - Analysis-claude]]
