"""
# Introduction

## Concept Overview:
1. **reduce() Function**:
   - The `reduce()` function from the `functools` module applies a given function to the items of an iterable (e.g., a list), reducing it to a single value.
   - This is useful for combining elements, such as summing a list, finding the maximum, or concatenating strings.

## Code Explanation:
- The code provides multiple examples of how to use the `reduce()` function, including summing, finding the maximum, flattening lists, and more.
"""

from functools import reduce

# Example 1: Sum of Elements
# This example demonstrates how to sum the elements of a list using reduce.
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

# Example 2: Product of Elements
# Calculate the product of all elements in a list.
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120

# Example 3: Finding the Maximum Element
# Use reduce to find the maximum element in a list.
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)  # Output: 5

# Example 4: Concatenating Strings
# You can use reduce to concatenate a list of strings into a single string.
words = ["Hello", "World", "from", "Python"]
result = reduce(lambda x, y: x + " " + y, words)
print(result)  # Output: "Hello World from Python"

# Example 5: Using an Initial Value
# The initial value is used as a starting point for the reduce function.
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)  # Output: 25 (10 + sum of list)

# Example 6: Flattening a List of Lists
# Reduce can flatten a list of lists into a single list.
lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
result = reduce(lambda x, y: x + y, lists)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Example 7: Finding the Greatest Common Divisor (GCD)
# Use reduce with the GCD function from the math module to find the GCD of a list of numbers.
import math
numbers = [48, 64, 256]
result = reduce(math.gcd, numbers)
print(result)  # Output: 16

# Example 8: Combining Dictionaries
# Reduce can be used to combine multiple dictionaries into one.
dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
result = reduce(lambda x, y: {**x, **y}, dicts)
print(result)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Example 9: Custom Function with reduce()
# A custom function with reduce() to calculate the sum of squares.
def sum_of_squares(x, y):
    return x + y**2

numbers = [1, 2, 3, 4]
result = reduce(sum_of_squares, numbers, 0)
print(result)  # Output: 30 (sum of squares of the list elements)

"""
# Additional Notes:
1. **Initial Values**: In Example 5, the `reduce()` function allows you to specify an initial value (like 10) which is added to the result.
2. **Custom Functions**: In Example 9, you can define your own custom function to perform more complex operations, such as summing the squares.
"""