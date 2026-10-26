---
title: "Modeling, Analysis, and Design of Shuttle-Based Storage Systems"
aliases:
  - "Shuttle-Based Storage Systems"
tags:
  - industrial-engineering
  - warehouse-automation
  - mathematical-modeling
  - operations-research
  - storage-systems
source: "Modeling, Analysis, and Design Insights for Shuttle-Based Storage compact systems.pdf"
document_type: "Scientific Technical Analysis"
---

# Modeling, Analysis, and Design of Shuttle-Based Storage Systems

## 1. Introduction and Research Objectives

The design and optimization of automated material handling systems represent a critical frontier in modern supply chain engineering. In contemporary distribution environments, warehouses are subjected to continuously changing product assortments, intense fluctuations in demand volume, and stringent customer response times that frequently contract to a matter of hours. Traditional automated unit-load storage systems, such as crane-based Automated Storage and Retrieval Systems (AS/RS), often fail to deliver the requisite flexibility in such dynamic contexts. They represent highly capital-intensive investments that are rigidly constrained in their throughput scalability. 

To address these systemic limitations, shuttle-based compact storage systems utilizing vertical lifts have emerged as a disruptive technological alternative. These systems aim to decouple the vertical and horizontal transport mechanisms, effectively pairing the volumetric space efficiency of multideep compact storage with the operational flexibility of Autonomous Vehicle Storage and Retrieval Systems (AVS/RS). By adding or removing shuttles, facility managers can scale throughput capacity independently of the physical storage volume. 

The primary research objective of the source literature is to develop accurate, computationally efficient analytical models capable of evaluating the performance of these complex systems. Specifically, the research addresses two foundational engineering questions: First, how can single-tier operations be modeled to accurately determine the optimal depth-to-width ratio of the physical storage rack, and does this optimal geometry shift depending on the specific type of shuttle technology deployed? Second, how can these models be robustly extended to multitier configurations to determine the optimal number of vertical storage tiers and to evaluate the economic trade-offs between different shuttle architectures? The ensuing analysis provides a rigorous theoretical framework grounded in queuing theory to answer these engineering challenges.

## 2. Scientific Background and Engineering Problem

In the domain of warehouse automation, compact storage systems are traditionally favored for inventory profiles characterized by relatively low unit-load demand but requiring high space-utilization efficiency. Examples include refrigerated environments where cooling costs necessitate dense footprints, or bulk storage buffers feeding forward picking areas. These traditional systems operate by minimizing or eliminating standard travel aisles. 

Historically, the literature has categorized compact storage systems into three primary architectures based on their movement mechanisms across the $x$ (depth), $y$ (cross-aisle), and $z$ (vertical) axes. Conveyor-based compact systems utilize a crane for simultaneous $y$ and $z$ movements while relying on gravity or powered conveyors for $x$-direction depth movements. Shuttle-based compact systems with cranes substitute the conveyors with tethered satellites (shuttles) for the $x$-movements but retain the crane for $y$ and $z$ positioning. Finally, live-cube compact storage systems provide extreme density by allowing each load to move independently on dedicated shuttles across the $x$ and $y$ axes, utilizing discrete elevators for $z$-axis transfers.

The engineering problem at the core of this analysis involves a novel permutation: shuttle-based compact storage systems using lifts instead of cranes. Because horizontal travel (via shuttles) is completely decoupled from vertical travel (via lifts), the system's mathematical behavior diverges fundamentally from crane-based systems. The physical resources—specifically the finite fleet of shuttles—act as strict operational bottlenecks. When transaction requests arrive stochastically from the external warehouse environment, they must be paired with available physical shuttles. If all shuttles are busy, incoming requests form a queue; conversely, if the system is idle, shuttles wait in a pooled buffer for new work. Standard open queuing networks fail to model the finite constraint of the shuttle fleet, and standard closed queuing networks fail to model the stochastic arrival of external orders. Therefore, the system necessitates the development of a Semi-Open Queuing Network (SOQN) to accurately capture the pairing dynamics and estimate the true transaction throughput times.

## 3. System Architecture and Operating Principles

The physical architecture of a shuttle-based compact storage system is structured around a three-dimensional matrix of storage locations. The system is divided vertically into distinct tiers. Each tier contains a set of multideep storage lanes oriented along the $x$-axis. These lanes intersect a central cross-aisle oriented along the $y$-axis. Products are stored in the multideep lanes and are managed strictly according to a Last-In-First-Out (LIFO) operational logic, meaning that a shuttle can only access the outermost pallet in any given lane.

