import pytest
from src.validators import validate_response

@pytest.mark.parametrize("data,passed", [
    ({"id":1,"status":"ok","elapsed_ms":10}, True),
    ({"status":"ok","elapsed_ms":10}, False),
    ({"id":1,"status":"bad","elapsed_ms":10}, False),
    ({"id":1,"status":"ok","elapsed_ms":-1}, False),
])
def test_contract(data, passed):
    assert (len(validate_response(data)) == 0) is passed
