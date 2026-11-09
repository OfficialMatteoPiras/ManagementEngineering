---
course: Smart Operations and Supply Chain Management
professor: Laura Macchion
chapter: 6
book: "Slack, Brandon-Jones, Burgess – Operations and Process Management (PDF in /pdf)"
tags: [SOSCM, summary, chapter6]
---
# Chapter 6 – Process design 2: Analysis

> [!abstract] In one breath (for the oral)
> Detailed process design matters because process networks make up the operation's performance. Operations managers must own it; it is **people *and* process**, not people *vs* process. First set **process performance objectives**: strategic ones (Table 6.1) and **flow objectives** (throughput rate, throughput time, WIP, utilisation, linked by **Little's Law**). Then **map** the process (levels of mapping, **visibility**, customer journey). Then **configure tasks and capacity**: task precedence, **cycle time** (vs takt time), number of stages, **series (long-thin) vs parallel (short-fat)**, **bottleneck**, **balancing loss**. Finally recognise **variability** (activity time and arrival time): waiting time explodes as utilisation approaches 100%.

[[Ch05 - Process design 1 - Positioning-claude|← Ch 5]]

---

## 6.1 Is the importance of detailed process design understood?

- These detailed decisions are **not mere "technicalities"**: they largely determine the actual performance of the process and therefore of the business. Detailed analysis must always be **thought through in the context of the positioning** in Ch 5 ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=218|p.218]]).
- Processes are the **building blocks** and link into **internal process chains**, and *no chain is stronger than its weakest link*: the output is limited by the **worst stage**, and no operation is better than its **weakest process**. The root causes of business failure are often failures of everyday processes.
- **Why it matters (from Changi):** good design pays back visibly, and bad design shows quickly in cost and service (a broken baggage system, slow security, a holiday rush). Don't be afraid to analyse processes **in great detail**: understand the current reality, allocate tasks and capacity carefully, and design for **variability**. Resources add their full value only through how they are used in processes, so periodically review: which are the key processes, what are they good at, where are they weak or vulnerable, how will they cope with the future ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=219|p.219–220]]).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=219|p.219]]
> OPERATIONS PRINCIPLE: Processes should always be designed to reflect customer and/or market requirements.

**Processes as networks** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=220|p.220]]): thinking of the process within the internal network (1) helps set its **objectives**; (2) gives everyone a **line of sight** to end customers ("how can each process help the intermediate processes between them and the customer?"); (3) clarifies the role of **suppliers** (looking backwards); (4) shows that process chains can become **channels for disruption** when things go wrong.

### "People vs process" is a false distinction

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=220|p.220]]
> The argument, sometimes referred to as 'people versus process', is based on a false distinction. People are the most important element in most processes, and 'process' is simply how we do things. In other words, not all processes are the same, nor should they be treated in the same way. […] The way processes are designed should depend on what we want them to do.

Two extreme views: (1) *everything is a process*, so standardise it all ("every time, all the time"); (2) *everything is about people*, and you can't reduce work to steps. Both are simplistic. Processes can be tightly specified **or** loose (broad objectives plus professional judgement).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=221|p.221]]
> OPERATIONS PRINCIPLE: Not all processes are the same; some need to be highly specified, but not all. 'Process' simply means 'how we do things'.

![[Summary SOSCM - Macchion-1792400270714.webp]]

> [!info] 📖 Figure 6.2 – A process network with an internal process chain · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=220|p.220]]
> - **Big box** = the operation, between **external suppliers** (left) and **external customers** (right).
> - **White boxes** = individual processes in the internal **process network**.
> - **Dark-blue boxes** = one **internal process chain**: a sequence of processes linked as internal supplier → internal customer to deliver a specific output.
> **Takeaway:** an operation is a network of many interlinked processes, so the design of each one affects the whole.

### Who should be involved in process design?

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=222|p.222]]
> […] delegating total responsibility for the design of processes entirely to junior staff, or to internal 'experts' (although they have their role), is neglecting an important opportunity to improve performance. Certainly, operations managers will (and should) be held accountable if the processes go wrong.

![[Summary SOSCM - Macchion-1792401853557.webp]]
![[Summary SOSCM - Macchion-1792401864757.webp]]

> [!info] 📖 Case example – Changi Airport (Singapore) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=218|p.218–219]]
> - **Why airports are a process-design challenge:** they handle passengers, aircraft, crew, baggage, cargo, food, security and retail under strict regulation, with thousands of contracts and constant disruptions (weather, strikes, volcanoes…).
> - **Terminal 4:** capacity raised to about **82 million passengers a year**. The aim was *fast, smooth and seamless flow*, with every stage of the customer journey designed for enough capacity.
> - **Automation:** self check-in, self bag-tagging and bag-drop, automated baggage handling, **face-recognition** immigration and boarding, the 'FAST' (fast and seamless travel) services. These raise throughput and efficiency.
> - **Experience:** 15,000 m² of shopping and dining and a 300-metre glazed galleria. Design stressed aesthetics and *passenger-centric* layout.
> - **Who was involved:** workshops with **many stakeholders** (airlines, ground handlers, immigration, security, retailers, users), so the design worked for every party and also for staff.
> **Link to the theory:** shows the importance of detailed design, involving the right people, and balancing efficiency with experience.

---

## 6.2 Are process performance objectives clear?

![[Summary SOSCM - Macchion-1792402146068.webp]]

