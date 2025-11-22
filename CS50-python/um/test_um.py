import pytest
from um import count

def test_um_count():
    assert count("um") == 1
    assert count("um teste") == 1
    assert count("um teste um") == 2
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2


