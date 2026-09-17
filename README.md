# Retention & Attrition Intelligence

An enterprise retention and recurring-revenue health platform for logo attrition, revenue attrition, GRR, NRR, contraction, expansion, GACV movement, health scoring, and executive commentary.

> **Portfolio note:** This public repository is a sanitized reference implementation. All customer names, financial values, identifiers, and scenarios used publicly are synthetic or generalized.

## Business Problem

Recurring-revenue businesses need more than a churn percentage. Finance and management teams need to understand where revenue is being lost, whether expansion offsets attrition, which customer segments are weakening, and how overall portfolio health is changing over time.

This project demonstrates a governed retention framework that converts recurring-revenue movements into a decision-support system for FP&A and leadership.

## Core Capabilities

- logo attrition rate
- revenue attrition rate
- gross revenue retention (GRR)
- net revenue retention (NRR)
- gross / net attrition
- lost revenue
- contraction revenue
- expansion revenue
- GACV loss and growth analysis
- expansion and growth coverage ratios
- customer / product / region segmentation
- weighted health scoring
- A–F health grades
- executive commentary

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
               |
       Executive Commentary
```

## Technology

`Power BI` `DAX` `Snowflake` `SQL` `FP&A` `Revenue Analytics` `Customer Retention`

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── case-study.md
│   ├── architecture.md
│   ├── retention-methodology.md
│   ├── metric-definitions.md
│   ├── business-rules.md
│   ├── data-dictionary.md
│   ├── security.md
│   └── runbook.md
├── sample-data/
├── dax/
├── sql/
├── diagrams/
├── screenshots/
└── tests/
```

## Portfolio Roadmap

- [x] Public-safe project definition
- [ ] Synthetic customer / contract / renewal dataset
- [ ] Movement-classification examples
- [ ] GRR / NRR / attrition metric library
- [ ] Health score methodology
- [ ] Architecture diagram
- [ ] Sanitized dashboard screenshots
- [ ] Demo walkthrough

## Decision-Support Focus

The goal is to move from descriptive churn reporting to a forward-looking retention framework that explains the drivers of revenue health and provides management with a consistent way to compare risk across customers, products, regions, and periods.