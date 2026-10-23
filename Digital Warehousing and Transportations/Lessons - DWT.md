
> [!Important] https://stem.elearning.unipd.it/course/view.php?id=16780

# Lesson 0

**Why DW&T:** because goods has to arrive to destination. The delivery 
networks contains warehouses and transport system

# Lesson 1
**Transport Classification**
- *Primary Transport:* BTB Transport
- *Secondary Transport:* BTC Transport
 
**Primary Transport**
- Large volumes of goods
- Full truck transport
- intermodal transport (could be)
- Fixed routes (one starting point - one delivery point)
![[Lessons-1791373315512.webp]]*BTB - Business To Business* 
- transport between factories
- transport between factory and distribution center
Performance pillars in transport are:
![[Lessons-1791373523930.webp]]

|  Type of Transport   | Primary Transport | Secondary Transport |
|:--------------------:|:-----------------:|:-------------------:|
|    Road Transport    |         x         |          x          |
|    Rail Transport    |         x         |                     |
|    Sea Transport     |         x         |                     |
|    Air Transport     |         x         |    x ("drones")     |
| Intermodal Transport |         x         |                     |

**Secondary Transport**
It's the sequence of delivery from warehouse to all the customers.

 ![InkDrawing](<Ink/Drawing/2026.10.8 - 13.13pm.svg>) [Edit Drawing](https://youtu.be/2arL1jh8ihA?type=inkDrawing&width=973.3226318359375&aspectRatio=1.393&viewBoxX=-903.624&viewBoxY=-1552.011&viewBoxW=3922.915&viewBoxH=2817.004)


the network could be:
- only customers
- only suppliers
- mixed situation

### Primary Transport
![[Lessons-1791458840119.webp]]
we need to reach the saturation of the vehicle or the saturation of the container (if we adopt adopt rail, sea, intermodal transport)

**But why we need to do this?**
With primary transport we pay the trip. we could do a direct trip or direct and return trip.

There are two types of containers:


 ![InkDrawing](<Ink/Drawing/2026.10.8 - 13.36pm.svg>) [Edit Drawing](https://youtu.be/2arL1jh8ihA?type=inkDrawing&width=781.1748046875&aspectRatio=1.200&viewBoxX=-657.163&viewBoxY=-959.846&viewBoxW=3879.944&viewBoxH=3234.255)

Primary Transport can be done by:
- own fleet: only road transport
- outsourcing provider: every type of transport

#### Road Transport  by own fleet
Cost classification:
- *Internal cost:* cost that the company has to pay like fuel, drivers ...
- *External cost:* cost that fall on society and on the environment like pollution, $co_2$ emission, road damage, congestions of traffic, noise..  

#### Internal Costs
Internal cost are like:
- driver cost
- fuel cost
- truck cost
- taxes cost
- highway cost (only for distance travelled on highway)
- maintenance cost
- Loading and unloading cost
Truck cost are measurement in units $[€/km]$. 

> [!Example] **EXAMPLE TO EXPLAIN THE FORMULAS (IMPORTANT)**
> **1] Truck cost:** with measurement unit [€/km] 
> **2] Driver Cost:** today it's about 25 €/km
> $$
> c_{driver} = \frac{25}{50} = 0.5 €/km
> $$
> where: 50 is the average value of the speed (more precisely 58[km/h]) 
> 
>  **3] Fuel Cost:**
>  1.6 €/l -> 3€/l for an articulated truck (big van truck)
>  $$
>  c_{fuel} = \frac{1.6}{3} = 0.54 €/km
>  $$
>  truck's cost (investment)
>  - 160.00€ (standard configuration)
>  - n = 5 years
>  - 250 000 km/year -> usually 400 000 km/year
>  $$
>  c_{truck} = \frac{160 000}{5 \cdot 250 000} = 0.13 €/km
>  $$
>  
>  **4] Country taxes insurance:**
>  4 000 €/year
>  $$
>  c_{taxes} = \frac{4 000}{250 000} = 0.02 €/km
>  $$
> ![[Lessons-1791619919361.webp|331x317]]
> 
> **5] Maintenance cost:**
> - record all the costs related to maintenance
> - % of investment cost 
> 	-> maintenance cost per year: 
> 		-> investment cost 4 $\div$ 7 %  is the target value
> 		-> costs like oil, tires, ordinary maintenance
> $$
> \text{remember: truck cost } 160 000 \\
> \text{assume: 5\% is the target value } \\
> \text{therefore: } c_{\text{target value}} = 160 000 * 5\% = 8 000 €/year \\
> c_{maintenance} = \frac{8 000}{250 000} = 0.032 €/km
> $$
> 
> **6] Now we sum all costs:**
> $$
> c_{\text{total cost}}(\text{big truck}) = 0.5_\text{driver cost} + 0.54_\text{fuel cost} + 0.13 + 0.02 + 0.2 * 0.5_\text{50\% of the road riute is in the highway} + 0.032 \simeq 1.4 €/km
> $$
> 
> **7] Now we have to add the time for loading and unloading**
> assume 45min
> the cost is the cos of the driver, therefore:
> $$
> \text{45 min} + \text{45 min} = 1.5 hours/trip \\
> c_\text{loading and unloading} = 1.5 \cdot 25_\text{cost of the driver per hour} = 37.5 €/trip 
> $$
> 
> **7] Final calculations**
> **Case a:**
> ![[Lessons-1791622604496.webp]]
> 
> > The truck at the end of the trip works for another job
> 
> $$
> d_\text{trip} = 500 km \\
> c_\text{total} = 1.4 \cdot 500 + 1.5 \cdot 25 = 737.5 €/km 
> $$
> 
> **Case b**
> ![[Lessons-1791622865373.webp]]
> 
> $$
> d = 500 + 500 km \\
> c_\text{tot} = 1 000 \cdot 1.4 + 1.5 \cdot 25 = 1 437.5 €/trip
> $$
> > [!Important] pay attention to the right distance!!
> >
> > ![[Lessons-1791619937676.webp|499x478]]
>>
>>case 1) trip distance of 500 km:
>>$$ 
>>c [€/km] = \frac{737.5}{500} \simeq 1.48 €/km
> >$$
> >case 2) trip distance of 200 km:
> >$$
> >c [€/km] = \frac{1.4 \cdot 200 + 1.5 \cdot 25}{200} = \frac{317.5}{200} = 1.59 €/km
> >$$
> >case 3) trip distance of 100 km:
> >$$
> >c [€/km] = \frac{1.4 \cdot 100 + 1.5 \cdot 25}{100} = \frac{177.5}{100} = 1.78 €/km
> >$$
> >![[Lessons-1791624073929.webp]]
>
> > [!Important] Temperature of transport cost increase
> > if we have (for example) 100 of a quantity at the temperature of the environment we increase by  
> >  -> $10 \div 15 \%$ for **fresh goods** between $2 \div 4 °C$
> >  -> $40 \div 50 \%$ for **frozen goods** from $-25 °C$ 


