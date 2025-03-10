import pytest
from numb3rs import validate

def test_validate():
    assert validate("1") == False
    assert validate("1.1") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1") == True
    assert validate("1.500.1.1") == False

# def test_valueerror():
#     with pytest.raises(ValueError):
#         validate("A")
#         validate("-")

