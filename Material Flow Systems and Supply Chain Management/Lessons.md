> [!IMPORTANT] 
> moodle: https://stem.elearning.unipd.it/course/view.php?id=17225
> 

# L1 - Introduction
https://stem.elearning.unipd.it/pluginfile.php/1464599/mod_resource/content/1/LECTURE%201-introduction.pdf

**Learning Objectives:** 
1. to acquaint students with the concepts of material flow systems in manufacturing and logistics, 
2. to learn optimization modeling and analyses of material flow systems, 
3. to understand material flow integration issues in flexible and resilient supply networks, 
4. to apply analytics software tools for case-based problem solving: Software Anylogistix, 50 student licenses and a teamwork during the cours

**Description:** 
1. Analyses of material flows in manufacturing: a particular focus on Assembly To Order systems and their impact on in-house logistics. 
2. Optimization modeling and analyses of material flow systems: part feeding problems for in-house logistics, Inventory Routing Problems for Outbound and Inbound Logistics. 
3. Material flow structures, physical assets (AGV and LGV fleet design), material handling systems and operational decisions influencing system performance. 
4. Digitalization of material flow systems, from MES (Manufacturing Execution System) to TMS (Transport Management System) and digital supply networks. 
5. AnyLogistix laboratory: logistics network design principles, logistic facilities location, transportation flows optimization and dynamic flow simulation. Emphasis is given to problem-based modeling and solving with a team working and real case data. 

***Prerequisites:*** Knowledge of industrial facilities design and planning, layout design, manufacturing system dimensioning and production planning and control.

Teaching material:
- suggested book: "Facilities Planning", 4th Edition, by Tompkins, White, Bozer and Tanchoco; published by J. Wiley, 2010, ISBN 978-0-470-44404-7. 
- slides/documents uploaded in Moodle by the teacher 
- laboratory video tutorials 
- anyLogistix full license: https://www.anylogistix.com/

---
## Logistics
***<font color="#ff0000">Definitions:</font>***
- **Logistics** is the discipline that supervise, optimize and manage material and information flows inside the supply chain, between the point of origin and the point of consumption in order to meet customer requirements, offering the desired service level at the minimum cost. 
- **Supply Chain** is a complex system made up by industrial partners, infrastructures and resources involved in transforming raw materials and components in a finished product or service from the first supplier to the final customer with the final aim to maximize the Supply Chain competitiveness and profitability. $\rightarrow$ Supply Network
- **Supply Chain Management** encompasses the planning and management of all activities involved in sourcing and procurement, conversion, and all logistics management activities. Importantly, it also includes coordination and collaboration with channel partners, which can be suppliers, intermediaries, third-party service providers, and customers. In essence, supply chain management integrates supply and demand management within and across companies. 

All partners: suppliers, delivers of raw material, production which transforms raw materials in semifinished products and then in finished products that will be stored in warehouses and then they will be distributed to costumers. 

There are two flows with two different directions: Physical flow goes from left to right, instead information flow goes from right to left. 

The market tells us what they want, and we need to provide what the market asks and the storages will give to the market what they order. The production system will put in the production only what the market wants, and we order raw material to produce what is required. The information that comes from the market is the demand, we don’t work with certain data, we need to make a plan: starting from the information that come from the customers, then we will decide to set the production quantity of the plant, in order to meet this forecast. From the production quantity of the plant, we know how many parts we need to deliver to the station per hour, in order to provide all the materials for the production system.

```horizontal

Logistic is divided in parts: 
- Inbound logistics→ It deals from supplier to company: Provided the raw material 
- Outbound logistics → It deals from company to customers (that can be retailer/ distribution/ persons) 
  
  Inside the company we have INHOUSE LOGISTICS
---
![[Lessons-1791026864110.webp|310x225]]


![[Lessons-1791026918612.webp|316x198]]

```

***<font color="#ff0000">Forward and Reverse Logistic Process</font>***