> [!info] 📖 Table 6.1 – From strategic objectives to process design objectives · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=223|p.223]]
> | Strategic objective | Process design objective | Benefit |
> |---|---|---|
> | Quality | Capable resources, error-free processing | On-specification output, less recycling and wasted effort |
> | Speed | Minimum throughput time, output rate matched to demand | Short waiting, low in-process inventory |
> | Dependability | Dependable resources, reliable output timing and volume | On-time deliveries, less disruption and rescheduling |
> | Flexibility | Resources with the right range of capabilities; easy change between states | Wide range, fast product/volume/timing changes, coping with unexpected events |
> | Cost | Capacity matched to demand; eliminate waste (excess capacity, excess capability, delays, errors, wrong inputs) | Low processing, resource and inventory costs |

### Process flow objectives
**Why "micro" objectives** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=224|p.224]]): "units" (whatever is processed) pass through activities but **wait in inventories** between them, so **throughput time > sum of activity times**. Resources aren't used all the time either (not all units need every activity, and capacity doesn't match demand at every stage). So units leave the process differently from how they arrived.

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=224|p.224]]
> The flow objectives are: Throughput rate (or flow rate) – the rate at which units emerge from the process […]. Throughput time – the average elapsed time taken for inputs to move through the process and become outputs. The number of units in the process (also called the 'work-in-process' […]). The utilisation of process resources – the proportion of available time that the resources within the process are performing useful work.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=224|p.224]]
> OPERATIONS PRINCIPLE: Process flow objectives should include throughput rate, throughput time, work-in-process and resource utilisation, all of which are interrelated.

![[Summary SOSCM - Macchion-1792402504886.webp]]

> [!info] 📖 Figure 6.3 – Flow objectives and the design factors that drive them · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=225|p.225]]
> - **The box** = the process, with the two internal measures **number of units in the process** (WIP) and **utilisation of resources**. Across the top is **throughput time**. On the right, **throughput rate** comes out; on the left, the **arrival rate** goes in.
> - **The four arrows at the bottom** are the **design factors** you control: *variability of input arrival*, *configuration of resources and activities*, *capacity of resources*, *variability of the activities*.
> **Takeaway:** the rest of the chapter goes through these four factors one by one.

![[Summary SOSCM - Macchion-1792402881378.webp]]

> [!info] 📖 Table 6.2 – Process design vocabulary · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=225|p.225]]
> Learn these definitions well; they come up again in every exercise:
> - **Process task** = all activities to be done. **Work content** = the total time of all of them.
> - **Precedence relationship** = which activities must come before which.
> - **Cycle time** = the average time between completions of units. **Throughput rate** = 1/cycle time.
> - **Process stage** = a work area that performs several activities. **Bottleneck** = the capacity-constraining stage that governs output.
> - **Balancing** = allocating activities as equally as possible between stages. **Utilisation** = the share of time doing useful work.
> - **Starving** = a stage underutilised because the previous stage supplies too little. **Blocking** = a stage can't work because the inventory in front of the next stage is full.
> - **Throughput time** = from entering to leaving. **Queue time** = time waiting to be processed.

---

## 6.3 Are processes designed to achieve process objectives? Process mapping

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=226|p.226]]
> OPERATIONS PRINCIPLE: Process mapping is needed to expose the reality of process behaviour.
>
> […] processes that are not formally defined can be interpreted in different ways, leading to confusion and inhibiting improvement.

Existing processes are often **not well defined**: they developed over time without being recorded, or were changed informally. Since **much process design is really redesign**, start by understanding the current process.

**Process mapping** (also called **process blueprinting**) describes how the activities in a process relate to each other. All techniques share **two features**: (1) they **identify the different types of activity**; (2) they show the **flow** of materials, people or information (the sequence of activities). The symbols aren't universal; most derive from early **"scientific" management** or from **information-system flowcharting** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=226|p.226]]).

**Figure 6.4, "enquiry-to-delivery" at the theatre lighting company** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=226|p.226–227]]): calls go to the store technician, who discusses requirements and checks the **availability file**. If it's in stock, the equipment is reserved, a **"kit wagon"** goes to the store the day before, and the kit is brought to the workshop, **checked (repaired if needed)**, packed and delivered. If not in stock, the customer may be offered a search among other suppliers (*depending on how busy and helpful the technician is*). If they decline, they receive a "Guide to Customers" leaflet; if they accept, the technician calls suppliers, and if nothing is found the customer is informed, while if something is found it is reserved and delivered to the company's site. Note that the variability ("depends on the technician") is itself a sign of a poorly defined process.

### Different levels of mapping

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=227|p.227]]
> […] processes are often mapped at a more aggregated level, called high-level process mapping, before more detailed maps are drawn. […] At the highest level the process can be drawn simply as an input–transformation–output process […]. At a slightly lower or more detailed level, what is sometimes called an outline process map (or chart) identifies the sequence of activities but only in a general way. […] all the activities are shown in a 'detailed process map' […]

![[Summary SOSCM - Macchion-1792404015097.webp]]

