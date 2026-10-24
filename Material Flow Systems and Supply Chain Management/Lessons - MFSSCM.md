> [!IMPORTANT] 
> moodle: https://stem.elearning.unipd.it/course/view.php?id=17225
> 

# L0 - Introduction
https://stem.elearning.unipd.it/pluginfile.php/1464599/mod_resource/content/1/LECTURE%201-introduction.pdf

**Learning Objectives:** 
1. to acquaint students with the concepts of material flow systems in manufacturing and logistics, 
2. to learn optimization modelling and analyses of material flow systems, 
3. to understand material flow integration issues in flexible and resilient supply networks, 
4. to apply analytics software tools for case-based problem solving: Software Anylogistix, 50 student licenses and a teamwork during the course

**Description:** 
1. Analyses of material flows in manufacturing: a particular focus on Assembly To Order systems and their impact on in-house logistics. 
2. Optimization modelling and analyses of material flow systems: part feeding problems for in-house logistics, Inventory Routing Problems for Outbound and Inbound Logistics. 
3. Material flow structures, physical assets (AGV and LGV fleet design), material handling systems and operational decisions influencing system performance. 
4. Digitalization of material flow systems, from MES (Manufacturing Execution System) to TMS (Transport Management System) and digital supply networks. 
5. AnyLogistix laboratory: logistics network design principles, logistic facilities location, transportation flows optimization and dynamic flow simulation. Emphasis is given to problem-based modelling and solving with a team working and real case data. 

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

# Lesson 1
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

```horizontal
Learning **Slopes for machining operations**
![[Lessons-1791365703249.webp|322]]
---
Learning Slopes for **various activities in the defense sector**
![[Lessons-1791365720851.webp|394x406]]
```


#### Example
![[Lessons-1791365838242.webp]]

![[Lessons-1791365936386.webp]]![[Lessons-1791365854967.webp]]

![[Lessons-1791365879363.webp]]

How to calculate the total time Tm to complete m cycles? Let’s assume that the number of repetitions is a continuous variable (the assumption is more exact for n>=15). Then, we can integrate the power model between 0 and m:
![[Lessons-1791366282377.webp|518]]
> m is the m-th unit. this integral tells us how much time it takes to go from unit 1 to unit m

### 1b) The Cumulative Average Power Model

This is the original version of the WLC, as Wright analysed the relationship between the direct labour man hours and the cumulative number of units produced:

$$
\hat{t_n} = t_1 \cdot n^{-b} \quad [\text{sec}]
$$

**where:**

- $n$ is the number of cycles (or repetitions) completed
- $t_1$ is the performance time to complete the first cycle
- $b$ is the learning constant

**and:**

- $\hat{t_n}$ is the cumulative average time for completing $n$ cycles

With this formulation, it is slightly more difficult to calculate $t_n$, the performance time for the $n$-th repetition:

$$
t_n = T_n - T_{n-1}
$$

$$
t_n = t_1 \cdot \left[n^{(1-b)} - (n-1)^{(1-b)}\right]
$$

This version of the WLC is generally used when regression values with the Power Model are too low. The cumulative average, in fact, dampens out the effect of outliers.

The Stanford B-model proposes a modification of the Power Model, introducing the parameter B:

![[Lessons-1791366837820.webp]]

![[Lessons-1791366862945.webp]]


#### 3) Plateau Learning Model
The main issue with the WLC and its derived models is that, for an infinite number of cycles, the execution time goes to zero. That is not realistic. The Plateau Model tries to avoid this problem:

![[Lessons-1791367044462.webp]]
$𝐴$ represents the **plateau (Threshold / limit / asymptote)**, the performance time of highly experienced workers under nominal motivating conditions.

![[Lessons-1791367026169.webp]]
> This model is way more realistic since it introduce a limit to the learning curve. The more you learn the less it's likely you find something new to learn.

#### 4) De Jong’s Learning Model
De Jong (1957) proposed a model that can account for both manual and machine-controlled tasks. While the manual parts are compressible with respect to experience, the machine part is not. Production time is split in two parts: one is subject to the traditional power learning process, while the other remains constant and represents the incompressible part of the task:
![[Lessons-1791367305988.webp]]
> This model works for bot human and machine. M = % of the work done by the machine.

![[Lessons-1791367398103.webp]]

```horizontal

![[Lessons-1791367653881.webp]]
---
![[Lessons-1791367662826.webp]]

```

