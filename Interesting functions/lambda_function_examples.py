# Example
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Explanation
#adding two lists together
combined_list = list(map(lambda x, y: x + y, list1, list2))

print(combined_list)

# The expected output should be: [7, 9, 11, 13, 15]

# Example removing non values
your_list = [1, 2, 3, 4, 5, ]

# Explanation
filtered_list = list(filter(lambda x: x is not None, your_list))

print(filtered_list)

# The expected output should be: [1, 2, 3, 4, 5]

# Example List For filtering a list to select even numbers:
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
filtered_list = list(filter(lambda x: x % 2 == 0, your_list))

print(filtered_list)
#Expected output: [2, 4, 6, 8, 10]

# Example List For mapping a list to square each element:
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
squared_list = list(map(lambda x: x ** 2, your_list))

print(squared_list)
#Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example List To filter even numbers from a list:
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
filtered_list = list(filter(lambda x: x % 2 == 0, your_list))

print(filtered_list)
#The expected output for this code is: [2, 4, 6, 8, 10]

# Example List To square each element in a list:
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
squared_list = list(map(lambda x: x ** 2, your_list))

print(squared_list)
#The expected output for this code is: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example For conditional mapping of a list (square if even, otherwise leave the element as is):
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
modified_list = list(map(lambda x: x ** 2 if x % 2 == 0 else x, your_list))

print(modified_list)
#The expected output for this snippet is: [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]


# Example For filtering a dictionary based on values (keep only entries where the value is even):
your_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Filters out key-value pairs where the value is even
filtered_dict = {k: v for k, v in your_dict.items() if v % 2 == 0}

print(filtered_dict)
#The expected output for this snippet is: {'b': 2, 'd': 4}

# Example Here's the code for sorting a list of dictionaries by a specific key as shown in your image:
your_list_of_dicts = [
    {'a': 1},
    {'b': 2},
    {'c': 3},
    {'d': 4},
    {'e': 5}
]

# Sorting based on the keys of the dictionaries
sorted_dict_list = sorted(your_list_of_dicts, key=lambda x: list(x.keys())[0])

print(sorted_dict_list)
#The expected output is a sorted list of dictionaries by their keys: [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}, {'e': 5}]


# Example To reverse a string:
s = "clcoding"

# Explanation
reversed_string = lambda s: s[::-1]

print(reversed_string(s))
#When s is "clcoding", the expected output will be "gnidolc".

# Example To extract the first N characters from a string:
s = "clcoding"
n = 3

# Explanation
first_n_chars = lambda s, n: s[:n]

print(first_n_chars(s, n))
#With s as "clcoding" and n as 3, the expected output will be "clc".

# Example Checking if a string is a palindrome:
s = "clcoding"

# Explanation
is_palindrome = lambda s: s == s[::-1]

print(is_palindrome(s))
#The output for the string "clcoding" will be False because it is not a palindrome.

# Example Counting the number of vowels in a string:
s = "clcoding"

# Explanation
count_vowels = lambda s: sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels(s))
#For the string "clcoding", the output will be 2 because there are two vowels ('o' and 'i').


# Regular function
def add(x, y):
    return x + y

# Equivalent Lambda function
lambda_add = lambda x, y: x + y

# Using both functions
result_regular = add(3, 5)
result_lambda = lambda_add(3, 5)

print("Result (Regular Function):", result_regular)
print("Result (Lambda Function):", result_lambda)

#Example 2: Sorting with Lambda
# List of tuples
students = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]

# Sort by age using a Lambda function
sorted_students = sorted(students, key=lambda student: student[1])

print("Sorted Students by Age:", sorted_students)

# Output:
# Sorted Students by Age: [('Charlie', 22), ('Alice', 25), ('Bob', 30)]

#Example 3: Filtering with Lambda
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter even numbers using a Lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

# Output:
# Even Numbers: [2, 4, 6, 8]


#Example 3: Filtering with Lambda
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter even numbers using a Lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

# Output:
# Even Numbers: [2, 4, 6, 8]


#Example 4: Mapping with Lambda
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Square each number using a Lambda function
squared_numbers = list(map(lambda x: x**2, numbers))

print("Squared Numbers:", squared_numbers)

# Output:
# Squared Numbers: [1, 4, 9, 16, 25]


#The code from the image provides an example of using a Lambda function
#with the max function in Python to find the minimum number in a list:
# List of numbers
numbers = [10, 5, 8, 20, 15]

# Find the maximum number using a Lambda function
max_number = max(numbers, key=lambda x: -x)  # Use negation for finding the minimum

print("Maximum Number:", max_number)

# Output:
# Maximum Number: 5

from functools import reduce

# Example 7: Using Lambda with reduce from functools

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the product of all numbers using a Lambda function and reduce
product = reduce(lambda x, y: x * y, numbers)

print('Product of Numbers:', product)

# Example 8: Using Lambda with Conditional Expressions

# List of numbers
numbers = [10, 5, 8, 20, 15]

# Use a Lambda function with a conditional expression to filter and square even numbers
filtered_and_squared = list(map(lambda x: x**2 if x % 2 == 0 else x, numbers))

print('Filtered and Squared Numbers:', filtered_and_squared)


# Example 9: Using Lambda with key in max and min to Find Extremes

# List of tuples representing products with names and prices
products = [("Laptop", 1280), ("Phone", 880), ("Tablet", 580), ("Smartwatch", 280)]

# Find the most and least expensive products using lambda functions
most_expensive = max(products, key=lambda item: item[1])
least_expensive = min(products, key=lambda item: item[1])

print("Most Expensive Product:", most_expensive)
print("Least Expensive Product:", least_expensive)



