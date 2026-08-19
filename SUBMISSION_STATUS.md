# Capstone Submission Status

The repository implements the three-part Paytm FinTech Analytics & AI capstone described in the supplied brief.

## Validation run

The local implementation was executed end to end on 19 August 2026.

### Part 1 — Payments & Fraud Analytics
- Ledger: 547 rows
- Users: 365 rows
- Merchants: 40 rows
- Gateway export: 530 rows
- Reconciliation counts: 27 missing in gateway, 10 extra in gateway, 16 amount mismatches, 9 status mismatches
- Dashboard outputs generated: trends, GMV by payment method, GMV by category, top-10 merchant detail table

### Part 2 — Credit Risk & Lending ML
- Applicants: 400 rows
- Default rate: 20.25%
- Missing bureau score: 20.00% (80 applicants)
- Training-only bureau median: INR-equivalent score 612
- Logistic Regression: accuracy 0.76, precision 0.389, recall 0.35, F1 0.368, AUC 0.719
- Decision Tree: accuracy 0.67, precision 0.240, recall 0.30, F1 0.267, AUC 0.531
- Isolation Forest seeded-anomaly recall: 73.33%

### Part 3 — AI-Augmented Advisory & Blockchain Risk
- All 5 investor profiles executed.
- Conservative and Moderate profiles finalized; Aggressive profiles escalated because volatility exceeds 20%.
- All 6 disclosure snippets processed in deterministic mock mode.
- Bull/Bear/Synthesizer debate executed.
- DCF executed with a 3x3 WACC/terminal-growth sensitivity table and EV/EBITDA cross-check.
- Blockchain/crypto risk appendix included.

## Reproducibility

Run `python run_all.py` from the repository root. The required deterministic seed generators use seed 42, and Part 3 defaults to keyless deterministic mock mode as required by the brief.

## Artifact note

The source code and reproducibility workflow are committed to this repository. Generated spreadsheet/database/image artifacts are produced by the Part 1 scripts and are intentionally reproducible from source; no external Paytm data or paid API service is required.