# Lesson 2
#### Saturation of the vehicle 
we can reach the saturation of the vehicle (**auto articulated truck**) in two different ways:
1. **weight saturation:** 28 tons
2. **volume saturation:** $\approx$ 80$m^3$

> see the values on the table below on secondary transport

We can "predict" the type of saturation comparing these two intervals:
- if the weight of the goods is $< 400 \frac{kg}{m^3}$ we reach first the **volume saturation**
- otherwise if the weight of the goods is $\geq 400 \frac{kg}{m^3}$ we reach first the **weight saturation**

<font color="#ff0000">To optimize at best we need to reach the saturation</font>

>[!example] 
> Washing machine weight is $\approx 100 \frac{kg}{m^3}$ 
> therefore we reach first the **volume saturation**  
> thus for a trip from Shanghai to Rotterdam with a 40ft container we have $3000 €/trip$

#### Outsourced flees (Primary Transport)

| Start Point | End Point |     Type of Transport     | One Way Trip<br>[€] | Double Trip [€]<br>($\approx 60\% increase$ big truck)<br>($\approx 54\% increase$ truck) |
| :---------: | :-------: | :-----------------------: | :-----------------: | :---------------------------------------------------------------------------------------: |
|   Vicenza   |   Milan   | Auto articulated (5 axes) |         300         |                                            480                                            |
|   Vicenza   |   Turin   | Auto articulated (5 axes) |         450         |                                            720                                            |
|   Vicenza   |   Turin   |      Truck (3 axes)       |         220         |                                            340                                            |

