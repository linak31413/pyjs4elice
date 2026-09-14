from src.runner import run_case

def test_run_case_contract_pass():
    tc = {
        "tc_id": "TC-UNIT-1",
        "type": "contract",
        "actual": {"id": 1, "status": "ok", "elapsed_ms": 50}
    }
    res = run_case(tc)
    assert res["status"] == "PASS"
    assert res["reason"] == []

def test_run_case_contract_fail():
    tc = {
        "tc_id": "TC-UNIT-2",
        "type": "contract",
        "actual": {"status": "ok", "elapsed_ms": -10}
    }
    res = run_case(tc)
    assert res["status"] == "FAIL"
    assert "missing=['id']" in res["reason"]