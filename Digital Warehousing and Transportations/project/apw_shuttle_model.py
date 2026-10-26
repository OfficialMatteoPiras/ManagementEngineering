#!/usr/bin/env python3
"""
APW 2026/27 - Six-way shuttle warehouse with lifts
Parametric model + sweeps + discrete-event simulation (DES)

Requirements:  pip install simpy matplotlib      (matplotlib optional, only for plots)

Usage
-----
  python apw_shuttle_model.py report                  # analytical design report for the current parameters
  python apw_shuttle_model.py sweeps                  # D/W, number of lifts, ABC, peak sweeps  -> out/*.csv (+ PNG)
  python apw_shuttle_model.py des                     # discrete-event simulation vs analytical numbers
  python apw_shuttle_model.py all                     # everything

Override any parameter from the command line, e.g.
  python apw_shuttle_model.py des --N_L 44 --n_lifts 2 --dist Uniform --peak_factor 1.25 --lifts_down 1

Every parameter lives in the Params dataclass below (N_C, N_L, N_T, n_lifts, f_hc, ABC split, ...).
Model assumptions (same as the guide document): single-command cycles, trapezoidal speed profile,
honeycombing factor f on the in-lane distance, tier 1 (index 0) at ground level without lift,
one cross-aisle per tier, lifts equally spaced along the aisle at (2k-1)L/(2n).
"""
from __future__ import annotations

import argparse
import csv
import math
import os
import random
import statistics
from dataclasses import dataclass, fields, replace

G = 9.81


# --------------------------------------------------------------------------------------
# 1. PARAMETERS
# --------------------------------------------------------------------------------------
@dataclass
class Params:
    # --- shuttle kinematics (assignment data)
    v_sh: float = 1.4          # m/s
    a_sh: float = 0.5          # m/s^2 (acceleration = deceleration)
    t_turn: float = 4.0        # s, change of direction
    t_sh: float = 25.0         # s, load/unload pallet in rack / at conveyor
    # --- lift kinematics (assignment data)
    v_lift: float = 1.0        # m/s
    a_lift: float = 0.7        # m/s^2
    t_pos: float = 1.0         # s, positioning
    t_ch: float = 7.0          # s, load/unload with chain conveyor (ground floor)
    t_lift_sh: float = 25.0    # s, load/unload with shuttle (tier side)
    lift_interface: str = "shuttle"   # "shuttle" (25 s) or "chain" (7 s chain conveyor at each tier)
    # --- geometry
    u_w: float = 0.85          # m, position pitch across lanes (pallet 800 + 50)
    u_d: float = 1.25          # m, position pitch along lane (pallet 1200 + 50)
    u_h: float = 1.85          # m, vertical pitch (1700 + 150)
    H_bldg: float = 20.0       # m
    L_bldg: float = 45.0       # m
    W_bldg: float = 30.0       # m
    aisle_w: float = 1.5       # m, cross-aisle width
    lane_off: float = 1.0      # m, offset aisle centre -> first slot
    # --- design variables
    N_C: int = 6               # positions per lane (depth), = pallets per SKU
    N_L: int = 44              # lanes per side of the cross-aisle
    N_T: int = 10              # tiers
    n_lifts: int = 3           # lifts along the cross-aisle
    lift_layout: str = "equispaced"   # "equispaced" or "end" (single lift at the aisle end)
    f_hc: float = 0.2          # honeycombing factor
    lanes_per_lift: int = 3    # lanes replaced by each lift shaft
    fill: float = 0.85         # average fill ratio for effective capacity
    # --- flows (assignment data)
    lam_in: float = 40.0       # pallets/h inbound
    lam_out: float = 60.0      # pallets/h outbound (during the working hours)
    peak_factor: float = 1.0   # design margin on the peak (1.25 = +25 %)
    hours_in: float = 24.0
    hours_out: float = 16.0
    # --- ABC split over tiers
    dist: str = "ABC"          # "ABC" or "Uniform"
    nA: int = 2                # tiers for class A
    nB: int = 3                # tiers for class B (remaining tiers = class C)
    shareA: float = 0.80       # share of transactions
    shareB: float = 0.15
    shareC: float = 0.05
    m_pallet: float = 1000.0   # kg (upper bound)
    # --- DES options
    lifts_down: int = 0        # number of lifts out of service (resilience test)
    lift_dwell: str = "ground" # "ground" (lift returns to ground, = analytical cycle) or "posc"
    shuttle_dwell: str = "lift"  # "lift" (returns to lift point, = analytical cycle) or "posc"