![[Lessons-1791626888185.webp]]

#### Secondary Transport
![[Lessons-1791628411731.webp|705x205]]

![[Lessons-1791628448097.webp|599x520]]

- the warehouse is usually close to the city
- we say customers but could be also supplier
![[Lessons-1791629841849.webp|603]]
> [!Danger] Max number of deliveries for 1 truck
> $$
> N_{max} = \frac{T - T_{a/r}}{t_{stop} + \frac{\bar d}{\bar v}}
> \\ \\
> \text{where:} \\
> T \text{ is the work time} \\
> T_{a/r} \text{ is the time to go to the region of delivery and come back} \\
> T - T_{a/r} \text{ is the available time for delivery} \\
> t_{stop} \text{ is the time stopped to a customer. usually } 5 \div 15 \text{ minutes}\\
> \bar d \text{ is the average distance between customers} \\
> \bar v \text{ is the average velocity} \\
> \frac{t_{stop}}{\frac{\bar d }{\bar v}} \text{ is the time for one delivery} \\
> $$

>[!Note] Work time:
> the regulation of driving time / work time of a driver is usually 8 hours / day

**How do we find $\bar d$ and $D_T$?**
we use the formulas:

Average km between customers
$$
\bar d = 0.9 \frac{\sqrt S}{\sqrt N}
$$

Total km for a round trip:
$$
D_T = 0.9 \sqrt S \cdot \sqrt N
$$
$N_T$ Total Number of deliveries that we have to do in a region
Therefore the number of trucks that we need to deliver to all the customers is:
$$
\frac{N_T}{N_{max}} = N_{trucks}
$$
#### Cross Docking Warehouse
By placing cross docking warehouse we can optimise the delivery time. A cross docking warehouse is a warehouse which doesn't store the goods but it's a place where the goods are removed from a truck (that came from the main warehouse to the cross warehouse) and placed in a new vehicle ready for delivery. 
By doing so we can optimise the work time of the people and use it more efficiently. The cross docking warehouse is a union of different bays where the goods are moved and organized for the delivery.

![[Lessons-1791630687919.webp|473x391]]

> [!danger] Therefore we can modify the formula above as:
> $$
> N_{\text{max deliveries for 1 truck}} = \frac{T - 0 }{t_stop + \frac{\bar d}{\bar v}}
> $$
> Obviously the maximum deliveries for one truck increases since we are already in the region of delivery


| Direct Delivery |                 "Function"                 |     Cross Docking Delivery     |
| :-------------: | :----------------------------------------: | :----------------------------: |
|   $\Uparrow$    | Truck for Delivery<br>Drivers for Delivery |          $\Downarrow$          |
|        0        |             Primary Transport              |           $\Uparrow$           |
|        0        |        Cross Docking Warehouse cost        |           $\Uparrow$           |
|        0        |  Handling cost in cross docking warehouse  |           $\Uparrow$           |
|  **$C_{Dir}$**  |                $\leq \geq$                 | **$C_{\text{Transit Point}}$** |



# Lesson 3 - Exam Exercise

![[Lessons - DWT-1792228978936.webp]]**Van delivery — Milano & Bologna**
1) MILAN

$$N_{\substack{\text{MAX}\\ \text{MI}}}=\frac{\overset{\text{8h}}{T}-T_{A/R}}{\underset{h}{t_{\text{stop}}}+\bar{d}/\bar{v}}=\frac{8-\overbrace{\frac{2\cdot 135\ \text{km}}{90\ \text{km/h}}}^{=3}}{\underbrace{\frac{10}{60}}_{t_{\text{stop in hours}}}+\frac{3}{20}}=\frac{5}{0.3166}=[15.8]=15\ \frac{\text{DELIVERIES}}{\text{VAN}}$$

