import pytest
from datetime import date
from seasons import convert_minutes, validate_date


def test_convert_minutes():

    assert convert_minutes(date.fromisoformat("1999-01-01")) == "Fourteen million, one hundred fifty-nine thousand, five hundred twenty minutes"



def test_invalid_format():
    with pytest.raises(ValueError):
        validate_date("1")

    with pytest.raises(ValueError):
        validate_date("February 6th, 1998")

