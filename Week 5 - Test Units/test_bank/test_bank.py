from bank import value

def main():
    test_value()


def test_value():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100


if __name__ == "__main__":
    main()

