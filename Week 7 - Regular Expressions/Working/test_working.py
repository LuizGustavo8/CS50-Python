import pytest
from working import convert


def test_01():
    with pytest.raises (ValueError):
         assert convert("11 AM - 9 PM")

def test_convert_02():
    with pytest.raises (ValueError):
        assert convert("3:73 AM to 12:25 PM")

def test_convert_03():
     assert convert("11 AM to 9 PM") == "11:00 to 21:00"


if __name__ == "__main__":
    pytest.main()
