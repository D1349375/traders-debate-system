# Pre-Registration (Hit Definition) — In Force

> English version of [`docs/zh/preregistration.md`](../zh/preregistration.md). The Chinese
> file is the signed original and is authoritative wherever the two differ.

> **Status: in force as of 2026-07-19 (confirmed by the user in conversation).**
> **This file must not be edited. Changing it means voiding it and re-registering a new
> version; the primary-metric sample restarts from the new version's effective date, and
> prior data is demoted to exploratory reference.**
> (Basis: quant-strategy-dev v11 hypothesis pre-registration + Phase 4 plan §7.1)

## 1. Object of evaluation

- **System:** trader-debate protocol v1-2026-07-19 (R1 blind judgment → R2 structured
  rebuttal, fixed two rounds; a single persona runs R1 only)
- **Personas in force:** **ICT** (`.claude/skills/ict-perspective/SKILL.md`, corpus cutoff
  mid-2026)
- **Instruments:** **BTC/USDT and ETH/USDT** (Binance spot, daily candles, UTC day boundary)
  - Judged independently per instrument (one isolated subagent per persona per instrument),
    with independent sample counts and independent applicable thresholds
  - Adding an instrument later requires an amendment entry, and that instrument's sample
    starts from zero
- **Execution engine:** Claude Code subagents. The `model_id` is written to the database on
  every record. **Switching model mid-stream means switching predictor: analysis must
  segment by model and may never pool across the boundary.**

## 2. Hit definition (core, locked)

- **Primary evaluation horizon: 1d** (judgment day UTC close → next UTC close,
  close-to-close)
- Secondary horizons: 5d, 20d (calendar days) — **exploratory only**, never a basis for
  pass or fail. Their overlapping windows are serially correlated, so confidence intervals
  require block bootstrap or non-overlapping sampling.
- Return definition: `r = price_after_Nd / price_at_bias - 1`
- **Neutral threshold (per instrument):**
  - **BTC/USDT: t = ±0.5%**
  - **ETH/USDT: t = ±1.0%** (ETH's daily volatility exceeds BTC's, so the threshold widens
    correspondingly)
  - Bullish hit ⟺ r > +t; Bearish hit ⟺ r < −t; Neutral hit ⟺ |r| ≤ t
  - The 5d/20d exploratory analysis reuses each instrument's same t. The primary conclusion
    recognizes only 1d at the thresholds in this file.

## 3. Aggregation rule (hard-coded in `engine/aggregate.py`, with pytest coverage)

- Confidence-weighted vote: each direction's score = Σ confidence; highest score wins; a tie
  resolves to Neutral
- `confidence_score` = winning score ÷ total confidence × 100
- Both the R1 bypass aggregation and the final-round aggregation are written to the
  database, enabling the ablation comparison "did the debate add value?"

## 4. Sample and evaluation thresholds (computed per instrument)

- **First descriptive report: n ≥ 30 for a single instrument** (descriptive only; no
  effective/ineffective conclusion whatsoever)
- **First statistical test (MCPT ≥1000 permutations + bootstrap CI): n ≥ 60 for a single
  instrument**
- Pass criteria (declared in advance, judged per instrument): the 1d primary-horizon hit
  rate is significantly above the random baseline (MCPT p < 0.05) **and** the Brier score
  beats the uninformative baseline of always predicting confidence = 50. Failing either
  means no effectiveness claim for that instrument.
- Any sub-category (e.g. high-disagreement days) with n < 20 is marked "insufficient sample"
  and excluded from evaluation.

## 5. Neutral threshold sensitivity and the amendment mechanism (added at user request, 2026-07-19)

- Every formal report (from n ≥ 30 onward) **must attach** a neutral threshold sensitivity
  analysis, recomputing all metrics for t ∈ {0.25%, 0.5%, 1.0%, 1.5%, 2.0%} as an
  **exploratory appendix**
