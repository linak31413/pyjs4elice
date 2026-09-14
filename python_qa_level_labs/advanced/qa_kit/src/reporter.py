import csv
import json
from collections import Counter
from pathlib import Path

def save_report(results, path="artifacts/results.json"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

def save_failed_cases_csv(results, path="artifacts/failed_cases.csv"):
    """과제 3: FAIL만 failed_cases.csv로 별도 추출"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    failed_cases = [r for r in results if r.get("status") == "FAIL"]
    
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["tc_id", "status", "reason", "evidence"])
        for case in failed_cases:
            # reason 리스트를 세미콜론 구분자로 연결
            reasons_str = "; ".join(case.get("reason", []))
            evidence = case.get("evidence", f"logs/{case['tc_id']}.log")
            writer.writerow([case["tc_id"], case["status"], reasons_str, evidence])

def summarize_results(results):
    """과제 2: reason별 실패 건수 집계 및 콘솔 요약"""
    total = len(results)
    passed = sum(1 for r in results if r.get("status") == "PASS")
    failed = sum(1 for r in results if r.get("status") == "FAIL")
    
    # 실패 케이스의 사유(reason) 집계
    fail_reasons = []
    for r in results:
        if r.get("status") == "FAIL":
            fail_reasons.extend(r.get("reason", []))
            
    reason_counts = Counter(fail_reasons)
    
    summary = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "reason_summary": dict(reason_counts)
    }
    return summary