- $T = 8\,\text{h}$, $t_{\text{stop}}$ misurato in ore ($h$ sotto), $T_{A/R}$ = andata/ritorno

2) \* VAN DELIVERY IN MILAN

$$N_{\text{VAN}}=\frac{N_{\text{DELIV.}}}{N_{\substack{\text{MAX DEL}\\ \text{VAN}}}}=\left\lceil\frac{120}{15}\right\rceil=8\ \text{VANS}$$

3) 

$$N_{\substack{\text{MAX}\\ \text{BO}}}=\frac{T-T_{A/R}}{\underset{h}{t_{\text{stop}}}+\bar{d}/\bar{v}}=\frac{8-\frac{2\cdot 160}{90}}{\frac{10}{60}+\frac{5}{30}}=\frac{4.44}{0.333}=[13{,}34]=13\ \text{DEL.}$$

4) 

$$N_{\text{VAN}}=\frac{N_{\text{DELIV.}}}{N_{\substack{\text{MAX DEL}\\ \text{VAN}}}}=\left\lceil\frac{85}{13}\right\rceil=7\ \text{VAN}$$
5) ANNUAL COST OF DRIVERS FOR DELIVERIES IN MILAN

- 8 VANS → 8 DRIVERS
- DRIVER'S COST → 30 €/HOUR
- COMPANY WORKS 220 DAYS/YEAR

$$C_{\substack{\text{DRIVERS}\\ \text{MILAN}}}=N_{\text{VAN}}\cdot\underbrace{T}_{\substack{\text{HOURS}\\ \text{DAY}}}\cdot\underbrace{D}_{\substack{\text{DAYS}\\ \text{YEAR}}}\cdot\underbrace{C_{\substack{\text{DRIV}\\ \text{COST}}}}_{\substack{\text{€}\\ \text{HOUR}}}=$$

$$=8\cdot 8\cdot 220\cdot 30=$$
$$=422\,400\ \frac{€}{\text{YEAR}}$$
6) ANNUAL COST OF DRIVERS FOR DELIVERY IN BOLOGNA \*VAN

$$C_{\substack{\text{DRIVERS}\\ \text{BOLO}}}=7\cdot 8\cdot 220\cdot 30=369\,600\ \text{€/year}$$

7) ANNUAL COST OF FUEL FOR DELIV. IN MILAN AREA

- FUEL CONSUMPTION: $7\ \text{l}/100\ \text{km}$
- FUEL COST: $1{,}2\ \text{€/litre}$
- schema: deposito ($\text{WH}$) → 15 punti di consegna numerati ($1,\dots,15$); andata e ritorno $135\ \text{km}$ ciascuna