- The appendix must give a threshold-revision recommendation with reasoning (e.g. too few or
  too many samples land in the Neutral class at some t, or calibration differs)
- **The primary conclusion always recognizes only the threshold locked in this file.**
  Adopting a revision means voiding this registration, registering a new version, and
  restarting the primary-metric sample.
- This mechanism guards against picking the flattering threshold after the fact, while
  keeping an institutional route for genuine improvement.

## 6. Known bias disclosures (attached to every report)

- Corpus leakage: the first live record post-dates the ICT corpus cutoff, so accumulation is
  strictly forward-looking and leakage is naturally avoided. **The corpus-covered period is
  never backtested.**
- This system is a research tool. Its output is not investment advice; all results are
  statistical evaluation, not a live trading record.

## 7. Signature

- User confirmation date: **2026-07-19** (confirming the added ETH/USDT threshold of ±1.0%,
  BTC remaining at ±0.5%, and the sensitivity appendix mechanism; otherwise as drafted)
- First record date: **2026-07-19** (BTC/USDT and ETH/USDT start the same day)

## 8. Amendments (date-stamped, append-only)

### 2026-07-19 | Summary v2 / protocol v2

The market summary was upgraded from v1 (a 24h snapshot) to v2: 52 weekly / 90 daily / 42
4-hour closed candles, plus funding rate and the current snapshot, with strict walk-forward,
a neutral information set, and an as-of generator. **The hit definition, aggregation rule,
instruments, personas and sample thresholds are all unchanged.** `protocol_version` becomes
`v2-2026-07-19`; the two records from 2026-07-19 are v1 samples, and the primary analysis
filters by version. Reasoning and design in `market-summary-v2-information-set.md` — v1's
information coverage was insufficient to support a higher-timeframe framework persona, and
on day one ICT returned low confidence citing exactly that.

### 2026-07-20 | Persona panel expanded to three

The active roster expands from ICT alone to **ICT + TJR + EmperorBTC**. Corpora and cutoffs:

- ICT: 537 YouTube transcripts, corpus cutoff mid-2026-07
- TJR: 765 transcripts, covering 2022-09 to 2026-07
- EmperorBTC: 81 transcripts, covering 2025-03 to 2026-07

R2 structured rebuttal activates automatically (the protocol and database already supported
it; no new rule needed). Samples before the effective date — the single-persona ICT v1
records of 2026-07-19 — retain single-persona identity and are **not** retroactively pooled
into the multi-persona sample. Subsequent samples must carry both `protocol_version` (summary
version) and this amendment's effective date (roster version); analysis must align on both
dimensions, never just one.

**Known residual risk of this combination** (full analysis in
[`three-persona-tradeoffs.md`](three-persona-tradeoffs.md)): ICT and TJR both belong to the
SMC / liquidity-hunt family, so confidence-weighted majority voting structurally favours that
school's direction — which is not a market signal. The panel also lacks any macro or cyclical
perspective. This risk does not change the decision to activate, but it must be factored into
any future reading of ensemble lift (§2.2): "the bullish direction wins often" cannot be
attributed to framework quality without first examining the vote structure.

Cost impact: three personas × two instruments × R1+R2 is roughly 650,000–700,000 tokens per
day, an accepted operating cost.

### 2026-07-20 | Daily execution timing discipline

The daily bias run is fixed to the **UTC 00:00–01:00** window (minute precision is not
required, but it may not drift arbitrarily across the day). Reasons: (1) the 4H candle and
the current snapshot change materially with execution time, so running later lets the persona
see more of the day's realized move, sliding daily bias from forward-looking judgment toward
confirmation of what already happened; (2) running near the daily candle open keeps the live
snapshot on the same basis as the backtest mode's "approximate with the day's open",
preventing a basis mismatch when comparing live against backtest; (3) it keeps daily samples
comparable to each other. This is an operational parameter, not part of the hit definition,
but it is equally fixed in advance and may not be adjusted for convenience after the fact. A
`snapshot_captured_at` column (see `database/schema.py`) records the actual execution time
for audit.