def tt(L: float, v: float, a: float) -> float:
    """Travel time for distance L, trapezoidal profile."""
    if L <= 0:
        return 0.0
    return L / v + v / a if L >= v * v / a else 2.0 * math.sqrt(L / a)


# --------------------------------------------------------------------------------------
# 2. ANALYTICAL MODEL
# --------------------------------------------------------------------------------------
def lift_positions(P: Params, n: int | None = None, layout: str | None = None):
    n = P.n_lifts if n is None else n
    layout = P.lift_layout if layout is None else layout
    L = P.N_L * P.u_w
    if layout == "end":
        return [0.0]
    return [(2 * k - 1) * L / (2 * n) for k in range(1, n + 1)]


def lane_y(P: Params, j: int) -> float:
    return (j + 0.5) * P.u_w


def aisle_mean_time(P: Params, n=None, layout=None, positions=None) -> tuple[float, float]:
    """Mean cross-aisle leg time and mean distance (lane -> nearest lift), exact over the N_L lanes."""
    pos = positions if positions is not None else lift_positions(P, n, layout)
    ds = [min(abs(lane_y(P, j) - p) for p in pos) + P.lane_off for j in range(P.N_L)]
    return sum(tt(d, P.v_sh, P.a_sh) for d in ds) / len(ds), sum(ds) / len(ds)


def lane_leg(P: Params) -> float:
    return (P.N_C - 1) * P.u_d / 2 * (1 + P.f_hc) + P.lane_off


def shuttle_cycle(P: Params, n=None, layout=None) -> float:
    """Single-command shuttle cycle (s): start and end at the lift point."""
    ta, _ = aisle_mean_time(P, n, layout)
    tl = tt(lane_leg(P), P.v_sh, P.a_sh)
    return 2 * P.t_sh + 2 * P.t_turn + 2 * ta + 2 * tl


def tier_heights(P: Params):
    return [i * P.u_h for i in range(P.N_T)]


def tier_probs(P: Params, mode: str | None = None):
    mode = P.dist if mode is None else mode
    if mode.lower() == "uniform":
        return [1.0 / P.N_T] * P.N_T
    nC = P.N_T - P.nA - P.nB
    out = []
    for i in range(P.N_T):
        if i < P.nA:
            out.append(P.shareA / P.nA)
        elif i < P.nA + P.nB:
            out.append(P.shareB / P.nB)
        else:
            out.append(P.shareC / nC if nC > 0 else 0.0)
    s = sum(out)
    return [x / s for x in out]


def t_iface(P: Params) -> float:
    return P.t_ch if P.lift_interface == "chain" else P.t_lift_sh


def lift_cycles(P: Params, probs):
    """Mean lift cycle for single command and for a dual (store+retrieve) pair, for tiers >= 2."""
    h = tier_heights(P)
    tI = t_iface(P)
    p_ground = probs[0]
    pl = 1 - p_ground
    if pl <= 0:
        return 0.0, 0.0, 0.0
    q = [probs[i] / pl for i in range(1, P.N_T)]
    hs = h[1:]
    single = sum(qi * (P.t_ch + tI + 2 * tt(x, P.v_lift, P.a_lift) + 2 * P.t_pos) for qi, x in zip(q, hs))
    dual = 0.0
    for qi, hi in zip(q, hs):
        for qj, hj in zip(q, hs):
            dual += qi * qj * (P.t_ch + tt(hi, P.v_lift, P.a_lift) + P.t_pos + tI
                               + tt(abs(hi - hj), P.v_lift, P.a_lift) + P.t_pos + tI
                               + tt(hj, P.v_lift, P.a_lift) + P.t_pos + P.t_ch)
    return single, dual, pl


def lift_utilization(P: Params, probs, n: int | None = None):
    n = P.n_lifts if n is None else n
    s, d, pl = lift_cycles(P, probs)
    rin = P.lam_in * P.peak_factor * pl
    rout = P.lam_out * P.peak_factor * pl
    single = (rin + rout) * s / 3600 / n
    pairs = min(rin, rout)
    dual = (pairs * d + abs(rout - rin) * s) / 3600 / n
    return single, dual, rin + rout


