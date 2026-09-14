import sys
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

@pytest.fixture
def test_policy():
    # Base template for allowed lists for keys and status
    return {
        "required_keys": {"id", "status", "elapsed_ms"},
        "allowed_status": {"ok", "fail"}
    }

@pytest.fixture
def sample_valid_data():
    # Base template for a passing test case
    return {"id": 999, "status": "ok", "elapsed_ms": 42}