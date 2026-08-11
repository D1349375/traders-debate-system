# Market Summary Protocol History (v1 → current)

> English version of [`docs/zh/market-summary-protocol-history.md`](../zh/market-summary-protocol-history.md).

> **What this document is for.** A single entry point answering "what changed in each
> `protocol_version`, and why", so nobody has to reassemble the story from TODO items,
> [pre-registration](preregistration.md) §8 (formal, chronological rather than thematic), and a
> one-line code comment.
>
> **Maintenance rule (binding on all future versions).** Every time `PROTOCOL_VERSION` in
> `main.py` is bumped, **the same change must add a section here**, matching the format below.
> This file is the authoritative source for *reasoning*; the code itself and
> pre-registration §8 remain authoritative for the full technical specification and the
> verbatim decision context at the time of the change.

---

## v1 — 2026-07-19 (first version, superseded)

**Contents:** a 24-hour slice only — spot price, today's high/low, previous close, volume.

**Problem (found the same day):** a persona like ICT is fundamentally driven by
higher-timeframe narrative — daily and weekly PD arrays set the bias, lower timeframes only
time entries. A 24-hour slice asks the persona to judge with its core tool removed. In the very
first record ICT complained that "I've only touched half of one of my four dimensions",
returning Neutral at confidence 25. **This version measured how much of a framework survives
amputation, which is worthless, so the upgrade was decided the same day.**

Samples: the two 2026-07-19 records (BTC/ETH) are v1, filtered by `protocol_version` and never
pooled with later versions.

---

## v2 — 2026-07-19 — the neutral information set

**Motivation:** directly fix v1's missing higher timeframes.

**What changed:** the summary went from a single slice to multi-timeframe closed candles (52
weekly, 90 daily, 42 4H) plus funding rate (current and 7-day average) plus the current
snapshot (unclosed, separately marked).

**Three key design principles** (full derivation in
[market summary v2 information set](market-summary-v2-information-set.md)):

1. **Neutral information set.** Supply raw candles, never pre-computed structure — no FVGs, no
   levels, no moving average values. Let ICT find his own liquidity pools and a moving-average
   trader compute their own averages: one input, each framework reading it its own way, which
   is the only way framework difference becomes measurable. **This is the precondition for the
   v4/v5 information routing, and it was set here in v2.**
2. **Text, not charts.** Deterministic and reproducible, producing bit-identical formats in
   live and backtest modes.
3. **The generator takes an as-of parameter.** One generator: live passes `None` (= now),
   backtest passes a historical date — which also builds the historical summary generator the
   backtest branch needs.

**Why adding history is not memory contamination:** look-ahead bias means using information
dated *after* the judgment. Price action *before* the judgment day is a legitimate walk-forward
input that any real trader would see. Past price action is input; future price action is
leakage.

**Excluded:** open interest — Binance's API reaches back only 30 days, so the backtest window
cannot be reproduced, violating the live/backtest input consistency principle. Revisit at the
information-asymmetry stage using Binance Vision archives.

---

## v3 — 2026-07-20 — intraday timeframes and required `intraday_scenario`

**Motivation:** dry runs showed a horizon mismatch — with only weekly/daily/4H, personas tended
toward medium-term swing calls, disconnected from the 1d primary evaluation horizon.

**What changed:**

1. Added 1H (48 candles ≈ 2 days), 15M (96 ≈ 1 day) and 5M (48 ≈ 4 hours). Total candles
   184 → 370; summary 12.2KB → 24.2KB. 5M was deliberately capped at four hours rather than a
   full day, to avoid heavy overlap with 15M — added cost with no new information.
2. `persona_debates` gained the required `intraday_scenario` field (mandatory in R1 and R2): a
   two-branch if-then for before that day's close, strictly scoped to the day, never a
   multi-day or weekly target. `record_opinion()` rejects an empty value outright.

**Decided in the same batch:**

