from pathlib import Path
from collections import Counter
from src.validators import validate_artifact

def run_batch_validation(target_dir="artifacts"):
    target_path = Path(target_dir)
    results = []
    
    # 폴더가 없으면 종료
    if not target_path.exists():
        print(f"'{target_dir}' 폴더가 존재하지 않습니다.")
        return
        
    print(f"=== '{target_dir}' 폴더 일괄 검증 시작 ===")
    
    # 과제 1: artifacts 폴더의 모든 파일을 검증하고 결과 리스트 만들기[cite: 1]
    for file_path in target_path.iterdir():
        if file_path.is_file(): # 파일만 대상
            passed, reason = validate_artifact(file_path)
            results.append({
                "file_name": file_path.name,
                "passed": passed,
                "reason": reason
            })
            
            status = "PASS" if passed else f"FAIL ({reason})"
            print(f" - {file_path.name}: {status}")

    # 과제 2: 실패 reason별 개수 집계[cite: 1]
    fail_reasons = [res["reason"] for res in results if not res["passed"]]
    reason_counts = Counter(fail_reasons)
    
    print("\n=== 실패 사유(Reason) 집계 결과 ===")
    if not reason_counts:
        print("모든 파일이 정상입니다 (실패 없음).")
    else:
        for reason, count in reason_counts.items():
            print(f"- {reason}: {count}건")

if __name__ == "__main__":
    run_batch_validation()