### 2026-07-20 | Handling a missed window

If the UTC 00:00–01:00 window is missed, **do not skip the day — run it as soon as possible
that day.** The real deadline is UTC 00:00 the following day; the `date` column is set by the
UTC date at execution, so anything before that still records as that day's sample. The timing
drift caused by a late run is recorded honestly in `snapshot_captured_at` for later audit —
whether to exclude or segment those samples is decided then, not by discarding them now.

If the whole day passes and the next window is missed entirely, that day's sample is
permanently lost. **It may not be reconstructed afterwards using backtest mode (`--as-of`)** —
backtest mode's open-price approximation makes it a materially different, exploratory sample
and it may not be backfilled as a formal one.

This rule must not become an excuse for loosening window discipline: if late runs become
routine, the window setting should be re-examined for practicality rather than leaning
indefinitely on this clause.

### 2026-07-20 | New required field `intraday_scenario`

`persona_debates` gains `intraday_scenario` (nullable in the schema, but mandatory in the
workflow for both R1 and R2 — `record_opinion` rejects an empty value). The content is a
two-branch if-then description of the path **before today's close** (e.g. "tags 65000 first
then reverses bearish toward 60000; if it tags 60000 first, flips bullish toward 65000"),
**strictly scoped to the judgment day, never a multi-day or weekly swing target.**

Motivation: correcting the horizon mismatch observed in dry runs, where persona narratives
landed on medium-term swings, disconnected from the 1d primary evaluation horizon (per Phase
4 plan §7.2). **The hit definition, aggregation rule and evaluation horizon are unchanged** —
this is a descriptive required field only, for future qualitative audit and potential path-
correctness analysis (not a current pre-registered metric). Samples predating this field carry
NULL, and analysis may not demand it retroactively.

### 2026-07-20 | Summary v3: intraday timeframes added

The market summary gains **1H (48 candles ≈ 2 days) / 15M (96 candles ≈ 1 day) / 5M (48
candles ≈ 4 hours, deliberately not a full day to avoid heavy overlap with 15M)**, alongside
the existing weekly/daily/4H, for six timeframes total.

Motivation: to support the `intraday_scenario` requirement. With only weekly/daily/4H, there
was no intraday granularity for a persona to anchor a "today" scenario on, making it easy to
attach a multi-day swing target to a same-day label.

Verified in practice: total candles 184 → 370 (roughly doubled), summary length 12.2KB →
24.2KB, with every timeframe strictly walk-forward in backtest mode (the latest 5M candle
stops at the instant before the as-of time; no leakage). `protocol_version` becomes
`v3-2026-07-20`, covering both this change and the preceding `intraday_scenario` amendment
(neither had any formal sample yet, so they share one version number). Earlier samples filter
by version.

Decision basis: `market-summary-v2-information-set.md` (original design) plus this
conversation — external data sources such as TradingView were evaluated and rejected in favour
of the existing Binance/ccxt live architecture, and a half-day 5M option was rejected for
overlapping 15M at poor cost-benefit. Cost impact: roughly 3,000–4,000 additional tokens per
subagent call, about 5–7% more per day.

### 2026-07-20 | ICT/TJR data-use boundary added, prohibiting volume references

Dry runs found ICT and TJR occasionally mentioning volume ("on volume", "volume drying up")
in R1 narratives. A full review of both SKILL.md files — core mental models, Step 2 research
dimensions, decision heuristics — confirmed **volume was never part of either framework.**
Tracing the R2 rebuttals showed their actual judgment logic (direction, confidence) did not
depend on volume, and both stated explicitly that they do not treat volume as a signal. This
was therefore harmless scene-setting at the narrative layer, not framework contamination.

