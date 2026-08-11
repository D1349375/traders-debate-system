# Market Summary v2 — Information Set Design

> English version of [`docs/zh/market-summary-v2-information-set.md`](../zh/market-summary-v2-information-set.md).

> Written 2026-07-19, prompted by what the user noticed on the day the first record landed
> (§1). Fixes the v2 summary specification and records the design reasoning. Related:
> [backtest contamination and dual memory](backtest-contamination-dual-memory.md),
> [pre-registration](preregistration.md) §8.

---

## 1. The finding: v1 was testing personas with their tools removed

The v1 summary contained only a 24-hour slice — current price, daily high and low, previous
close, volume. But a persona like ICT is **fundamentally driven by higher-timeframe
narrative**: daily and weekly PD arrays set the bias, and lower timeframes only time the
entry. Supplying a 24-hour slice asks the persona to judge while stripped of its core tool.

**First-hand evidence.** In the very first record (2026-07-19), the ICT persona volunteered
that "I've only touched half of one of my four dimensions" and "it's a guess, it's not
scientific", returning Neutral at confidence 25 — the persona itself complained the input was
insufficient. Accumulating three months on v1 inputs would measure "how much of the framework
survives after amputating higher timeframes", which is not a question worth answering. The
same applies to any other persona: a moving-average trader cannot see the MA stack, a
level-based trader cannot see higher-degree resistance.

## 2. Why adding price history is not memory contamination

**Look-ahead bias means using information dated after the judgment.** Giving the model 90
daily and 52 weekly candles from *before* the judgment day is a fully legitimate
walk-forward information set — a real trader looking at a chart sees exactly that. Past price
action is **input**; future price action is **leakage**.

One asterisk: inside the model's memorized period (before 2026-01), rich historical candles
may help the model recognize which period this is and recall weighted expectations about what
followed. But that interval is permanently abandoned anyway (see the dual-memory report §4),
so it is not an argument against this change. In the semi-clean zone (2026-02 to 07-14) the
model has no memory of the period to recall, and the forward main line has no issue at all.
**Conclusion: this upgrade is safe for both the main line and the backtest branch.**

## 3. The v2 specification

```
[Summary v2 structure] (generated for an as-of timestamp; closed candles only)
├─ Weekly: last 52 OHLCV candles (about a year of structure)
├─ Daily:  last 90 OHLCV candles (about three months)
├─ 4H:     last 42 candles (about a week, intraday structure)
├─ Funding rate (perpetuals): current value plus 7-day average
└─ Current snapshot: spot price, 24h change, today's intraday high/low (marked unclosed)
```

Candles are rendered as CSV text tables (`date,open,high,low,close,volume`), totalling
roughly 5–8KB — about 4,000–6,000 extra input tokens per judgment.

### Three design principles

1. **A neutral information set.** Supply raw candles, never pre-computed structure — no FVGs,
   no support/resistance levels, no moving average values. Pre-computing structure injects our
   interpretation into the input. Raw data lets ICT find his own liquidity pools and a moving
   average trader compute their own averages: one input, each framework reading it its own
   way, which is the only way framework difference becomes measurable. This is also the
   precondition for any future information-asymmetry design — establish the common baseline
   first, then discuss differentiated facets.
2. **Text, not charts.** Text OHLCV is deterministic and reproducible, so live and backtest
   modes can produce bit-identical input formats and stay comparable. Chart rendering adds a
   layer of nondeterminism and is not used.
3. **The generator takes an as-of parameter.** One generator: live passes today, backtest
   passes a historical date. This also builds the historical summary generator the backtest
   branch needs, in one pass.

### What was included and excluded

| Item | Decision | Reasoning |
|---|---|---|
| Funding rate | **Include** | Objective data with a historical ccxt API (`fetch_funding_rate_history`), reproducible in backtest; a core input for positioning-oriented personas |
| Open interest | **Exclude in v2** | Binance's OI history reaches back only 30 days, so the backtest window (from 2026-02) cannot be reproduced — violating the "live and backtest inputs must match" principle. Revisit at the information-asymmetry stage using Binance Vision archive files (the quant project's `data_metrics/` pipeline already handles these) |
| Today's unclosed candle | Only in the "current snapshot" block, marked unclosed | Strict separation of closed and unclosed, preventing same-day information leaking into backtests |

### Snapshot semantics in backtest mode (open question)

In live mode the snapshot is the real-time price at execution. Historical as-of mode cannot
reproduce the intraday state at a particular moment that day, so v2 approximates the snapshot
with **that day's open price**, labelled as such in the summary. The consequence — a live
judgment includes intraday information while a backtest judgment only reaches the open — is a
known comparability gap between live and backtest, and is on the backtest branch's agenda.

## 4. Governance: handling the version bump

- The input format is part of the system under test, so changing the input changes the system
  → `PROTOCOL_VERSION` becomes `v2-2026-07-19`
- The two 2026-07-19 records (BTC and ETH) are v1 samples, distinguishable by the
  `protocol_version` column, and the primary analysis filters by version
- Timing: at n = 1 day, this is the cheapest possible moment to upgrade. The pre-registered
  hit definition, aggregation rule, instruments and personas are all untouched, so it is
  recorded as an append-only §8 amendment
