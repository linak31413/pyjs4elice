from src.loader import load_cases
from src.runner import run_all
from src.reporter import save_report, save_failed_cases_csv, summarize_results

# 1. TC 로딩
cases = load_cases("data/cases.json")

# 2. 러너를 통한 일괄 실행
results = run_all(cases)

# 3. 결과 저장 및 리포팅
save_report(results, "artifacts/results.json")
save_failed_cases_csv(results, "artifacts/failed_cases.csv")

# 4. 요약 출력
summary = summarize_results(results)
print("=== Mini QA Framework 실행 완료 ===")
print(f"총 TC: {summary['total']} | 통과: {summary['passed']} | 실패: {summary['failed']}")