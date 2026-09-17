# Retention & Attrition Intelligence

An enterprise retention and recurring-revenue health reference for logo attrition, revenue attrition, GRR, NRR, contraction, expansion, health scoring, and executive decision support.

> **Working public demo:** Includes deterministic synthetic recurring-revenue data, executable GRR/NRR and attrition logic, an interactive Streamlit app, automated tests, and run instructions. See [`DEMO.md`](DEMO.md).

> **Portfolio note:** All customer names, financial values, identifiers, and scenarios used publicly are synthetic or generalized.

## Try It

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Business Problem

Recurring-revenue businesses need more than a churn percentage. Finance and management teams need to understand where revenue is being lost, whether expansion offsets attrition, which customer segments are weakening, and how overall portfolio health is changing.

## Demo Capabilities

- 600-customer synthetic recurring-revenue portfolio
- full renewal / expansion / contraction / churn movements
- GRR
- NRR
- logo attrition
- revenue attrition
- expansion and contraction analysis
- region and product filtering
- weighted portfolio health score
- A–F health grade
- retention movement bridge

## Reference Architecture

```text
CRM / Contracts / Renewal Schedule
               |
               v
      Recurring Revenue Snapshot
               |
               v
       Movement Classification
      /      |       |        \
 Renewal  Churn  Contraction Expansion
      \      |       |        /
               v
        Retention Engine
               |
       GRR / NRR / Attrition
               |
        Health Scoring Layer
               |
 Customer / Region / Product Views
```

## Technology

`Power BI` `DAX` `Snowflake` `SQL` `Python` `Streamlit` `Pandas` `Plotly` `FP&A` `Revenue Analytics` `Customer Retention`

## Repository Structure

```text
.
├── app.py
├── core.py
├── synthetic.py
├── requirements.txt
├── DEMO.md
├── docs/
│   ├── case-study.md
│   ├── architecture.md
│   ├── retention-methodology.md
│   ├── metric-definitions.md
│   ├── business-rules.md
│   ├── data-dictionary.md
│   ├── security.md
│   └── runbook.md
└── tests/
    └── test_core.py
```

## Demo Status

- [x] Public-safe project definition
- [x] Synthetic customer / renewal portfolio
- [x] Movement classification
- [x] GRR / NRR / attrition metric engine
- [x] Health score methodology
- [x] Interactive dashboard demo
- [x] Automated tests
- [ ] Hosted live-demo URL
- [ ] Sanitized Power BI screenshot gallery
- [ ] Recorded walkthrough

## Decision-Support Focus

The goal is to move from descriptive churn reporting to a repeatable retention framework that explains the drivers of revenue health and gives management a consistent way to compare risk across customers, products, regions, and periods.
