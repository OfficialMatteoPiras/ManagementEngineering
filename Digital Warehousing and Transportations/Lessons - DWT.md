
> [!Important] https://stem.elearning.unipd.it/course/view.php?id=16780

# Lesson 0

**Why DW&T:** because goods has to arrive to destination. The delivery 
networks contains warehouses and tansport system

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

6) ANNUAL COST OF DRIVERS FOR DELIVERY IN BOLOGNA \*VAN

$$C_{\substack{\text{DRIVERS}\\ \text{BOLO}}}=7\cdot 8\cdot 220\cdot 30=369\,600\ \text{€/year}$$

7) ANNUAL COST OF FUEL FOR DELIV. IN MILAN AREA

- FUEL CONSUMPTION: $7\ \text{l}/100\ \text{km}$
- FUEL COST: $1{,}2\ \text{€/litre}$
- schema: deposito ($\text{WH}$) → 15 punti di consegna numerati ($1,\dots,15$); andata e ritorno $135\ \text{km}$ ciascuna

$$d_{\substack{\text{VAN}\\ \text{MIL.}\\ \text{DAY}}}=2\cdot 135+(15-1)\,\bar{d}_{\text{CUSTOMERS}}=2\cdot 135+14\cdot 3=312\ \text{km/DAY}\ \text{(VAN MILAN)}$$

$$D_{\substack{T\\ \text{VAN}\\ \text{YEAR}\\ \text{MILAN}}}=\underbrace{312}_{\substack{\text{km/VAN}\\ \text{DAY}}}\cdot\underbrace{8}_{\substack{\#\ \text{VAN MILAN}\\ \text{REQ.}}}\cdot\underbrace{220}_{\text{DAY/YEAR}}=549\,120\ \text{km/YEAR}$$

$$C_{\substack{\text{FUEL}\\ \text{COST}\\ \text{MILAN}}}=549\,120\cdot\frac{7}{100}\cdot 1{,}2=46\,127\ \text{€/YEAR}$$

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

$$N_{\text{max del}}=\frac{T-T_{A/R}}{\ldots}=$$

- freccia rossa da $T_{A/R}$ verso uno **0** scritto in rosso: col cross docking la van parte dal cross docking point → $T_{A/R}=0$
- sotto la linea di frazione: due trattini verdi (evidenziazione)

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

**disegno:** scatola (parallelepipedo 3D) con dentro **2 kg** — quote: **400 mm**, **500 mm**, **600 mm**

**WEIGHT PRIMARY TRANSPORT**

$$2\cdot 85=170\ \frac{\text{kg}}{\text{DAY}}$$

**VOLUME PRIMARY TRANSPORT**

$$(0{,}4\cdot 0{,}6\cdot 0{,}5)\cdot 85=10{,}2\ \frac{\text{m}^3}{\text{DAY}}$$

**disegno:** furgone in profilо, due linee che portano a:

- VOLUME CAPACITY **12 m³**
- WEIGHT CAPACITY **1500 kg**

$$\Rightarrow\ \underline{1}\ \text{VAN IS ENOUGH FOR PRIMARY TRANSPORT}$$

*(scritta tagliata sopra il titolo: «TIME …» — coda del punto precedente, es. «1) TIME SAVING»)*

2) DRIVERS SAVING

**schema:** $[\text{AS-IS}]$ — *7 DRIVERS* $\longrightarrow$ $[\text{TO-BE}]$ — *4 + 1 DRIVERS*

$$S_{\text{DRIVERS}}=\underbrace{(8\cdot 220)}_{\substack{\text{HOURS}\\ \text{YEAR DRIVER}}}\cdot(7-5)\cdot\underbrace{30}_{\text{€/HOUR}}=$$

$$=105.600\ \frac{€}{\text{YEAR}}$$

*(risultato cerchiato in verde)*



c) TRAVELLED DISTANCE : SAVING (FUEL)

*(«SAVING (FUEL)» cerchiato in verde)*

- TO-BE: 85 → 4 VANS — $21{,}25\ \frac{\text{DELIVERIES}}{\text{VAN}}$ — MAX 24
- 1 VAN → 22 DELIVERIES
- 3 VANS → 21 DELIVERIES

$$d_{\substack{\text{SECONDARY}\\ \text{TRANSPORT}}}=1\,(22-1)\cdot 5+3\,(21-1)\,5=405\ \frac{\text{Km}}{\text{day}}$$

annotazioni a margine: **DISTANCE PER DAY** (in alto a sinistra), **1 DAY** (sopra «= 160 + 160»)

$$d_{\substack{\text{PRIMARY}\\ \text{TRANSPORT}}}=160+160=320\ \frac{\text{Km}}{\text{day}}$$

$$d_{\substack{T\\ \text{PRI+SEC}}}=320+405=725\ \frac{\text{Km}}{\text{day}}$$

$$\text{TO-BE } D_T=725\cdot 220=159\,500\ \frac{\text{Km}}{\text{YEAR}}$$

*(159 500 sottolineato in rosso)*

in basso: riquadri **[AS-IS]** **[TO-BE]** (inizio dello schema riepilogo)

*(titolo del punto tagliato dal bordo superiore, illeggibile)*

$$\text{SAVING FUEL}=\left(\underset{\text{AS-IS}}{578\,600}-\underset{\text{TO-BE}}{159\,500}\right)\frac{7}{100}\cdot 1{,}2=$$

$$=35\,204\ \frac{€}{\text{YEAR}}$$

*(risultato cerchiato in verde e sottolineato in rosso)*

**tabella riepilogo:**

|              | AS-IS                                 | TO-BE                                        |
| ------------ | ------------------------------------- | -------------------------------------------- |
|              | NETWORK DIRECT TRANSPORTS FROM VR      | NETWORK WITH CROSS DOCKING POINT AT BOLOGNA  |
|              | SAVINGS                               | SAVINGS                                      |
| DRIVERS      |                                       | 105'600                                      |
| VANS         |                                       | 20'200                                       |
| FUEL         |                                       | 35 204                                       |
| HIGHWAY      | · · ·                                 | ~ ~ ~                                        |
| CROSS DOCKING WAREHOUS | · · ·                     | ~ ~ ~                                        |

*(i tre valori della colonna TO-BE sono scritti in verde; «WAREHOUS» è senza la E finale sul foglio)*

> **⚠ Note di verifica (non sono sul foglio):**
> - In questo blocco i conti tornano tutti: $8/(10/60+5/30)=24{,}02$ → 24; $85/24=3{,}54$ → 4 vans; $22+3\cdot 21=85$ ✓; $(578\,600-159\,500)\cdot\frac{7}{100}\cdot 1{,}2=35\,204{,}4$ → sul foglio 35 204; $8\cdot 220\cdot 2\cdot 30=105\,600$ ✓.
> - Qui come AS-IS è usato il valore **corretto** $578\,600$ km/anno (nella prima parte il foglio aveva scritto 577 600, con svista).
> - «g)» è stato letto come lettera g minuscola in entrambe le verifiche OCR (occhiello + coda curva a sinistra); se nei tuoi appunti è «9)» correggi pure.
> - Volume: $10{,}2 \le 12\ \text{m}^3$ e peso: $170 \le 1500\ \text{kg}$ → conferma che 1 van basta per il primary transport.























