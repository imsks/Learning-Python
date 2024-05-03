from calculator.index import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 4) == -8

def test_divide():
    assert divide(10, 2) == 5
    assert divide(0, 5) == 0
    assert divide(-8, 4) == -2

def test_divide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"