To stop that phrasing confusing report readers (into believing ICT/TJR use volume evidence)
and to foreclose genuine contamination later, both SKILL.md files gain a hard "data-use
boundary" rule prohibiting volume as a basis for judgment or as vocabulary in reasoning.
**The hit definition and aggregation rule are unchanged** — this is narrative quality control
at the persona prompt layer. EmperorBTC is unaffected (volume is a core tool of his
framework).

### 2026-07-21 | Persona statistical independence: informal monitoring, plus a methodological commitment for future architecture changes

Two reports produced with an outside collaborating agent (held in the user's Downloads, not
material in this repository) observed that the current architecture achieves *process-level*
independence (R1 isolation, no sycophantic convergence) but not necessarily *statistical*
independence — the personas share one underlying LLM and one market summary, so their
disagreement may partly be same-model noise rather than genuine framework difference.
Conclusions:

1. **An informal divergence / pairwise-agreement diagnostic script now exists** (reading
   `persona_debates` and `daily_bias_results`, kept in scratchpad, deliberately not part of
   the repository or `bias_report_metrics.py`). **It is explicitly exploratory monitoring: not
   a formal sample, not a statistical test, not bound by the n ≥ 30/60 thresholds.** It may be
   rerun at any time, purely as an early signal of whether same-model bias risk is worsening,
   and **may not be cited in support of any accuracy or effectiveness conclusion.**
2. **First reading (2026-07-21, four date × asset combinations since the three-persona
   roster):** ICT vs TJR agreed on direction 4/4 (100%); EmperorBTC vs ICT and EmperorBTC vs
   TJR each 3/4 (75%). The sole divergence was 2026-07-20 BTC (EmperorBTC Neutral, ICT/TJR
   Bearish), consistent with EmperorBTC's framework scepticism toward deliberate institutional
   liquidity-hunt narratives. **n = 4 constitutes no conclusion.** The high ICT/TJR agreement
   overlaps the already-registered SMC framework-kinship risk (2026-07-20 amendment), and
   existing tooling cannot distinguish framework kinship from same-model bias.
3. **Methodological commitment (locked now, not contingent on future readings):** should the
   market summary later move to a "neutral core layer plus persona-specific data facets"
   architecture (the information-asymmetry design), **a comparable baseline period under the
   current shared-summary architecture must be accumulated first, and paired comparison must
   verify the change itself works, before switching.** A diagnostic reading that looks alarming
   is not grounds for skipping the baseline — doing so would leave the project permanently
   unable to answer whether the information-asymmetry design actually solved the same-model
   problem, which is worse than not acting. This is a major protocol change and would require
   its own §8 entry when it ships.
4. **No architecture change triggered this round.** The readings show no sign of the three
   personas collapsing into a single output, so the information-asymmetry rewrite is not
   started, avoiding pointless over-optimization. Instead the diagnostic is rerun periodically
   (suggested every 10–15 accumulated days) to watch the trend.

### 2026-07-21 | Summary v4: genuine information routing (EmperorBTC-only volume / RSI / volume ratio)

Following the preceding discussion, an audit of all three SKILL.md files confirmed: ICT and
TJR's mental models need only precise swing high/low coordinates (already provided by the raw
candle CSV, nothing new required); EmperorBTC's model explicitly needs volume (core model 2:
volume corroboration / lie detection) and RSI (Step 2, dimension 4: regime filter). Since the
first two were prohibited from citing volume on 2026-07-20, merely computing new indicators
and leaving them in a shared summary that ICT/TJR "can see but must not use" is not real
routing. This amendment therefore implements **genuine data-layer isolation**:

1. **The summary splits into two variants** (`data/ingestion.py` v4): `core` (shared by
   ICT/TJR; the candle CSV contains no volume column — the header does not even appear) and
   `emperorbtc` (volume-bearing candles plus a new "volume and momentum" block: daily RSI(14,
   standard Wilder), 7-day average volume, and current-to-average volume ratio). These fields
   **do not exist** in the ICT/TJR prompt; it is not a rule saying not to use them.