> [!info] 📖 Figure 6.5 – Theatre-lighting operation mapped at three levels · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=228|p.228]]
> - **Level 1 (top-left):** the whole operation "supplying and installing lighting equipment" as one input → output box.
> - **Level 2 (blue box), outline process:** three activities, *enquiry to delivery → install and test → collect and check*.
> - **Level 3 (pink oval), detailed process of "install and test":** *safety check → compliant? (N: rectify in time? → rectify, or file a failure note and inform the customer) → install → routine control check → pass check? (N: rectify in time? → rectify, or call for help) → job sign-off → return to base.*
> **Symbols:** circles = activities, diamonds = decisions (Y/N).
> **Takeaway:** map only as deep as is useful. Simple steps ("return to base") need no more detail; activities that rely on skill and discretion ("rectify faulty equipment") are hard to map in detail. Some activities **must** be mapped in detail for quality or **legal** protection (the **site safety check** proves the company met its legal responsibilities). An even more micro level could specify **every motion** (some **quick-service restaurants** do exactly that).

### Process visibility

![[Summary SOSCM - Macchion-1792404053649.webp]]

> [!info] 📖 Figure 6.6 – "Collect-and-check" mapped by levels of visibility · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=229|p.229]]
> Horizontal bands from top to bottom:
> - **Very high visibility** (above the *line of interaction*): direct contact with the customer, e.g. *call customer to agree terms*, *check it worked OK*, *agree report*.
> - **High visibility:** at the customer's site but with little interaction, e.g. *take out equipment*.
> - **Medium visibility:** visible to potential customers but not to this one, e.g. the transport steps *to site* and *to base*.
> - **Back office / low visibility** (below the *line of visibility*): *check and clean equipment → did it work OK? → prepare report / amend usage records → equipment to store*.
> **Why:** design the high-visibility steps to *enhance customer perception*, and the hidden ones for efficiency. This is the same front/back office idea as [[Ch01 - Operations and processes-claude#Front office and back office|Ch 1]].

### Designing the customer experience
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=229|p.229–230]]
- High-visibility processes can't be designed like processes for materials or information: *material and information are processed, but customers **experience** the process*. Experience creates **emotions** (not always rational) and affects satisfaction, loyalty, expectations and emotional bonds, which is why many service firms put the **customer journey** at the core of process design. This applies to **any** high-contact service, not just entertainment (theme parks).
- **Customer service ≠ customer experience:** *service* concerns each single touchpoint; *experience* concerns feelings and emotions across **all encounters of the whole journey** (sights, sounds, smells, atmosphere). Experience exists **only in the customer's mind**, so no two people have the same one. Some say experiences can't be designed, only the **mechanisms** that create them: build the right **clues** into the process.
- **Touchpoints** = *"everything the consumer uses to verify their service's effectiveness"* (Shostack): the points of contact. Their accumulation shapes judgement. **Clues/cues** = the messages received at the touchpoints; the resulting emotions shape how the process is judged.
- **Tools:** map the route customers take (websites, **clinical pathways**); **walk-through audits** (staff or advisers as surrogate customers); **emotion mapping** (capture positive and negative emotions, change, re-check). All clues must be **consistent** with the intended emotions.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=230|p.230]]
> OPERATIONS PRINCIPLE: The design of processes that deal with customers should consider the emotions engendered at each stage of the process.

![[Summary SOSCM - Macchion-1792404459641.webp]]

> [!info] 📖 Figure 6.7 – Customer experience map of a CT scan visit · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=231|p.231]] (text on [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=230|p.230]])
> - **Middle row:** the customer journey *park car → check in → wait → scan → wait for results → results explained*.
> - **Top table, "What do you intend the patient to…"**: the intended **think / feel / say / do** at each step ("it's obvious where I park", "relaxed", "this is easier than I expected"…).
> - **Bottom table, "What does the patient actually…"**: reality ("Where do I go?", "frustrated", "worry", "what's happening?").
> - **Zig-zag line (−3 to +3):** the emotion score along the journey, with lows at parking/waiting and highs at check-in and the final explanation.
> **Concepts:** **touchpoints** (every contact point with the customer), **clues/cues** (the messages received there) and **emotion mapping**. Design the clues so the intended and actual emotions match.

---

## 6.4 Are process tasks and capacity configured appropriately?

What you need to master: **task precedence → series/parallel configuration → cycle time and capacity (bottlenecks) → balancing → throughput, cycle time and WIP (Little's Law)**.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=231|p.231]]
> OPERATIONS PRINCIPLE: Process design must respect task precedence.

**Task precedence** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=231|p.231]]) defines which activities must occur before others *because of the nature of the task*. It is defined by (1) the individual activities and (2) their relationships. A **precedence diagram** also shows the time of the total task (work content) and of each activity. It doesn't determine the design, but it constrains how activities can be grouped into stages.

### The book's running example: computer test and repair
Table 6.3 / precedence diagram, Figure 6.8 ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=232|p.232]]): a (5 min) → b (6) → c (4) → d (8), e (6), f (4) in parallel → g (10). **Total work content = 43 min.** Required: **one computer every 12 minutes**.

$$\text{Number of stages}=\frac{\text{work content}}{\text{required cycle time}}=\frac{43}{12}=3.58\ \Rightarrow\ 4\text{ stages}$$

### Series and parallel configurations

![[Summary SOSCM - Macchion-1792586003781.webp]]

> [!info] 📖 Figure 6.9 – "Long–thin" arrangement · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=234|p.234]]
> Four stages in **series**: stage 1 = a, b (11 min); stage 2 = c, d (**12 min**, the bottleneck); stage 3 = e, f (10); stage 4 = g (10). Output = **one every 12 minutes** (set by the slowest stage). The precedence diagram underneath shows that the split respects the order of activities.

