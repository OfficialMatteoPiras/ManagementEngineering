---
course: Smart Operations and Supply Chain Management
professor: Laura Macchion
chapter: "Supplement to Chapter 4 – Forecasting"
book: "Slack, Brandon-Jones, Burgess – Operations and Process Management, Supplement to Ch. 4 (PDF p.175–184)"
slides: "Forecasting_260128_162152.pdf (Macchion – Demand forecasting)"
tags: [SOSCM, summary, forecasting]
---
# Supplement to Chapter 4 – Demand forecasting

> [!abstract] In one breath (for the oral)
> Forecasting predicts **independent demand** (market-driven, uncertain); **dependent demand** is derived from it through the bill of materials. Forecasts support decisions at every horizon (long term: business/investments; medium: aggregate planning; short: items and materials), the choice of **production model** (MTS/ATO/MTO/PTO/ETO, decoupling point) and the fight against the **bullwhip effect**. Principles: forecasts are usually wrong, more accurate for groups, short horizons and large areas, and should always carry an error estimate. Methods are **qualitative** (market research, historical analogy, panel, Delphi, scenarios) or **quantitative** (time series: moving average simple/weighted and exponential smoothing; causal: linear regression; simulation). Choose the method that minimises error, measured with **MFE, MAD, RSFE, tracking signal, σ of errors**.

> [!info] Sources used here
> - 📖 **Book:** Supplement to Chapter 4, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=175|p.175–184]].
> - 🎓 **Macchion's slides** (photos in your notes): most of them are in [[Forecasting_260128_162152.pdf]], linked as "slide N". The final slides on MFE/MAD/RSFE/TS/σ (newer, light-grey style) are **not** in that PDF or in the book, so they get full explanations.

[[Ch04 - Operations scope and structure-claude|← Ch 4]]

---

## 1. What is forecasting?

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=175|p.175]]
> Forecasting in a business context, however, is far more difficult and therefore prone to error. We do not know precisely how many orders we will receive or how many customers will walk through the door tomorrow, next month or next year. But such forecasts are necessary to help managers make decisions about resourcing the organisation for the future.

![[Summary SOSCM - Macchion-1793615276776.webp|600]]