- Three personas formally active (ICT + TJR + EmperorBTC), R2 structured rebuttal auto-enabled.
- Execution timing discipline fixed at UTC 00:00–01:00, with missed windows run as soon as
  possible the same day and the real deadline at 00:00 UTC the next day.
- ICT/TJR SKILL.md gained a hard data-use boundary prohibiting volume references — the
  precursor to v4's genuine routing, though at this point still "visible but forbidden".
- External data sources such as TradingView evaluated and rejected (they break live/backtest
  consistency and layer on visual-reading noise); the Binance/ccxt architecture stands.

---

## v4 — 2026-07-21 — genuine information routing (core / emperorbtc)

**Motivation:** two reports produced with an outside collaborating agent raised the statistical
independence problem — several personas sharing one LLM reading one summary. Process-level
independence was achieved; statistical independence was not. On review, v3's "can see volume
but forbidden to use it" was a half measure: the right answer is that it should not exist in
the data at all.

**What changed:** the summary split into two variants rather than one shared text.

- `core` (originally shared by ICT/TJR, ICT-only from v5): candle CSV **with no volume
  column** — the header does not even appear.
- `emperorbtc`: volume-bearing candles plus a "volume and momentum" block — RSI (14, standard
  Wilder), 7-day average volume, and current-to-average volume ratio, all objective formula
  values computed in code.

**Two candidates explicitly rejected, which set this project's routing criterion:**

- **POC / value area.** Requires choosing a lookback window and volume-bin granularity, and
  different choices produce different levels — **already a methodological interpretation, not
  objective fact extraction.** Having the main agent pick those parameters would be making a
  framework choice on the persona's behalf, violating full delegation of interpretation.
- **Pre-computed swing highs and lows.** Spot-checking the frozen 2026-07-20 raw candles
  against three levels cited in that day's report found exact agreement with no calculation
  error — no empirical problem, so no pointless over-optimization.

**The criterion (carried forward):** compute only "single formulas with no methodological
dispute" (RSI, volume ratio); do not compute "methodological constructs involving parameter
choice" (POC).

**Same batch:** `get_session()` in `database/db.py` gained automatic schema migration
(`_sync_schema()`) — manual column migration had already been done three times, and after
automation a collaborator pulling a new schema no longer needs to run `ALTER TABLE` by hand.

---

## v5 — 2026-07-22 — macro calendar flags, TJR-only SMT reference, ICT confidence ceiling fix

**Motivation:** the user observed ICT cutting its own confidence for several consecutive days
over "missing COT/SMT", suspecting a distorted confidence distribution; and separately, whether
TJR should receive the data his cross-asset SMT requires.

**Three changes:**

1. **Macro calendar flags** (in all three variants, a shared neutral fact layer): NFP week
   (rule-computed, valid for any year), FOMC decision week (2026 only, source
   federalreserve.gov, **requiring manual annual update**), and an August flag. Pure date rules,
   no external live lookup. Coverage honestly disclosed as excluding CPI and holiday calendars.

