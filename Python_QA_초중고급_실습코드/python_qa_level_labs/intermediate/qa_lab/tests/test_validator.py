import pytest
from src.validator import is_valid_status

@pytest.mark.parametrize("actual,expected,result", [(200,200,True),(404,200,False),(500,500,True)])
def test_status(actual, expected, result):
    assert is_valid_status(actual, expected) is result
