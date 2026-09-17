# Architecture — Retention & Attrition Intelligence

## System Overview

```text
CRM / Contracts / Renewal Schedule / Revenue
                     |
                     v
          Recurring Revenue Baseline
                     |
                     v
          Movement Classification
       +------+------+------+------+
       |      |      |      |      |
     Renew  Churn  Contract Expand Flat
                    |
                    v
            Retention Engine
                    |
        GRR / NRR / Attrition
                    |
         GACV Movement Layer
                    |
        Health Scoring / Grades
                    |
 Customer / Product / Region Views
                    |
          Executive Commentary
```

## Components
### Baseline Layer
Defines the governed starting recurring-revenue population and period.

### Movement Classification
Assigns renewal outcomes into mutually understandable business movements such as full renewal, churn, contraction, expansion, and flat renewal.

### Metric Layer
Calculates logo attrition, revenue attrition, GRR, NRR, contraction, expansion, and GACV movement.

### Health Layer
Combines selected metrics into weighted health scores and letter grades for management interpretation.

### Reporting Layer
Provides customer-, region-, product-, and portfolio-level views with executive commentary.

## Design Principles
- one governed starting denominator
- movement categories remain mutually explainable
- GRR and NRR use documented formulas
- expansion does not mask gross retention loss
- health scoring is transparent and reproducible
- commentary must be grounded in calculated metrics
