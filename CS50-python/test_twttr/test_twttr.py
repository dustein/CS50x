import pytest
from twttr import shorten

def test_shorten():
    assert shorten("frase") == "frs"
    assert shorten("teste") == "tst"
    assert shorten("FRASE") == "FRS"
    assert shorten("1uma") == "1m"
    assert shorten("certo.") == "crt."

if __name__ == "__main__":
    main()
