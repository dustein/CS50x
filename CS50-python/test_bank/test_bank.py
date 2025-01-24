from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hello ") == 0
    assert value("hi") == 20
    assert value("hope amigo") == 20
    assert value("Whats up") == 100
    assert value("HELLO") == 0
