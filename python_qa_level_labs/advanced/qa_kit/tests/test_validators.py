import pytest
from src.validators import validate_response

@pytest.mark.parametrize("data,passed", [
    ({"id": 1,  "status":"ok",      "elapsed_ms":120},  True),
    ({"id": 2,  "status":"fail",    "elapsed_ms":80},   True),
    ({"id": 3,  "status":"ok",      "elapsed_ms":10.5}, True),
    ({          "status":"fail",    "elapsed_ms":13.2}, False),
    ({"id": 5,                      "elapsed_ms":2},    False),
    ({"id": 6,  "status":"ok"                     },    False),
    ({"id": 7,  "status":"bad",      "elapsed_ms":836}, False),
    ({"id": 8,  "status":"ok",      "elapsed_ms":"123"},False),
    ({"id": 9,  "status":"ok",      "elapsed_ms":0},    True),
    ({"id":10,  "status":"ok",      "elapsed_ms":-1},   False),
])
def test_contract(data, passed):
    assert (len(validate_response(data)) == 0) is passed