![[Summary SOSCM - Macchion-1792586009949.webp]]

> [!info] 📖 Figure 6.10 – Intermediate configuration · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=234|p.234]] (your annotations W1–W4 = the four workers)
> **Two parallel lines of two stages each.** Stage 1 = a, b, c, e (21 min) and stage 2 = d, f, g (22 min). Each line gives one computer every 22 min, so two lines give **one every 11 min** on average.

![[Summary SOSCM - Macchion-1792586142044.webp]]

> [!info] 📖 Figure 6.11 – "Short–fat" arrangement · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=235|p.235]]
> **Four parallel single stages**, each worker (W1–W4) doing *all* activities (43 min). Together: four computers every 43 min = **one every 10.75 min**.

*"Long" = number of stages; "fat" = amount of work per stage.* Most processes **combine** series and parallel, with technical constraints limiting the extremes, but there is usually a real choice ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=233|p.233]]).

| Long–thin (series) ✅ | Short–fat (parallel) ✅ |
|---|---|
| Controlled flow, easy to manage | **Mix flexibility** (each stage can specialise in a product) |
| Simple materials handling | **Volume flexibility** (open or close stages as demand varies) |
| Lower capital needs (equipment not duplicated) | **Robustness** (one stage down, the others keep going) |
| More efficient: more direct productive work per person | **Less monotonous** work (repeats every 43 min instead of 12) |

### Cycle time and process capacity: bottlenecks (book)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=235|p.235–236]]
- **Cycle time** = the time between completed units emerging. It is usually **one of the first things calculated**, because it represents both the **demand** on the process and the process's **capacity**, and sets its **pace or "drum beat"**. It is calculated from likely demand over a period and the production time available in that period.
- **Process capacity:** given the required cycle time, the capacity needed depends on the **work content**. The larger the work content and the smaller the cycle time, the more capacity is needed.
- Capacity is often expressed as **throughput rate** (= 1/cycle time): a theme-park ride takes 1,000 customers an hour, a bottling line 100 bottles a minute. But **high capacity ≠ fast throughput time**: if many units are in the process, they wait in WIP inventories → Little's Law ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=239|p.239]]).

### Cycle time vs takt time (lecture)

![[Summary SOSCM - Macchion-1792586817215.webp]]

> [!example] 🎓 Lecture slide – Takt time vs cycle time (not in the book)
> *"Both use time per unit, but they describe different things."*
> - **TAKT TIME: how fast *must* we produce to meet demand?**
>   $$\text{Takt}=\frac{\text{available production time}}{\text{customer demand}}$$
>   A **target pace set by demand**. Recalculate it when demand or available time changes. *Takt is demand-based.*
> - **CYCLE TIME: how long *does* the process actually take?** The *observed* elapsed time between consecutive completed units. It varies with method, workload and interruptions. *Cycle time is process-based.*
> **Rule:** the process works only if **cycle time ≤ takt time**. In the book, "required cycle time" plays the role of takt (e.g. the 12 min above).

![[Summary SOSCM - Macchion-1792586803528.webp|500]]

> [!example] 🎓 Lecture slide – Example 1 (photo of the projected slide)
> A line has **7 productive hours** per shift and customers need **420 units** per shift.
> - Available time = 7 h × 60 min × 60 s = **25,200 s**.
> - Takt = 25,200 s / 420 units = **60 s per unit**.
> - Observed process cycle time = **50 s per unit**.
> - The slide's bar compares the two: the process completes a unit in **50 s** while demand requires one every **60 s**, so the line is **fast enough**, with 10 s of slack per unit.

![[Summary SOSCM - Macchion-1792586999436.webp|400]]

> [!example] 🎓 Hand-drawn precedence diagram from class (exercise sketch)
> Five activities with their times: **10 → 20 →** then two branches **45** and **40** in parallel, both feeding the final **50**. Total work content = 10+20+45+40+50 = **165**.
> How to use it in an exercise: (1) respect precedence (the 50 can't start until 45 and 40 are both done); (2) given a required cycle time, the minimum number of stages = 165 / cycle time, rounded **up**; (3) no stage can be shorter than its longest single activity (50 here). That is why a cycle time below 50 would require putting that activity in **parallel** stations.

### Process balancing and balancing loss

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=236|p.236]]
> Balancing a process involves attempting to allocate activities to each stage as equally as possible. […] The effectiveness of the balancing activity is measured by balancing loss. This is the time wasted through the unequal allocation of activities as a percentage of the total time invested in processing. The stage of a process that has the longest allocation of work is known as the bottleneck. It is the bottleneck stage that will dictate the output of the whole process.

$$\text{Balancing loss}=\frac{\text{total idle time per cycle}}{\text{number of stages}\times\text{cycle time}}$$

![[Summary SOSCM - Macchion-1792587086777.webp]]

> [!info] 📖 Figure 6.12 – Balancing loss in three configurations · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=237|p.237]]
> - **(a) Ideal:** 43/4 = 10.75 min per stage, so **idle = 0** and **balancing loss = 0**. In practice this is impossible because activities can't be split.
> - **(b) Best four-stage allocation:** cycle time = 12. Idle = (12−11) + (12−10) + (12−10) = **5 min**. Loss = 5/(4×12) = **10.4%**.
> - **(c) Best two-stage allocation:** cycle time = 22. Idle = 22−21 = **1 min**. Loss = 1/(2×22) = **2.3%**.
> - **Green tops** = idle time at the non-bottleneck stages (they are *starved* by the bottleneck).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=236|p.236]]
> OPERATIONS PRINCIPLE: Process analysis derives from an understanding of the required process cycle time.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=237|p.237]]
> OPERATIONS PRINCIPLE: Allocating work equally to each stage in a process (balancing) smooths flow and avoids bottlenecks.

