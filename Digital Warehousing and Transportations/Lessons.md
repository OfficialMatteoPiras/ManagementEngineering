
> [!Important] https://stem.elearning.unipd.it/course/view.php?id=16780

# Lesson 1 

**Why DW&T:** because goods has to arrive to destination. The delivery 
networks contains warehouses and tansport system

# Lesson 2
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


# Lesson 3
#### Saturation of the vehicle 
we can reach the saturation of the vehicle in two different ways (considering a *20ft container*):
1. **weight saturation:** 28 tons
2. **volume saturation:** $\approx$ 80$m^3$
We can "predict" the type of saturation comparing these two intervals:
- if the weight of the goods is $< 400 \frac{kg}{m^3}$ we reach first the **volume saturation**
- otherwise if the weight of the goods is $\geq 400 \frac{kg}{m^3}$ we reach first the **weight saturation**

>[!example] 
> Washing machine weight is $\approx 100 \frac{kg}{m^3}$ 
> therefore we reach first the **volume saturation**  
> thus for a trip from Shanghai to Rotterdam 













