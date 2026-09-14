from pathlib import Path
from src.validators import validate_response, validate_artifact

# 과제 2: 검증 종류를 매핑하는 Validator Registry 구성
VALIDATOR_REGISTRY = {
    "contract": validate_response,
    "artifact": lambda actual: validate_artifact(Path(actual["path"]))
}

def run_case(tc):
    """단일 TC를 실행하여 결과 딕셔너리를 반환"""
    tc_type = tc.get("type", "contract") # 기본값은 계약 검증
    validator = VALIDATOR_REGISTRY.get(tc_type)
    
    if not validator:
        return {
            "tc_id": tc["tc_id"],
            "status": "FAIL",
            "reason": [f"unknown-validator-type: {tc_type}"],
            "evidence": f"logs/{tc['tc_id']}.log"
        }
    
    # 검증 종류별 결과 판정
    if tc_type == "contract":
        errors = validator(tc["actual"])
        status = "PASS" if not errors else "FAIL"
        reason = errors
    elif tc_type == "artifact":
        passed, error_reason = validator(tc["actual"])
        status = "PASS" if passed else "FAIL"
        reason = [] if passed else [error_reason]

    return {
        "tc_id": tc["tc_id"],
        "status": status,
        "reason": reason,
        "evidence": f"logs/{tc['tc_id']}.log"
    }

def run_all(cases):
    """전체 TC 목록을 순차 실행"""
    return [run_case(tc) for tc in cases]