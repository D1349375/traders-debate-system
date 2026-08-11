# Dual-Layer Memory Contamination in LLM Persona Backtesting

> English version of [`docs/zh/backtest-contamination-dual-memory.md`](../zh/backtest-contamination-dual-memory.md).

> Written 2026-07-19. This report answers one question: **can a trader-persona debate system
> be backtested against past market data?** The answer up front: the usable window is
> determined by the *model's* knowledge cutoff, not by whether the ICT corpus happens to
> discuss crypto. Related: [Phase 4 plan](phase4-backtest-system-plan.md) §2.4 and
> [pre-registration](preregistration.md) §6.

---

## 1. Why an LLM persona cannot be backtested like a mechanical strategy

A mechanical strategy is a set of mathematical rules, and rules have no memory. Feed them
2023 data and they can only honestly compute what the rules say, so a historical backtest
genuinely measures the rules' predictive power. What remains is overfitting, and there are
tools for that (DSR, PBO, MCPT).

An LLM persona is **a judge with a memory.** Show it a 2023 chart and ask for a direction,
and its output may come from either of two indistinguishable sources:

1. Reasoning through the distilled mental framework (what we want to measure)
2. Recalling from training memory what actually happened next (contamination)

**The two are completely indistinguishable in the output** — both produce a plausible piece
of analysis and a direction. This is the LLM form of look-ahead bias, and it is more insidious
than numerical data leakage: numerical leakage can be excluded mechanically by cutting on
time, whereas memory leakage is hidden in the weights.

---

## 2. Layer one: the persona corpus's memory (auditable)

### 2.1 Cause

The ICT persona is distilled from 537 YouTube teaching transcripts. Those transcripts do not
only teach method — they also contain ICT's commentary on **the actual market at the time.**
If a backtest date falls inside the corpus coverage, the persona's judgment may indirectly
draw on the corpus's description of that period's price action.

### 2.2 Inventory (2026-07-19 reconnaissance, first-hand evidence)

- Total corpus: 538 transcript files
- Most recent: **2026-07-14** (five days prior) — coverage runs right up to the present
- 2026 videos: **23**. Title sampling shows the overwhelming majority are **NQ futures**
  commentary, not crypto
- 2025 videos: 65

### 2.3 Why this layer is auditable

This memory is **explicit, finite and enumerable** — 537 text files sitting on disk. The
audit:

1. Scan the full text of the 23 transcripts falling inside the backtest window (2026)
2. Check for specific mentions of BTC/ETH/bitcoin/ethereum price levels, directions or dates
3. Remove the corresponding dates from the backtest window and record the exclusion list in
   the report

ICT's home market is NQ/ES index futures, so specific BTC/ETH commentary is expected to be
rare — **the audit will probably pass.** But its limits must be recorded honestly:

- "The audit found no mention" ≠ "zero leakage". It only reduces the risk to something
  statable.
- Indirect leakage remains possible: ICT commenting on NQ in a risk-on/risk-off context
  indirectly reveals the market state of the same period, and BTC's correlation with NQ is not
  low. This is a residual risk the report must disclose.

---

## 3. Layer two: the base model's weight memory (uncleanable)

### 3.1 Cause — the persona is a mask, and the brain behind it has seen all of history

What runs the persona is not ICT; it is Claude (or any base LLM). The model's training data
runs to its knowledge cutoff (current engine: January 2026) and includes **the entire public
history of the crypto market**: every major candle, every crash, every news article, every
panic and mania thread.

Therefore "ICT never discussed BTC" **does not imply** "the persona has no memory of BTC". The
persona prompt is a behavioural constraint (a mask), not memory isolation (a lobotomy). Ask
the ICT persona to judge BTC on 2025-08-15 and the brain behind the mask may simply remember
how that week resolved — and it needs no *intent* to cheat, because memory retrieval and
framework reasoning are entangled during generation.

### 3.2 Why it cannot be cleaned

- The memory lives in **weights**, not in data. Corpus files can be deleted; weights cannot be
  selectively erased (no reliable machine unlearning exists for this scenario).
- **Nor can its absence be verified.** You can probe — blind-ask the model "what was BTC's
  price on 2025-08-15, and did it rise or fall that week?" — but a probe's evidential power is
  **one-directional**:
  - It answers correctly → contamination is proven ✔
  - It fails to answer → this does **not** prove the judgment is free of implicit memory
    influence ✘ (failed explicit recall ≠ absent implicit influence; the model may be unable to
    state the price while still leaning toward what actually happened)
