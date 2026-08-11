# Documentation

Every document exists in Traditional Chinese under `zh/`. English versions live under `en/`,
and the table below marks which are available — the rest are in progress. Where both exist,
the Chinese original remains authoritative: the project is operated in Chinese and the
personas reason in it.

## Start here

| Document | English | Why it matters |
|---|---|---|
| **Pre-registration** | [**en**](en/preregistration.md) · [zh](zh/preregistration.md) | The locked hit definition, thresholds, aggregation rule and pass criteria, plus every dated amendment since. This is what constrains the project's claims — read it before anything else |

## Design and methodology

| Document | English | What it covers |
|---|---|---|
| Evaluation framework analysis | [zh](zh/evaluation-framework-analysis.md) — English pending | How to tell whether a persona debate system predicts anything: hit rate, Brier score, calibration, ensemble lift, and what each cannot show |
| Phase 4 backtest system plan | [zh](zh/phase4-backtest-system-plan.md) — English pending | The statistical design for scoring accumulated records — MCPT, bootstrap intervals, walk-forward embargo, drift detection |
| Three-persona trade-offs | [**en**](en/three-persona-tradeoffs.md) · [zh](zh/three-persona-tradeoffs.md) | Why three personas rather than one or five, and the structural bias introduced by two of them sharing a school |
| Backtest contamination and dual memory | [**en**](en/backtest-contamination-dual-memory.md) · [zh](zh/backtest-contamination-dual-memory.md) | How replaying history to an agent that has read that history leaks, and what the frozen-snapshot design does about it |
| Market summary v2 information set | [**en**](en/market-summary-v2-information-set.md) · [zh](zh/market-summary-v2-information-set.md) | What each persona is allowed to see, and the reasoning behind the information-isolation design |
| Market summary protocol history | [**en**](en/market-summary-protocol-history.md) · [zh](zh/market-summary-protocol-history.md) | v1 through v6 of the information set, and what changed at each step |
| Scenario integration study | [zh](zh/scenario-integration-study.md) — English pending | Comparison of two candidate designs for combining daily-bias and intraday-scenario outputs |
| WBS and technical architecture | [zh](zh/wbs-technical-architecture.md) — English pending | Component breakdown and build sequence |
| YouTube scraper guide | [**en**](en/youtube-scraper-guide.md) · [zh](zh/youtube-scraper-guide.md) | Rebuilding the transcript corpus locally — the transcripts are not redistributed here |
| TODO | [**en**](en/todo.md) · [zh](zh/todo.md) | Open work, with the reasoning for what has deliberately not been built |
