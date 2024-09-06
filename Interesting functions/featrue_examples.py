"""
# Introduction

## 1. Default Dictionary (defaultdict):
   - A `defaultdict` is a subclass of the Python `dict` class that returns a default value if the requested key does not exist.
   - This avoids `KeyError` when accessing non-existent keys and automatically initializes keys with a default value, making it useful for counting or grouping operations.

Example:
"""
from collections import defaultdict

# Initialize defaultdict with default value type 'int'
dd = defaultdict(int)
dd['key'] += 1  # No KeyError, 'key' is automatically initialized with 0 and then incremented
print(dd)

"""
# 2. Named Tuples:
   - A `namedtuple` is a subclass of tuples that allows you to define fields by name instead of by position, making your code more readable and self-documenting.
   - Named fields improve code readability and allow accessing tuple elements using names instead of indexes.
"""

from collections import namedtuple

# Define a named tuple 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', 'x y')
p = Point(10, 20)

# Access fields using names instead of indices
print(f"x: {p.x}, y: {p.y}")

"""
# 3. Dataclass:
   - A `dataclass` is a decorator that simplifies class creation by automatically adding special methods like `__init__`, `__repr__`, and `__eq__`.
   - It eliminates the need to manually define common methods for your class, making your code cleaner and easier to maintain.
"""

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Create an instance of the dataclass and print
p = Point(10, 20)
print(p)

"""
# 4. Set Comprehensions:
   - Set comprehensions are similar to list comprehensions but create sets instead of lists.
   - They are used to create sets in a concise and readable manner.
"""

# Set comprehension to generate a set of unique squares
unique_squares = {x**2 for x in range(10)}
print(unique_squares)

"""
# 5. Frozenset:
   - A `frozenset` is an immutable version of a Python set. Once created, its elements cannot be changed.
   - Frozensets are useful when you need a set that cannot be modified, such as when using sets as dictionary keys.
"""

# Create a frozenset
fs = frozenset([1, 2, 3, 2, 1])
print(fs)

"""
# 6. Enumerate Function:
   - The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object.
   - This is useful when you need both the index and the value of items while iterating through an iterable.
"""

for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

"""
# 7. Zip Function:
   - The `zip()` function combines multiple iterables into a single iterable of tuples.
   - This is useful when you want to iterate over multiple sequences simultaneously.
"""

names = ['a', 'b', 'c']
ages = [20, 25, 30]
combined = list(zip(names, ages))

# Print combined values as tuples
print(combined)

"""
# 8. List Comprehensions:
   - List comprehensions provide a concise way to create lists, replacing the need for `for` loops to generate lists.
"""

# Create a list of squares using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

"""
# 9. Generator Expressions:
   - Similar to list comprehensions but with parentheses, generator expressions are used to create generators.
   - Generators are memory-efficient and suitable for handling large datasets.
"""

# Generator expression for squares
squares_gen = (x**2 for x in range(10))

# Print values from the generator
for value in squares_gen:
    print(value)

"""
# 10. Counter:
   - The `Counter` class from the `collections` module counts the occurrences of elements in a collection.
   - It is useful for counting hashable objects.
"""

from collections import Counter

# Count the occurrences of elements in a list
counts = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(counts)

"""
# 11. Context Managers:
   - Context managers (using the `with` statement) handle resource management, such as opening and closing files, efficiently and cleanly.
"""

# Using context manager to read a file
with open('file.txt', 'r') as file:
    contents = file.read()
    print(contents)

"""
# Additional Examples:
1. For `defaultdict`, you can use other types like `list` or `set` as the default value. This is useful when you need to group items.
2. For `namedtuple`, you can create more complex structures, such as 3D points or records with many fields.
3. For `dataclass`, you can use more advanced features like default values, type hints, and frozen classes (immutable).
"""