![[Lessons-1791367703187.webp]]
# LECTURE 3: CLUSTERING METHODS
### Create a group layout: clustering methods
The DCA (Direct Clustering Algorithm) was introduced in 1982 by H.M. Chan and D.A. Milner. The algorithm restructures the existing machine / component (product) matrix of a job shop layout by switching the rows and columns in such a way that a resulting matrix shows component families (groups) with corresponding machine groups.
The method link parts and machines but also we can say products and workstations. It build and incidence matrix (*binary matrix*) and find clusters in order to process products as a family.
![[Lessons - MFSSCM-1792234942250.webp]]
## DCA method: 7 steps - Example 1
1. Form machine part matrix -> **incidence matrix**
2. Sum the 1s in each column and row
![[Lessons - MFSSCM-1792234991939.webp]]

3. Order the rows in **descending order**
4. Order the columns in **ascending order**
![[Lessons - MFSSCM-1792235060783.webp]]
5. Sort the **columns** -> 1 in the first row moves left then the second row etc
![[Lessons - MFSSCM-1792235114586.webp]]
6. Sort the **rows** -> 1 in the first column moves upwards then the second column etc
![[Lessons - MFSSCM-1792235204207.webp]]

7. Form sells -> Final Solution
![[Lessons - MFSSCM-1792235248110.webp]]
### Bottleneck machines - Example 2
Possible solutions:
- locate the bottleneck machines close to each other:
	- in different cells 
	- at the boundary between cells
- redesign the parts
- outsource the parts
- duplicate machines and place the min each cell
### Direct clustering algorithm "bottleneck machines"
![[Lessons - MFSSCM-1792252736374.webp|439]]
- Duplicate machines and place them in each cell 2a and 2b
- Duplicate machines and place them in each cell 3a and 3b
![[Lessons - MFSSCM-1792252778399.webp]]

![[Lessons - MFSSCM-1792252857340.webp|636]]
 
## Hierarchical Clustering method: single and complete linkage
Values = effective processing times [min], learning effect included
![[Lessons - MFSSCM-1792253320864.webp]]
***Where do these numbers come from?***
We get the numbers by taking the pieces. we measure the time between start and end of the task. this is called the **chrono tecnique**

1. *Stopwatch time study:* each product model was timed on each workstation over the first units produced.
![[Lessons - MFSSCM-1792254390764.webp|248]]
2. *First units are slower:* operators are still learning the task.
3. *Learning curve 80%:* every time output doubles, processing time drops by 20%.
![[Lessons - MFSSCM-1792254415742.webp|356]]
4. The value in the matrix is the effective time at the *learning plateau*, not the first measured time.

Example: product a, workstation 1 → 4.9 min (1st unit) → 2.0 min (plateau)
They are the processing time (we use the Euclidian distance):
![[Lessons - MFSSCM-1792253896053.webp]]
By putting the close distances before we get:
$$
d_{ab} = \sqrt{(b_{a1} - b_{b1})^2 + (b_{a2} - b_{b2})^2 + \dots + (b_{an} - b_{bn})^2}
$$

**Important:** if we had put the first measured time (4.9 min) in the matrix, we would have more than doubled the real workload of the 
 workstation, and the clustering would have grouped the products incorrectly.

### Linkage criterion

| Criteria Name              | Formula                         |
| -------------------------- | ------------------------------- |
| complete linkage           | $\max{d(a,b) : a\in A, b\in B}$ |
| Minimum or single distance | $\min{d(a,b) : a\in A, b\in B}$ |
**Single Linkage**
Clustering criterion based on the shortest distance
![[Lessons - MFSSCM-1792254532625.webp]]
**Complete Linkage**
Clustering criterion based on the longest distance
![[Lessons - MFSSCM-1792254576679.webp]]
>[!Note] Important note
> By applying one or the other most of the times we obtain similar solutions

### Bottom up agglomerative clustering
- each point is initially considered as a cluster
- closest clusters are iteratively merged
- single linkage criterion $dist(C_i,C_j) = \min_{a\in C_i b \in C_j}{d(a.b)}$
- "It's A tree upside down"

![[Lessons - MFSSCM-1792254631560.webp]]


### A simple Example to understand the concept better
![[Lessons - MFSSCM-1792254823469.webp]]
![[Lessons - MFSSCM-1792254832499.webp]]

