from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(45) == "45%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("sd")
        convert("s/d")
        convert("s/50")
    with pytest.raises(ValueError):
        convert("-5/10")
        convert("5/-3")
    with pytest.raises(ValueError):
        convert("1.5/3")
        convert("5/3")

def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("99/0")