$$d_{\substack{\text{VAN}\\ \text{MIL.}\\ \text{DAY}}}=2\cdot 135+(15-1)\,\bar{d}_{\text{CUSTOMERS}}=2\cdot 135+14\cdot 3=312\ \text{km/DAY}\ \text{(VAN MILAN)}$$
$$D_{\substack{T\\ \text{VAN}\\ \text{YEAR}\\ \text{MILAN}}}=\underbrace{312}_{\substack{\text{km/VAN}\\ \text{DAY}}}\cdot\underbrace{8}_{\substack{\#\ \text{VAN MILAN}\\ \text{REQ.}}}\cdot\underbrace{220}_{\text{DAY/YEAR}}=549\,120\ \text{km/YEAR}$$
$$C_{\substack{\text{FUEL}\\ \text{COST}\\ \text{MILAN}}}=549\,120\cdot\frac{7}{100}\cdot 1{,}2=46\,127\ \text{€/YEAR}$$
![[Lessons - DWT-1792231098565.webp]]

8) ANNUAL COST OF FUEL FOR DEL. IN BOLOGNA AREA

annotazioni a margine:

- $\frac{85}{7}=12{,}14\ \frac{\text{DEL}}{\text{VAN}}$
- km BETWEEN CUSTOM. $\to \bar{d}=5\ \text{km}$
- schema: 85 DELIV. → 1 VAN → 13 DELIV.
- schema: 85 DELIV. → 6 VAN (every van does) → 12 DELIV.

$$d_{\substack{\text{VAN}\\ \text{BOLO}\\ \text{DAY}}}\ (\text{1 VAN})=2\cdot 160+(13-1)\cdot 5=380\ \text{km/DAY}$$
$$d_{\substack{\text{VAN}\\ \text{BOLO}\\ \text{DAY}}}\ (\text{6 VANS})=2\cdot 160+(12-1)\cdot 5=375\ \text{km/DAY}$$
$$D_{\substack{T\\ \text{VANS}\\ \text{YEAR}\\ \text{BOLO}}}=\underbrace{\left[(380\cdot 1)+(375\cdot 6)\right]}_{\text{km/DAY}}\cdot 220=577\,600\ \text{km/YEAR}$$
$$C_{\substack{T\\ \text{FUEL}\\ \text{BOLO}\\ \text{YEAR}}}=579\,600\cdot\frac{7}{100}\cdot 1{,}2=48\,603\ \text{€/YEAR}$$

**Van delivery — cross docking & savings (segue dell'esercizio Milano/Bologna)**

> *(in cima alla pagina, tagliato dal bordo: si legge solo «(YEARS)» — coda di una formula della pagina precedente)*

9) 

$$N_{\text{max deliveries}/\text{van}}=\frac{T-T_{A/R}}{T_\text{stop} + d / v}= \frac{8 - 0 }{10/60 + 5/30} = 8/0.333 = 24.024 = 24$$

![[Lessons - DWT 2026-10-17 11.53.53.excalidraw]]


**schema** (in alto a destra):

- triangolo nero con dentro **VR**
- freccia nera verso destra, etichetta: **1 TRIP/DAY (MASSIVE)**
- linea tratteggiata **verde** parallela, da VR verso Bologna
- grande cerchio con scritta **BOLOGNA** sopra; al centro un punto **rosso** con frecce rosse attorno = cross docking point
- **4 VANS** scritto in rosso dentro un ovale blu

$$\frac{\text{MAX DELIVERIES}}{\text{VAN}}=\frac{\ldots}{t_{\text{stop}}+\frac{\bar{d}}{\bar{v}}}=\frac{8-0}{\frac{10}{60}+\frac{5}{30}}=\left[\frac{8}{0{,}333}\right]=[24{,}024]=24$$

- annotazione in rosso sopra la frazione: «CROSS DOCKING POINT»

$$N_{\text{VANS CROSS}}=\left\lceil\frac{85}{24}\right\rceil=\lceil 3{,}54\rceil=4\ \text{VANS}$$

in basso a margine:

- EVERY DAY → 85 CUSTOMERS
- → 85 · 1 <u>TOTE</u>

![[Lessons - DWT-1792231141853.webp]]

**WEIGHT PRIMARY TRANSPORT**

$$2\cdot 85=170\ \frac{\text{kg}}{\text{DAY}}$$

**VOLUME PRIMARY TRANSPORT**

$$(0{,}4\cdot 0{,}6\cdot 0{,}5)\cdot 85=10{,}2\ \frac{\text{m}^3}{\text{DAY}}$$

![[Lessons - DWT-1792231172388.webp]]- VOLUME CAPACITY **12 m³**
- WEIGHT CAPACITY **1500 kg**
$$\Rightarrow\ \underline{1}\ \text{VAN IS ENOUGH FOR PRIMARY TRANSPORT}$$

2) DRIVERS SAVING

**schema:** $[\text{AS-IS}]$ — *7 DRIVERS* $\longrightarrow$ $[\text{TO-BE}]$ — *4 + 1 DRIVERS*

| AS-IS     | TO-BE         |
| --------- | ------------- |
| 7 drivers | 4 + 1 drivers |

$$S_{\text{DRIVERS}}=\underbrace{(8\cdot 220)}_{\substack{\text{HOURS}\\ \text{YEAR DRIVER}}}\cdot(7-5)\cdot\underbrace{30}_{\text{€/HOUR}}=$$
$$=105.600\ \frac{€}{\text{YEAR}}$$
c) TRAVELLED DISTANCE : SAVING (FUEL)
- TO-BE: 85 → 4 VANS — $21{,}25\ \frac{\text{DELIVERIES}}{\text{VAN}}$ — MAX 24
- 1 VAN → 22 DELIVERIES
- 3 VANS → 21 DELIVERIES