![[Lessons - MFSSCM-1792254844065.webp|651]]

![[Lessons - MFSSCM-1792254858490.webp|669]]

## Process constraints (internal supply chain):
**Installation sequence:** installed in shingle fashion, starting either from the bottom or top of the building and going around each floor until the whole building is dressed up
Pre-defined **assembly sequence:** determined by the packing and the installing sequence (constrained by the project)
![[Lessons - MFSSCM-1792254923028.webp]]
The binary $A(=a_{ij})$ PTIM is defined as follows:
$$
a_{ij} =
\begin{cases}
1 & \text{if assembly task } j \text{ is required by product } i \\
0 & \text{otherwise}
\end{cases}
$$

Project-Task incidence matrix (33 projects x 146 tasks)
![[Lessons - MFSSCM-1792255437376.webp]]

```horizontal
![[Lessons - MFSSCM-1792255474784.webp]]
---
![[Lessons - MFSSCM-1792255503714.webp]]
```

Design of 3 new assembly lines dedicated to the 3 product families:
![[Lessons - MFSSCM-1792255523210.webp]]

# LESSON 4 

## Supply chain
A supply chain is a system of organizations, processes, activities, information, and resources involved in supplying a product or service to a consumer.
![[Lessons - MFSSCM-1792255636974.webp]]

## Supply Network
We need a sw to optimise the network and it has to be intended even for people who don't have a background
![[Lessons - MFSSCM-1792255661581.webp]]

## Supply Network Challenges
We need to consider location, size, tactical decisions etc. Therefore we need to have the informations before the simulation even starts.
- **Strategic:** size and location of manufacturing plants or distribution centres, the structure of service networks and designing the supply chain. 
- **Tactical:** production, transportation and inventory planning.
- **Operative:** production scheduling and control, inventory control and vehicle routing.

## Your Supply Chain Is Being Constantly Evaluated (Common questions)
![[Lessons - MFSSCM-1792255884371.webp]]

> [!Danger] From here the slides show the Anylogistic Software. It's best to directly see them to understand at best how it works

## What is GreenfieldAnalysis
Greenfield analysis is an analytical type of experiment that uses the center-of- gravity approach to find optimal locations for new site(s) that will be managing the given demand of the supply chain.
- Objective: Find the number and potential areas to locate supply chain facilities
- Criteria: Minimizing "transportation flows" which is calculated as \<distance\> * \<product amount\>
- Assumptions: routes are straight
**GFA allows you to:**
- Find the optimal locations for the specified number of sites (DCs by default)
- Calculate the optimal number of sites considering the specified maximum distance to a customer
**GFA considers the following data:**
- Products
- Demand
- Supply Sources
- Customer Locations
- Service distance constraints ($x_{ij} \leq 200km$)
- Number of potential facilities (example: from historical data)

### Center-of-gravity analysis \[$\approx$ GFA is almost the same\]
> Location of the customers are the input parameters

In technical terms, an ordered pair of ($x;y$)-coordinates represents each customer location. You can’t change these data; they are input data or problem parameters. 
- By contrast, your new warehouse’s ($x;y$)-coordinates ($p_x;p_y$) are variable. We will determine them after it calculates the data you provide in a way that matches the parameters you set. As a result, we say $p_x$ and $p_y$ are this scenario’s decision variables.
- We also assume our transportation cost is linearly proportional to the distance and the transportation volume (that is, the demand). We can see the total transportation costs will depend on the coordinates ($p_x;_py$) of our prospective warehouses and distances. We assume the transportation costs from the prospective warehouse ($p_x;p_y$) to a customer location ($x_i;y_i$) is more or less equal to the distance and demand.
We need to determine the distances d((px; py); (xi;yi)) between the i customer location and the warehouse to calculate transportation costs. To minimize payments to the forwarding company, you must vary px and py as long as Z(px, py) becomes minimal. 
Total costs Z(px;py) is a determinant in GFA since we seek to find the optimal location of a warehouse subject to total costs minimization to serve all customer demands from the warehouse. We assume that the total transportation cost sum is proportional to the distance and the transportation volume (i.e., the demand). This leads us to the formulation of the objective function, as shown in below equation:
$$
Z(p_x,p_y) = \sum_{i=1}^{N} d((p_x,p_y),(x_i,y_i))\cdot D \rightarrow \min
$$
> [!Important] this is the center of gravity model of location analysis


