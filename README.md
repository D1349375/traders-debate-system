# Multi-Agent Consensus & Persona Distillation Framework (`traders-debate-system`)

> An open-source research framework designed to distill domain-expert decision heuristics into executable LLM persona skills, orchestrate blind multi-agent debate protocols, and statistically calibrate consensus predictions using Brier Scores.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Test Suite](https://img.shields.io/badge/tests-65%20passed-brightgreen.svg)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview

Traditional decision-making heuristics expressed in raw video or text transcripts are often unquantifiable. This framework establishes an end-to-end pipeline to:

1. **Distill**: Extract core mental models, decision heuristics, and communication styles from raw transcript data into structured, executable `SKILL.md` persona files using LLM agents (Nuwa Distillation Protocol).
2. **Debate**: Orchestrate parallel LLM subagents (e.g., ICT, TJR, EmperorBTC personas) to perform blind evaluations on market context snapshots, followed by a structured two-round debate to synthesize daily consensus bias.
3. **Verify**: Persist all judgments and trade plans into an SQLite database, aligning predictions against actual price action using Brier Score calibration, calibration curves, and Monte Carlo Permutation Tests (MCPT).

---

## 🏗️ Architecture & Workflow

```mermaid
graph TD
    A[Raw Video/Text Transcripts] -->|Nuwa Distillation| B[Structured Persona SKILL.md]
    C[Daily Market Context Snapshot] -->|Isolated Context| D[Master Orchestrator Agent]
    D -->|Parallel Dispatch| E[Blind Persona Evaluation (R1)]
    E -->|Structured Arguments| F[Two-Round Debate Protocol (R2)]
    F -->|Consensus Aggregation| G[Trade Plan & Daily Bias Output]
    G -->|SQLite Persistence| H[Brier Score Calibration Engine]
    H -->|Outcome Verification| I[Statistical Benchmark Reports]
```

---

## ✨ Key Features

- **Persona Skill Distillation**: Automated extraction of mental models from 500+ transcripts with multi-layer verification (cross-scenario consistency, predictive power, and exclusion checks).
- **Blind Evaluation & Context Isolation**: Prevents anchoring bias by forcing agents to render initial judgments independently before entering the debate round.
- **Strict Protocol Governance**: Version-controlled debate protocols (`PROTOCOL_VERSION`) ensuring deterministic audit trails and regression safety.
- **Statistical Calibration Engine**: Implements Brier Score metrics, probability calibration curves, and non-parametric permutation testing to verify true predictive edge.

---

## 📁 Repository Structure

```
.
├── engine/              # Core multi-agent debate & stance evaluation engine
├── database/            # SQLite persistence, schema migrations, and outcome matching
├── tests/               # PyTest regression and protocol verification test suite (65+ tests)
├── preregistration.md   # Formal scientific research pre-registration & protocol spec
├── main.py              # CLI entry point for orchestration and reports
├── requirements.txt     # Python dependency specifications
└── LICENSE              # MIT License
```

---

## 🧪 Testing & Verification

Run the full automated test suite covering memory isolation, protocol validation, and score calibration:

```bash
# Install dependencies
pip install -r requirements.txt

# Run unit and integration tests
pytest tests/
```

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
