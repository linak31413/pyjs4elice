import pytest
from src.validators import validate_response

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
