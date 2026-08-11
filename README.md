# traders-debate-system

**Can a panel of AI personas distilled from trading educators predict tomorrow's direction better than chance? This repository is the apparatus built to find out — and to make the answer falsifiable.**

[![tests](https://github.com/D1349375/traders-debate-system/actions/workflows/tests.yml/badge.svg)](https://github.com/D1349375/traders-debate-system/actions/workflows/tests.yml)
[![python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![license](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

Three personas — distilled from the public teaching of ICT, TJR and EmperorBTC — each
receive a frozen market snapshot, commit to a direction and a confidence score without
seeing each other's answers, then critique each other in a structured second round. The
aggregated verdict is written to SQLite and scored against what the market actually did.

The interesting part is not the debate. It is the
[**pre-registration**](docs/en/preregistration.md): the hit definition, the neutral
threshold, the aggregation rule, the sample thresholds and the pass criteria were all
written down and locked *before* results accumulated. It is append-only. Amendments are
dated and never overwrite earlier text, and any change to the hit definition restarts the
sample count from zero.

---

## Current status, stated plainly

**No effectiveness claim is being made, because the sample is nowhere near large enough to
support one.**

The pre-registration requires n ≥ 30 per asset before even a descriptive report, and n ≥ 60
before any statistical test. As of the last committed daily run, roughly a week of records
exist. Everything in `data/reports/` is a daily log, not evidence.

That gap is the point of publishing the apparatus first. A framework whose pass criteria are
fixed in advance can be wrong in public; one where the threshold is chosen after seeing the
data cannot.

**This is a research instrument. It does not place orders, and nothing it produces is
investment advice.**

## Quick start

```bash
git clone https://github.com/D1349375/traders-debate-system.git
cd traders-debate-system
pip install -r requirements.txt
python -m pytest tests/ -v
```

65 tests covering aggregation, database integrity and the market-summary ingestion pipeline.

Fetch and freeze a market snapshot:

```bash
python main.py market --asset BTC/USDT --variant core
```

The four subcommands map onto the daily cycle:

| Command | What it does |
|---|---|
| `market` | Fetch OHLCV via ccxt and write the frozen context summary to the database. `--variant core\|tjr\|emperorbtc` selects which information set to build; `--as-of` reconstructs a historical snapshot under strict walk-forward |
| `record` | Persist one persona's R1 or R2 opinion from a JSON file. Rejects records missing `intraday_scenario` or `trade_plan` |
| `finalize` | Confidence-weighted aggregation into the day's final bias |
| `outcomes` | Backfill realized prices at the 1d / 5d / 20d horizons |

Running the personas themselves requires an agent runtime that loads skills from
`.claude/skills/`; the orchestration protocol lives in
`.claude/skills/trader-debate/SKILL.md`.

## How the design defends against the obvious objections

| Objection | What the design does about it |
|---|---|
| "The personas just agree with each other" | Round 1 is blind — each persona is a separate subagent with no visibility into the others. R1 aggregation is stored *alongside* the final aggregation, so the ablation question "did the debate round add anything?" is answerable from the data rather than asserted |
| "You picked the threshold that made the numbers look good" | The neutral threshold (±0.5% BTC, ±1.0% ETH) is locked in the pre-registration. Every report ships a sensitivity appendix across other thresholds, explicitly marked exploratory — adopting one means voiding the registration and restarting the sample |
| "The model already saw this price history" | Records run forward from the registration date, which post-dates every persona's corpus cutoff. The covered period is never backtested |
| "Running it later in the day makes it easier" | Execution is fixed to the UTC 00:00–01:00 window, and `snapshot_captured_at` records the real time for audit. A missed window cannot be backfilled with the historical reconstruction mode |
| "The three personas share one underlying model, so their disagreement is noise" | Acknowledged, unresolved, and [written into the record](docs/en/preregistration.md) rather than hidden. An informal divergence monitor exists but is explicitly barred from being cited as evidence. A methodological commitment is locked in advance: any move to an information-asymmetry architecture requires a comparable baseline period first |
| "ICT and TJR come from the same school, so the vote is structurally biased" | Registered as a known residual risk. Both belong to the SMC/liquidity family, so confidence-weighted majority voting leans that way by construction — which must be accounted for when interpreting ensemble lift, rather than read as a market signal |

Data isolation is enforced at the input level, not by instruction. ICT and TJR receive a
`core` snapshot whose OHLCV columns contain no volume field at all — not a rule telling them
not to look. EmperorBTC receives volume and RSI because his framework demands them. TJR
additionally receives the correlated asset's candles because his framework calls for SMT
divergence; ICT does not, because his corpus never mentions crypto-internal correlation and
supplying it would mean inventing a framework extension his source material never validated.

Derived indicators requiring a methodological choice — POC, value area, pre-computed swing
highs and lows — are deliberately **not** provided. Choosing the lookback window would mean
making the interpretive decision on the persona's behalf. Only raw candles go in.

## Repository layout

```
traders-debate-system/
├── main.py                  # CLI: market / record / finalize / outcomes
├── data/
│   ├── ingestion.py         # Market summary builder, per-variant, strict walk-forward
│   ├── fetch_transcripts.py # Rebuilds the corpus (transcripts are not redistributed)
│   ├── market_context/      # Frozen snapshots -- the audit trail behind each judgment
│   └── reports/             # Daily reports (markdown + html)
├── database/
│   ├── schema.py            # persona_debates, daily_bias_results, market_data
│   └── db.py                # record_opinion, fill_outcomes, upsert_market
├── engine/aggregate.py      # Confidence-weighted aggregation
├── tests/                   # 65 tests
├── docs/                    # Pre-registration and design documents (en + zh)
├── .claude/skills/          # Distilled personas + the debate orchestration protocol
└── .agents/skills/          # Vendored third-party tooling (see Attribution)
```

## Documentation

[**docs/**](docs/README.md) is the index. Everything exists in English (`docs/en/`) and
Traditional Chinese (`docs/zh/`), with the Chinese originals authoritative where they differ.

Start with the [pre-registration](docs/en/preregistration.md). If you only read one file in
this repository, read that one — it is where the project's claims are constrained.

## Attribution

**The persona distillation is performed by [Nuwa (女娲)](https://github.com/alchaincyf), an
independent open-source skill by Huashu (花叔), vendored at `.agents/skills/huashu-nuwa/`
under its own MIT license.** This project did not create it. What this repository
contributes is the debate protocol, the information-isolation design, the pre-registration,
and the scoring and audit pipeline built around the personas Nuwa produces.

The personas themselves are distilled from the public educational material of ICT, TJR,
EmperorBTC and RektCapital. They are interpretations built for research, are not endorsed by
or affiliated with those individuals, and should not be read as representing their actual
present views.

## Corpus

The raw YouTube transcripts behind the distillation (roughly 1,900 videos) are **not
included in this repository.** They are third-party copyrighted material and the MIT license
here does not extend to them.

`data/fetch_transcripts.py` and [the scraper guide](docs/en/youtube-scraper-guide.md) let you
rebuild the corpus locally. Corpus provenance — per-persona video counts and date coverage —
is recorded in the [pre-registration](docs/en/preregistration.md), so what the distillation
was built from remains auditable without redistributing it.

## License

MIT for the code and original documentation in this repository — see [LICENSE](LICENSE).

The MIT grant does **not** cover: the vendored Nuwa skill (MIT, but its own copyright — see
`.agents/skills/huashu-nuwa/LICENSE`), the source transcripts, or the market data retrieved
through ccxt.

## Disclaimer

Simulated and research output only. Nothing here is a trading record, a signal service, or
investment advice. Past or simulated performance does not indicate future results.