$$d_{\substack{\text{SECONDARY}\\ \text{TRANSPORT}}}=1\,(22-1)\cdot 5+3\,(21-1)\,5=405\ \frac{\text{Km}}{\text{day}}$$
 **DISTANCE PER DAY** (in alto a sinistra), **1 DAY** (sopra «= 160 + 160»)
$$d_{\substack{\text{PRIMARY}\\ \text{TRANSPORT}}}=160+160=320\ \frac{\text{Km}}{\text{day}}$$
$$d_{\substack{T\\ \text{PRI+SEC}}}=320+405=725\ \frac{\text{Km}}{\text{day}}$$
$$\text{TO-BE } D_T=725\cdot 220=159\,500\ \frac{\text{Km}}{\text{YEAR}}$$
$$\text{SAVING FUEL}=\left(\underset{\text{AS-IS}}{578\,600}-\underset{\text{TO-BE}}{159\,500}\right)\frac{7}{100}\cdot 1{,}2=$$

$$=35\,204\ \frac{€}{\text{YEAR}}$$

|                        | AS-IS                             | TO-BE                                       |
| ---------------------- | --------------------------------- | ------------------------------------------- |
|                        | NETWORK DIRECT TRANSPORTS FROM VR | NETWORK WITH CROSS DOCKING POINT AT BOLOGNA |
|                        | SAVINGS                           | SAVINGS                                     |
| DRIVERS                |                                   | 105'600                                     |
| VANS                   |                                   | 20'200                                      |
| FUEL                   |                                   | 35 204                                      |
| HIGHWAY                | $\dots$                           | $\dots$                                     |
| CROSS DOCKING WAREHOUS | $\dots$                           | $\dots$                                     |

# Lesson 4
### Van delivery — highway, warehouse & routing (segue)

| WE HAVE TO EVALUATE | AS-IS [PRESENT SITUATION] | TO-BE [FUTURE SITUATION] |
|---|---|---|
| DRIVERS | | 105 600 €/year |
| VANS | | 20 000 " |
| FUEL | | 35 204 " |
| HIGHWAY | | 24 002 |
| CROSS DOCKING / WAREHOUSE | 80 000 | |
| **TOT (Σ)** | **80 000** | **184 802** |

BOLO AREA :
- WITHOUT CROSS DOCKING POINT: $D_T = 578\ 600$ €/year  *(annotato a destra: 7 VANS)*
- HIGHWAY % → $H_W = 50\%$
- COST HIGHWAY → $C_W = 0{,}1$ €/km $\Big\}$ *(graffa che raccoglie le due righe)*

$$C_{\substack{HW\\ \text{AS-IS}}} = 578\ 600 \cdot 0{,}5_{50\%} \cdot 0{,}1 = 28\ 930\ \text{€/year}$$
- WITH CROSS DOCKING POINT:

$$D_T = \underbrace{(16 + 160)}_{\substack{\uparrow\\ \text{TOT DIST.}}} \cdot \underbrace{220}_{\text{DAYS/YEAR}} \cdot \underbrace{1}_{\text{VAN}} = 70\ 400\ \text{km/year}$$
- 70% DIST ON HIGHWAY WITH CROSS DOCKING
- 0,1 €/km

$$C_{\substack{HW\\ \text{TO-BE}}} = 70\ 400 \cdot 0{,}7 \cdot 0{,}1 = 4928\ \text{€/year}$$
- SAVING HIGHWAY:

$$S_{HW} = 28\ 930 - 4928 = 24\ 002\ \text{€/year}$$

- COST OF WAREHOUSE CROSS DOCKING POINT: **80 000 €/year** [RENTAL]
- SCENARIO WITH CROSS DOCKING PERMITS SAVING OF ABOUT:

$$S_{\text{TO-BE vs AS-IS}} = 184\ 802 - 80\ 000 = 104\ 802 \approx 100\ 000\ \text{€/year}$$
which is about ≈ 10% SAVE

