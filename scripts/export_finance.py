PROJECT_NAME = "Project Aurora"
EXPORT_FILES = [
    "payments_Q2_2026.csv",
    "supplier_summary_Q2_2026.csv",
    "invoice_register_Q2_2026.xlsx",
]

def build_export_manifest():
    return {
        "project": PROJECT_NAME,
        "destination": "companyx-training-finance",
        "files": EXPORT_FILES,
    }

if __name__ == "__main__":
    print(build_export_manifest())
