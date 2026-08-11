PROJECT_NAME = "Project Aurora"
PROJECT_CODE = "AURORA"

EXPORT_BUCKET = "companyx-training-finance"
EXPORT_PATH = "exports/2026/Q2/"
CURRENT_EXPORT = "payments_Q2_2026.csv"

def build_export_manifest():
    return {
        "project": PROJECT_NAME,
        "code": PROJECT_CODE,
        "bucket": EXPORT_BUCKET,
        "path": EXPORT_PATH,
        "file": CURRENT_EXPORT,
    }

if __name__ == "__main__":
    print(build_export_manifest())