- TODAY WAREHOUSE COST $(6 \div 8)$ €/(m² · month) ⇒ 80 000 €/year ⇒ 50 000 €/year
  *(nota sotto la seconda freccia: LABOR COST 30 000 €/year)*

$$7 \cdot 12 = 84\ \text{€/m}^2 \qquad \frac{50\ 000}{84} \simeq 600\ \text{m}^2$$
**SECONDARY TRANSPORT *(in rosso)* ->(OWN FLEET)** 
$$N_{MAX} \Rightarrow N_{TRUCKS}$$

PLAN THE TRIPS (ROUTES) FOR EVERY TRUCK

2 APPROACHES TO PLAN TRANSPORT EVALUATED DAILY:
**a) CONSOLIDATION METHOD:** [WIDELY USED]
**b) HEURISTIC METHODS:**
1. SAVING METHOD
2. EXTRATILE METHOD

**Moreover:** 
**a)** CONSIDER A SPECIFIC DAY, THERE ARE SOME USUAL DESTINATIONS RELATED TO IMPORTANT CUSTOMERS

![[Lessons - DWT-1792233760086.webp]]

*(disegno — mappa: triangolo deposito con scritta VI sopra; 3 rette tratteggiate arancioni a ventaglio. Nodi in verde: TREVISO, GRISIGNANO, MONSELICE, ROVIGO, VERONA, MONTEBELLO; in nero: PADOVA, VENICE, FERRARA, BOLOGNA, PESCHIERA, MANTOVA)*

STARTING FROM THESE ROUTES (EG PADOVA-PESCH.) WE TRY TO ADD THE OTHER CUSTOMERS OF THE DAY AS LONG AS POSSIBLE

ADVANTAGE OF THESE APPROACH:
- RELATIVELY LITTLE PLANNING WORK
- SAME DRIVER OVER THE TIME ON THE SAME ROUTE
  - ↳ LEARNING EFFECT: DRIVER LEARNS ROUTES, DELIVERY POINT...
- LONGER DISTANCES COULD OCCUR

**b)** CONSIDERS OF HEURISTIC SOFTWARE

*(margine in alto a destra, con frecce: MAPPING SW / GEOGRAPHIC SW ↳ MOST FAMOUS METHOD IS CALLED SAVING AND SW NAME "PTV")*

INPUT DATA: EVERY DAY LOAD
- CUSTOMERS ADDRESSES AND CONSTRAINTS
- DELIVERY WINDOWS
- CONSTRAINTS ARE LIKE NARROW ROADS, SMALL UNLOADING AREA
- CUSTOMERS DELIVERIES [PRODUCTS QUANTITY]
- OWN FLEET DESCRIPTION

### HEURISTIC SAVING [METHOD] *(in arancione)*
![[Lessons - DWT-1792233743317.webp]]

**STEP 0)** IT STARTS WITH DEDICATED ROUND TRIPS FOR EVERY CUSTOMERS
COST FUNCTION *(in arancione)*:

$$F_0 \sim D$$
*(TO SIMPLIFY THE CALCULATIONS)*
$$D_0 = 2\,d[M - i] + 2\,d[M - j]$$

**STEP 1)** FOR EACH COUPLE OF CUSTOMERS CALCULATES THE SAVING RESULTING FROM THEIR AGGREGATION $i, j$
$$D_1 = d[M - i] + d[i - j] + d[M - j]$$
$$\text{SAVING}\quad S_{ij} = D_0 - D_1 = 2\,d[M - i] + 2\,d[M - j] - [d[M - i] + d[i - j] + d[M - j]]$$
$$= d[M - i] - d[i - j] + d[M - j]$$$S_{ij}$ MAX → CONSOLIDATE CUSTOMERS $[i]\,[j]$ INTO SINGLE ROUTE

$$S_{ij} > 0$$

*(disegno: 3 rotte a "petali" dal deposito triangolare — ROUTE 1 sopra, ROUTE 2 a destra, ROUTE 3 a sinistra; punto azzurro isolato con freccia: EXCLUDED CUSTOMER)*