**Objective function**
$$
Z(p_x,p_y) = \sum_{i=1}^{N} d((p_x,p_y),(x_i,y_i))\cdot D \rightarrow \min(1)
$$
![[Lessons - MFSSCM-1792318272280.webp]]

![[Lessons - MFSSCM-1792318283079.webp|682]]

#### Euclidian Distance
The following consecutive steps have to be executed in the given order.
- The partial derivatives of Z with respect to px and py are determined.
- The partial derivatives are set equal to zero to determine the optimal location.
$$
Z(p_x,p_y) = \sum_{i=1}^{N} d((p_x,p_y),(x_i,y_i))\cdot D \rightarrow \min(1)
$$
![[Lessons - MFSSCM-1792318525269.webp|540]]

We first consider the case in which all customers have equal demand, i.e. $D_i=1$ for all i.

![[Lessons - MFSSCM-1792318711422.webp]]
![[Lessons - MFSSCM-1792318722472.webp]]
![[Lessons - MFSSCM-1792318734702.webp]]

## Miehle algorithm
To break the circulation in the formulas (6) and (7), Miehle (1958) proposes an approximation approach. The basic idea of the Miehle algorithm comprises the consecutive calculation of a sequence of solutions $(a_0;b_0), (a_1;b_1), (a_2;b2_), ... of (1)$. The values of $(a_{i-1};b_{i-1})$ are used as $p_x$- and $p_y$-values in the right-hand part of  he Eqs. (6) and (7) and they are used to calculate the next solution (ai ;bi). This approach represents an example of a recursive calculation. If we calculate the coordinate pairs in this way, then the sequence of objective function values $Z(a_0;b_0), Z(a_1;b_1), Z(a_2;b_2), \cdots$ decreases and converges towards the minimal possible performance value. Therefore, the sequence of calculated coordinates approximates the optimal pair of coordinates of the new warehouse with respect to the minimization of the overall required transport performance.

**Iterations of the Miehle algorithm applied to the TT Profi data**
![[Lessons - MFSSCM-1792318885018.webp]]

**Graphic representation of the progress of the Miehle algorithm**

![[Lessons - MFSSCM-1792318903764.webp]]

> [!Danger] Summary of Miehle algorithm
> The main steps of the Miehle approach:
> - Start: determine an initial pair of coordinates ($a_0;b_0$) by applying Eq. (4) to determine a0 and Eq. (5) to determine b0.
> - Iteration: Use ($a_i; b_i$) in Eqs. (6) and (7) to calculate the new coordinates ($a_{i+1};b_{i+1}$). Repeat the calculation until the distance between two consecutive solutions is smaller than a predefined threshold. The final coordinates approximate the optimal facility location.

#### Rectilinear distance
$$
\begin{equation*}
p_x = \frac{\sum_{i=1}^{N} D_i \cdot x_i}{\sum_{i=1}^{N} D_i}
\qquad
p_y = \frac{\sum_{i=1}^{N} D_i \cdot y_i}{\sum_{i=1}^{N} D_i}
\end{equation*}
$$

![[Lessons - MFSSCM-1792320338002.webp]]

$$
p_x = \frac{30-45+39+157.5-150}{11} = 7.5 \\
py = \frac{-240-30+75-363.5+160}{11} = -27
$$
## Greenfield Analysis Experiment
Greenfield Analysis considers the following data that we will specify during the tutorial steps:
- Customers
- Locations of the customers -> Latitude (x) and Longitude (y)
- Products
- Demand for each customer and product
- Direct distance between customers and DCs/Warehouses

anyLogistix uses GIS (Geographic Information System) data provided by OpenStreetMap. The GIS map displays the elements of the supply chain scenario and their connections. Once you create a new element (e.g. a customer) or alter an existing connection, the GIS map will be instantly updated.

**What is GreenfieldAnalysis with Roads?**
GFA does not take into account roads, cities, peculiarities of geographical areas etc., that is why it may suggest putting DCs on top of a mountain or in the middle of a sea. To consider actual roads and population of the cities, use the GFA with road experiment. In contrast to GFA, the GFA with roads experiment considers actual roads and population of cities, which allows it to suggest more accurate DC locations.