2. **POC and value area deliberately excluded.** EmperorBTC's core model 2 also mentions
   POC / naked POC / value area, but such indicators require choosing a lookback window and
   volume-bin granularity first, and different choices yield different levels — **that is
   already a methodological interpretation, not objective fact extraction.** Having the main
   agent's code pick those parameters and feed the result would be making a framework choice
   on his behalf, violating the design principle of fully delegating interpretation (per the
   concentric-circle model in §5.3: the neutral core layer may contain only
   methodologically uncontested facts such as raw OHLCV; RSI and volume ratio are single
   uncontested formulas and qualify, POC does not). If his framework needs volume-profile
   concepts, the `emperorbtc` variant already supplies per-candle raw volume for his own logic
   to interpret.
3. **Pre-computed swing highs and lows deliberately excluded.** Spot-checking the frozen
   2026-07-20 raw candles (`data/market_context/2026-07-20_BTCUSDT.txt`) against the three
   specific levels cited in that day's report (65,600 weekly/4H high; 63,886.65 daily low;
   63,748.74 4H low) found all three exactly matching the raw CSV with no sign of calculation
   error. A sample of three values on one day cannot prove this never fails, but there is no
   empirical problem today, so it is not pre-emptively fixed — no pointless over-optimization;
   if a future audit finds a real error, handle it then.
4. **Implementation:** `main.py market` gains `--variant core|emperorbtc`; `upsert_market()`
   writes `market_data.context_summary` (core) and `context_summary_emperorbtc` (a new
   column); trader-debate SKILL.md Step 1 now freezes two files per instrument
   (`..._core.txt` / `..._emperorbtc.txt`), Steps 2 and 3 route per persona, and the Step 6
   report generator (visualization only, affecting no persona judgment) reads the emperorbtc
   variant for the volume subplot. The two variants are independent live fetches, so their
   spot prices may differ by seconds — far below the Neutral threshold, so this is not
   specially handled and `snapshot_captured_at` records reality. 18 new pytest cases (RSI and
   volume-ratio boundaries, variant output differences, per-column database writes) plus the
   existing 52, all passing.
5. **Relationship to the preceding commitment.** The previous amendment required a baseline
   period and paired comparison before any information-asymmetry rewrite. That referred to the
   **systemic rewrite** envisaged in report 2 (splitting the whole summary into modules, aimed
   at testing the same-model independence hypothesis). This change is a **far narrower
   individual-field addition**, motivated by closing a real data gap EmperorBTC's framework
   always required and that was previously missed, not by testing the independence hypothesis
   — so it is not bound by that commitment. Consistent with this project's discipline, it is
   still recorded honestly: **this is the first time the three personas receive materially
   different inputs.** `protocol_version` becomes `v4-2026-07-21`; earlier samples filter by
   version. Future analysis of EmperorBTC's divergence rate must treat this date as a
   structural boundary in the inputs (giving him data his framework genuinely needs, rather
   than removing something he had, means a subsequent change in divergence should first be read
   as improved judgment quality rather than manipulated independence — but the data must still
   be examined rather than the conclusion assumed).
6. **Persona SKILL.md files unchanged.** This touched only `data/ingestion.py`,
   `database/schema.py`, `database/db.py`, `main.py` and `trader-debate/SKILL.md`. The existing
   data-use boundary clauses stay in place as defensive redundancy (ICT/TJR can no longer see
   these fields at all, but retaining the clauses costs nothing).

### 2026-07-22 | Summary v5: macro calendar flags + TJR-only correlated-asset reference + ICT confidence ceiling fix

Prompted by the user noting that ICT had cut its own confidence three days running for
"missing COT/SMT", raising the concern that this distorts the confidence distribution and
undermines backtest validity; and by a related question of whether TJR should receive the data
his cross-asset SMT requires. Three changes:

