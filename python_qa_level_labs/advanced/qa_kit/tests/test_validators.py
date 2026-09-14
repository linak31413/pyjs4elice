import pytest
from src.validators import validate_response
from src.validators import validate_artifact

@pytest.mark.smoke
def test_contract_basic(sample_valid_data):
    errors = validate_response(sample_valid_data)
    assert len(errors) == 0, f"[Smoke Fail] Failure on validating error. Error: {errors}"

@pytest.mark.regression
@pytest.mark.parametrize("data,passed", [
    ({"id": 1,  "status":"ok",      "elapsed_ms":120},  True),  # Passing on ok
    ({"id": 2,  "status":"fail",    "elapsed_ms":80},   True),  # Passing on fail
    ({"id": 3,  "status":"ok",      "elapsed_ms":10.5}, True),  # Passing on float ok
    ({          "status":"fail",    "elapsed_ms":13.2}, False), # Failing on no id
    ({"id": 5,                      "elapsed_ms":2},    False), # Failing on no status
    ({"id": 6,  "status":"ok"                     },    False), # Failing on no elapsed_ms
    ({"id": 7,  "status":"bad",      "elapsed_ms":836}, False), # Failing on invalid status
    ({"id": 8,  "status":"ok",      "elapsed_ms":"123"},False), # Failing on string elapsed_ms
    ({"id": 9,  "status":"ok",      "elapsed_ms":0},    True),  # Passing on boundary 0 elapsed_ms
    ({"id":10,  "status":"ok",      "elapsed_ms":-1},   False), # Failing on boundary -1 elapsed_ms
])
def test_contract_edge_cases(data, passed):
    errors = validate_response(data)
    actual_passed = (len(errors) == 0)

    # Impovement for asserting failure reasoning
    assert actual_passed is passed, (
        f"\n[Assertion Fail] TC 불일치"
        f"\n  - Input data      : {data}"
        f"\n  - Expected result : PASS == {passed}"
        f"\n  - Actual result   : PASS == {actual_passed}"
        f"\n  - Returned error  : {errors}"
    )


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