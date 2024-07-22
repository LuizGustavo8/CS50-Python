import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("WORLD") == True
    assert is_valid("PYTHON") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("TOOLONG") == False

def test_invalid_characters():
    assert is_valid("CS50!") == False
    assert is_valid("HELLO WORLD") == False
    assert is_valid("GREET.") == False

def test_numbers_not_at_end():
    assert is_valid("CS50PY") == False
    assert is_valid("HEL5LO") == False

def test_invalid_number_zero():
    assert is_valid("CS05") == False

def test_valid_numbers():
    assert is_valid("AB123") == True
    assert is_valid("AB1") == True
    assert is_valid("AA") == True
    assert is_valid("A2") == False

    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False



if __name__ == "__main__":
    pytest.main()