Horizontal movements within the tiers are executed by shuttles, while vertical movements across the tiers are executed by lifts. The engineering models distinguish between two fundamental classifications of shuttle technology, which drastically alter the kinematic behavior of the system:

1.  **Specialized Shuttles:** These vehicles are mechanically constrained to one-dimensional travel. They can drive deep into the storage lanes (the $x$-direction) to deposit or retrieve pallets. However, to navigate the central cross-aisle (the $y$-direction), they must drive onto a dedicated transfer car. This transfer car operates as a mobile platform, carrying the specialized shuttle to the target lane. This architecture introduces a single-server bottleneck at each tier, as all cross-aisle movements must queue for the single transfer car.
2.  **Generic Shuttles:** These advanced vehicles are equipped with omnidirectional wheels. They can navigate both the storage lanes and the central cross-aisle autonomously. By eliminating the need for a transfer car, generic shuttles remove a significant queueing delay and decrease total S/R travel distance. However, they incur a substantial capital cost premium, typically costing twice as much as specialized shuttles due to their complex steering and drive mechanisms.

Vertical transportation is facilitated by elevators located at the Input/Output (I/O) points of the cross-aisles. Elevators are classified mechanically as either continuous or discrete. A continuous elevator operates similarly to a vertical conveyor; it possesses multiple load-bearing platforms and can process multiple unit loads simultaneously without interference. A discrete elevator, by contrast, possesses a single load platform. It processes transactions sequentially and is modeled as a strictly constrained single-server queue subject to Point-of-Service-Completion (POSC) dwell policies.

## 4. Modeling Assumptions, Terminology, and Notation

To construct a tractable mathematical model of the physical system, several standard operational assumptions are formalized. The arrival of storage and retrieval requests from the external warehouse is modeled as a Poisson process. The assignment of unit loads to specific storage lanes follows a random storage policy, meaning every eligible storage lane has an equal probability of being selected. The scheduling of waiting transactions, idle shuttles, the transfer car, and the discrete elevator all strictly follow a First-Come-First-Served (FCFS) queuing discipline. 

The primary notation used throughout the mathematical modeling is summarized in the table below.

| Symbol | Definition and Engineering Context | Unit |
| :--- | :--- | :--- |
| $\lambda_s$, $\lambda_r$ | Arrival rates for storage ($s$) and retrieval ($r$) requests, modeled as Poisson parameters. | requests/sec |
| $N_C$, $N_L$, $N_T$ | Number of storage columns (depth), lanes (width per side), and vertical tiers. | integer |
| $N_S$ | Number of autonomous shuttles operating within a specific single tier. | integer |
| $u_w$, $u_d$, $u_h$ | Unit width, unit depth, and gross unit height per individual storage position. | meters (m) |
| $v_{sh}$, $v_t$ | Constant operational velocity of the shuttle and the transfer car, respectively. | m/s |
| $v_d$, $v_c$ | Constant operational velocity of the discrete and continuous elevators, respectively. | m/s |
| $t_t$, $t_{sh}$, $t_e$ | Constant time delays for the transfer car, shuttle, and elevator to load/unload a unit. | seconds (s) |
| $d$ | Shuttle turning delay time (applicable to generic shuttles transitioning axes). | seconds (s) |
| $T_s$, $T'_s$ | Total expected throughput time for a storage transaction (specialized and generic). | seconds (s) |
| $W_{sh}$, $W_t$, $W_a$ | Expected queuing delay times to access an available shuttle, transfer car, or cross-aisle. | seconds (s) |
| $W_d$ | Expected queuing delay time to access the discrete elevator. | seconds (s) |
| $f$ | Honeycombing factor, capturing internal lane fragmentation due to LIFO logic. | dimensionless $[0, 1]$ |

## 5. Theoretical Foundations

The single-tier system is the fundamental building block of the analytical framework. A single tier is modeled as a multiclass Semi-Open Queuing Network (SOQN) with class switching. The network is "open" with respect to the transaction requests arriving from the external warehouse environment at rates $\lambda_s$ and $\lambda_r$. It is "closed" with respect to the physical shuttles, which are strictly limited to $N_S$ units. 

An synchronization station is utilized to model the pairing logic between the open and closed components. Arriving transactions enter an external queue (Buffer $B_1$) and wait for an available shuttle. Idle shuttles wait in an internal resource queue (Buffer $B_2$) for new transactions. When both a transaction and a shuttle are present, they are paired and enter the inner service network.