1. **Macro calendar flags (in all three variants: `core` / `tjr` / `emperorbtc`).** Flags for
   whether the judgment day falls in an NFP week (rule-computed: the first Friday of each
   month, valid for any year), an FOMC decision week (2026 meeting dates, source
   federalreserve.gov, verified 2026-07-22, **covering 2026 only and requiring manual annual
   update**), or August (conventionally thin liquidity). Pure date-rule computation, no
   methodological choice, no external live lookup required. **Coverage disclosed honestly:**
   CPI release dates and US market holidays are not covered, and the absence of a flag does not
   guarantee no macro event that day. All three SKILL.md files explicitly require a "news day
   / risk week" judgment (ICT heuristic 7, TJR heuristic 6, EmperorBTC heuristic 7), making
   this a shared neutral fact layer that needs no routing. Genuinely unpredictable live news
   (breaking events, unscheduled Fed remarks) remains entirely uncovered; whether to add a
   dedicated news subagent is listed in TODO as explicitly optional with hidden costs, and is
   not undertaken here.

2. **The `tjr` variant (replacing TJR's former sharing of `core`).** TJR's SKILL.md Step 2
   dimension 4 explicitly requires checking "whether a correlated asset (BTC vs ETH, or the
   index) shows SMT divergence reinforcing the bias", and heuristic 7 likewise names
   "ES/NASDAQ, or BTC/ETH". This is a genuine framework requirement distilled from his corpus,
   but the isolation rule against mixing in another instrument's summary meant he had never
   received any of it — across three days of formal samples he himself disclosed being unable
   to see SMT for lack of an ETH reference. The `tjr` variant is `core` plus the correlated
   asset's (BTC↔ETH) daily/4H/1H/15M closed candles — no volume, per the core principle, and
   no 5M, because SMT is a swing/intraday confirmation tool rather than a shortest-timeframe
   timing tool and 5M is more noise than signal for it. **Raw candles only; no pre-computed
   divergence conclusion**, for the same reason POC and pre-computed swing points were
   rejected: interpretation stays with the persona's framework.

   **This is an explicit, narrowly scoped exception to the isolation rule** (flagged as
   possible in the 2026-07-21 amendment): TJR's BTC and ETH judgments are no longer fully
   independent samples, and Phase 4 hit-rate analysis must account for that cross-asset
   correlation (per Phase 4 plan §3, portfolio-level correlation checks, previously marked not
   applicable because there was only one debate output — this change triggers its
   applicability).

   **ICT deliberately does not receive equivalent data.** His corpus discusses SMT only as
   "ES vs NASDAQ etc.", and heuristic 3 likewise says only "ES vs NASDAQ etc."; BTC/ETH or
   crypto-internal correlation is never mentioned. Handing him ETH data without prompting would
   probably waste it, since his framework holds no such connection; prompting him to use it
   would amount to inventing a framework extension his corpus never validated, violating the
   full-delegation-of-interpretation principle (§5.2, 2026-07-20 amendment) — the same reasoning
   that rejected POC. EmperorBTC is unaffected (he does not use the SMT concept).

3. **ICT SKILL.md confidence table fix (Step 2 dimension 4 description and the Step 4
   confidence table).** The diagnosis: COT (BTC/USDT has no corresponding regulated futures COT
   filing) and cross-asset SMT (not supplied to ICT, above) are **structurally and permanently
   absent in this system** — not "missing today" but missing every day. The original confidence
   table bundled COT, seasonality and SMT into one "dimension 4"; read strictly as "dimension 4
   requires data on all three", dimension 4 could never be satisfied, locking ICT's confidence
   permanently into the 2–3 dimension band (45–70) and making the 75–95 top band unreachable in
   practice. That is not weak judgment or strong risk awareness — it is a structural ceiling in
   the scoring rule, occurring every day, which will not wash out as the sample grows, and which
   systematically distorts the calibration curve on days that should be high-confidence.

   The fix separates "COT/SMT are permanently absent and do not count against whether dimension
   4 is met" from "the seasonality judgment (NFP week / FOMC week / August, per the macro
   calendar flags) is not subject to that limitation", restoring his confidence ceiling to the
   75–95 range the framework intends. **This is a real behavioural change to ICT's confidence
   distribution**, so `protocol_version` becomes `v5-2026-07-22`; earlier samples (v4 and
   before) filter by version and may not be pooled with v5+ samples for confidence calibration.