**Detail of the book's balancing explanation** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=237|p.237–238]]): stage 1 (11 min) is idle 1 minute per cycle, *or* it keeps working every 11 minutes and the **inventory between stages 1 and 2 grows to infinity**. Stages 3 and 4 are **starved** for 2 minutes every 12. In practice non-bottleneck stages **slow down** to the bottleneck's pace, but that is still effective idle time. **Total invested time** = number of stages × cycle time = 4 × 12 = 48 minutes; idle time = 5 minutes; loss = 10.4%.

![[Summary SOSCM - Macchion-1792587451370.webp]]

> [!example] 🎓 Lecture slide – Yamazumi chart (not in the book)
> A **stacked bar chart** of work per workstation (1–4), in **seconds**, with a horizontal **takt line at about 110 s**.
> - **Green blocks = value-added** work; **red blocks = non-value-added** work (waiting, walking, searching…).
> - **Station 2 exceeds takt** (about 112 s): it is the **bottleneck** and can't keep up with demand. Station 3 (about 43 s) is heavily **under-loaded**. Stations 1 (about 87 s) and 4 (about 65 s) are below takt.
> **How to use it:** (1) remove the red (non-value-added) blocks, especially at station 2; (2) **re-balance** by moving work from station 2 to station 3 (respecting precedence) until every bar is below the takt line and the bars are as even as possible. It is a visual tool for **balancing** and **waste** together, from Japanese "yama-zumi" = "stacked up".

### Passport office (worked example: cycle time and capacity)

![[Summary SOSCM - Macchion-1792588698612.webp]]

> [!info] 📖 Worked example – Passport office · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=236|p.236]]
> 1,600 applications per week; 40 hours available per week; work content = 30 min per passport.
> $$\text{Cycle time}=\frac{\text{time available}}{\text{number to process}}=\frac{40}{1600}=0.025\text{ h}=1.5\text{ min}$$
> $$N=\frac{\text{work content}}{\text{cycle time}}=\frac{30}{1.5}=20\text{ people}$$
> **Logic:** one person alone would produce a passport every 30 min; you need one every 1.5 min, so 20 people.

### Little's Law

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=239|p.239]]
> The mathematical relationship that relates cycle time to work-in-process and throughput time is called Little's Law. It is simple but very useful, and it works for any stable process.

$$\boxed{\text{Throughput time}=\text{WIP}\times\text{Cycle time}}\qquad\Longleftrightarrow\qquad \text{WIP}=\text{Throughput time}\times\text{Throughput rate}$$

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=239|p.239]]
> OPERATIONS PRINCIPLE: Little's Law states that throughput time = work-in-process × cycle time.

- **Computer repair:** cycle time 12 min, WIP = 4 (one per stage), so throughput time = 4 × 12 = **48 min**.
- **Passport office, "clear desk" policy:** 450 min = WIP × 1.5, so **WIP = 300 applications** can be loaded in the morning and cleared by evening.

> 💡 *Intuition:* a queue at the supermarket. If there are 10 people in front of you (WIP) and one leaves every 2 min (cycle time), you'll wait 20 min (throughput time).

![[Summary SOSCM - Macchion-1792587983865.webp]]

> [!example] 🎓 Lecture slide – Little's Law on a production line (not in the book)
> A straight line with **three stations**, each holding **8 units**, so **WIP = 24 units** on the conveyor between entry and exit. Cycle time = **10 min/unit** (6 units per hour leave the line).
> $$\text{Throughput time}=24\times10=240\text{ min}=4\text{ hours}$$
> The picture makes each term visible: WIP = the units *inside* the boundary; cycle time = the interval between units leaving; throughput time = how long one unit stays inside.

![[Summary SOSCM - Macchion-1792588577747.webp]]

> [!example] 🎓 Lecture slide – Why use Little's Law? (not in the book)
> It turns three everyday flow measures into a practical planning tool:
> 1. **Estimate flow time:** from average WIP and throughput, estimate how long work spends in the process.
> 2. **Set a WIP target:** work backwards from a desired flow time and expected throughput.
> 3. **Evaluate changes:** compare before and after to see whether WIP, throughput or flow time changed.
> 4. **Spot flow problems:** a long flow time prompts a closer look at queues, bottlenecks and uneven work.
> ⚠️ Footnote on the slide: Little's Law describes **average** flow. It does **not** identify the *cause* of delays, nor guarantee that lowering WIP alone will fix them.

> [!info] 📖 Case example – Little's Law at an IT support unit · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=240|p.240]]
> Every August all workstations must be renovated in **one week (40 h)**. *Last year:* 500 workstations, 2 h each, so throughput rate = 0.5N per hour; 500 = 40 × 0.5N gives **N = 25 technicians**. *This year:* 530 workstations, 1.5 h each, so throughput rate = N/1.5; 530 = 40 × N/1.5 gives N = 19.9 ≈ **20 technicians**. Faster work more than compensates for the extra workload.

---

## 6.5 Is process variability recognised?

