"""Run the complete Paytm FinTech Analytics & AI capstone locally.

The assignment uses synthetic data only. Run from the repository root:
    python run_all.py
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
STEPS = [
    (ROOT / "payments_fraud_analytics", "generate_data.py"),
    (ROOT / "payments_fraud_analytics", "reconcile.py"),
    (ROOT / "payments_fraud_analytics", "dashboard.py"),
    (ROOT / "credit_risk_lending_ml", "generate_data.py"),
    (ROOT / "credit_risk_lending_ml", "model.py"),
    (ROOT / "ai_advisory_blockchain", "advisory_agent.py"),
    (ROOT / "ai_advisory_blockchain", "extract_disclosure.py"),
    (ROOT / "ai_advisory_blockchain", "debate.py"),
    (ROOT / "ai_advisory_blockchain", "dcf_calculator.py"),
]

for cwd, script in STEPS:
    print(f"\n=== {cwd.name}/{script} ===")
    subprocess.run([sys.executable, script], cwd=cwd, check=True)

print("\nCapstone run completed successfully.")
