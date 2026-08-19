# Paytm FinTech Analytics & AI Platform

A single capstone repository implementing the three required Paytm analytics, lending ML, and AI-advisory components.

## Structure
- `payments_fraud_analytics/` — payments/fraud analytics, SQL, reconciliation, Excel workbook, dashboard artifacts.
- `credit_risk_lending_ml/` — seeded lending dataset, preprocessing, classifiers, risk pricing, anomaly detection.
- `ai_advisory_blockchain/` — deterministic advisory agent, disclosure extraction, debate, DCF, blockchain/crypto risk appendix.

## Setup
Use Python 3.10+ and install the consolidated dependencies:

```bash
pip install -r requirements.txt
```

The required graded AI path uses `MOCK_LLM=1` (or leaves `MOCK_LLM` unset), so no API key is needed.

## Run
```bash
cd payments_fraud_analytics && python generate_data.py
cd ../credit_risk_lending_ml && python generate_data.py
cd ../ai_advisory_blockchain && python advisory_agent.py
python extract_disclosure.py
python debate.py
python dcf_calculator.py
```

See each part README for details. All monetary figures are INR and all seed-data generation follows the supplied specification.

## Design decisions
Part 1 uses a normalized SQLite schema, deterministic reconciliation via transaction IDs, and code-generated four-layer dashboard artifacts. Part 2 preserves thin-file applicants, performs training-only imputation/scaling, compares Logistic Regression with a Decision Tree, and uses Isolation Forest for seeded behavioural anomalies. Part 3 keeps the required Think–Act–Observe loop deterministic in mock mode, uses CAPM beta rather than the analyst reference return, applies the prescribed allocation lookup, and includes human escalation above 20% portfolio volatility.