To capture the physical kinematics accurately, the model defines multiple customer classes. Transactions are classified as either storage ($s$) or retrieval ($r$). Shuttles are classified based on their physical dwell location at the moment they are dispatched: interior point shuttles (class $i$) are dwelling deep within a storage lane, while load/unload point shuttles (class $l$) are dwelling at the tier's central I/O point. This multiclass distinction is critical because the expected travel time of a shuttle depends entirely on its starting coordinates. After completing a transaction, a shuttle switches its class based on its new dwell location. 

## 6. Mathematical Models and Detailed Derivations

The derivation of the system's performance begins with the deterministic kinematic equations that calculate the time required to execute a single transaction. These deterministic travel times will later form the basis of the stochastic service rates in the queuing network.

### 6.1. Kinematic Model for Specialized Shuttles

When a specialized shuttle executes a storage transaction, its total throughput time is the sum of several distinct waiting and travel components.

*   **PURPOSE:** To mathematically quantify the total expected time required for a specialized shuttle system to process a storage transaction from arrival to completion.
*   **NOTATION:**
    $$ T_s = W_{sh} + \frac{X_{sh} - x_0}{v_{sh}} + W_t + \frac{|Y_t - Y_{sh}|}{v_t} + \frac{Y_{sh} - y_0}{v_t} + \frac{Y_s - y_0}{v_t} + \frac{X_s - x_0}{v_{sh}} + 2t_t + 2t_{sh} $$
