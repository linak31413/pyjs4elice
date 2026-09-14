from src.loader import load_cases
from src.validators import validate_response
from src.reporter import save_report, save_failed_cases_csv, summarize_results

# 1. 테스트 케이스 로드 (10건 기준)
cases = load_cases()
results = []

# 2. 실행 및 결과 수집
for tc in cases:
    errors = validate_response(tc["actual"])
    status = "PASS" if not errors else "FAIL"
    results.append({
        "tc_id": tc["tc_id"],
        "status": status,
        "reason": errors,
        "evidence": f"logs/{tc['tc_id']}.log" # 재현을 위한 evidence 경로 추가
    })

# 3. 과제 1: 결과 JSON 저장
save_report(results, "artifacts/results.json")

# 4. 과제 3: FAIL 건수 CSV 저장
save_failed_cases_csv(results, "artifacts/failed_cases.csv")

# 5. 과제 2: reason 집계 및 결과 출력
summary = summarize_results(results)
print("=== 테스트 실행 결과 요약 ===")
print(f"전체 TC: {summary['total']}건 | 성공: {summary['passed']}건 | 실패: {summary['failed']}건")
print("\n=== 실패 사유(Reason)별 집계 ===")
for reason, count in summary["reason_summary"].items():
    print(f"- {reason}: {count}건")