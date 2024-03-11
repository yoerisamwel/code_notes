#regular function

def add(x,y):
    return x+ y

#equvalant lambda function
lambda_add = lambda x,y : x + y

result_regular = add(3,5)
result_lambda = lambda_add(3,5)

print(result_regular)
print(result_lambda)


#Lambda functions in Python are small, anonymous functions defined using the lambda keyword. Unlike regular functions declared with the def keyword, lambda functions can be defined in a single line. They follow this basic syntax:

#lambda arguments: expression
#Lambda functions can take any number of arguments but can only have one expression. The expression is evaluated and returned. They are useful for when you need a simple function for a short period of time, and often used with functions like filter(), map(), and sorted().

#Examples:
#Adding Two Numbers:
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

#Square of a Number:
square = lambda x: x ** 2
print(square(4))  # Output: 16

#Sorting a List of Tuples by the Second Item:
list_of_tuples = [(1, 5), (2, 2), (3, 4)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
print(sorted_list)  # Output: [(2, 2), (3, 4), (1, 5)]

#Filtering a List of Numbers:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: (x % 2 == 0), numbers))
print(even_numbers)  # Output: [2, 4, 6]

#Mapping a List to Square Its Values:
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

#Lambda functions provide a concise way to perform simple operations without the need for formally defining a function. This makes your code more readable and brief, especially when you're using them as arguments to higher-order functions.