> [!Important] Summary
> Greenfield analysis is used to find the NUMBER and AREAS to locate facilities
> To conduct a GFA experiment you need to define: 
> - Customers/Market Node Locations
> - Products 
> - Demand 
>
> Criteria: Minimize transportation flows which is calculated as \<distance\> * \<product amount\>
> 
> GFA Results: 
> - Areas to locate the facilities 
> - Flows between facilities and customers 
> - Customer center of gravity & service distances
> 
> Options: 
> -  The GFA experiment can calculate locations based on direct distance or leveraging actual road pathways
> - Inbound supply nodes and flows can be considered

# LECTURE 5: ASSEMBLY SYSTEMS DESIGN
## Wortmann classification 
WHY DO WE USE THIS CLASSIFICATION? TO UNDERSTAND WHERE TO PUT THE INVENTORY [Stocks]
Example: Fincantieri  -> a Designed To Customers Specifications
![[Lessons - MFSSCM-1792321720193.webp]]

> [!Definition] FLOW LINE
> A transfer line is a manufacturing system with a very special structure. It is a linear network of service stations or machines ($M_1, M_2, \dots, M_n$) separated by buffer storages ($B_0, B_1, \dots, B_n$). Material flows from outside the system to $B_0$, then to $M_1$, then to $B_1$, and so forth until it reaches $B_n$ after which it leaves. Figure 1 depicts a two-machine transfer line. The squares represent machines and the triangles represent buffers.


![[Lessons - MFSSCM-1792321738768.webp]]

DEFINITION OF ASSEMBLY LINE (SYSTEM)
An assembly line is one of the subsystems in a manufacturing system where the individual components of a product are joined together and thus integrated into a semi-finished or into the final product.

THIS IS A CONVERGENT PROCESS: from several parts to a final finished product

![[Lessons - MFSSCM-1792321907652.webp]]

**Inputs, outputs and resources of an assembly system**

![[Lessons - MFSSCM-1792321925183.webp]]![[Lessons - MFSSCM-1792321932636.webp]]

![[Lessons - MFSSCM-1792321941909.webp]]

![[Lessons - MFSSCM-1792321948392.webp]]

### Assembly cycle and assembly chart definition
Once the products to be produced in-house have been defined, decisions are needed as to how the products will be assembled. 
**Assembly cycle definition** involves the following steps:
1. Define elemental operations: called TASK
2. Identify alternative processes
3. Analyse task precedence (by understanding the technical constraint) based on technological constraints
4. Define an assembly chart and a precedence diagram
![[Lessons - MFSSCM-1792322026579.webp]]

The easiest method of understanding the assembly cycle and constructing an assembly chart is to begin with the completed product and to trace the product disassembly back to its basic components.

![[Lessons - MFSSCM-1792322055582.webp]]![[Lessons - MFSSCM-1792322061623.webp]]

#### PRECEDENCE DIAGRAM DEFINITION
A second viewpoint, based on graph and network theory, is to interpret the charts as network representations, and generate the so-called PRECEDENCE DIAGRAM. A precedence diagram shows assembly task in the circles and precedence relations between tasks by arrows/arcs
--> ALTERNATIVE ASSEMBLY SEQUENCES In some cases, industrial engineers report also the parts codes on the arcs.

![[Lessons - MFSSCM-1792322094012.webp|608]]


```horizontal
![[Lessons - MFSSCM-1792322102562.webp|593]]
---
![[Lessons - MFSSCM-1792322132584.webp]]
---
![[Lessons - MFSSCM-1792322141266.webp]]
```

![[Lessons - MFSSCM-1792322152481.webp]]

# LECTURE 6: ASSEMBLY SYSTEMS LAYOUT AND BALANCING PROBLEM
![[Lessons - MFSSCM-1792322177182.webp|1073]]

![[Lessons - MFSSCM-1792322188824.webp]]

#### PACED ASSEMBLY SYSTEMS
In a “paced line”, the handling system is periodically moving from station to station and a product stays at a station for a fixed time period c, and this period is the same for all stations. The cycle time is defined also as the maximal amount of time a product can be worked by a station.
If $n$ stations are involved: 
$n * c = \text{Assembly Flow Time}$ 
$\text{Assembly Lead Time} = \sum t_j$ 
$c = \text{cycle time (takt time)}$
$c = (460 \text{ min/day} * 60 \text{ s/min}) / (920 \text{ pcs/day}) = (27600 \text{ s/day}) / (920 \text{ pcs/day}) = 30 \text{ s/pcs}$
![[Lessons - MFSSCM-1792322255589.webp]]