Deterministic analysis is a good first approximation (and its relationships hold **for average values**), but real processes have **variability** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=241|p.241]]).

**Sources of variability:** early or late arrival of material, information or customers; temporary **breakdowns**; **recycling** misprocessed units to an earlier stage; **misrouting**; each product or service being **different**; the same product needing **slightly different treatment** (e.g. depending on diagnostic results); natural **human variation** in coordination and effort.
These produce **two fundamental types**: (1) variability in **demand at each stage** (**inter-arrival times**); (2) variability in **activity times** at each stage.

### Activity time variability

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=241|p.241]]
> […] that synchronised indexing time would have to be set at 15 minutes. This then becomes the effective cycle time of the process. Note that the effective bottleneck stage is now stage 1 rather than stage 2. Although stage 2 has the longer average activity time (12 minutes), stage 1 with an average activity time of 11 minutes has a degree of variability that results in a maximum activity of 15 minutes.

![[Summary SOSCM - Macchion-1792588891127.webp]]

> [!info] 📖 Figure 6.14 – Processing-time variability in a synchronised process · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=242|p.242]]
> - **Blue bars** = average activity time per stage (11, 12, 10, 10). The **red bell curves** show the variability around each average.
> - If all stages move **together** (indexing conveyor), the interval must fit the **slowest possible** time of any stage, so **cycle time = 15 min**. Stage 1, with the widest curve, becomes the real bottleneck.
> - Idle time = (15−11) + (15−12) + (15−10) + (15−10) = **17 min** per cycle (vs 5 min without variability).
> **Takeaway:** variability, not just imbalance, wastes capacity. Without synchronisation stages wait less, but arrivals at later stages become variable.

- **Synchronised flow** (indexing conveyor, a traffic-light system, a **car assembly belt** whose speed accommodates variability): the inter-arrival time is **fixed** at the cycle time.
- **Unsynchronised flow** (more common with information and customers): units move as soon as each stage finishes, so less waiting, but the **inter-arrival times at later stages become variable** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=242|p.242]]).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=242|p.242]]
> OPERATIONS PRINCIPLE: Variability in a process acts to reduce its efficiency.

### Arrival time variability and utilisation

> [!PDF|note] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=242|p.242]]
> […] in a perfectly constant and predictable world, the relationship between process waiting time and utilisation is a rectangular function […]

![[Summary SOSCM - Macchion-1792589585791.webp]]

> [!info] 📖 Figure 6.15 – Utilisation vs units waiting · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=243|p.243]] (with your annotations)
> A single stage of **10 min**.
> - **Dotted line (no variability):** arrivals every 30 min give 33% utilisation (**A**); every 20 min, 50% (**B**); every 10 min, 100% with no queue (**C**). Faster than that, and the queue grows forever (**D**).
> - **Red curve (with variability):** queues start forming well *before* 100% (points **Z → X → Y**) and the curve shoots up as utilisation approaches 100%.
> - **Your notes:** *"Point C is the best but performing well → not a feasible situation in reality"*; the **"best spot"** box around **80–90%** is the best % to arrange production: high utilisation without explosive queues.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=243|p.243]]
> OPERATIONS PRINCIPLE: Process variability results in simultaneous waiting and resource underutilisation.

**Book's supermarket checkout example** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=243|p.243]]) for points X, Y, Z: a real checkout is sometimes idle and sometimes has a queue, i.e. point **X** (some underutilisation *and* a positive average queue). The manager **closes checkouts** to raise utilisation, and waiting rises (**Y**). She **opens more checkouts** to cut waiting, and utilisation falls (**Z**). As utilisation approaches 100%, average waiting time keeps rising. *The only way to guarantee very low waiting is to accept low utilisation.* The greater the variability, the further the curve moves from the rectangular "no-variability" function.

### The "OM triangle" (Figure 6.16)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=243|p.243–244]]
**(a)** A family of utilisation-vs-waiting curves: the higher the variability, the higher the curve. **(b)** The three options for designers:
1. accept **long waiting** times and get **high utilisation** (X);
2. accept **low utilisation** and get **short waiting** (Y);
3. **reduce variability** (in arrivals, activities or both) and get **high utilisation *and* short waiting** (Z), moving to a lower curve.
This is a **strategic choice**: fast throughput or high utilisation? Having both requires reducing variability, which may mean **limiting customisation** or imposing stricter limits on how services are delivered. Day-to-day corollary: guaranteeing **100% utilisation** means accepting **infinite WIP and/or waiting** (→ Ch 8, capacity). Processes with both arrival and activity variability are analysed with **queuing (waiting-line) theory** (supplement to Ch 6).

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=244|p.244]]
> OPERATIONS PRINCIPLE: Process design involves some choice between utilisation, waiting time and variability reduction.

### Critical commentary
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=244|p.244–245]]
- Some reject mapping the **current** process and prefer a radical **"clean sheet of paper"** approach, the only way, they say, to be imaginative enough in redesign.
- The chapter's examples are **assembly-line-like** (linear, synchronised), but many business processes are **fuzzy, simultaneous and interactive** in unpredictable ways, and conventional theory offers little guidance for them.

### Summary checklist (book)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=245|p.245]]: Clear performance objectives for each process, linked to strategy? Are throughput rate, throughput time, WIP and utilisation known for key processes? Are processes mapped, and the emotions of customers understood? Are formal descriptions followed, or should they be changed or enforced? Is visibility mapped? Is task precedence known? Have series and parallel options been explored? Is the process balanced, and can the bottleneck be redesigned? Is Little's Law understood? Are the sources and effects of variability recognised in the design?

