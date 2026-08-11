# Three-Persona Panel — Trade-off Analysis

> English version of [`docs/zh/three-persona-tradeoffs.md`](../zh/three-persona-tradeoffs.md).

> Written 2026-07-20. Subject: the ICT + TJR + EmperorBTC combination as a debate panel.
> Based on observations from the three-persona dry run (2026-07-19, BTC/USDT) plus each
> persona's SKILL.md positioning. Related: [README](../../README.md) §3 (protocol design) and
> [pre-registration](preregistration.md) §8 (activation amendment).

---

## 0. Two kinds of value, kept separate

This report evaluates **process and decision-support value** — whether the debate mechanism
produces structured multi-framework analysis. That was verified in the dry run.
**Predictive value** — whether these judgments beat chance — is a different question,
answerable only at n ≥ 30/60, out of scope here, and not to be borrowed against on the
strength of this report's positive assessment.

---

## 1. The panel

| Persona | School | Corpus | Home market | Register |
|---|---|---|---|---|
| ICT | SMC / liquidity hunts / PD arrays / algorithmic determinism | 537 videos, cutoff mid-2026-07 | Futures (NQ/ES) | Assertive; honest when cutting his own confidence |
| TJR | A younger repackaging of ICT/SMC concepts | 765 videos, 2022-09 to 2026-07 | General intraday / forex | Colloquial, oscillating between assertive and candid |
| EmperorBTC | Auction market theory / volume-price lie detection / classical TA | 81 videos, 2025-03 to 2026-07 | Crypto (BTC home turf) | Calm, probabilistic humility |

---

## 2. Strengths

### 2.1 Genuine framework disagreement, not the same view renamed

The SMC liquidity narrative of ICT/TJR and EmperorBTC's auction theory and volume-price lie
detection produced **concrete, actionable disagreement** in the dry run — methodological
difference, not stylistic:

- Different range anchoring (ICT computes discount from a higher-timeframe leg down;
  EmperorBTC computes premium from the recent balance range)
- Opposite readings of the evidentiary status of the same volume data (EmperorBTC treats a
  rally on declining volume as a warning; ICT/TJR hold that algorithmic price delivery needs
  no volume corroboration)

This is exactly the **real signal** the divergence analysis in Phase 4 §2.3 needs, rather than
performed disagreement staged for the sake of a debate.

### 2.2 EmperorBTC is the only persona on home turf

ICT and TJR trade futures and forex professionally; applying them to crypto is framework
extrapolation. EmperorBTC is the only one whose core market actually is BTC. That lets the
panel test more than "does the SMC framework transfer to crypto" — one member's specialty
maps directly onto the asset being judged.

### 2.3 Confidence-expression style adds variance for calibration analysis

EmperorBTC habitually hedges probabilistically ("this is only a probabilistic guess"); ICT and
TJR are assertive-but-qualified. That calibration-style difference may itself be an
interesting between-persona variable in Brier score and calibration curve analysis.

### 2.4 All three showed internally coherent argument quality in the dry run

In the single observation available, all three argued from evidence and engaged directly with
the opponent's strongest point, with no sign of fabricated reasoning. A positive early signal
— but n = 1, which is no conclusion about stability.

---

## 3. Weaknesses and risks

### 3.1 ⚠️ Two of three votes structurally favour one school (the most important finding here)

TJR's positioning *is* "a younger repackaging of ICT/SMC concepts". He and ICT are not two
independent viewpoints; they are **one framework plus its simplified version.** The dry run
demonstrated this perfectly: ICT and TJR reached the same direction through nearly identical
logic (a sweep of 57,800 pointing toward buy stops at 65,600), differing only in range anchor
arithmetic. The only genuine dissent came from EmperorBTC.

**Consequence:** confidence-weighted majority voting structurally favours whichever direction
the SMC narrative points — not because SMC is more accurate, but because the panel is 2:1 SMC
by construction. **If ensemble results later show the bullish direction winning often, that
must be excluded as a vote-structure artefact before it can be attributed to framework
quality.** This is the single most important line in this analysis.

### 3.2 No macro or cyclical perspective

All three are technical, price-action or volume traders. None represents macro narrative or
on-chain cycles. That echoes the gap left by Mark Douglas (psychology) and GCR (macro
narrative) both being absent from the original WBS shortlist. The **RektCapital corpus (173
videos, four-year and halving cycle theory)** recently pulled in by a collaborator offers a
genuinely different axis — not disagreement within technical analysis, but microstructure
versus macro cycle. That is worth more than adding another technical analyst.

### 3.3 EmperorBTC's corpus effectively removes him from the backtest branch

See [backtest contamination and dual memory](backtest-contamination-dual-memory.md):
EmperorBTC's corpus is day-by-day BTC commentary running up to 2026-07, so under semi-clean
zone auditing he would be excluded across nearly the entire window. **This affects only the
exploratory backtest branch, not the forward daily accumulation that is the main line** — he
participates normally in formal samples.

### 3.4 TJR and EmperorBTC distillation depth has not been independently verified by us

ICT went through direct chat and real-chart testing. TJR and EmperorBTC were verified by a
collaborator (three sub-agent verifications), and we have only observed adequate quality
through one dry run. Their quality is not necessarily lower, but it is **less confirmed**
relative to ICT. This is a reversible risk: if formal samples later show unstable output
quality from a persona, the protocol supports demoting them after the fact (removal via a §8
amendment), at the cost of voiding that persona's accumulated samples.

### 3.5 Cost and statistical granularity

Cost is roughly 6× the single-persona baseline (650,000–700,000 tokens per day). With three
votes, the divergence measure can only take a few discrete values (0, 0.33, 0.67, 1.0), so
making the high/medium/low divergence bucketing analysis (§2.3) meaningful requires enough
samples for each bucket to hold sufficient days. This is a common small-panel problem, not
specific to this combination, but worth expecting.

---

## 4. Conclusion and recommendations

**Keep the three-persona panel live.** Do not stall progress over an imperfect combination.
But two things must happen:

1. **The vote-structure bias in §3.1 must be recorded in a pre-registration amendment** as a
   mandatory check when interpreting future ensemble lift results — done, in
   [pre-registration](preregistration.md) §8.
2. **The next persona genuinely worth distilling is RektCapital** (adding the macro-cycle
   axis), ahead of adding another technical-analysis trader.

---

> Methodological analysis, not investment advice. All personas are role simulations distilled
> from publicly available video transcripts.