**UNPACED ASSEMBLY SYSTEMS** _(Handwritten: INSERT BUFFERS BETWEEN WORKSTATION)_
While an "un-paced line" is equipped with buffers located between stations (the decoupling buffers can be realized between groups of stations or between single stations), and in this case the cycle time serves as maximal possible average station time.
c realized -> work load of the bottleneck station, that is S2
$\text{Assembly Flow Time} = \text{Assembly Lead Time} = \sum t_j$

> EACH STATION INDEPENDENT TALK OF CYCLE TIME ALWAYS LOWER THAN C OBJECTIVE
  
![[Lessons - MFSSCM-1792322456497.webp]]

#### ASSEMBLY LINE BALANCING PROBLEMS: ALBP
The assembly line balancing problem (ALBP) consists of assigning tasks to an ordered sequence of stations such that the precedence relations among the tasks are satisfied and some performance measure is optimized.

![[Lessons - MFSSCM-1792322558827.webp]]

#### ASSEMBLY LINE BALANCING PROBLEMS: CLASSIFICATION

![[Lessons - MFSSCM-1792322582219.webp]]

# LECTURE 7: METHODS FOR ASSEMBLY LINE BALANCING HEURISTIC PROCEDURES
Consider the example reported in Dolgui and Proth (2010): a manufacturing process consisting of 15 tasks denoted $A, B, \dots, O$. The manufacturing times and the direct predecessors of the tasks are given in the following table. The cycle time (or takt time) is $c=40$.

## **The Largest Candidate Rule (LCR)**

![[Lessons - MFSSCM-1792322642764.webp]]
**Procedure:**
Step 1) List all elements in descending order of $T$ value, starting with the largest $T$ at the top of the list.
Step 2) Assign elements to the first workstation starting at the top of the list and selecting the first feasible element for placement in the station. A feasible element is one that satisfies the precedence requirements and does not cause the sum of the $T$ values at each station to exceed the cycle time.
Step 3) Repeat step 2.

![[Lessons - MFSSCM-1792322799561.webp]]
## ***5.2.3 Ranked Positional Weights Method (RPW)***
This heuristic approach was introduced by Helgeson and Birnie in 1961 and it can be easily used manually to solve small-size problems, since it takes into account both the T value of the element and its position in the precedence diagram. According to this algorithm the tasks are assigned to workstations in the general order of their RPW values that are used as task weights and computed as follows:

$$RPW_j = t_j + \sum_{h \in F_j^*} t_h$$
Step 1) Calculate the RPW for each task by adding the task time and the time values for all the tasks that follow it in the arrow chain of the precedence diagram (the followers).
Step 2) List the elements in the order of their RPW, starting with the largest RPW, include the task value and immediate predecessors for each element, for convenience.
Step 3) Consider the set A of available tasks for each workstation and assign tasks to stations in the decreasing order of their RPW value, avoiding cycle time violations.

By applying the heuristic procedure to the numerical example done before we obtain the following RPW weights:

| TASKs | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RPW | 101 | 79 | 74 | 91 | 67 | 51 | 77 | 47 | 60 | 51 | 41 | 22 | 26 | 17 | 9 |


![[Lessons - MFSSCM-1792322854759.webp]]



![[Lessons - MFSSCM-1792322904124.webp]]

## ***5.2.4 Kilbridge and Wester’s Method (KWM)***
In the heuristic approach presented in Kilbridge and Wester (1961), tasks are organized into levels according to their position in the precedence diagram. This overcomes one of the difficulties with the largest candidate rule (LCR), with which elements at the end of the precedence diagram might be the first candidates to be considered, simply because their task time values are large.

Procedure:
Step 1) Construct the precedence diagram so those nodes representing work elements of identical precedence are arranged vertically in columns.
Step 2) List the elements in order of their columns, where the first column represents level 1, which is composed by tasks without predecessors. More generally, level $i$ represents tasks with at least a direct predecessor at level $i - 1$. If one task can be located in more than one level, list all levels by the element to show the transferability of the element.
Step 3) To assign elements to workstations, start with the first level and continue the assignment procedure in order of level number until the cycle time is reached.

At each level, if the tasks cannot be assigned together at a station, they can be selected using a rule: decreasing order of task time, decreasing order of weights as in the RPW method, or others).
Following a balancing solution is provided applying the KWM heuristic approach and using the task weights according to RPW method in case of several assignment possibilities.