def energy_kwh_day(P: Params, probs) -> float:
    h = tier_heights(P)
    mean_h = sum(p * x for p, x in zip(probs, h))
    moves = P.lam_in * P.hours_in + P.lam_out * P.hours_out
    return moves * P.m_pallet * G * mean_h / 3.6e6


def default_groups(P: Params):
    """Shuttle groups [(tiers, count)] following the recommended fleet (ABC: A x2, B x1, C pooled x2)."""
    if P.dist.lower() == "uniform":
        return [([i], 1) for i in range(P.N_T)]
    g = [([i], 2) for i in range(P.nA)]
    g += [([i], 1) for i in range(P.nA, P.nA + P.nB)]
    c = list(range(P.nA + P.nB, P.N_T))
    if c:
        g.append((c, 2))
    return g


def design_report(P: Params):
    probs = tier_probs(P)
    T = shuttle_cycle(P)
    ta, da = aisle_mean_time(P)
    L = P.N_L * P.u_w
    gross = 2 * P.N_C * P.N_L * P.N_T
    displaced = P.n_lifts * P.lanes_per_lift * P.N_C * P.N_T
    net = gross - displaced
    kappa = 0.5 if P.lift_layout == "end" else 1 / (4 * P.n_lifts)
    dw = P.N_C * P.u_d / (P.N_L * P.u_w)
    dw_star = 2 * kappa / (1 + P.f_hc)
    print("=" * 72)
    print(f"DESIGN REPORT  (dist={P.dist}, peak x{P.peak_factor}, lifts={P.n_lifts} {P.lift_layout}, interface={P.lift_interface})")
    print("=" * 72)
    print(f"Tiers {P.N_T}: height {P.N_T*P.u_h:.2f} m of {P.H_bldg} m {'OK' if P.N_T*P.u_h<=P.H_bldg else 'EXCEEDED'}")
    print(f"Aisle length {L:.1f} m / {P.L_bldg} m ; footprint depth {2*P.N_C*P.u_d+P.aisle_w:.1f} m / {P.W_bldg} m")
    print(f"Positions: gross {gross}, lifts displace {displaced}, net {net} ({net//P.N_C} lanes), effective @fill {net*P.fill:.0f}")
    print(f"D/W = {dw:.2f}   theoretical optimum 2k/(1+f) = {dw_star:.2f}")
    print(f"Lift positions along aisle (m): {[round(x,1) for x in lift_positions(P)]}")
    print(f"Shuttle cycle {T:.1f} s  -> {3600/T:.1f} tx/h per shuttle (mean aisle distance {da:.1f} m)")
    for mode in ("Uniform", "ABC"):
        pr = tier_probs(P, mode)
        s, d, pl = lift_cycles(P, pr)
        us, ud, rl = lift_utilization(P, pr)
        un1 = us * P.n_lifts / (P.n_lifts - 1) if P.n_lifts > 1 else float("nan")
        print(f"[{mode:7s}] lift tx/h {rl:5.1f}  cycle single {s:5.1f}s dual {d:5.1f}s  util single {us*100:5.1f}%  dual {ud*100:5.1f}%  one lift down {un1*100:5.1f}%  energy {energy_kwh_day(P,pr):5.1f} kWh/day")
    lam = (P.lam_in + P.lam_out) * P.peak_factor
    print("Shuttle utilization per tier group (selected distribution):")
    tot = 0
    for tiers, cnt in default_groups(P):
        load = lam * sum(probs[i] for i in tiers)
        print(f"  tiers {[t+1 for t in tiers]} x{cnt}: {load:5.1f} tx/h -> util {load*T/3600/cnt*100:5.1f}%")
        tot += cnt
    print(f"Fleet in service {tot} (+2 spares recommended = {tot+2})")


# --------------------------------------------------------------------------------------
# 3. SWEEPS
# --------------------------------------------------------------------------------------
def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print("written", path)


