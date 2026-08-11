# Documentation

Every document exists in both languages. The **English version under `en/` is the one to
read**; `zh/` holds the Traditional Chinese originals, which remain authoritative where the
two differ — the project is operated in Chinese, and the personas reason in it.

## Start here

| Document | Why it matters |
|---|---|
| [**Pre-registration**](en/preregistration.md) | The locked hit definition, thresholds, aggregation rule and pass criteria, plus every dated amendment since. This is what constrains the project's claims — read it before anything else |

## Design and methodology

| Document | What it covers |
|---|---|
| [Evaluation framework analysis](en/evaluation-framework-analysis.md) | How to tell whether a persona debate system predicts anything: hit rate, Brier score, calibration, ensemble lift, and what each cannot show |
| [Phase 4 backtest system plan](en/phase4-backtest-system-plan.md) | The statistical design for scoring accumulated records — MCPT, bootstrap intervals, walk-forward embargo, drift detection |
| [Three-persona trade-offs](en/three-persona-tradeoffs.md) | Why three personas rather than one or five, and the structural bias introduced by two of them sharing a school |
| [Backtest contamination and dual memory](en/backtest-contamination-dual-memory.md) | How replaying history to an agent that has read that history leaks, and what the frozen-snapshot design does about it |
| [Market summary v2 information set](en/market-summary-v2-information-set.md) | What each persona is allowed to see, and the reasoning behind the information-isolation design |
| [Market summary protocol history](en/market-summary-protocol-history.md) | v1 through v6 of the information set, and what changed at each step |
| [Scenario integration study](en/scenario-integration-study.md) | Comparison of two candidate designs for combining daily-bias and intraday-scenario outputs |
| [WBS and technical architecture](en/wbs-technical-architecture.md) | Component breakdown and build sequence |
| [YouTube scraper guide](en/youtube-scraper-guide.md) | Rebuilding the transcript corpus locally — the transcripts are not redistributed here |
| [TODO](en/todo.md) | Open work, with the reasoning for what has deliberately not been built |