- Statistically this is an **unprovable negative**. A pre-registration worldview has only one
  honest response: **assume contamination is present.**

### 3.3 Conclusion: the backtest boundary is set by the model cutoff

The usable boundary for broad backtesting is not "did ICT ever discuss crypto" (layer-one
logic) but **the base model's knowledge cutoff** (layer-two logic). Layer one can be audited;
layer two can only be routed around — and the only route around it is to use dates the model
is *physically incapable* of remembering: after the training cutoff.

---

## 4. Three zones on the timeline

```
──────────────┬──────────────────────┬─────────────┬──────→
   before 2026-01     2026-02 to 07-14      after 07-14
   model memory zone    semi-clean zone      truly clean zone
   (permanently         (explorable after    (forward accumulation,
    abandoned)           audit)               the main line)
```

| Zone | Contamination | Usability |
|---|---|---|
| **Before 2026-01** | Layer two (model memory) — uncleanable, negative unprovable | **Permanently abandoned.** No sample size redeems it: it measures whether the model remembers price history, not whether the framework predicts, and the contamination magnitude cannot be quantified — so not even a "discount the result" reading is available |
| **2026-02 to 07-14** (≈164 trading days) | Layer two physically impossible (past the training cutoff); only layer one remains, and it is auditable | **An exploratory branch**, subject to the four preconditions in §5 |
| **After 2026-07-14** | Neither layer | **The main line:** daily forward accumulation, the only formal evidence source under the active pre-registration |

---

## 5. Four preconditions for exploratory backtesting in the semi-clean zone

1. **Corpus audit first.** Scan the 23 transcripts from 2026 and exclude dates with specific
   BTC/ETH price, direction or date mentions. If the audit fails (extensive mentions), abandon
   the whole branch.
2. **Backtest subagents get no tools at all.** Whether a subagent can browse in live mode is
   irrelevant (the future is unknown to everyone). In backtest mode, a subagent with WebSearch
   can simply look up what happened next. Backtest prompts must be pure text, zero tools.
3. **A separate exploratory pre-registration.** Window, metrics and audit procedure fixed
   before running; results land in the `backtest_runs` table, **permanently marked exploratory
   and never merged into the main sample.** Only the main line — forward accumulation — is
   entitled to claim the system works.
4. **Lock the model ID.** One model throughout, with `model_id` persisted.

### Shelf-life warning

This window depends on the fact that the current engine's cutoff is 2026-01. **Once Claude
Code upgrades to a model with a later cutoff, the window shrinks or disappears** — the
semi-clean zone is a wasting asset, so it must be used early if at all. Conversely, once a
model upgrade lands, exploratory backtests already run may not be "topped up" or rerun on the
new model, which would change the window's nature entirely.

---

## 6. Cost and feasibility (estimated 2026-07-19)

- Single persona, R1 only: one subagent per judgment, input ≈ 15k tokens (ICT SKILL.md 27KB ≈
  12k, plus summary and instructions), output ≈ 500
- Full window: 164 days × 2 instruments = **328 calls ≈ 5M input tokens**
- Roughly $15–20 at API pricing (a few dollars with prompt cache hits). Under a Claude Code
  subscription **this will not finish in a single session** and needs 4–5 batches.
- "Won't finish" is not a risk: the persistence layer is write-once-final with a unique
  constraint, so resumption is natural — fill in whichever days are missing.
- **Suggested order:** audit script → exploratory pre-registration → historical summary
  generator (current ingestion only fetches the last two days and needs a small change) →
  **a 30-day pilot** (60 records, to measure real cost and check for any signal) → run the rest
  in batches only if a signal appears.

### Side benefit

Exploratory backtest samples feed directly into the **neutral threshold sensitivity analysis**
in [pre-registration](preregistration.md) §5, giving any future threshold revision an evidence
base without waiting for the main line to accumulate slowly.

---

## 7. In one sentence

**A mechanical strategy's backtest boundary is set by where you cut the data; an LLM persona's
is set by memory — corpus memory can be audited, weight memory can only be avoided, so the
usable window is dates after the model's knowledge cutoff that also pass the corpus audit.**
