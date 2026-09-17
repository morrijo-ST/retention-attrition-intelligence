# Run the Public Demo

This repository includes a deterministic synthetic-data demo. No external credentials or proprietary datasets are required.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests with:

```bash
pytest -q
```

The demo creates a reproducible recurring-revenue customer portfolio and calculates GRR, NRR, logo attrition, revenue attrition, expansion, contraction, churn, and a portfolio health score/grade.