def sweeps(P: Params, outdir="out", prod_per_side=240):
    configs = [("end", 1, "1 lift at end"), ("equispaced", 1, "1 lift centre"),
               ("equispaced", 2, "2 lifts"), ("equispaced", 3, "3 lifts")]
    # 1) D/W sweep at constant capacity
    rows = []
    for nc in [2, 3, 4, 6, 8, 12, 16, 24]:
        nl = prod_per_side // nc
        Q = replace(P, N_C=nc, N_L=nl)
        row = [nc, nl, round(nc * P.u_d / (nl * P.u_w), 3)]
        for layout, n, _ in configs:
            row.append(round(shuttle_cycle(Q, n, layout), 1))
        rows.append(row)
    write_csv(f"{outdir}/sweep_dw.csv", ["N_C", "N_L", "D/W"] + [c[2] for c in configs], rows)
    # 2) number of lifts
    rows = []
    pu, pa = tier_probs(P, "Uniform"), tier_probs(P, "ABC")
    for n in range(1, 7):
        T = shuttle_cycle(P, n, "equispaced")
        row = [n, round(T, 1), round(3600 / T, 1)]
        for pr in (pu, pa):
            s, d, _ = lift_utilization(P, pr, n)
            row += [round(s * 100, 1), round(d * 100, 1)]
        rows.append(row)
    write_csv(f"{outdir}/sweep_lifts.csv",
              ["n_lifts", "T_sh_s", "cap_per_shuttle", "U_unif_single_%", "U_unif_dual_%", "U_ABC_single_%", "U_ABC_dual_%"], rows)
    # 3) peak factor
    rows = []
    for pf in [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]:
        Q = replace(P, peak_factor=pf)
        row = [pf, round((P.lam_in + P.lam_out) * pf, 0)]
        for n in (2, 3):
            for pr in (pu, pa):
                row.append(round(lift_utilization(Q, pr, n)[0] * 100, 1))
        rows.append(row)
    write_csv(f"{outdir}/sweep_peak.csv",
              ["peak_factor", "tx_per_h", "U_2lifts_unif_%", "U_2lifts_ABC_%", "U_3lifts_unif_%", "U_3lifts_ABC_%"], rows)
    # 4) honeycombing
    rows = [[f, round(shuttle_cycle(replace(P, f_hc=f)), 1)] for f in (0.0, 0.05, 0.1, 0.2, 0.3)]
    write_csv(f"{outdir}/sweep_honeycombing.csv", ["f", "T_sh_s"], rows)
    # optional plots
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        data = list(csv.reader(open(f"{outdir}/sweep_dw.csv")))[1:]
        fig, ax = plt.subplots(figsize=(7, 4))
        for k, (_, _, lab) in enumerate(configs):
            ax.plot([float(r[2]) for r in data], [float(r[3 + k]) for r in data], marker="o", label=lab)
        ax.set_xscale("log"); ax.set_xlabel("D/W"); ax.set_ylabel("shuttle cycle (s)")
        ax.set_title("Shuttle cycle vs depth/width ratio (constant capacity)"); ax.legend(); ax.grid(alpha=.3)
        fig.tight_layout(); fig.savefig(f"{outdir}/sweep_dw.png", dpi=150)
        data = list(csv.reader(open(f"{outdir}/sweep_lifts.csv")))[1:]
        fig, ax = plt.subplots(figsize=(7, 4))
        xs = [int(r[0]) for r in data]
        ax.bar([x - 0.2 for x in xs], [float(r[3]) for r in data], 0.4, label="Uniform")
        ax.bar([x + 0.2 for x in xs], [float(r[5]) for r in data], 0.4, label="ABC")
        ax.axhline(75, color="r", ls="--", lw=1); ax.set_xlabel("number of lifts"); ax.set_ylabel("lift utilization (%)")
        ax.set_title("Lift utilization at peak (single command)"); ax.legend()
        fig.tight_layout(); fig.savefig(f"{outdir}/sweep_lifts.png", dpi=150)
        print("plots written")
    except ImportError:
        print("matplotlib not installed: plots skipped")


# --------------------------------------------------------------------------------------
# 4. DISCRETE-EVENT SIMULATION (SimPy)
# --------------------------------------------------------------------------------------
class Shuttle:
    __slots__ = ("id", "tier", "y", "depth", "busy", "active")

    def __init__(self, i, tier, y):
        self.id, self.tier, self.y, self.depth = i, tier, y, 0.0
        self.busy = 0.0     # time held by transactions (incl. waiting for the lift)
        self.active = 0.0   # time spent working (moving / handling)


class Lift:
    def __init__(self, env, simpy, pos):
        self.pos, self.res, self.tier, self.busy = pos, simpy.Resource(env, 1), 0, 0.0


class Group:
    def __init__(self, env, simpy, tiers, shuttles):
        self.tiers, self.shuttles = tiers, shuttles
        self.store = simpy.Store(env)
        for s in shuttles:
            self.store.put(s)


