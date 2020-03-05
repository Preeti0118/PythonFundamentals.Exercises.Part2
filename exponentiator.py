def exponentiate(a,b):
    """take two integers and return a value of first integer to the power of second."""

    return a ** b


def raise_to_fourth_power(c):
    """call exponentiate to raise to the power of four"""

    return exponentiate(c,4)

square = lambda x: exponentiate(x,2)
cube = lambda y: exponentiate(y,3)
print square(2)
print cube(2)
print raise_to_fourth_power(2)
