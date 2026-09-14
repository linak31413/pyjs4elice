import pytest
from src.validators import validate_response
from src.validators import validate_artifact

import pytest
from src.validators import validate_response

# 10개 이상의 파라미터화 TC를 통해 계약 조건 전수 검증
@pytest.mark.regression
@pytest.mark.parametrize("case_id,data,expected_valid", [
    ("TC-01", {"id": 1, "status": "ok", "elapsed_ms": 100}, True),
    ("TC-02", {"id": 2, "status": "fail", "elapsed_ms": 50}, True),
    ("TC-03", {"id": 3, "status": "ok", "elapsed_ms": 0}, True),
    ("TC-04", {"id": 4, "status": "ok", "elapsed_ms": 0.5}, True),
    ("TC-05", {"status": "ok", "elapsed_ms": 100}, False),               # id 누락
    ("TC-06", {"id": 6, "elapsed_ms": 100}, False),                     # status 누락
    ("TC-07", {"id": 7, "status": "ok"}, False),                        # elapsed_ms 누락
    ("TC-08", {"id": "8", "status": "ok", "elapsed_ms": 100}, False),   # id 타입 에러
    ("TC-09", {"id": 9, "status": "error", "elapsed_ms": 100}, False),  # 허용되지 않은 status
    ("TC-10", {"id": 10, "status": "ok", "elapsed_ms": -1}, False),     # 음수 경계 초과
    ("TC-11", {"id": 11, "status": "ok", "elapsed_ms": "100"}, False),  # elapsed_ms 타입 에러
])
def test_contract_rules(case_id, data, expected_valid):
    errors = validate_response(data)
    actual_valid = (len(errors) == 0)
    assert actual_valid == expected_valid, (
        f"[{case_id}] 판정 불일치: 기대값={expected_valid}, 실제값={actual_valid}, 사유={errors}"
    )


@pytest.mark.smoke
def test_smoke_valid(sample_valid_data):
    """Smoke: 기본 정상 데이터 통과 검증"""
    assert len(validate_response(sample_valid_data)) == 0


def test_validate_artifact_success(tmp_path):
    """정상적인 로그 파일 테스트"""
    valid_log = tmp_path / "TC-001_result.log"
    valid_log.write_text("INFO: Test started\nINFO: Test passed")
    assert validate_artifact(valid_log) == (True, "ok")

def test_validate_artifact_log_error(tmp_path):
    """내부에 ERROR가 포함된 로그 파일 테스트[cite: 1]"""
    error_log = tmp_path / "TC-002_result.log"
    error_log.write_text("INFO: Test started\nERROR: null pointer exception")
    assert validate_artifact(error_log) == (False, "log-error-found")

def test_validate_artifact_empty(tmp_path):
    """크기가 0인 빈 파일 테스트"""
    empty_file = tmp_path / "TC-003_result.log"
    empty_file.touch() # 빈 파일 생성
    assert validate_artifact(empty_file) == (False, "empty")

def test_validate_artifact_name_missing(tmp_path):
    """파일명에 TC- 아이디가 없는 테스트"""
    invalid_name = tmp_path / "result.log"
    invalid_name.write_text("ok")
    assert validate_artifact(invalid_name) == (False, "tc-id-missing")