2. **New `tjr` variant** (replacing TJR's use of `core`): core content plus correlated-asset
   (BTC↔ETH) daily/4H/1H/15M reference candles, without volume and without a pre-computed
   divergence conclusion. **ICT deliberately does not get equivalent data.** The criterion: TJR's
   SKILL.md explicitly requires checking BTC vs ETH SMT divergence (grounded in his corpus),
   whereas ICT's corpus cites SMT only as ES/NASDAQ and never mentions BTC/ETH — supplying it
   would probably go unused, and prompting him to use it would invent a framework extension his
   corpus never validated. This is an explicit, narrow exception to the isolation rule, with a
   known consequence: TJR's BTC and ETH judgments are no longer fully independent samples, and
   Phase 4 analysis must account for that cross-asset correlation.

3. **ICT confidence table fix.** COT and cross-asset SMT are structurally and permanently absent
   in this system — not "missing today". The original table bundled COT, seasonality and SMT
   into one "dimension 4", so dimension 4 could never be satisfied and confidence was locked in
   the 45–70 band, with the 75–95 band unreachable in practice. That is a structural ceiling in
   the scoring rule, not conservative judgment; it occurs every day and will not wash out with
   sample size. The fix separates "COT/SMT permanently absent, not counted against dimension 4"
   from "the seasonality judgment is unaffected and evaluates normally against the macro calendar
   flags".

**Same batch:** the trader-debate SKILL.md preflight gained an FOMC year-coverage check — once
the judgment date reaches 2027, Step 5 proactively reminds the user to update the
`_FOMC_MEETINGS_2026` constant rather than relying on memory.

**Discussed and explicitly not done** (listed in TODO as optional): a news-compiler agent.
Genuinely unpredictable live news is entirely uncovered, but the hidden costs are high
(WebSearch latency, token cost, source reliability), the calendar flags already resolve most of
the cases the SKILL.md files mention, and no evidence suggests existing samples were misjudged
because of it. `bias_report_metrics.py` and sample accumulation remain the priority.

**First live verification** (2026-07-22 formal samples): ICT's R1 explicitly noted it would not
cut confidence over structurally unavailable COT/SMT; TJR's R1 cited an ETH comparison for the
first time ("checking ETH, it topped at the same time and fell at the same time — synchronized,
no SMT divergence").

---

## v6 — 2026-07-23 — required `trade_plan` field

**Motivation:** reviewing the daily reports from 2026-07-19 to 07-22, the user observed that the
personas' output never stated concretely how they would actually take the trade — no entry
trigger, stop logic, target, or position size / risk percentage; only chart reading (reasoning)
and the day's two scenarios (`intraday_scenario`). Given the project's clear positioning toward
BTC/ETH intraday traders, this had to be explicit. All three SKILL.md files already contained
distilled risk rules (ICT/TJR 1–3% per trade, EmperorBTC 0.25–1%); what was missing was a prompt
asking them to apply those rules to the current judgment.

**What changed:** `persona_debates` gained the required `trade_plan` field (R1 and R2, matching
the `intraday_scenario` rules from v3). Specification: entry trigger (specific level or
condition), stop (specific level plus structural basis), target (may be staged), and position
size / risk percentage (applying the persona's own existing risk rules). **"No trade / standing
aside" is explicitly valid content** — so no persona is forced to manufacture an unsupported
signal to fill a field, consistent with each framework's own selectivity discipline.

**Criterion carried forward:** this is a purely additive required field that changes neither the
existing direction/confidence logic nor the hit definition, but it falls under "changing the
template means changing the protocol", so it still bumps the version, still gets a
pre-registration §8 entry, and v5-and-earlier samples may not be pooled with v6.

**Same batch:** the report templates gained an "if I were taking this trade" block after each
persona card's falsifier, reproducing that persona's `trade_plan` verbatim without
reinterpretation — following the "quote verbatim, the judge does not re-derive" principle set
by the v5 range and premium/discount table.

**Pending verification:** whether the prompt actually elicits concrete rather than vague trade
plans awaits the next live daily run. If the content proves vague, the wording may need another
iteration — which would be a further protocol change.

---

## The fixed criteria running through every version

- **Neutral information set** (set in v2): supply objective fact, never pre-computed
  interpretation; interpretation belongs to the persona's framework.
- **Compute only formulas with no methodological dispute, never methodological constructs
  involving parameter choice** (set in v4 — the POC versus RSI / swing-high-low distinction).
- **Information routing must be grounded in the corpus; never invent a framework extension on a
  persona's behalf** (set in v5 — the TJR versus ICT SMT data difference).
- **Do not pre-emptively fix what shows no empirical problem** (set in v4 — swing highs and lows
  were spot-checked before deciding not to).
- **Any change to input or protocol changes the system under test:** `PROTOCOL_VERSION` must be
  bumped, pre-registration §8 must record it, and samples are filtered by version and never
  pooled across versions.
