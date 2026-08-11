"""Public reporting configuration for Company X."""

PUBLIC_SITE = "https://companyx-reporting-portal.example"
REPORT_BUCKET = "companyx-training-finance"
REPORT_BASE_URL = "https://companyx-training-finance.s3.amazonaws.com/"
REPORT_PREFIX = "exports/2026/Q2/"

def report_root() -> str:
    return f"{REPORT_BASE_URL}{REPORT_PREFIX}"