Implementation: `data/ingestion.py` gains `classify_macro_calendar()` and the `tjr` variant
logic; `database/schema.py` gains `context_summary_tjr`; `main.py --variant` gains `tjr`;
trader-debate SKILL.md Step 1 now freezes three files (`core` / `tjr` / `emperorbtc`) with
three-way routing in Steps 2 and 3. 63 pytest passing (9 new), with a live smoke test verifying
all three variants (the `tjr` variant at 35.4KB, containing ETH daily/4H/1H/15M reference data
and no volume).

### 2026-07-22 | Outcome horizon calculation fix (off-by-one; four historical records corrected)

While reviewing backtest logic, `fill_outcomes()` in `database/db.py` was found to compute the
target date one day late for the 1d/5d/20d horizons. §2 defines 1d as "judgment day UTC close →
next UTC close", but `price_at_bias` is actually captured near the **open** of judgment day D
(execution window UTC 00:00–01:00), so the reference point aligned with "one day later" is D's
**own** daily candle close (occurring at D+1 00:00 UTC). The code was instead taking the close
of the D+1 candle (occurring at D+2 00:00 UTC) — one day too many, meaning the 1d horizon was
actually measuring roughly 42–48 hours rather than 24, with 5d and 20d each off by one day
likewise.

**Fix:** the horizon target in `fill_outcomes()` changes from `D + N` to `D + N - 1` (1d takes
D's own candle, 5d takes D+4, 20d takes D+19), with a regression test locking the correct target
date (`test_1d_horizon_targets_judgment_days_own_candle`). **The hit definition itself is
unchanged** (§2's thresholds and direction logic are untouched); this simply makes the
implementation match what §2 already specified, so it is not a protocol change requiring a
sample restart.

**Four historical records were retroactively corrected** (the `price_after_1d` values for both
instruments on 2026-07-19 and 2026-07-20, the only backfilled records at the time; 5d/20d had
not matured and were unaffected). Old and new values with an explanation are stored in a new
`daily_bias_results.outcomes_correction_note` column for future audit.

This is the only time in the project's history that an already-persisted outcome value has been
modified. It does not conflict with the "record/finalize is final and may not be overwritten"
discipline, because that discipline protects **the persona's judgment** (direction, confidence,
reasoning — against convenient after-the-fact tampering), not the **computational correctness of
an objective outcome.** `price_after_1d` was never a judgment; it is a purely mathematical
backfill, and an error in it should be fixed — with n = 2 days, this is the lowest-cost moment to
do so.

Corrections: BTC 07-19 65,255.51 → 64,722.54; ETH 07-19 1,904.77 → 1,872.23; BTC 07-20
66,556.16 → 65,255.51; ETH 07-20 1,930.09 → 1,904.77. (Old and new values are offset by exactly
one candle, which incidentally corroborates the diagnosis: 07-19's old wrong value exactly equals
07-20's new correct value, because both originally pointed at the same 07-20 daily close.) 64
pytest passing, including the new `TestFillOutcomes` horizon target regression test.

### 2026-07-22 | Discussed and explicitly rejected: changing the 1d hit definition to touch-based

The user asked how it should count if, after a directional call, price touches the Neutral
threshold intraday and then closes further in the opposite direction. Confirmed: under the
current close-to-close definition only the two endpoints count, and the intervening path does not
affect the hit determination (this case is a miss, because the terminal return lands the opposite
way).

Checking the industry methodology (quant literature), the standard approach for direction
accuracy / hit ratio metrics is exactly this — a fixed holding period and a close-to-close return
from reference price to future price. Touch-based (path-dependent) evaluation belongs to the
*trading profitability* family of simulated-P&L measures, not to *forecast accuracy*; the two
serve different purposes.

**Keeping close-to-close; not adopting touch-based.** Reasons: (1) this system is positioned as a
research tool rather than a signal service, placing it in the former category; (2) touch-based
requires deciding precedence when both thresholds are touched the same day, which needs tick data
the daily candles cannot provide; (3) crypto's volatility would make Neutral almost impossible to
hit under a touch-based rule, distorting the three-way classification; (4) it is incompatible with
the existing Brier score, calibration curve and MCPT toolchain, all of which assume discrete,
non-path-dependent outcomes per sample.

The `intraday_scenario` field is retained as the place for a future **independent exploratory**
path-accuracy metric, not folded into the primary hit definition. This is a discussion conclusion
only: no code or hit definition changed, and `protocol_version` is unaffected.

### 2026-07-23 | Summary v6: new required field `trade_plan` for R1/R2

Reviewing the daily reports from 2026-07-19 to 07-22, the user observed that the three personas'
outputs (direction, confidence, reasoning, falsifier, intraday_scenario) describe the chart and
the day's scenario but never state concretely how the persona would actually take the trade — no
entry trigger, stop logic, target, or position size / risk percentage. Given that this project's
technical analysis is plainly aimed at BTC/ETH intraday traders, that had to be made explicit. All
three SKILL.md files already contain distilled risk rules (ICT/TJR 1–3% risk per trade,
EmperorBTC 0.25–1%, each grounded in the source heuristics); the raw material was there, but the
R1/R2 prompts had never asked them to apply those rules to the current judgment.

**Content specification.** `trade_plan` requires an entry trigger (specific level or condition), a
stop (specific level plus structural basis, not an arbitrary percentage), a target (which may be
staged), and position size / risk percentage (applying that persona's existing risk rules, not
inventing new numbers). **Stating "no trade / standing aside today" is explicitly a valid answer**,
so that no fabricated signal is manufactured merely to fill the field — consistent with each
framework's own selectivity discipline (ICT's reasoning already includes phrasing like "this is
not a setup I would take").

**Scope.** Required in both R1 and R2 (matching the existing `intraday_scenario` specification).
If R2 carries R1's version forward, it must be re-confirmed as still valid and may not be left
blank; if the opponent's rebuttal shifts a key level, `trade_plan` must update with it and may not
become disconnected from direction and confidence.

**This is a "changing the template means changing the protocol" change** (an established principle
in the trader-debate SKILL.md stochasticity-control section): a purely additive required field
that alters neither the existing direction/confidence logic nor the hit definition, but does
change the prompt output structure and the `persona_debates` schema. `protocol_version` becomes
`v6-2026-07-23`; earlier samples (v5 and before, without `trade_plan`) filter by version and may
not be pooled with v6+ samples.

Implementation: `templates/r1_prompt.txt` and `r2_prompt.txt` gain the required item and JSON
schema field; `database/schema.py` gains `trade_plan` (Text, nullable, enforced at the application
layer like `intraday_scenario`); `record_opinion()` in `database/db.py` gains the required-field
check; `main.py cmd_record` passes the field through and `PROTOCOL_VERSION` is bumped;
trader-debate SKILL.md Steps 2 and 3 are updated; the report templates (`report_reference.md` /
`.html`) gain an "if I were taking this trade" block after each persona card's falsifier,
reproducing that persona's R2 `trade_plan` verbatim (R1's if only R1 ran), without
reinterpretation. 65 pytest passing (1 new: `test_trade_plan_required`).

Whether the prompt actually elicits concrete rather than vague trade plans awaits verification on
the next live daily run; if the content proves vague, the wording may need another iteration —
which would be a further protocol change.
