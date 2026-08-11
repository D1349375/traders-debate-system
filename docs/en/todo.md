# TODO / Roadmap

> English version of [`docs/zh/todo.md`](../zh/todo.md).

> Project overview, debate protocol and progress snapshot live in the
> [README](../../README.md); this list is kept in sync with it.

## Done

- [x] README as the master document (2026-07-19): project plan, distillation process, debate
      protocol (fixed two rounds, judge remit boundaries, R1 bypass aggregation, R2 structured
      rebuttal plus falsifier), progress snapshot
- [x] Nuwa skill installed at project level (`.claude/skills/huashu-nuwa`)
- [x] Full ICT persona distillation (phases 0.5 → 1 → 1.5 → 2 → 2.5 → 3 → 4 → 5), producing
      `.claude/skills/ict-perspective/SKILL.md`, with register and framework both verified by
      chat plus real-chart testing
- [x] Phase 4 backtest system plan, adapting the `quant-strategy-dev` skill methodology
- [x] Phase 4 document aligned to skill v13 (2026-07-19): pre-registered hit definition, 1d
      primary horizon, block bootstrap for overlapping windows, mandatory metrics table script,
      BH-FDR
- [x] `database/schema.py` extended with outcome columns and a `backtest_runs` table
      (2026-07-19; `is_correct` is deliberately not stored, being computed at the analysis layer
      from the pre-registered hit definition)
- [x] Architecture implementation (2026-07-19): `main.py` CLI, `database/db.py` persistence,
      `engine/aggregate.py` mechanical aggregation, trader-debate orchestrator skill; 25 pytest
      passing; the old Gemini engine archived as `engine/legacy_gemini_runner.py`
- [x] Corpus leakage approach settled (2026-07-19): wait for new data — accumulate forward
      daily, never backtest the corpus-covered period
- [x] Pre-registration in force (2026-07-19): both instruments, BTC ±0.5% / ETH ±1.0%, 1d
      primary horizon, n ≥ 30/60 per instrument, mandatory threshold sensitivity appendix
- [x] Daily accumulation started: first records 2026-07-19 (one each for BTC and ETH, ICT R1)
- [x] `snapshot_captured_at` added to schema (2026-07-20) for `market_data` and
      `daily_bias_results`; backtest mode uses the as-of day's 00:00 UTC reference, live mode
      the real fetch time. Existing three records migrated by `ALTER TABLE` (old rows NULL,
      honestly reflecting that it was not recorded at the time); 36 pytest passing
- [x] Three personas in force (2026-07-20): ICT + TJR + EmperorBTC
- [x] Execution timing discipline settled: UTC 00:00–01:00, missed windows run as soon as
      possible the same day rather than skipped, with the real deadline at 00:00 UTC the next
      day
- [x] Required field `intraday_scenario` (2026-07-20): mandatory in R1 and R2, a two-branch
      if-then scenario scoped to before today's close, correcting the horizon mismatch seen in
      dry runs; 37 pytest passing
- [x] Summary v3 (2026-07-20): added 1H (48) / 15M (96) / 5M (48, four hours) intraday
      timeframes to support `intraday_scenario`; candles 184 → 370, summary 12.2KB → 24.2KB,
      with all six timeframes verified strictly walk-forward in backtest mode
- [x] **First formal three-persona samples (2026-07-20):** BTC (Bearish 76, divergence 33%)
      and ETH (Bearish 100, divergence 0%) — the first formal application of the v3 summary,
      `intraday_scenario`, and the data-use boundary rules
- [x] ICT/TJR data-use boundary added (2026-07-20): volume prohibited as a basis for judgment,
      after tracing dry-run phrases like "on volume" to harmless narrative description
- [x] **Summary v4: genuine information routing (2026-07-21).** Split into `core` (shared by
      ICT/TJR) and `emperorbtc` variants, replacing the earlier "visible but forbidden"
      approach; `main.py market` gained `--variant`, schema gained `context_summary_emperorbtc`
- [x] **Automatic schema migration (2026-07-21).** `get_session()` gained `_sync_schema()`,
      diffing existing columns against `schema.py` on each call and issuing `ALTER TABLE ADD
      COLUMN` as needed; 54 pytest passing
- [x] **Summary v5 (2026-07-22):** macro calendar flags in all three variants (NFP week by
      rule, 2026 FOMC weeks verified from federalreserve.gov); new `tjr` variant adding
      correlated-asset (BTC↔ETH) daily/4H/1H/15M reference candles; ICT confidence table fixed
      so the seasonality judgment keys off the macro calendar flags
- [x] **Outcome horizon off-by-one fix (2026-07-22).** `fill_outcomes()` had the 1d/5d/20d
      target date one day late; industry methodology confirms close-to-close as standard for
      direction accuracy metrics
- [x] **Range and premium/discount table added to the daily report (2026-07-22)** in both
      report templates, for the user's own subjective review
- [x] **Summary v6: required `trade_plan` field (2026-07-23).** Mandatory in R1 and R2, with
      "no trade right now" an explicitly valid answer so no fake signal is manufactured;
      `protocol_version` bumped to `v6-2026-07-23`

## Open

- [ ] **Implement `bias_report_metrics.py` before n ≥ 30**: direction hit rate, Brier score and
      calibration curve, MCPT, and the neutral threshold sensitivity appendix, with mandatory
      tables and charts plus pytest. **Must include a per-persona hit-rate comparison** (ICT,
      TJR and EmperorBTC individually versus the post-debate aggregate — the ensemble lift
      question). `persona_debates` already records per persona per round, so no new data
      collection is needed. **But comparing 3 personas plus 1 aggregate is a 4-way comparison,
      so BH-FDR correction is mandatory before concluding who is more accurate — picking the
      single best-performing persona and concluding from that is not permitted.**
- [ ] **Consider adding DXY data for EmperorBTC.** His SKILL.md Step 2 dimension 4 explicitly
      judges BTC/ETH direction using DXY direction (weakness favouring risk assets), making it
      a genuine macro dependency of his framework.
- [ ] **Manually update `_FOMC_MEETINGS_2026` before end of 2026** — the FOMC logic in
      `data/ingestion.py` needs 2027 meeting dates added by hand.

## Open-source roadmap

- [ ] Package the multi-agent debate flow as a standardized skill / agent protocol
      (`/debate-consensus`)
- [ ] Build a web dashboard (`DebateSystem-Web`) so others can view Brier score calibration
      charts and historical debate records
- [ ] Evaluate a news-flow subagent: how to bring real-time news in as an independent agent's
      input dimension. Explicitly optional, with hidden costs, and deliberately not bundled
      into any current change
- [ ] Publish an open benchmark dataset: once ≥ 100 debate records accumulate, release the
      dataset for evaluation research
