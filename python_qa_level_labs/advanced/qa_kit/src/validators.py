import re
from pathlib import Path

KEYS_REQUIRED  = {"id", "status", "elapsed_ms"}
STATUS_ALLOWED = {"ok", "fail"}
# Regular expression for TCs and logs
TC_PATTERN = re.compile(r"TC-\d{3}")
LOG_ERROR_PATTERN = re.compile(r"ERROR|FATAL")


def validate_response(data):
    errors = []
    missing = KEYS_REQUIRED - data.keys()
    if missing:
        errors.append(f"missing={sorted(missing)}")
    if "status" in data and data["status"] not in STATUS_ALLOWED:
        errors.append("invalid-status")
    if "elapsed_ms" in data:
        if not isinstance(data["elapsed_ms"], (int,float)):
            errors.append("elapsed-type")
        elif data["elapsed_ms"] < 0:
            errors.append("elapsed-negative")
    return errors


def validate_artifact(path: Path) -> tuple[bool, str]:
    """파일의 메타데이터와 내용을 검증하여 (성공여부, 사유)를 반환합니다."""
    
    # 1. 경로 및 메타데이터 검증
    if not path.exists():
        return False, "missing"
    if not path.is_file():
        return False, "not-file"
    if path.stat().st_size == 0:
        return False, "empty"
    if not TC_PATTERN.search(path.name):
        return False, "tc-id-missing"
        
    # 2. 내용 검증 (로그 파일인 경우에만 추가 검증)[cite: 1]
    if path.suffix == ".log":
        # 인코딩 에러 방지를 위해 errors="ignore" 처리
        content = path.read_text(encoding="utf-8", errors="ignore")
        if LOG_ERROR_PATTERN.search(content):
            return False, "log-error-found"
            
    return True, "ok"