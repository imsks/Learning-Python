def sum(a, b):
    if not (isinstance(a, (int, float))) and not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b