![[Lessons - MFSSCM-1792322973847.webp]]

# LECTURE 7: ASSEMBLY SYSTEM BALANCING WITH A MATHEMATICAL METHOD
The following mathematical formulation is based on the Patterson and Albracht algorithm (1975), and considers the following assumptions:
- Single-product assembly line
- Fixed cycle time
- Deterministic and integral operation times
- No assignment restrictions beside the precedence constraints
- Serial line layout with one-sided stations
- All stations are equally equipped

> the points above are the **assumptions of the model**

## Steps to the solution
Generally, starting from the data regarding the tasks operation time, the precedence diagram and the required production rate, the balancing procedure follows these phases:
1. calculation of cycle time (c)
2. definition of number of stations (m)
3. identification of earliest and latest stations
4. definition of constraints
5. optimization of solution

### Step 1
in step 1, the calculation of cycle time is very simple and it is related to the required production rate by this formula:
$$ c = \frac{60}{p} $$expressed in \[min\] if p is measured in \[pcs/h\] or:
$$ c = \frac{3600}{p} $$expressed in \[sec\] if p is measured in \[pcs/h\]

### Step 2
Next, to define the number of stations, the theoretical value m∗ is calculated as the ratio between the total time to assemble the products and the cycle time:
$$ m^* = \left\lceil \frac{\sum_j t_j}{c} \right\rceil $$
Usually the next higher integer is chosen to define the real number of stations m, but in some cases it could be higher, mainly due to the operation time and precedence diagram.
### Step 3
In step 3, the precedence relations are used to restrict the number of stations to which a task can be assigned, delimited by the earliest possible workstation for task j ($E_j$ ) and the latest possible workstation for task j ($L_j$ ) using the following equations:

$$ x_{jk} = \begin{cases} 1 & \text{if task } j \text{ assigned to work station } k \\ 0 & \text{if task } j \text{ not assigned to work station } k \end{cases} $$
$$ e_j = \left\lceil \frac{t_j + \sum_{h \in p_j^*} t_h}{c} \right\rceil $$

slide before (riferito a $m$). Latest station index (riferito a $l_j$)

$$ l_j = m + 1 - \left\lceil \frac{t_j + \sum_{h \in f_j^*} t_h}{c} \right\rceil $$

example:
- 10 task
- 4 ws
- $4 \cdot 10 = 40$ \text{ variables \[binary\]}
resolution time is lower.

The first one considers that a task j must not start before all its preceding tasks are performed, while the second formula delimits the latest station to which the same task j can be allocated based on its successors and the total number of stations. As a result, the range of workstations \[$E_j, L_j$\] to which each task can be assigned is obtained and the number of binary variables is reduced, this range is called the Station Interval of task j ($SI_j$).
### Step 4
Then, based on the formulation developed by Patterson & Albracth (1975), with the binary variable $x_{jk}$ as 1, if task j is assigned to station k and 0 otherwise, the following constraints are introduced:
1. Occurrence constraints (ensuring that each task is assigned to exactly one stations in its interval.
$$ \sum_{k \in si_j} x_{jk} = 1 \quad \text{for } j = 1, \dots, n $$
2. Cycle time constraints (guaranteeing the respect of cycle time in each station)
$$ \sum_{j \in b_k} t_j \cdot x_{jk} \le c \quad \text{for } k = 1, \dots, m $$
3. Precedence constraints (assuring that no task is assigned to an earlier station than its predecessor)
$$ \sum_{k \in si_h} k \cdot x_{hk} \le \sum_{k \in si_j} k \cdot x_{jk} \quad \text{for } (h,j) \in a \text{ and } l_h \ge e_j $$
Based on these constraints, the algorithm will find all the existing feasible solutions for m=m* and a fixed and known cycle time c. If none feasible solution exist, the algorithm will be reiterated for m=m*+1, and so on until it will find at least one feasible solution. Without defining an objective function to minimize or maximize, the model is a so-called SALBP-F, since the aim is not to find an optimal solution but all the existing feasible solution for fixed values of m and c.
![[Lessons - MFSSCM-1792849037250.webp]]
### Step 5
#### Objective functions for SALBP-1
When the cycle time c is fixed and we want to minimize the number of stations m opened in the system in order to reduce the labour costs, we need to add to the previous algorithm an objective function. The analyst according to the specific objectives to reach in the system design can define different objective functions. The most used objective functions have the final scope to smooth the workload among the workstations. This can be achieved in several ways, two most used objectives functions are the following.
1) Minimize the maximum station idle time as:
$$ o.f. = \min \left\{ \max_k \left( c - \sum_{j \in b_k} t_j \cdot x_{jk} \right) \right\} $$
2) Minimize the station smoothness as:
$$ o.f. = \min \sum_k \left| \sum_{j \in b_k} t_j \cdot x_{jk} - \frac{\sum_j t_j}{m} \right| $$