> [!example] 🎓 Slide – "What is forecasting?" · [[Forecasting_260128_162152.pdf#page=4|slide 4]]
> **Definition:** forecasting is a *tool for predicting the future based on past demand information*, through the *observation of correlations between variables*.
> **Chart:** demand for a product from Jan to Jul (blue dots = past sales). The **red dot in August** is the predicted demand, obtained "looking back at the previous months".
> **Independent demand** (slide 3) is driven by the **market**: it is uncertain, and you don't know exactly what or how much will be sold next period. **This is what we forecast.**

![[Summary SOSCM - Macchion-1793615392317.webp|600]]

> [!example] 🎓 Slide – Dependent demand · [[Forecasting_260128_162152.pdf#page=5|slide 5]]
> **Dependent demand** is driven by the demand of *another* product. *"You do not know how many wheels you need, but it is always 5 times the number of cars"* (4 + the spare). The Fiat 500 picture links to **×5 tyres, ×2 headlights, ×2 doors**.
> **So:** you **forecast** independent demand (cars). Dependent demand (components) is **calculated** from the bill of materials (BOM) through MRP. It is not forecast.

### Why demand forecasting matters

![[Summary SOSCM - Macchion-1793615401288.webp|600]]

> [!example] 🎓 Slide – Importance by time horizon · [[Forecasting_260128_162152.pdf#page=6|slide 6]]
> Along a time arrow:
> - **Long term → business forecasting**, used for *investment programmes*.
> - **Medium term → aggregate forecasting**, used for company resources: purchasing, production, human resources.
> - **< 12 months → item / raw material / component forecasting**, used for operational production organisation.

![[Summary SOSCM - Macchion-1793615587505.webp|600]]

> [!example] 🎓 Slide – Forecasting levels linked to planning levels · [[Forecasting_260128_162152.pdf#page=7|slide 7]]
> Three columns that match row by row:
> - **Green (forecasts):** business → aggregate → item → raw material/component forecasting.
> - **Blue (plans that use them):** corporate strategic planning → product and market planning → aggregate production planning → master production scheduling (MPS) → material requirements planning (MRP).
> - **Red (resource checks):** financial planning → resource planning → rough-cut capacity planning → capacity requirements planning.
> **Left arrow:** as you go **up**, the forecast **horizon** gets longer (+) and the **detail** gets lower (−). Going **down**: short horizon, high detail.

![[Summary SOSCM - Macchion-1793615699338.webp|600]]

> [!example] 🎓 Slide – Forecasting feeds supply chain planning · [[Forecasting_260128_162152.pdf#page=8|slide 8]]
> **Top:** the supply chain planning chain *design → purchasing → production → stock of finished products → distribution*. **Gears:** distribution requirements planning, material requirements planning, master production planning, aggregate planning. **Right:** past sales are turned into a demand forecast (the dotted continuation), which drives all the gears.
> **Message:** every planning process in the chain starts from the demand forecast.

![[Summary SOSCM - Macchion-1793615788039.webp|600]]

> [!example] 🎓 Slide – (1) Supporting the production model: the decoupling point · [[Forecasting_260128_162152.pdf#page=9|slide 9]]
> **Columns:** design → purchasing → production → assembly. Each row is a production model, with **blue = driven by forecast** and **green = driven by demand (orders)**. The **DP (decoupling point)** is where the colour switches, i.e. where the customer order enters.
> - **MTS** (make to stock): DP at the very end, so *everything* is driven by forecast.
> - **ATO** (assemble to order): components are forecast; assembly starts on order.
> - **MTO** (make to order): production and assembly on order.
> - **PTO** (purchase to order): from purchasing on.
> - **ETO** (engineer to order): even design is on order, so almost nothing is forecast.
> **Right arrow:** the difficulty of forecasting is **highest for MTS** (+) and **lowest for ETO** (−). The more of the chain runs on forecasts, the more forecast quality matters.

![[Summary SOSCM - Macchion-1793615889685.webp|600]]

> [!example] 🎓 Slide – (3) Eliminating the bullwhip effect · [[Forecasting_260128_162152.pdf#page=10|slide 10]]
> *"The variability of demand is increasing in the upper side of supply chains. Small variations of final demand can create very big variations in the supply chain."* The drawing shows a person flicking a whip: a small movement of the hand becomes a huge wave at the far end. Better forecasts dampen the whip → see [[Ch07 - Supply chain management-claude#7.6 Are supply chain dynamics under control? The bullwhip (Forrester) effect|Ch 7, bullwhip]] and the book: *"Improving forecast accuracy directly reduces the inventory-holding requirements"* ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=283|p.283]]).

---

### What the book adds: know the options and their lead times
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=175|p.175–177]]
- Knowing that demand is rising or falling isn't enough: you need the **rate of change**. A **law firm** must know when to recruit a new partner (hiring takes months). A **plant manager** buys a machine only when needed, but in time to order, build, deliver, install and test it. The same applies to governments planning airports or schools.
- **How far ahead to forecast depends on the options available and their lead times.** **Table 4.3** (a local authority must provide school places for children aged 4–11):

| Option | Lead time | Capacity horizon |
|---|---|---|
| Hire short-term (supply) teachers | Hours | Short-term capacity management |
| Hire or buy temporary classrooms | About 2 weeks | Short–medium |
| Hire or lay off permanent staff | Months | Medium-term |
| Amend school catchment areas | Lengthy consultations | Medium |
| Build new classrooms or schools | 1–5 years | Long-term |

- **Simple extrapolation** (Fig 4.11): tomorrow's attendance = today's; in five years = this year's births. It is error-prone, and some councils built schools that were nearly empty when finished while others overflowed (falling morale and educational standards).
- **Causal variables** (Fig 4.12): **death rate** of children 0–5 (minor in developed countries, major in developing ones; higher in poorer areas); **immigration/emigration** (driven by housing, jobs and prosperity); **amount and type of housing stock** (city-centre tenements have more children per dwelling than suburban semi-detached houses), including planned developments.

## 2. Principles of forecasting

![[Summary SOSCM - Macchion-1793616004646.webp|600]]

> [!example] 🎓 Slide – General problems of forecasts · [[Forecasting_260128_162152.pdf#page=12|slide 12]]
> ✔ Forecasts are **usually wrong**.
> ✔ More accurate for **groups/families** of items (errors cancel out).
> ✔ More accurate for **shorter time periods** (long horizon → large errors).
> ✔ More accurate for **larger areas** (Europe vs Veneto vs a specific city).
> ✔ Every forecast should include an **error estimate**.
> ✔ Use **different approaches**.
> ✔ Use **any other known information** (an advertising campaign just launched, a new product replacing an old one).

![[Summary SOSCM - Macchion-1793616510590.webp|600]]

> [!example] 🎓 Slide – Options and times · [[Forecasting_260128_162152.pdf#page=13|slide 13]] · book equivalent: Table 4.3, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=175|p.175]]
> **Phenomenon:** sales are growing. Options, ordered by the **time needed** to implement them (hours → years): *increase production rate (units/hour)* → *recruiting* → *new line construction* → *new plant construction*.
> **Message:** how far ahead you must forecast depends on the **lead time of the options** you might need. The book uses the same logic with school places (hire short-term teachers in hours … build a new school in years).

![[Summary SOSCM - Macchion-1793616661625.webp|600]]
![[Summary SOSCM - Macchion-1793616764357.webp|600]]

> [!example] 🎓 Slides – Forecasting based on intuition, and its errors · [[Forecasting_260128_162152.pdf#page=14|slides 14–15]] · book: [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=176|p.176–177]]
> - **Short term:** "How many children will be at school tomorrow?" Look at who is in the classroom today.
> - **Long term:** "How many will attend in 5 years?" Use population statistics: **births → future school population**.
> - **But intuition is error-prone:** births are themselves influenced by economic prosperity, developments in residential building, availability and type of accommodation, **immigration**, and more ("…"). A simple link hides a network of causes, which is the reason for causal models.

![[Summary SOSCM - Macchion-1793616813663.webp|600]]

> [!example] 🎓 Slide – Deciding the structure of a forecast model · [[Forecasting_260128_162152.pdf#page=16|slide 16]]
> Five decisions: (1) **data availability**; (2) **time horizon** (year, semester, quarter, month, week, day); (3) **level of aggregation** (world, country, region, client, point of sale / business unit, brand, family, article, SKU); (4) **required accuracy**; (5) **required resources**.

![[Summary SOSCM - Macchion-1793616929966.webp|600]]

> [!example] 🎓 Slide – Levels of aggregation (Coca-Cola) · [[Forecasting_260128_162152.pdf#page=17|slide 17]]
> A tree: *The Coca-Cola Company* → **Product** (Fanta, Coca-Cola, Sprite) → **Variant** (light, classic, diet, cherry) → **Article** (glass, plastic, tin) → **SKU**. Each level serves a different decision:
> - Product → **production capacity**.
> - Variant → **planning and purchasing**.
> - Article → **scheduling/production**.
> - SKU → **distribution**.
> The more detailed the level, the less accurate the forecast.

![[Summary SOSCM - Macchion-1793617116296.webp|600]]

> [!example] 🎓 Slide – Consider the product life cycle · [[Forecasting_260128_162152.pdf#page=19|slide 19]]
> The volume-vs-age curve with introduction → growth → maturity → decline. Where a product sits changes how predictable it is and which method fits: no history at introduction (qualitative); trend in growth; stable in maturity (time series). It links back to [[Ch02 - Operations strategy-claude#The product/service life cycle and performance objectives|Fig 2.7]].

---

## 3. Approaches to forecasting

![[Summary SOSCM - Macchion-1793617260862.webp|600]]

> [!example] 🎓 Slide – Different approaches · [[Forecasting_260128_162152.pdf#page=21|slide 21]]
> 1. **Qualitative** (the slide's first item is mistakenly titled "Quantitative"): relies on *subjective opinions* of one or more experts.
> 2. **Quantitative:** relies on *data and analytical techniques*.
> 3. **Mix of both.**

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=177|p.177]]
> Although no approach or technique will result in an accurate forecast, a combination of qualitative and quantitative approaches can be used to great effect by bringing together expert judgements and predictive models.

### 3.1 Qualitative methods

![[Summary SOSCM - Macchion-1793617416565.webp|600]]

> [!example] 🎓 Slide – Qualitative methods · [[Forecasting_260128_162152.pdf#page=22|slide 22]] (repeated in [[Summary SOSCM - Macchion-1793799499965.webp|this photo]])
> Based on **past experiences**, **views, insight and opinions** and **experts**. Five techniques: **market research** (ask customers about their habits), **historical analogy** (use the history of a similar product), **panel of experts**, **Delphi method**, **scenario planning**.

**Book view of qualitative methods** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=177|p.177]]): forecasting a **football match** by extrapolating recent results is unlikely to be right. The outcome depends on the opposition, form, injuries, location and weather. Qualitative methods collect and appraise judgements, options, best guesses and past performance from "experts". The panel works like a **focus group**: "several brains are better than one", but consensus is hard and the **loudest or highest-status** view may win (the **bandwagon effect**), and even experts can be wrong.

![[Summary SOSCM - Macchion-1793617901731.webp|600]]

> [!example] 🎓 Slide – Panel of experts · [[Forecasting_260128_162152.pdf#page=25|slide 25]] (also [[Summary SOSCM - Macchion-1793799477725.webp|this photo]])
> All participants talk **openly and freely**.
> ✅ Many people at work → more suggestions.
> ❌ Hard to reach full agreement; people with more **power** can impose their view; **errors of judgement** (even experts can be wrong).

**Delphi method** (book [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=178|p.178]], slides 26–27): designed to avoid the face-to-face biases of a panel.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=178|p.178]]
> It employs a questionnaire, emailed or posted to the experts. The replies are analysed and summarised and returned, anonymously, to all the experts. The experts are then asked to reconsider their original response in the light of the replies and arguments put forward by the other experts. This process is repeated several more times to conclude either with a consensus, or at least a narrower range of decisions.

Refinement: weight the experts (experience, past accuracy). Problems: designing the questionnaire, choosing the panel, handling biases.

**Scenario planning** is for even greater uncertainty and long range. The panel builds a *range of future scenarios* and plans for them. Unlike Delphi, it does **not** seek consensus ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=178|p.178]]).

### 3.2 Quantitative methods

![[Summary SOSCM - Macchion-1793799876967.webp|600]]

> [!example] 🎓 Slide – Three families · [[Forecasting_260128_162152.pdf#page=28|slide 28]]
> - **Time series:** predict future demand from **past history and trends**.
> - **Causal relationship:** statistical techniques that link demand to **other variables** (e.g. **linear regression**).
> - **Simulation:** models that include **randomness and non-linear effects**.

![[Summary SOSCM - Macchion-1793799629549.webp|600]]

> [!example] 🎓 Slide – Time series analysis: the idea · [[Forecasting_260128_162152.pdf#page=29|slide 29]] · book [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=178|p.178]]
> The idea is that **the past evolution will continue into the future**: analyse past stages of a phenomenon to predict future ones, examining its **trend** (increase or decrease).
> **Limit:** it considers only historical data and **ignores the causal variables**. Watch out for other variations (e.g. seasons).

![[Summary SOSCM - Macchion-1793799727021.webp|500]] ![[Summary SOSCM - Macchion-1793799887562.webp|500]]

> [!example] 🎓 Slide – The three components of a time series · [[Forecasting_260128_162152.pdf#page=30|slide 30]] · book: Figure 4.13, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=179|p.179]]
> Three small demand-vs-time plots:
> 1. **Trend:** points rising along a straight line.
> 2. **Seasonality:** a repeating cluster (circled) that comes back every cycle.
> 3. **Random variation:** scatter around the line that no cause explains.

![[Summary SOSCM - Macchion-1793799898501.webp|600]]
![[Summary SOSCM - Macchion-1793799956463.webp|600]]
![[Summary SOSCM - Macchion-1793800092442.webp|600]]

> [!example] 🎓 Slides – Decomposing a series (panettoni example) · [[Forecasting_260128_162152.pdf#page=31|slides 31–36]]
> - **Objective:** identify the future sales of a company from past periods. The raw scatter shows growth plus ups and downs.
> - **Step 1, trend:** fit the *linear increase in sales*.
> - **Step 2, seasonality:** remove the trend, and a **cyclical** wave appears (panettoni sell at Christmas).
> - **Step 3, random variations:** remove trend and seasonality, and points still fluctuate around a flat line. These are fluctuations **within the same cycle whose cause cannot be identified**.

**Book definition of the two quantitative families** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=178|p.178]]):
1. **Time series analysis** examines the pattern of past behaviour of a **single phenomenon** over time, accounting for reasons for variation, to forecast its future.
2. **Causal modelling** describes and evaluates the complex **cause–effect relationships** between key variables (like those in Fig 4.12).
In the decomposition, future sales are predicted as lying **within a band** around the projected trend plus seasonality. The **width of the band** depends on the random variation. Random variation has *no known or assignable cause*, which doesn't mean it has no cause.

> [!PDF|yellow] [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=182|p.182]]
> OPERATIONS PRINCIPLE: In demand forecasting, 'seasonality' refers to any repeating pattern of demand – annual, quarterly, monthly, weekly, daily or even hourly.

#### Seasonality in forecasting: the multiplicative seasonal model (book)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=180|p.180–182]]
Causes of seasonality: **climatic** (holidays), **festive** (gifts), **financial** (tax), social, political. Patterns can be **annual, weekly or daily**: a utility has yearly, weekly and daily patterns; a supermarket is low in the morning, peaks at lunchtime and after work, low Mon–Tue, peaks Fri–Sat. **Multiplicative model** = seasonal index × average demand (assuming no trend). Five steps:
1. **Average demand per season**, e.g. March = (80 + 75 + 100)/3 = **85**.
2. **Average demand over all seasons**, e.g. 1,320/12 = **110**.
3. **Seasonal index** = step 1 / step 2, e.g. 85/110 = **0.77**.
4. **Estimate next period's total demand** (with any qualitative or quantitative method).
5. **Divide by the number of seasons and multiply by the index** to get the seasonal forecast.

#### Moving average

![[Summary SOSCM - Macchion-1793800131427.webp|600]]

> [!example] 🎓 Slide – Moving average · [[Forecasting_260128_162152.pdf#page=38|slide 38]]
> Uses **the last periods to predict demand in the next period**. Assumption: the best prediction is a **linear combination of past demand**. Two types: **simple** and **weighted**.

![[Summary SOSCM - Macchion-1793800141910.webp|600]]

> [!example] 🎓 Slide – Simple moving average (SMA) · [[Forecasting_260128_162152.pdf#page=39|slide 39]] · book [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=179|p.179]]
> $$F_t=\frac{\sum_{j=t-n}^{t-1}A_j}{n}$$
> *n* = horizon (how far back you look); *A_j* = actual sales in period j; *F_t* = forecast for period t.
> It **smooths out random variations**, **all n periods have the same weight**, and **only the last n periods count** (older data plays no part). The book adds that *n* is usually 4 to 7.

![[Summary SOSCM - Macchion-1793800160747.webp|600]]
![[Summary SOSCM - Macchion-1793800258332.webp|600]]

> [!example] 🎓 Slides – 4-period SMA, Eurospeed data · [[Forecasting_260128_162152.pdf#page=40|slides 40–41]] · book: Table 4.4, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=180|p.180]]
> Weekly sales from weeks 20–34. The first forecast is possible at week 24 (it needs 4 past weeks). Example:
> $$F_{35}=\frac{A_{34}+A_{33}+A_{32}+A_{31}}{4}=\frac{67.0+68.3+66.7+72.5}{4}=68.6$$
> The book prints 68.8 for the same sum ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=179|p.179]]), but 274.5/4 = 68.6, so the slide is right.
> **The chart:** the red forecast line is **smoother and lags behind** the blue actual line. It reacts late to peaks and dips. That is the price of stability.

#### Weighted moving average

![[Summary SOSCM - Macchion-1793800978067.webp|600]]
![[Summary SOSCM - Macchion-1793800986432.webp|600]]

> [!example] 🎓 Slides – Weighted moving average · [[Forecasting_260128_162152.pdf#page=43|slides 43–44]]
> $$F_t=w_{t-1}A_{t-1}+\dots+w_{t-n}A_{t-n},\qquad \sum w=1$$
> Gives **more importance to recent data** without losing the impact of the past. Choose the weights according to (1) **how important past data is**, and (2) the **presence of seasonality** (weights can also be **zero**, e.g. to pick only the same month of previous years).

#### Exponential smoothing

![[Summary SOSCM - Macchion-1793800480421.webp|600]]

> [!example] 🎓 Slide – Exponential smoothing · [[Forecasting_260128_162152.pdf#page=45|slide 45]] · book [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=180|p.180–181]]
> $$F_t=\alpha A_{t-1}+(1-\alpha)F_{t-1}$$
> The future depends mostly on **the most recent observation** and **the error of the latest forecast**. α = smoothing constant. The first term uses the **actual sales** of the previous period; the second uses the **forecast** of the previous period.
> 💡 *Intuition:* rewrite it as $F_t = F_{t-1} + \alpha(A_{t-1}-F_{t-1})$: **new forecast = old forecast + α × last error.** α is how much you "correct yourself".

**Why the book prefers exponential smoothing to the moving average** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=180|p.180]]): the MA has two drawbacks: (1) it gives **equal weight** to the n periods (fixable with weights); (2) more importantly, it **ignores all data older than n periods**. Exponential smoothing fixes both and is **easier to calculate**. Since $F_{t-1}$ already contains the previous data, **all past data have a (diminishing) effect**. The weights fall exponentially, hence the name. α governs the balance between **responsiveness** and **stability**: the closer to 0, the more forecasts are dampened by previous forecasts.

![[Summary SOSCM - Macchion-1793800620321.webp|600]]

> [!example] 🎓 Slide – Choosing α · [[Forecasting_260128_162152.pdf#page=46|slide 46]]
> α is the **weight of the latest information**, i.e. how much the forecast reacts to the gap between A and F. **0 < α < 1**:
> - α close to **0** → little reaction, so the forecast is **stable** but not sensitive to change.
> - α close to **1** → strong reaction, so the forecast is **reactive** (and also chases noise).

![[Summary SOSCM - Macchion-1793800737545.webp|600]]

> [!example] 🎓 Slide – Exponential smoothing, α = 0.2 · [[Forecasting_260128_162152.pdf#page=48|slide 48]] · book: Table 4.5, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=181|p.181]]
> Same Eurospeed data, with a starting forecast of 60.00 at week 20.
> $$F_{35}=0.2\cdot 67.0+0.8\cdot 68.30=68.04$$

![[Summary SOSCM - Macchion-1793800758426.webp|600]]

> [!example] 🎓 Slide – Comparing α = 0.2/0.4/0.6 and the moving average · [[Forecasting_260128_162152.pdf#page=49|slide 49]] · book: Fig 4.14, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=181|p.181]]
> - **Yellow (α = 0.2):** the slowest, lowest line; it lags most.
> - **α = 0.4, 0.6 (greens):** progressively closer to the actual (blue) peaks.
> - **Red:** the moving average.
> **Takeaway:** higher α tracks changes faster. (The slide title "previsioni con modelli causali" is a leftover; the chart compares time-series methods.)

![[Summary SOSCM - Macchion-1793800915756.webp|600]]

> [!example] 🎓 Slide – Response to impulse, step and ramp · [[Forecasting_260128_162152.pdf#page=47|slide 47]]
> How exponential smoothing with α = 0.5 / 0.3 / 0.1 reacts to three demand shapes (black = actual):
> - **Impulse** (one-off spike): high α jumps up and then decays; low α barely moves. Good: low α **ignores one-off noise**.
> - **Step** (permanent jump): every α eventually reaches the new level, but low α takes much longer.
> - **Ramp** (steady growth): all forecasts **lag** below the line. The gap is constant, and bigger for low α. Simple exponential smoothing always lags a trend.

#### Causal models: linear regression

![[Summary SOSCM - Macchion-1793801120664.webp|600]]
![[Summary SOSCM - Macchion-1793801183468.webp|600]]

> [!example] 🎓 Slides – Linear regression and least squares · [[Forecasting_260128_162152.pdf#page=50|slides 50–51]] · book: Fig 4.15, [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=183|p.183]]
> $$Y=a+bX$$
> *Y* = dependent variable (demand); *X* = independent variable (the cause); *a* = intercept; *b* = slope. You fit a straight line to the data, explaining changes in *y* through changes in *x*.
> **Least squares:** choose the line that minimises the distances (errors) $\varepsilon_i=y_i-Y_i$ between each **observed** point $y_i$ and the line's **predicted** value $Y_i$ (strictly, it minimises the sum of the squared errors). Example: **ice-cream sales vs temperature**. The book's version (Fig 4.15) plots demand (thousands of cases) against the previous week's average temperature.

**Book example of regression** ([[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=182|p.182–183]]): an **ice-cream company** finds that factory demand depends mainly on the **average temperature of the previous week** and plots the regression line (Fig 4.15). It is reliable only if other market conditions stay stable; otherwise more variables must enter the model, which gets more complex. Complex causal networks (many variables, feedback) are beyond the book's scope.

### How well do forecasting models perform? (book)
[[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=183|p.183]]
- **Hogarth & Makridakis (1981):** the record of forecasters using judgement *and* sophisticated mathematics is **"not good"**. But **short-term** (≤ 3 months) phenomena have **inertia**, so simple time-series methods are accurate and can **outperform** elaborate econometric ones.
- **Armstrong & Grohman (1972):** for **long-range** forecasts, **econometric (objective causal) methods** beat expert opinion and time series, and their superiority **grows with the horizon**.
- → In practice: **time series for the short term, causal models for the long term** (consistent with Macchion's "which family when" slide).

---

## 4. Selecting the right approach

![[Summary SOSCM - Macchion-1793801252279.webp|600]]

> [!example] 🎓 Slide – Six-step procedure · [[Forecasting_260128_162152.pdf#page=52|slide 52]]
> **Goal: minimise the sum of forecast errors.**
> 1. Analyse past data (trend, seasonality).
> 2. Choose candidate forecasting techniques.
> 3. Set the parameters (weights, α).
> 4. Simulate the forecast on past data.
> 5. Analyse the errors.
> Steps 3–5 are **iterated** until the errors are acceptable. 6. Final demand forecast.

![[Summary SOSCM - Macchion-1793801510197.webp|600]]

> [!example] 🎓 Slide – Which family when (newer slide, not in the PDF)
> Three cards:
> - **Qualitative** (judgement: Delphi, market research, expert opinion). **Best when:** new products, **no history**.
> - **Time series** (moving average, exponential smoothing, trend and seasonality models). **Best when:** **stable demand**, reliable history, **short term**.
> - **Causal** (regression, econometric models with explanatory variables). **Best when:** demand **depends on** price, promotions or the economy.

### Worked exercise: SMA(3) vs exponential smoothing (α = 0.1)

![[Summary SOSCM - Macchion-1793801549906.webp|600]]

> [!example] 🎓 Slides – Exercise · [[Forecasting_260128_162152.pdf#page=53|slides 53–57]]
> Actual demand: weeks 6–12 = 11, 10, 15, 12, 16, 18, 15. ES starting forecast F₉ = 3. Forecast weeks 10–12 with both methods.

![[Summary SOSCM - Macchion-1793801561259.webp|600]]
![[Summary SOSCM - Macchion-1793801569920.webp|600]]
![[Summary SOSCM - Macchion-1793801579168.webp|600]]

| Week | A | SMA 3 | ES α=0.1 | \|A−F\| SMA | \|A−F\| ES |
|---|---|---|---|---|---|
| 10 | 16 | (12+15+10)/3 = **12.33** | 0.1·12 + 0.9·3 = **3.90** | 3.67 | 12.10 |
| 11 | 18 | (16+12+15)/3 = **14.33** | 0.1·16 + 0.9·3.9 = **5.11** | 3.67 | 12.89 |
| 12 | 15 | (18+16+12)/3 = **15.33** | 0.1·18 + 0.9·5.11 = **6.40** | 0.33 | 8.60 |
| **Σ** | | | | **7.67** | **33.59** |

Your note: *"for 10 we need to do 16 − 12.33 = 3.67 and 16 − 3.9 = 12.10"*. ES performs badly here only because it **starts from F₉ = 3**, far from real demand, and α = 0.1 corrects very slowly (see the "step" response above).

![[Summary SOSCM - Macchion-1793801589758.webp|700]]

> [!example] 🎓 Slide – Error indicators for the exercise · [[Forecasting_260128_162152.pdf#page=57|slide 57]]
> SMA 3: **MFE = (3.67 + 3.67 − 0.33)/3 = 2.34**, **MAD = 7.67/3 = 2.56**, **TS = 7.01/2.56 = 2.74**. ES: MAD = 33.59/3 = **11.20**, TS ≈ 3.0. **Conclusion on the slide: "Use in this case SMA 3"** (lower MAD, TS closer to 0).
> ⚠️ For ES all errors are positive, so its MFE should equal its MAD (11.20). The 11.31 on the slide comes from an "8.93" written in place of 8.60.

---

## 5. Measuring forecast error (newer slides, not in the PDF)

![[Summary SOSCM - Macchion-1793802437298.webp|650]]
![[Summary SOSCM - Macchion-1793802455834.webp|500]]

> [!example] 🎓 Slide – MFE and MAD
> **Period error:** $E_t=A_t-F_t$ (actual minus forecast).
> - **MFE – Mean Forecast Error** $=\frac{\sum E_t}{n}$ measures **bias**. **Positive → under-forecasting** (actual > forecast); **negative → over-forecasting**. Opposite errors cancel out. Ideal ≈ 0; MFE ≠ 0 means the forecast is systematically biased.
> - **MAD – Mean Absolute Deviation** $=\frac{\sum |E_t|}{n}$ measures the **average size** of the error, ignoring sign. It does **not** show direction. **Lower = more precise.**

![[Summary SOSCM - Macchion-1793802473445.webp|650]]

> [!example] 🎓 Slide – Reading MFE and MAD together (target diagrams)
> Three dartboards (red dots = forecasts, centre = actual demand):
> 1. **MFE ≈ 0, low MAD:** dots tight in the centre. **Accurate and unbiased.**
> 2. **MFE ≈ 0, high MAD:** dots scattered all around the board. Large errors cancel out, so MFE **hides** them. **Unbiased but imprecise.**
> 3. **High |MFE|, high MAD:** dots clustered off-centre on one side. Large errors mostly of the same sign. **Biased and inaccurate.**
> Rule at the bottom: **always |MFE| ≤ MAD**, so a high bias with a low MAD cannot occur.

![[Summary SOSCM - Macchion-1793802657470.webp|650]]

> [!example] 🎓 Slide – RSFE and tracking signal
> - **RSFE – Running Sum of Forecast Errors** $=\sum E_t$ (cumulative, signed). A steady drift reveals **systematic bias**.
> - **TS – Tracking Signal** $=\frac{RSFE}{MAD}$: the cumulative deviation expressed **in MADs**. It shows whether the model stays **in control**.
> - **Rule of thumb:** keep TS within **±4** (±2 to 3 for critical items). Outside the limits, review the method or its parameters.

![[Summary SOSCM - Macchion-1793802627081.webp|650]]

> [!example] 🎓 Slide – Direction of the bias
> Two scatter charts over six months (orange = actual, blue = forecast):
> - **Positive TS:** actual is *above* forecast every month, i.e. **under-forecasting**. RSFE = +53, MAD = 8.8, **TS = +6.0** (out of control).
> - **Negative TS:** actual is *below* forecast, i.e. **over-forecasting**. RSFE = −53, MAD = 8.8, **TS = −6.0**.

![[Summary SOSCM - Macchion-1793802765285.webp|650]]

> [!example] 🎓 Slide – RSFE builds up
> Same data. Monthly errors are +8, +10, +12, +10, +8, +5, so the cumulative line climbs 8 → 18 → 30 → 40 → 48 → **53**. RSFE₆ = +53 units, which means **under-forecasting overall**. A line that keeps climbing (instead of oscillating around 0) is the visual sign of bias.

![[Summary SOSCM - Macchion-1793802682541.webp|650]]

> [!example] 🎓 Slide – Worked example (4 periods)
> | t | A | F | E | \|E\| | RSFE |
> |---|---|---|---|---|---|
> | 1 | 100 | 95 | +5 | 5 | +5 |
> | 2 | 110 | 115 | −5 | 5 | 0 |
> | 3 | 105 | 110 | −5 | 5 | −5 |
> | 4 | 120 | 110 | +10 | 10 | +5 |
> **MFE = 5/4 = 1.25** (slight under-forecast) · **MAD = 25/4 = 6.25** · **TS = 5/6.25 = 0.8**, well within ±4, so no significant bias.

![[Summary SOSCM - Macchion-1793802879067.webp|650]]

> [!example] 🎓 Slide – Standard deviation of forecast errors
> Errors 8, 10, 12, 10, 8, 5 have mean $\bar e = +8.8$ (the orange reference line). The spread around that mean is
> $$\sigma_e=\sqrt{\frac{\sum(e_i-\bar e)^2}{n}}=\sqrt{28.83/6}=2.2\text{ units}$$
> (population formula: the six periods are the whole population). In the right chart the band between the orange lines is ±σ around the mean. **Meaning:** MFE/MAD tell you the *bias* and *size*; σ tells you how **consistent** the errors are. A low σ with a high mean error means a stable bias that is easy to correct.

---

## 📚 Worked examples (Supplement) – summary for the oral

> [!example] Worked example – **Eurospeed parcels** (moving average and exponential smoothing) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=179|p.179–181]]
> A Europe-wide parcel company measures weekly demand in **number of parcels** (whatever their size).
> - **4-week MA:** $F_t=\tfrac14(A_{t-4}+A_{t-3}+A_{t-2}+A_{t-1})$, so $F_{35}=(72.5+66.7+68.3+67.0)/4=68.6$ (the book prints 68.8).
> - **ES with α = 0.2:** $F_{35}=0.2\cdot67.0+0.8\cdot68.30=68.04$ (Table 4.5, which starts from F₂₀ = 60.00).
> - **Fig 4.14** compares MA(4), ES 0.2 and ES 0.3: higher α follows changes more closely.

> [!example] Worked example – **Phoenix Consulting** (multiplicative seasonal model) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=182|p.182]]
> Supply-chain strategy consulting. Expected **annual demand for 2018 = 7,500 hours**. Table 4.6 uses monthly hours sold in 2015–2017.
>
> | Month | 2015 | 2016 | 2017 | 3-yr avg | Index (avg / 570.14) |
> |---|---|---|---|---|---|
> | Jun | 600 | 625 | 650 | 625.00 | **1.10** |
> | Jul | 700 | 750 | 800 | 750.00 | **1.32** |
> | Aug | 450 | 400 | 500 | 450.00 | **0.79** |
>
> 570.14 = average monthly demand over all months and years.
> **Forecasts:** 7,500/12 = 625 per month on average, so **June** = 625 × 1.10 = **687.50**; **July** = 625 × 1.32 = **825.00**; **August** = 625 × 0.79 = **493.75** hours.
> **Use it to explain** that a seasonal index above 1 means a month above average.

> [!example] Worked example – **ice-cream demand vs temperature** (regression) · [[Operations-and-Process-Management-–-Gestión-por-Procesos.pdf#page=182|p.182–183]] → see the regression section above.

> [!example] Macchion's class exercise – **SMA(3) vs ES(0.1)** with MFE/MAD/TS → see section 4 above (choose SMA 3).

---

> [!question] 🎤 Likely oral questions
> - *Independent vs dependent demand?* Market-driven and forecast vs BOM-driven and calculated (the 5 wheels).
> - *Why is forecasting important?* Planning at every horizon (slides 6–8), the production model and decoupling point (slide 9), the bullwhip effect (slide 10).
> - *Principles of forecasting.* Slide 12.
> - *Qualitative methods; Delphi vs panel vs scenario planning.*
> - *Time series components; SMA vs weighted MA vs exponential smoothing; effect of α.*
> - *How do you choose the method?* Minimise the errors: MFE (bias), MAD (size), TS (control, ±4), σ.
> - Be ready to **compute** an SMA, an ES forecast and MFE/MAD/TS by hand, as in the exercise above.

---

## 🗺️ Concept map (Supplement)

![[Ch04S concept map-claude.png]]

> [!tip] How to read the map
> **Dark blue box** = the chapter; **coloured blocks** = its sections, each with its key concepts. **Red arrows** = links between concepts (with the relation written on them); **orange dashed boxes** = links to other chapters. **Thumbnails** (blue dashed line) = the book figure or slide that explains that concept, with its page.
>
> 🎤 **Oral storyline:** Why forecast (planning levels, decoupling point, bullwhip) → principles (forecasts are always wrong) → the three families: qualitative, time series, causal → time-series components and the methods (SMA, WMA, ES) → choose the approach → measure error (MFE = bias, MAD = accuracy, tracking signal).
