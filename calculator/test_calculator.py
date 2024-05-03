from calculator.calculator import add, subtract, multiply, divide
import pytest

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

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (5, -3, 2),
])
def test_add_with_params(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, -1),
    (-1, 1, -2),
    (0, 0, 0),
    (5, -3, 8),
])
def test_subtract_with_params(a, b, expected):
    assert subtract(a, b) == expected

def test_mocked_divide_with_pytest_mock(mocker):
    # Mock the 'divide' function from the calculator module
    mock_divide = mocker.patch('calculator.calculator.divide')

    # Define the return value for the mock 'divide' function
    mock_divide.return_value = 5

    # Call the function under test
    result = divide(10, 2)

    # Print the return value of the mocked function
    print(f"Mocked divide result: {result}")

    # Verify that the mock 'divide' function was called with the correct arguments
    mock_divide.assert_called_once_with(10, 2)

    # Print the arguments passed to the mocked function
    print(f"Mocked divide call arguments: {mock_divide.call_args}")