---

## 📚 Case examples and worked examples (Chapter 6)

> [!example] Case – **Changi Airport** → full summary in 6.1 above · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=218|p.218–219]]
> Extra facts: more than **100 airlines**, about **300 cities in 70 countries**, almost **60 million passengers a year** (about 10 times Singapore's population), a movement every **90 seconds**, the **sixth-busiest** international airport. T4 has an overhead bridge to the highway, **2 car parks (1,500 vehicles)** with sheltered links, a butterfly garden, orchid and sunflower gardens, a koi pond. "T4 breaks new ground in passenger experience… passenger-centric and user-friendly" (Yam Kum Weng, CAG).

> [!example] Worked example – **Lobbying team (IPA) at a European pulp and paper company** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=221|p.221–222]]
> **Situation:** **Jim Glazier** (Head of Institutional and Public Affairs) wants his experienced lobbyists (at the European Parliament, accredited with special passes to reach MEPs) to be more **systematic**. **Anders** objects: *"I'm a qualified professional, not a process worker in a sausage factory… our job is the very antithesis of 'process'"*, warning against a box-ticking mentality and loss of creativity, freedom and self-worth. Jim: *"All I am proposing is that we should articulate three things: **what we actually do, how we should go about doing it, and maybe how we could do it better**."*
> **Outcome:** **Marie Louise Bourg** (head of European Parliament lobbying) has her team write down what they do to prepare and deliver parliamentary briefings. Everyone had **different views** of the activities, frequency, sequence and importance. It took **2 hours** just to agree on the list of quarterly, weekly and daily tasks. They then assessed each stage (importance to the mission, how good they are, how to improve), and the team became motivated to make changes.
> **Message:** "people vs process" is a false distinction. Even professional services benefit from **defining** their processes (loosely, by outcome).

> [!example] Case – **Ecover** (environmental process objectives) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=223|p.223–224]]
> The world's largest producer of **ecological detergents** and cleaning products (factories in France and Belgium). **100% green electricity**; energy-efficient lighting; standard machinery but **low-speed** appliances that need no water to clean (mixers that mix **25 tonnes** while using "no more electricity than a few flat irons"); a "squeezy gadget" that empties pipes so they **don't need rinsing**; minimal and recyclable packaging; **"Plant-astic"**, a 100% renewable, reusable and recyclable plastic made from **sugarcane**. The building follows the **sun** (natural daylight), with a **pine** frame, bricks of clay, wood pulp and mineral waste (less energy to bake), and a **flowering-plant roof** for insulation, so **no heating or air conditioning**.
> **Message:** processes are increasingly judged also on their **environmental impact** (TBL).

> [!example] Worked examples – **computer test and repair** · **passport office** · **IT support unit** → all solved in 6.4 above.

