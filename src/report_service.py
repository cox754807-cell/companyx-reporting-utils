"""Public report location configuration for Company X."""
REPORT_BASE_URL = "https://companyx-training-finance.s3.amazonaws.com/reports/"
PUBLIC_REPORT_PREFIX = "quarterly/"
DEFAULT_REPORT = "Q2_2026_summary.pdf"

def report_url(filename: str) -> str:
    return f"{REPORT_BASE_URL}{PUBLIC_REPORT_PREFIX}{filename}"