```horizontal

![[Lessons-1791026950725.webp|530x266]]

---

![[Lessons-1791027011385.webp]]

```

The traditional flow goes **from left to right**, the reverse logistic process goes **from right to left**: to solve problems of returning flows, discard products that need to return to company to try to refurbish them or to recreate new products, in same case it’s not possible because they’re completely broken and in this case, they will become waste. We need to manage waste.

![[Lessons-1791027577129.webp|619]]


***<font color="#ff0000">Closed Loop Supply Chain</font>***
Design, control and operation of a system to maximize value over the entire product life cycle, with the dynamic recovery of value from product that come back from users

The term ***‘Closed Loop Supply Chain’*** represents the design, control, and operation of a system to maximize the creation of value over the entire life cycle of a product with the dynamic recovery of value from different types and volumes of products that come back from users. The most common activities involved in a Closed-loop Supply Chain are: 
1. **Product reuse**: collected products/ materials can be recovered in order to return the product the functionality it previously had. Before reusing, some maintenance activities could be necessary such as cleaning and/or repairing /refurbishing/reconditioning of some minor previously worn part components. 
2. **Products recycle:** in recycling, the identity and functionality of products and components are lost. Product recycling aims at repurposing used components in manufacturing processes of original parts if the quality of the materials is high or in the production of other parts. Materials like aluminium or titanium or carbon fibres are often recycled because they are expensive but there are other materials that can’t be recycle or that their recycling process is expensive. The product is completely disassembled and we can try to recycle some parts and bring to the landfill the parts that can’t be recycled anymore.
3. **Energy recovery (from process waste/inventories):** collected materials/products are not eligible to reusage or recycle and they are therefore employed for energy generation. 
4. **Secondary market:** collected products are directly repurposed on secondary markets without any additional operation/transformation.
![[Lessons-1791027854570.webp]]
In this picture are contained all the kinds of activities that are close to supply chain in order to close a loop. Recycling arrive to deliver the raw material ; while waste-to-energy, remanufacturing and cannibalisation of components will provide components to manufacturer ; while the repair activities and refurbishing activities can be managed by 3PL provider (directed by manufacturer but also by partners). The landfill is the final stage.

> The most closed supply chain is the chain of paper and corrugated fibreboard packaging. It’s closed around 98%.

In spite of we need to increase the profit, because we have also economic variables and we have to take in mind that logistic choices need to be sustainable by an economical point of view, we need to find a solution less expensive.

> How to translate environmental objectives into economic objectives?

We have the carbon footprint market: carbon price change day by day and if we are making a project and we are evaluating the cost of a project, we have to consider the environmental impact! →software ANYLOGISTIC help us to do this.
![[Lessons-1791033984161.webp|565]]
We need to consider that we have the **4th industrial revolution right now**, so companies have to invest in digitalization and in the equipment that will substitute humans in some cases, *when the works aren’t safe and in the majority of cases will collaborate with humans*. Implement industry 4.0 means to implement technologies interconnected each other.

> All companies are connected each other with the help of different technologies.


```horizontal
Interconnective of different companies in the same reality, they need to collect data . The logistic manager needs the possibility to use several kind of 4.0 technologies. The first one is Internet of Things: we need to collect data, to know where the products are , so data capturing, sensors, barcodes etc The fourth industrial revolution, also termed Industry4.0, represents a trend of industrial automation that integrates some new production technologies to improve working conditions, create new business models and increase the productivity and production quality of the plants
---
![[Lessons-1791034104821.webp]]

```

***<font color="#ff0000">Industry 4.0 and 5.0</font>***
```horizontal
![[Lessons-1791028262029.webp|562x377]]
---

![[Lessons-1791028270082.webp|489x253]]

INDUSTRY 5.0: Promoted by the European commission and other governmental bodies in 2021, Industry 5.0 emphasizes a triple-bottom-line of economic, environmental, and societal impact, bringing ESG (Environment, Social and Governance) perspective and balance to what have often been technology-led and economic-driven choices.

> Ref: Xu, Xun & Lu, Yuqian & Vogel-Heuser, Birgit & Wang, Lihui. (2021). Industry 4.0 and Industry 5.0-Inception, conception and perception. Journal of Manufacturing Systems. 61. 530-535.

```