> [!example] Case – **London Underground escalators at Holborn** (bottleneck) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=238|p.238]] · Figure 6.13
> **Situation:** Londoners traditionally **stand on the right and walk on the left**. At Holborn the escalators are **over 24 m high**, and the taller the escalator, the fewer people walk (at 30 m only the very energetic do), so the left side is under-used and the escalator becomes a **bottleneck**. New stations are expensive, so capacity has to be found in existing ones.
> **Trial:** **stand on both sides** at peak times. Capacity went from about **115 to about 150 people per minute** (+30%). **Technically successful, but not made permanent:** it slowed the (vocal) minority who walk up as their daily workout, and it removed the **feeling of choice** (even if most people didn't use it).
> **Message:** removing a bottleneck increases capacity, but **human behaviour** (behavioural operations, Ch 1) can defeat the "optimal" design.

> [!example] Worked example – **Coffee break and Little's Law** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=240|p.240]]
> At 10:45, **20 managers** are queuing for coffee and the seminar restarts at 11:00. Each serving takes **48 s = 0.8 min** (cycle time). Throughput time = WIP × CT = 20 × 0.8 = **16 minutes**, plus time for the last person to drink, so **just over 20 minutes**. *"You just haven't allowed long enough for the process"* (Mike to Shaun). The problem isn't motivation, it's **process capacity**.

> [!example] End-of-chapter case study – **Action Response Applications Processing Unit (ARAPU)** · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=246|p.246–247]]
> **Context:** a London charity (CEO **Susan N'tini**) giving **fast short-term aid** to small projects until larger donors step in (*"…he might starve while he's training to catch fish"*). Problems: **funds arrive too slowly**, **costs are rising** (the administration share is a key objective), risk of **bad publicity** if money goes to the "wrong" place. Stakeholders complain about delays and that staff **can't say where a file is**. Some assessors fear more efficiency would reduce **flexibility** and the **counselling** role.
> **Process data** (35-hour week; about **300 new applications per week** in and out; turnaround target **20 days**, not measured; about **2,000 files in the process**):
> | Stage | Staff | Time per application |
> |---|---|---|
> | Receipt (checks forms complete) | 4 clerks (**2 almost full-time searching for files**) | 10 min |
> | Coding (in batches twice a day) | 5 | 20 min |
> | Assessment | 7 assessors | **100/week returned after 10 min** for more information (1–8 weeks, then they **re-enter** the process); the rest about **60 min**: **150 accepted / 150 declined** |
> | Committee of trustees | — | **Only on Thursdays** (samples decisions, reviews unusual cases) |
> | Declines | 3 | 30 min |
> | Payments | 4 | 50 min |
> | Dispatch | 2 | 10 min |
> **Analysis with the chapter's tools** (my calculations from the case data, to use as answer hints):
> - **Little's Law:** throughput time = WIP / throughput rate = 2,000 / 300 ≈ **6.7 weeks ≈ 33 working days**, well over the 20-day target.
> - **Load vs capacity** (2,100 min per person per week): assessors need 100 × 10 + 300 × 60 = **19,000 min** vs 7 × 2,100 = **14,700 min**, i.e. **~129% load**, so they are the **bottleneck** (queues build in front of them). The other stages are below capacity (payments 7,500/8,400; coding 8,000/10,500; declines 4,500/6,300; dispatch 3,000/4,200).
> - **Other causes:** the **weekly committee** batches everything (up to a week of waiting, and "completers" waiting on Thursdays); coding in **batches**; **recycling** of incomplete files; no visibility of files (staff wasted on searching).
> **Book questions and hints:**
> 1. *Objectives:* speed (turnaround), dependability (knowing status and keeping promises), quality (correct decisions, avoiding bad publicity), low cost (administration share), flexibility (unusual requests).
> 2. *Main problem:* excessive **WIP and throughput time** caused by the assessment bottleneck, recycling, batching and the weekly committee, with no tracking.
> 3. *Improvements:* check completeness **at receipt** (reduce recycling), add assessor capacity or rebalance (use receipt staff, simple triage), let the committee approve **more often or by sampling** without blocking payment, a **tracking system** (status visibility), **smaller batches**, and track turnaround time as a KPI.

> [!note] Book exercises (p.248–249), with the logic of each answer
> - **Drive-through:** map the process with a **line of visibility** (order point, payment, pick-up window; behind it the kitchen and assembly).
> - **Expense claims (Sweden):** 12 staff, 10 working days, 20 min per claim. *Assuming 7.5 h per day* (as in the passport office): capacity per person = 10 × 450 = 4,500 min per cycle. Average 3,200 claims × 20 = 64,000 min, so **≈ 14.2 staff**; minimum 1,000, so **≈ 4.4**; maximum 4,300, so **≈ 19.1** (12 are not enough at peak). **(b)** At 15 min: 10.7 / 3.3 / 14.3. **(c)** With 15 days at 20 min: 9.5 / 3.0 / 12.7. Earlier submission has an effect similar to automation.
> - **Budget estimates (Table 6.4):** 20 per week × 35 h → **required cycle time = 2,100/20 = 105 min**. Work content = 20+15+80+65+20+80+80 = **360 min**, so **N = 360/105 = 3.43 → 4 people/stages**. **Long–thin** respecting precedence, e.g. S1 = A+C (100), S2 = B+D (80), S3 = E+F (100), S4 = G (80): bottleneck 100 min, idle = 0+20+0+20 = 40, **balancing loss = 40/(4 × 100) = 10%**. **Two parallel lines of 2 stages:** S1 = A+B+C+D (180) and S2 = E+F+G (180), perfectly balanced, **loss = 0%**; each line gives one estimate every 180 min, so two lines give one every 90 min ≤ 105.
> - **King Lear toilets:** demand = 86 × 3 = **258 cubicle-minutes**; capacity = 10 × 20 = **200**, so **not enough**. Interval needed = 258/10 = **25.8 ≈ 26 minutes** (ignoring variability, which would require even more time).
> - **Gourmet burgers:** cycle time = 600/250 = **2.4 min**; servers = 7.2/2.4 = **3**. With stages 2.0 / 3.0 / 2.2 the bottleneck is 3.0: idle = 1.0 + 0 + 0.8 = 1.8, **balancing loss = 1.8/(3 × 3) = 20%** (and actual output is one every 3 min, not 2.4: demand isn't met).

---

> [!question] 🎤 Likely oral questions
> - *What are the process flow objectives and how are they linked?* Throughput rate, throughput time, WIP, utilisation; Little's Law.
> - *Explain Little's Law with an example* (computer repair, passport clear desk, IT support unit).
> - *Takt time vs cycle time* (lecture example: 60 s vs 50 s).
> - *Long-thin vs short-fat: pros and cons.*
> - *What is the bottleneck? How do you compute balancing loss?* (10.4% vs 2.3%; Yamazumi chart).
> - *Levels of process mapping; line of visibility; customer journey/emotion mapping.*
> - *Why can't a process run at 100% utilisation?* Variability (Fig 6.15).

Next → [[Ch07 - Supply chain management-claude]]

---

## 🗺️ Concept map (Chapter 6)

![[Ch06 concept map-claude.png]]

**Figures A–D of the map, full size:**

![[Ch06 concept map figures-claude.png]]

> [!tip] How to read the map
> **Dark blue box** = the chapter; **coloured blocks** = its sections, each with its key concepts. **Red arrows** = links between concepts (with the relation written on them); **orange dashed boxes** = links to other chapters. **Thumbnails A–D** (blue dashed line) = the book figure or slide that explains that concept, with its page; they are shown full size below the map.
>
> 🎤 **Oral storyline:** Why detail matters (weakest link) → flow objectives → mapping (visibility, customer experience) → configure tasks and capacity: cycle time → number of stages → balancing → Little's Law → variability and the utilisation–waiting trade-off.