*   **VARIABLES:** $T_s$ is the total storage throughput time. $W_{sh}$ and $W_t$ are the stochastic waiting times for the shuttle and transfer car. $X$ and $Y$ variables represent physical coordinate positions (e.g., $X_{sh}$ is the shuttle's initial depth coordinate, $Y_s$ is the target storage lane coordinate). $x_0$ and $y_0$ are the coordinates of the I/O point. $v_{sh}$ and $v_t$ are velocities. $t_t$ and $t_{sh}$ are constant handling delays.
*   **TERMS:** 
    *   $W_{sh}$: Delay in Buffer $B_1$ waiting for a shuttle.
    *   $\frac{X_{sh} - x_0}{v_{sh}}$: Time for the shuttle to travel from its dwell depth to the cross-aisle.
    *   $W_t$: Delay waiting for the single transfer car to become available.
    *   $\frac{|Y_t - Y_{sh}|}{v_t}$: Time for the transfer car to travel from its current location to the shuttle's lane.
    *   $\frac{Y_{sh} - y_0}{v_t}$: Time for the transfer car carrying the shuttle to travel to the I/O point to pick up the incoming pallet.
    *   $\frac{Y_s - y_0}{v_t}$: Time for the transfer car to transport the loaded shuttle to the target storage lane.
    *   $\frac{X_s - x_0}{v_{sh}}$: Time for the shuttle to drive the pallet deep into the target lane.
    *   $2t_t + 2t_{sh}$: The aggregated physical handling times (loading/unloading the pallet and the shuttle itself).
*   **DERIVATION:** The equation is derived through standard kinematic decomposition, breaking the continuous operational cycle into independent, discrete phases of constant-velocity travel and instantaneous stationary delays.
*   **ASSUMPTIONS:** Assumes constant velocities (ignoring acceleration/deceleration curves for analytical tractability), FCFS queue processing, and a random storage assignment policy.
*   **INTERPRETATION:** This equation physically maps the dependency of the specialized shuttle on the transfer car. Every y-axis movement is mediated by the transfer car's velocity ($v_t$) and subject to its availability ($W_t$), creating a rigid constraint.
*   **APPLICATION:** Used as the foundational travel time equation to compute the service rates for the inner nodes of the SOQN.
*   **LIMITATIONS:** Real-world systems experience acceleration delays; treating velocity as constant strictly under-approximates travel time for very short distances.
*   **CONNECTIONS:** This deterministic formulation is translated into the stochastic expected service times ($\mu^{-1}$) evaluated in the Markov chain model.

### 6.2. Kinematic Model for Generic Shuttles

Generic shuttles bypass the transfer car, altering the kinematic profile fundamentally.

*   **PURPOSE:** To quantify the total expected time for a generic shuttle to execute a storage transaction.
*   **NOTATION:**
    $$ T'_s = W_{sh} + \frac{X_{sh} - x_0}{v_{sh}} + W_a + \frac{|Y_{sh} - y_0|}{v_{sh}} + \frac{Y_s - y_0}{v_{sh}} + d + 2t_{sh} $$
*   **VARIABLES:** $T'_s$ distinguishes the generic shuttle throughput time. $W_a$ replaces $W_t$ as the delay to access the cross-aisle. $d$ is the directional turning delay. 
*   **TERMS:** The transfer car travel times are replaced by the shuttle's own velocity ($v_{sh}$) executing the $y$-axis movements ($|Y_{sh} - y_0|$ and $Y_s - y_0$). The handling time of the transfer car ($2t_t$) is eliminated and replaced by the shuttle's mechanical wheel-turning delay ($d$).
*   **INTERPRETATION:** By eliminating $W_t$ (the single-server queue for the transfer car), the generic shuttle significantly reduces horizontal interference. The cross-aisle access delay ($W_a$) is substantially lower than $W_t$ because multiple generic shuttles can traverse the cross-aisle simultaneously, provided they maintain safety headways.

### 6.3. The Honeycombing Factor and Expected Service Times

To solve the queuing network, the deterministic travel coordinates must be integrated over the entire storage grid to find the expected (mean) travel times. A critical theoretical contribution of the paper is the modeling of LIFO-induced fragmentation, termed the "honeycombing factor."

*   **PURPOSE:** To accurately calculate the expected travel time for a shuttle driving deep into a storage lane, accounting for the reality that multideep lanes are rarely completely full due to LIFO retrieval dynamics.
*   **NOTATION:**
    $$ \mu_{is}^{-1} = \left[ \frac{(N_C - 1)u_d}{2v_{sh}} \right](1+f) + t_{sh} $$
*   **VARIABLES:** $\mu_{is}^{-1}$ is the expected service time for an interior-dwelling shuttle executing a storage task. $N_C$ is the number of columns (maximum depth). $u_d$ is the unit depth clearance. $v_{sh}$ is shuttle velocity. $f$ is the honeycombing factor ($f \in [0,1]$). $t_{sh}$ is handling time.
*   **TERMS:** $\frac{(N_C - 1)u_d}{2}$ calculates the strict mathematical average depth of a lane assuming a perfectly uniform probability distribution across all positions. The multiplier $(1+f)$ mathematically expands this distance to account for fragmentation.
*   **DERIVATION:** In standard random storage, a shuttle travels on average halfway into a lane. However, because pallets are retrieved LIFO, outer positions are emptied while inner positions remain occupied. Incoming storage pallets must therefore travel deeper than the mathematical halfway point to find the first available empty slot. The parameter $f$ scales the uniform average to match this empirical reality.
*   **ASSUMPTIONS:** Valid specifically for multideep LIFO lanes under random storage assignment. 
*   **INTERPRETATION:** If $f=0$, the lane is perfectly dense and S/R operations occur uniformly. If $f > 0$, the system experiences internal fragmentation, forcing shuttles to drive deeper, increasing cycle times.
*   **APPLICATION:** This equation defines the processing rate for the infinite-server nodes representing deep-lane travel in the SOQN.
*   **CONNECTIONS:** Directly impacts the system's sensitivity to physical depth geometry ($N_C$).

## 7. Analytical Methodology: Solving the Queuing Network

Because the single-tier model with specialized shuttles contains a general service time distribution (the transfer car), it forms a non-product-form network. The authors solve this by mathematically reducing the complex inner network of shuttle travel times into a state-dependent exponential server using Mean Value Analysis (MVA).

This reduction yields a simplified two-node system that can be evaluated as a Continuous-Time Markov Chain (CTMC) using the Matrix-Geometric Method (MGM). The transition rate matrix for this CTMC exhibits a repetitive block-tridiagonal structure. By solving the matrix equation $R = A_1 + R B_1 + R^2 C_1$ for the rate matrix $R$, the stationary probability vectors of the system states are extracted. 

### 7.1 Expected External Queue and Total Throughput

*   **PURPOSE:** To compute the ultimate expected throughput time for a storage transaction in the single-tier system based on the MGM solution.
*   **NOTATION:**
    $$ E[T_s] = \frac{Q_{B1}}{\lambda_s + \lambda_r} + \frac{\sum E[\text{Queue Lengths at Nodes}]}{\lambda_s} $$
*   **VARIABLES:** $E[T_s]$ is the expected storage throughput time. $Q_{B1}$ is the expected number of transactions waiting in the external buffer. $\lambda_s, \lambda_r$ are the arrival rates. 
*   **TERMS:** The term $\frac{Q_{B1}}{\lambda_s + \lambda_r}$ applies Little's Law to the external synchronization buffer to find the expected waiting time for a shuttle ($W_{sh}$). The subsequent summation applies Little's Law to the internal nodes of the network to find the expected processing delays across the hardware components.
*   **INTERPRETATION:** Total latency is explicitly partitioned into environmental latency (waiting for available hardware) and kinematic latency (the physical execution of the task).

## 8. Extension to Multitier Architectures

When evaluating a complete 3D facility, multiple single-tier SOQNs operate in parallel, mechanically coupled by the vertical lift. The mathematical modeling diverges sharply based on the elevator type.

A continuous elevator is modeled as an infinite-server station. Because it can process multiple loads simultaneously, transactions from different tiers do not queue against one another. The service time is a deterministic delay based purely on vertical travel distance.

A discrete elevator, however, operates as a strict single-server queue with a Point-of-Service-Completion (POSC) policy. 

### 8.1 Multitier Throughput Time (Discrete Elevator)

*   **PURPOSE:** To compute the expected throughput time in a multitier system bound by a discrete elevator bottleneck.
*   **NOTATION:**
    $$ E[T_s]_{MT} = E[T_s] + E[S_{d,s}] + W_d $$
*   **VARIABLES:** $E[T_s]_{MT}$ is the multitier expected storage throughput time. $E[T_s]$ is the expected delay within the destination tier (from the single-tier MGM model). $E[S_{d,s}]$ is the expected mechanical service time of the discrete elevator moving the load vertically. $W_d$ is the expected queuing delay to access the discrete elevator.
*   **INTERPRETATION:** The total time is the additive sum of horizontal tier operations, vertical elevator kinematics, and vertical elevator queuing. The difficulty lies entirely in calculating $W_d$. 
*   **ANALYTICAL METHOD (Whitt's Decomposition):** Because the departure processes from the individual tier SOQNs are not Markovian (not pure Poisson processes), they cannot be simply summed to find the arrival process at the elevator. The arrival stream is highly variable. To calculate $W_d$, the methodology employs Whitt’s Parametric Decomposition. This iterative algorithm estimates the first moment (the mean) and the second moment (the Squared Coefficient of Variation, SCV) of the interarrival and interdeparture times linking the independent tiers to the lift server. By approximating the variance in the flow streams, the model can estimate the GI/G/1 queue delay ($W_d$) accurately.

## 9. Detailed Results and Design Insights

The rigorous evaluation of the analytical models across various parameter spaces yields several profound engineering insights for warehouse design.

### 9.1 The Convex Geometry Constraint (Optimal Depth/Width Ratio)
The most significant spatial design variable in a shuttle system is the configuration of the tier dimensions, quantified mathematically as the Depth/Width (D/W) ratio. The analytical model calculates $E[T_s]$ iteratively across a discretized spectrum of D/W ratios while holding total storage capacity constant.

The results demonstrate a strict, convex relationship. Regardless of fleet size (e.g., 2 to 5 shuttles) or arrival rates (driving utilization from 60% up to 90%), the mathematical minimum for expected throughput time consistently manifests at a D/W ratio of approximately **1.25**. 
*   **If D/W < 1.25** (a wide, shallow configuration): The physical tier requires a massive cross-aisle. The transfer car travel time ($y$-direction) dominates the transaction cycle, exacerbating the single-server bottleneck delay ($W_t$). 
*   **If D/W > 1.25** (a narrow, deep configuration): The multideep storage lanes become excessively long. Shuttle travel time ($x$-direction) dominates, a delay severely amplified by the honeycombing factor ($f$) because LIFO fragmentation forces shuttles to drive deeper into the lengthy lanes.

Crucially, the numerical models prove that this 1.25 optimal ratio remains identical for both specialized and generic shuttle architectures. While generic shuttles are faster overall, the geometric balance point between $x$-axis and $y$-axis travel distance is invariant.

### 9.2 Generic vs. Specialized Performance and Economic Trade-offs
By eliminating the transfer car delay ($W_t$), generic shuttles fundamentally alter the performance ceiling of the tier. The analytical models quantify this advantage: generic shuttles yield an average throughput capacity that is **24.3% higher** than specialized configurations, reducing expected S/R cycle times by 18.5%. 

However, engineering design is ultimately governed by capital expenditure. Generic shuttles cost approximately €50,000 per unit, while specialized shuttles cost roughly €20,000. When the analytical throughput results are coupled with a cost-minimization objective function to achieve a target total warehouse throughput (e.g., 200 pallets/hour), an important counter-intuitive design insight emerges. 

In multitier configurations utilizing continuous elevators, achieving the target throughput is **cheaper using specialized shuttles**. To compensate for their lower per-tier throughput, the warehouse architect must design a building with a higher number of vertical tiers. The mathematical optimization models prove that the structural cost of building more racking tiers and deploying more specialized shuttles is consistently lower than paying the massive capital premium required to deploy kinematic generic shuttles. 

## 10. Limitations and Model Validity

The analytical SOQN models were validated against discrete-event simulations and empirical data from an active warehouse facility in the United Kingdom. For single-tier configurations, the model proved exceptionally accurate, maintaining throughput time relative errors strictly below 10.4%. 

However, in multitier discrete elevator configurations, the maximum error ceiling expanded to 27%. This degradation in accuracy highlights the specific theoretical limitations of the analytical methodology:
1.  **MGM Instability at High Utilization:** The Matrix-Geometric Method's estimation of external queue lengths ($Q_{B1}$) becomes numerically unstable when the bottleneck utilization exceeds 85%, struggling to accurately capture the long-tail probabilities of the Markov chain.
2.  **Variance Leakage in Decomposition:** Whitt's parametric decomposition relies on two-moment approximations (mean and SCV) to link the tier departures to the lift arrivals. When traffic is highly congested, third-order moments and flow correlations become significant. The two-moment approximation leaks this variance, slightly miscalculating the heavy-traffic lift queue ($W_d$).

Furthermore, the analytical models treat velocities as constants, purposefully excluding acceleration and deceleration integrals to maintain closed-form algebraic tractability. While acceptable for long travel distances, this assumption underestimates travel times for extremely short S/R operations near the I/O point.

## 11. Conclusions

The rigorous mathematical modeling of shuttle-based compact storage systems bridges a critical gap in contemporary material handling engineering. By translating the complex physical kinematics of autonomous shuttles and vertical lifts into Semi-Open Queuing Networks and subsequently solving them via Matrix-Geometric methods and Parametric Decomposition, the research provides a computationally efficient toolset for warehouse conceptualization. 

The analytical formulations prove conclusively that tier geometry is governed by a strict convex constraint optimizing at a Depth/Width ratio of 1.25. Furthermore, the economic integration of these performance models demonstrates that despite the kinematic superiority and reduced cycle times of generic omnidirectional shuttles, the traditional specialized shuttle architecture remains the dominant economic choice for high-throughput, multitier distribution environments.

## 12. Equation Reference Sheet

*   **Eq 1: Specialized Storage Kinematics:** 
    $T_s = W_{sh} + \frac{X_{sh} - x_0}{v_{sh}} + W_t + \frac{|Y_t - Y_{sh}|}{v_t} + \frac{Y_{sh} - y_0}{v_t} + \frac{Y_s - y_0}{v_t} + \frac{X_s - x_0}{v_{sh}} + 2t_t + 2t_{sh}$
*   **Eq 6: Generic Storage Kinematics:** 
    $T'_s = W_{sh} + \frac{X_{sh} - x_0}{v_{sh}} + W_a + \frac{|Y_{sh} - y_0|}{v_{sh}} + \frac{Y_s - y_0}{v_{sh}} + d + 2t_{sh}$
*   **Eq 12 (Equivalent): Expected Deep-Lane Time w/ Honeycombing:** 
    $\mu_{is}^{-1} = \left[ \frac{(N_C - 1)u_d}{2v_{sh}} \right](1+f) + t_{sh}$
*   **Eq 31: Multitier Storage Throughput (Discrete Lift):** 
    $E[T_s]_{MT} = E[T_s] + E[S_{d,s}] + W_d$
*   **Eq 32: Multitier Retrieval Throughput (Discrete Lift):** 
    $E[T_r]_{MT} = E[T_r] + E[S_{d,r}] + W_d$

## 13. Source References

*   Tappia, E., Roy, D., De Koster, R., & Melacini, M. (2016). *Modeling, Analysis, and Design Insights for Shuttle-Based Compact Storage Systems*. Transportation Science.