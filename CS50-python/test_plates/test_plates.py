from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("HELLO") == True
    assert is_valid("OUTATIME") == False
    assert is_valid("1HELLO") == False
    assert is_valid("CS50A") == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
