# Data Dictionary — Retention & Attrition Intelligence

| Table | Field | Type | Description |
|---|---|---|---|
| dim_customer | customer_id | string | Synthetic customer key |
| dim_customer | customer_name | string | Fictional customer name |
| dim_customer | region | string | Reporting region |
| dim_product | product_id | string | Product / suite key |
| fact_contracts | contract_id | string | Contract key |
| fact_contracts | customer_id | string | Customer foreign key |
| fact_contracts | product_id | string | Product foreign key |
| fact_contracts | start_date | date | Contract start |
| fact_contracts | end_date | date | Contract end |
| fact_contracts | starting_acv | decimal | Starting recurring value |
| fact_renewals | renewal_id | string | Renewal event key |
| fact_renewals | contract_id | string | Contract foreign key |
| fact_renewals | renewal_date | date | Renewal date |
| fact_renewals | renewal_acv | decimal | Renewed recurring value |
| fact_movements | movement_type | string | renewal / churn / contraction / expansion / flat |
| fact_movements | movement_value | decimal | Revenue movement amount |
| fact_movements | period | date | Reporting period |
| scoring | component | string | Metric included in health score |
| scoring | weight | decimal | Component weight |
| scoring | score | decimal | Calculated component score |
| scoring | grade | string | A–F management grade |

All public examples are synthetic.