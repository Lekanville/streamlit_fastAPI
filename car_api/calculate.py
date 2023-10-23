import numpy as np


def calculate(operation, x, y):
    """
    operation - takes the string [add, sub, mul. div]
    x & y - two numbers
    """

    if operation == "Addition":
        return x + y

    elif operation == "Subtraction":
        return np.absolute(x - y)

    elif operation == "Multiplication":
        return x*y

    elif operation == "Division":
        return x/y