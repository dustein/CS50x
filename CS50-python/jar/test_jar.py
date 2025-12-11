import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_capacity():
    # valid capacity
    jar = Jar(5)
    assert jar.capacity == 5

    # invalid capacity should raise
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12

def test_deposit():
    jar = Jar(capacity=10)
    jar.deposit(5)
    assert str(jar) == "🍪" * 5
    jar.deposit(2)
    assert str(jar) == "🍪" * 7

    with pytest.raises(ValueError):
        jar.deposit(4)


def test_withdraw():
    jar = Jar(capacity=10)
    jar.deposit(5)
    assert str(jar) == "🍪" * 5
    jar.withdraw(2)
    assert str(jar) == "🍪" * 3

    with pytest.raises(ValueError):
        jar.withdraw(4)