**CONSIDERATION 1 :**

$$\uparrow S(i-j) = d[M - i] + d[M - j] - d[i - j]$$

*(sotto i termini: 9 in verde sotto $d[M - i]$, 4 in verde sotto $d[M - j]$, 6 in rosso sotto $d[i - j]$)*

*(disegno a destra: deposito = triangolo con Π, etichetta VR sopra; punti i con scritta FURTHEST e j sotto)*

**CONSIDERATION 2 :**

$$F_0 = \beta d + (1 - \beta)t$$

$$0 \le \beta \le 1$$

*(annotazione in arancione con freccia alla formula: OBJ FUNCTION THAT CONSIDERS DISTANCE AND TIME)*

$$\beta = 0 \rightarrow \text{FOR SMALL QTY} \rightarrow F_0 = t$$

$$\beta = 1 \xrightarrow{\hspace{1.8cm}} F_0 = d$$

*(la prima riga sta fisicamente sopra la lunga freccia della seconda)*

$$\beta = 0{,}2\ \text{IS THE MOST COMMON VALUE}$$
### EXTRA MILE *(in arancione)* [GOOD BUT NOT AS GOOD AS HEURISTIC]

![[Lessons - DWT-1792233943804.webp]]
**STEP 0)** EXTRA MILE STARTS FROM FURTHEST CUSTOMER AND EVALUATE DISTANCE
$$D_i = 2d[M - i]$$
**STEP 1)** EXTRA DISTANCE RESULTING FROM THIS AGGREGATION OF CUSTOMER "j" WITH CUSTOMER "i":
$$E_1 = d[M - i] + d[M - j] + d[i - j] - 2d[M - i]$$
*(freccia che punta al termine $-2d[M - i]$: WE CALCULATE THE EXTRA MILE THUS REMOVE Π-i DISTANCE)*
$$E_1\ \text{MINIMUM} \qquad E_1 \le E_{\text{TARGET}}$$
*(disegno sotto: 3 rotte a petali dal deposito triangolare)*
## OUTSOURCED FLEET BUT DONE BY OUTSOURCED FLEET [IMPORTANT FOR EXAM] *(in arancione)*
- TRANSPORT RATES → RATES ARE LINKED TO DIFFERENT UNITS OF MEASURMENTS:
  - PALLETS [UNIT LOADS]
  - BOXES [TOTES, PARCELS]
  - kg
  - m³

- EXAMPLE OF RATES:
  - PALLETS
  - STARTING POINT → VICENZA WAREHOUSE
  - GEOG AREA : DELIVERY ZONE

| PROVIDER | FROM → TO | 1 PALLET | 2 | 3 PALL. | 4-5 | 6-10 | >10 | |
|---|---|---|---|---|---|---|---|---|
| PROVIDER 1 | VICENZA → BOLO | 30 | 25 | 20 | 16 | 14 | 12 | €/PALLET |
| PROVIDER 2 | VI → BO | 27 *(1-2 PALL.)* | | 18 *(3-5 PALL.)* | | | 13 *(>5)* | €/PALLET |
### Delivery spectrum — confronto provider

I HAVE TO KNOW MY DELIVERY SPECTRUM FOR A DAY
![[Lessons - DWT-1792233998902.webp]]
**PROVIDER 1:**
$$C_1 = 15 \cdot 30 + \overbrace{(7 \cdot 2)}^{\substack{\text{\# OF}\\ \text{PALLETS}}} \cdot 25 + 3 \cdot 3 \cdot 20 + 9 \cdot 4 \cdot 16 + 5 \cdot 5 \cdot 16 + 2 \cdot 6 \cdot 14 = 2\,124\ \text{€/DAY}$$
**PROVIDER 2:**
$$C_2 = (15 + 7 \cdot 2) \cdot 27 + (9 + 36 + 25)\,18 + 12 \cdot 13 = 2\,199\ \text{€/DAY}$$![[Lessons - DWT-1792234006052.webp]]


# Lesson 5 - Packaging

![[Lessons - DWT-1792784790859.webp]]

## Primary Transport
