class Warehouse:
    def __init__(self, P: Params, groups, seed, simpy):
        self.P, self.simpy = P, simpy
        self.env = simpy.Environment()
        self.rng = random.Random(seed)
        self.probs = tier_probs(P)
        self.h = tier_heights(P)
        pos = lift_positions(P)
        if P.lifts_down:                         # remove lifts starting from the middle one
            for _ in range(min(P.lifts_down, len(pos) - 1)):
                pos.pop(len(pos) // 2)
        self.lifts = [Lift(self.env, simpy, p) for p in pos]
        self.groups, self.group_of = [], {}
        sid = 0
        for tiers, cnt in groups:
            sh = []
            for k in range(cnt):
                sh.append(Shuttle(sid, tiers[k % len(tiers)], self.lifts[0].pos))
                sid += 1
            g = Group(self.env, simpy, tiers, sh)
            self.groups.append(g)
            for t in tiers:
                self.group_of[t] = g
        self.stats = {"S": [], "R": []}
        self.active_per_tx = []
        self.relocations = 0
        self.warm = 0.0

    # -- kinematic helpers -------------------------------------------------------
    def nearest_lift(self, y):
        return min(self.lifts, key=lambda L: abs(L.pos - y))

    def t_goto_lane(self, sh, y, dep):
        P = self.P
        t = 0.0
        if sh.depth > 0:
            t += tt(sh.depth, P.v_sh, P.a_sh) + P.t_turn
        t += tt(abs(sh.y - y) + P.lane_off, P.v_sh, P.a_sh) + P.t_turn + tt(dep, P.v_sh, P.a_sh)
        return t

    def t_goto_lift(self, sh, pos):
        P = self.P
        t = 0.0
        if sh.depth > 0:
            t += tt(sh.depth, P.v_sh, P.a_sh) + P.t_turn
        if sh.depth > 0 or abs(sh.y - pos) > 1e-9:
            t += tt(abs(sh.y - pos) + P.lane_off, P.v_sh, P.a_sh)
        return t

    def lift_move(self, lift, tier):
        P = self.P
        if lift.tier == tier:
            return 0.0
        d = abs(self.h[lift.tier] - self.h[tier])
        lift.tier = tier
        return tt(d, P.v_lift, P.a_lift) + P.t_pos

    # -- relocation of a pooled shuttle to another tier --------------------------
    def relocate(self, sh, target):
        P, env = self.P, self.env
        lift = min(self.lifts, key=lambda L: abs(L.pos - sh.y))
        t = self.t_goto_lift(sh, lift.pos)
        sh.active += t
        yield env.timeout(t)
        sh.y, sh.depth = lift.pos, 0.0
        with lift.res.request() as rq:
            yield rq
            t0 = env.now
            yield env.timeout(self.lift_move(lift, sh.tier))
            yield env.timeout(P.t_lift_sh)
            yield env.timeout(self.lift_move(lift, target))
            yield env.timeout(P.t_lift_sh)
            if P.lift_dwell == "ground":
                yield env.timeout(self.lift_move(lift, 0))
            lift.busy += env.now - t0
        sh.tier = target
        self.relocations += 1

    # -- transactions ------------------------------------------------------------
    def store(self, i, y, dep, t_arr):
        P, env = self.P, self.env
        grp = self.group_of[i]
        sh = yield grp.store.get()
        t_acq = env.now
        a0 = sh.active
        if sh.tier != i:
            yield from self.relocate(sh, i)
        lift = self.nearest_lift(y)
        tI = t_iface(P)
        if i == 0:
            t = self.t_goto_lift(sh, lift.pos) + P.t_sh
            sh.active += t
            yield env.timeout(t)
            sh.y, sh.depth = lift.pos, 0.0
        else:
            tmove = self.t_goto_lift(sh, lift.pos)
            ev_sh = env.timeout(tmove)
            sh.active += tmove
            with lift.res.request() as rq:
                yield rq
                t0 = env.now
                lt = self.lift_move(lift, 0) + P.t_ch + self.lift_move(lift, i)
                yield ev_sh & env.timeout(lt)
                sh.y, sh.depth = lift.pos, 0.0
                sh.active += tI
                yield env.timeout(tI)                   # hand-over lift -> shuttle
                if P.lift_dwell == "ground":
                    yield env.timeout(self.lift_move(lift, 0))
                lift.busy += env.now - t0
        t = self.t_goto_lane(sh, y, dep) + P.t_sh
        sh.active += t
        yield env.timeout(t)
        sh.y, sh.depth = y, dep
        if t_arr >= self.warm:
            self.stats["S"].append(env.now - t_arr)
        if P.shuttle_dwell == "lift":
            t = self.t_goto_lift(sh, lift.pos)
            sh.active += t
            yield env.timeout(t)
            sh.y, sh.depth = lift.pos, 0.0
        sh.busy += env.now - t_acq
        if t_arr >= self.warm:
            self.active_per_tx.append(sh.active - a0)
        yield grp.store.put(sh)

    def retrieve(self, i, y, dep, t_arr):
        P, env = self.P, self.env
        grp = self.group_of[i]
        sh = yield grp.store.get()
        t_acq = env.now
        a0 = sh.active
        if sh.tier != i:
            yield from self.relocate(sh, i)
        lift = self.nearest_lift(y)
        tI = t_iface(P)
        t = self.t_goto_lane(sh, y, dep) + P.t_sh
        sh.active += t
        yield env.timeout(t)
        sh.y, sh.depth = y, dep
        if i == 0:
            t = self.t_goto_lift(sh, lift.pos) + P.t_sh
            sh.active += t
            yield env.timeout(t)
            sh.y, sh.depth = lift.pos, 0.0
            if t_arr >= self.warm:
                self.stats["R"].append(env.now - t_arr)
            sh.busy += env.now - t_acq
            if t_arr >= self.warm:
                self.active_per_tx.append(sh.active - a0)
            yield grp.store.put(sh)
            return
        tback = self.t_goto_lift(sh, lift.pos)
        sh.active += tback
        ev_sh = env.timeout(tback)
        with lift.res.request() as rq:
            yield rq
            t0 = env.now
            lt = self.lift_move(lift, i)
            yield ev_sh & env.timeout(lt)
            sh.y, sh.depth = lift.pos, 0.0
            sh.active += tI
            yield env.timeout(tI)                       # hand-over shuttle -> lift
            sh.busy += env.now - t_acq                  # shuttle is free from here
            if t_arr >= self.warm:
                self.active_per_tx.append(sh.active - a0)
            yield grp.store.put(sh)
            yield env.timeout(self.lift_move(lift, 0) + P.t_ch)
            lift.busy += env.now - t0
        if t_arr >= self.warm:
            self.stats["R"].append(env.now - t_arr)

    def arrivals(self, rate_per_h, kind):
        P, env = self.P, self.env
        if rate_per_h <= 0:
            return
        mean = 3600.0 / rate_per_h
        while True:
            yield env.timeout(self.rng.expovariate(1.0 / mean))
            i = self.rng.choices(range(P.N_T), weights=self.probs)[0]
            y = lane_y(P, self.rng.randrange(P.N_L))
            dep = P.lane_off + self.rng.randrange(P.N_C) * P.u_d * (1 + P.f_hc)
            env.process((self.store if kind == "S" else self.retrieve)(i, y, dep, env.now))

    def run(self, hours, warm_h):
        P, env = self.P, self.env
        self.warm = warm_h * 3600
        env.process(self.arrivals(P.lam_in * P.peak_factor, "S"))
        env.process(self.arrivals(P.lam_out * P.peak_factor, "R"))
        env.run(until=self.warm)
        snap_l = [L.busy for L in self.lifts]
        snap_s = [[s.busy for s in g.shuttles] for g in self.groups]
        env.run(until=hours * 3600)
        span = hours * 3600 - self.warm
        res = {
            "lift_util": [(L.busy - b) / span for L, b in zip(self.lifts, snap_l)],
            "group_util": [sum(s.busy - b for s, b in zip(g.shuttles, bs)) / (span * len(g.shuttles))
                           for g, bs in zip(self.groups, snap_s)],
            "T_store": statistics.mean(self.stats["S"]) if self.stats["S"] else float("nan"),
            "T_retr": statistics.mean(self.stats["R"]) if self.stats["R"] else float("nan"),
            "p95_store": sorted(self.stats["S"])[int(0.95 * len(self.stats["S"]))] if self.stats["S"] else float("nan"),
            "p95_retr": sorted(self.stats["R"])[int(0.95 * len(self.stats["R"]))] if self.stats["R"] else float("nan"),
            "active": statistics.mean(self.active_per_tx) if self.active_per_tx else float("nan"),
            "n_tx": len(self.stats["S"]) + len(self.stats["R"]),
            "reloc_per_h": self.relocations / hours,
        }
        return res


def run_des(P: Params, groups=None, hours=60.0, warm_h=5.0, reps=5, seed=1):
    try:
        import simpy
    except ImportError:
        raise SystemExit("simpy is required for the simulation: pip install simpy")
    groups = groups or default_groups(P)
    out = []
    for r in range(reps):
        out.append(Warehouse(P, groups, seed + r, simpy).run(hours, warm_h))
    return groups, out


def mean_of(out, key):
    return statistics.mean(o[key] for o in out)


def des_report(P: Params, hours=60.0, warm_h=5.0, reps=5, outdir="out"):
    groups, out = run_des(P, hours=hours, warm_h=warm_h, reps=reps)
    probs = tier_probs(P)
    T = shuttle_cycle(P)
    lam = (P.lam_in + P.lam_out) * P.peak_factor
    s, d, pl = lift_cycles(P, probs)
    us, _, _ = lift_utilization(P, probs, max(1, P.n_lifts - P.lifts_down))
    nl = max(1, P.n_lifts - P.lifts_down)
    print("=" * 72)
    print(f"DES vs ANALYTICAL  ({reps} replications x {hours:.0f} h, warm-up {warm_h:.0f} h, dist={P.dist}, "
          f"lifts={nl}, peak x{P.peak_factor})")
    print("=" * 72)
    print(f"Shuttle active time per transaction : DES {mean_of(out,'active'):6.1f} s   analytical T_sh {T:6.1f} s")
    lu = [statistics.mean(o["lift_util"][k] for o in out) for k in range(len(out[0]["lift_util"]))]
    print(f"Lift utilization (mean of lifts)     : DES {statistics.mean(lu)*100:5.1f} %   analytical (single cmd) {us*100:5.1f} %")
    print(f"  per lift (DES): {[round(x*100,1) for x in lu]}")
    rows = []
    for k, (tiers, cnt) in enumerate(groups):
        load = lam * sum(probs[i] for i in tiers)
        an = load * T / 3600 / cnt
        de = statistics.mean(o["group_util"][k] for o in out)
        print(f"Shuttles tiers {[t+1 for t in tiers]} x{cnt}: DES util {de*100:5.1f} %   analytical {an*100:5.1f} %")
        rows.append([str([t + 1 for t in tiers]), cnt, round(de * 100, 1), round(an * 100, 1)])
    print(f"Throughput time storage   : mean {mean_of(out,'T_store'):6.1f} s   p95 {mean_of(out,'p95_store'):6.1f} s")
    print(f"Throughput time retrieval : mean {mean_of(out,'T_retr'):6.1f} s   p95 {mean_of(out,'p95_retr'):6.1f} s")
    print(f"Shuttle relocations per hour: {mean_of(out,'reloc_per_h'):.2f}")
    write_csv(f"{outdir}/des_groups.csv", ["tiers", "shuttles", "DES_util_%", "analytical_util_%"], rows)
    write_csv(f"{outdir}/des_summary.csv",
              ["metric", "DES", "analytical"],
              [["shuttle active time per tx (s)", round(mean_of(out, 'active'), 1), round(T, 1)],
               ["lift utilization (%)", round(statistics.mean(lu) * 100, 1), round(us * 100, 1)],
               ["throughput time storage mean (s)", round(mean_of(out, 'T_store'), 1), ""],
               ["throughput time retrieval mean (s)", round(mean_of(out, 'T_retr'), 1), ""]])


# --------------------------------------------------------------------------------------
# 5. CLI
# --------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["report", "sweeps", "des", "all"])
    ap.add_argument("--outdir", default="out")
    ap.add_argument("--hours", type=float, default=60.0)
    ap.add_argument("--warm", type=float, default=5.0)
    ap.add_argument("--reps", type=int, default=5)
    for f in fields(Params):
        ap.add_argument(f"--{f.name}", type=type(f.default), default=None)
    args = ap.parse_args()
    P = Params(**{f.name: getattr(args, f.name) for f in fields(Params) if getattr(args, f.name) is not None})
    if args.command in ("report", "all"):
        design_report(P)
    if args.command in ("sweeps", "all"):
        sweeps(P, args.outdir)
    if args.command in ("des", "all"):
        des_report(P, args.hours, args.warm, args.reps, args.outdir)


if __name__ == "__main__":
    main()