# Lesson 2
***<font color="#ff0000">Three important consideration in Logistics:</font>***

```horizontal
There are three important considerations in logistic in inhouse: 
1. **Flow** of people, of materials 
2. **Space problems**: human resources, materials store, layout of machines 
3. **Activity relationships** between department and inside a department 

A company can be seen as a material flow system, we have materials that are raw materials, semifinished products and instrument used to produce that come from supplier to incoming storage that we call STORE. Then these are put into production system where also energy and water go inside the system. From the production process there is the output that is the finished product that will be delivered to an outgoing storage system, and from this, we will send these products to the packaging area and finally to another storage point or directly to the trucks to be sent to the retailers or to the users. Some parts are discorded in the disposal system.

---
![[Lessons-1791032941577.webp]]
```

```horizontal
When a company has a “good” material flow, materials at different stage moves steadily and predictability, but a “bad” flow means there is a lot of stops and starts in the process, ultimately resulting in an inefficient system. If a company is looking to go Lean, the material flow is a great place to start.
---
![[Lessons-1791032816444.webp|273x240]]
```

> [!PDF|red] [[Material flow system and logistic networks.pdf#page=6&selection=60,0,83,20&color=red|Material flow system and logistic networks, p.6]]
>Def. Flow system: flows in the supply network are movements of goods, materials, energy, information and workers. We can have two kind of flows: - Discrete flow process: discrete items move through the flow process. These is the most used flow in the industrial system. Ex. automotive, textile products, mechanical parts, home appliances, etc - Continuous flow process: products continuously move through successive productions states. Ex. chemical plants, oil productions plants, electric current flow, etc.
> 
> 


# Lesson 2 - AN INTRODUCTION TO LEARNING CURVES

> What do we mean by “learning” in the field of industrial engineering and operations management?

**Learning effect:** the phenomenon in which humans or human organizations gain experience through the repetition of the same activity. Experience takes the form of either or both improved manipulative skills and in process procedures. (adapted from Dar-El, 2000)

**Human learning** has developed almost independently in four areas: 
- *Individual learning*: I study myself the things i need to learn
- *Product learning:* the focus is on integrating the efforts of individual learning together with improvements in all aspects of materials and information flow involved in putting the whole product together 
- *Product development learning:* product design changes are the essential ingredients in this type of learning, with an emphasis on design quality. Change the product to become better. 
- *Learning Organizations*: how companies gets better at realizing multiple products and how fust they learn to change it. 

**Learning curve:** a graphical/mathematical representation of the empirical relationship between performance in completing an activity and experience, where increased repetition of a task leads to efficiency improvements
![[Lessons-1791363294221.webp]]

> *Learning curve synonyms:* progress function, cost-quantity relationship, cost curve, product acceleration curve, improvement curve, performance curve, experience curve, efficiency curve

### Why are learning curves important?
Learning curves provide several benefits at different levels of decision-making: 
1. At the **planning/operations level**: 
	1. setting more accurate labor standards and monitoring realistic production objectives 
	2. forecasting the available working time of a process 
	3. predicting production output and non-conforming units 
2. At the **management decision support systems/tactical level**: 
	1. more accurate inventory management and lot-sizing models 
	2. better supplier selection 
	3. more accurate vehicle routing algorithms 
	4. improved manual order picking procedures 
3. At the **strategic level**: 
	1. optimal timing of new product introductions
	2. competitive pricing decisions 
	3. determining investment levels to stimulate process and product innovations
	4. vertical integration decisions

> amazon: has a lot of temporary workers thus it has to change continuously the work flow.
> We need to know how fast the workers are to coordinate at its beast the work flow.

we need to ask ourself how fast the flow is and how we could seed it up by changing (e.g.) from linear to batch production.

Factors influencing learning at individual level: 
1. Methods improvements: you do things slightly more efficiently 
2. Worker Selection 
	1. Differences between workers: every worker has its own speed. ideally for the company we would like to have all the same speed.
	2. Variations within each operator 
3. Previous experience 
4. Training
5. Motivation: even in the same day a worker could be more ore less motivated. for example before and after lunch.
6. Job Complexity 
7. Number of Repetitions 
	1. Does learning continue forever? 
	2. How many cycles to reach Time Standard? 
	3. The size of job orders 
8. Length of Task 
9. Errors 
10. Forgetting 
11. Continuous Improvement

### 1) The Power Model
The Power Model was first introduced in 1936 by T. P. Wright while studying aircraft production. He discovered that as output doubles, the time required to produce each unit reduced by a constant percentage (20%)![[Lessons-1791364050157.webp]]
the more aircraft you produce the less time it takes. eg producing 4 instead of 2 is 20% faster.
Also known as Wright’s Learning Curve (WLC), follows this formula:
$$
t_n = t_1 \cdot n^{-b} \space{} [sec] 
\\ \\
\text{where:} \\ 
- n \text{ is the number of cycles (or repetitions) completed} \\ 
- t_n \text{ is the performance time to complete the n-th cycle} \\
- t_1 \text{ is the performance time to complete the first cycle} \\
- b \text{ is the learning constant}\\
$$
> b is the most important parameter since it tells how fast we are learning.

The WLC can also be expressed in terms of cost:
$$
C_n = C_1 \cdot n^{-b} \space{} [sec] 
\\ \\
\text{where:} \\ 
- n, b \text{ are defined as before} \\
- C_n { is the cost for producing the n-th unit} \\
- C_1 { is the cost for producing the first unit} \\
$$
Taking the logarithm of both sides of the WLC results in a linear equation. Thus:
$$
t_n = t_1 \cdot n^{-b} \\
\ln(t_n) = \ln(t_1 \cdot n^{-b}) \\
\ln(t_n) = \ln(t_1) - b \cdot \ln(n) \\ 
\ln(C_n) = \ln(C_1) - b \ln(n)
$$
![[Lessons-1791364651586.webp]]

An interesting characteristic of the Power Model is that each time production is doubled, the performance time is reduced by a fraction that depends from the value of the learning constant, b. 

Consider two different number of cycles, $n_1$ and $n_2$ , such as:

$$ n_2 = 2 n_1$$

Substituting these two values into the Power Model:
$$
t_{n_2} = t_1 \cdot (2n_1) ^ {-b} \\
t_{n_1} = t_1 \cdot (n_1) ^ {-b} 
$$

Dividing the first by the second equation gives:
$$
\frac{t_{n_2}}{t_{n_1}} = 2^{-b}
$$

Therefore, we can derive a new parameter called Φ, the Learning Rate (LR or Learning Slope):
$$
\Phi = 100 \cdot 2^{-b}
$$
$\Phi$ can be interpreted as the «percent learning» that occurs each time output is doubled. In fitting data from the aircraft industry, Wright empirically found $\Phi$ to equal 80% (hence the 20% rule), with its equivalent b value of 0.322. 

> Although there is a tendency to consider the 80% learning rate as a fixed value, $\Phi$ varies depending on job complexity, ranging from **65% up to 95%** (see next slides)

In the image on the right we change $\Phi$ keeping $t_1$ constant. Vice versa on the right we keep $\Phi$ constant but change $t_1$

![[Lessons-1791364981913.webp]]
![[Lessons-1791365406344.webp]]
This table shows the learning slope based on different skills starting on the same point
![[Lessons-1791365529068.webp]]
Learning **Slopes for machining operations**
![[Lessons-1791365703249.webp|322]]
Learning Slopes for **various activities in the defense sector**
![[Lessons-1791365720851.webp|378x389]]








