from pathlib import Path
base = Path("data/logs")
fail_count = 0
for log_file in base.rglob("*.log"):
    text = log_file.read_text(encoding="utf-8")
    if "ERROR" in text or "FAIL" in text:
        fail_count += 1
        print("CHECK:", log_file.name)
print("문제 로그 수:", fail_count)
