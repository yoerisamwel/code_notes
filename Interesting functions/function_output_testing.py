import doctest

def square(x: int) -> int:
    """
    This function squares the input.
    >>> square(3)
    9
    >>> square(5)
    25
    >>> square(-4)
    16
    """
    return x ** 2

print(doctest.testmod())

# Output:
# TestResults(failed=0, attempted=3)



'''
Explanation:

The function square takes an integer x as an argument and returns x squared (x ** 2).
The docstring contains three examples of how the function is supposed to be used along with the expected output.
doctest.testmod() runs all the tests embedded in the docstrings throughout the module and prints a summary of the results.
The output shows that all three tests were attempted and none failed, meaning the function behaves as expected for the test cases provided.
This is a simple yet powerful way to write and run tests for functions in Python, making sure that code changes do not unexpectedly alter functionality.

'''



