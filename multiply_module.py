import doctest

def multiply_two_numbers(a, b):
    """
    Return the product of a and b.
    
    Examples:
    >>> multiply_two_numbers(2, 3)
    6
    >>> multiply_two_numbers(-1, 5)
    -5
    >>> multiply_two_numbers(0, 100)
    0
    >>> multiply_two_numbers(4, 2.5)
    10.0
    """
    return a * b

if __name__ == "__main__":
    doctest.testmod()
    