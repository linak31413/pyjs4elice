import json
import pytest
from src.loader import load_cases

def test_load_cases_success(tmp_path):
    """정상적인 JSON 케이스 로드 테스트"""
    sample_data = [
        {"tc_id": "TC-TEST-1", "actual": {"id": 1, "status": "ok", "elapsed_ms": 10}}
    ]
    test_file = tmp_path / "test_cases.json"
    test_file.write_text(json.dumps(sample_data), encoding="utf-8")
    
    loaded = load_cases(str(test_file))
    assert len(loaded) == 1
    assert loaded[0]["tc_id"] == "TC-TEST-1"