import csv
from pathlib import Path
from src.validator import is_valid_status

path = Path("data/test_cases.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    for tc in csv.DictReader(f):
        passed = is_valid_status(int(tc["actual"]), int(tc["expected"]))
        print(tc["tc_id"], "PASS" if passed else "FAIL")