> WHERE: Both objective functions also subject to the constraints sets 1, 2 and 3 on step 4

#### Objective functions for SALBP-2
When the number of stations m is fixed and the cycle time needs to be minimized, the following objective function should be added to the previous SALBP-F algorithm:
$$
O.F. = \min Z = c
$$
Where c is a variable in the model and not a fixed numerical value, and constraints sets 1, 2 and 3 introduced in the previous paragraph assure the respect of the basic assembly line requirements and in particular, the constraint set 3 ensures that the total task processing time assigned to workstation k does not exceed the cycle time c.
![[Lessons - MFSSCM-1792849263881.webp]]

Using these parameters, we can now write all the equations about the constraints:
1) Occurrence Constraints (one equation for each task):
$$ \sum_{k \in si_j} x_{jk} = 1 \quad \text{for } j = 1, \dots, n $$
$$ \begin{cases} x_{a1} = 1 \\ x_{b1} + x_{b2} = 1 \\ x_{c1} + x_{c2} = 1 \\ x_{d1} + x_{d2} = 1 \\ x_{e1} + x_{e2} = 1 \\ x_{f2} + x_{f3} = 1 \\ x_{g2} + x_{g3} = 1 \\ x_{h3} = 1 \end{cases} $$
2) Cycle time constraints (one inequality formula for each station):
$$ \sum_{j \in b_k} t_j \cdot x_{jk} \le c \quad \text{for } k = 1, \dots, m $$$$ \begin{cases} t_a \cdot x_{a1} + t_b \cdot x_{b1} + t_c \cdot x_{c1} + t_d \cdot x_{d1} + t_e \cdot x_{e1} \le 10 \\ t_b \cdot x_{b2} + t_c \cdot x_{c2} + t_d \cdot x_{d2} + t_e \cdot x_{e2} + t_f \cdot x_{f2} + t_g \cdot x_{g2} \le 10 \\ t_f \cdot x_{f3} + t_g \cdot x_{g3} \le 10 \end{cases} $$
3) Precedence constraints (one inequality formula for each arc in the precedence diagram)
$$ \sum_{k \in si_h} k \cdot x_{hk} \le \sum_{k \in si_j} k \cdot x_{jk} \quad \text{for } (h,j) \in a \text{ and } l_h \ge e_j $$
$$ \begin{cases} 1 \cdot x_{a1} \le 1 \cdot x_{b1} + 2 \cdot x_{b2} \\ 1 \cdot x_{a1} \le 1 \cdot x_{c1} + 2 \cdot x_{c2} \\ 1 \cdot x_{a1} \le 1 \cdot x_{d1} + 2 \cdot x_{d2} \\ 1 \cdot x_{b1} + 2 \cdot x_{b2} \le 2 \cdot x_{f2} + 3 \cdot x_{f3} \\ 1 \cdot x_{c1} + 2 \cdot x_{c2} \le 2 \cdot x_{f2} + 3 \cdot x_{f3} \\ 1 \cdot x_{d1} + 2 \cdot x_{d2} \le 1 \cdot x_{e1} + 2 \cdot x_{e2} \\ 1 \cdot x_{e1} + 2 \cdot x_{e2} \le 2 \cdot x_{f2} + 3 \cdot x_{f3} \\ 2 \cdot x_{f2} + 3 \cdot x_{f3} \le 2 \cdot x_{g2} + 3 \cdot x_{g3} \\ 2 \cdot x_{g2} + 3 \cdot x_{g3} \le 3 \cdot x_{h3} \end{cases} $$
![[Lessons - MFSSCM-1792849386595.webp]]


```horizontal
![[Lessons - MFSSCM-1792849428722.webp|504x401]]
---
![[Lessons - MFSSCM-1792849437877.webp]]
```


















