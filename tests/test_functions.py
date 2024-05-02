import functions
import pytest

def test_sum():
    assert functions.sum(2, 3) == 5
    assert functions.sum(0, 0) == 0

    # Invalid inputs
    with pytest.raises(TypeError) as e:
        functions.sum("Hello", "World")
    assert str(e.value) == "Inputs must be numbers"
