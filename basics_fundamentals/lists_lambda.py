# Example
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Explanation Combining Lists:
combined_list = list(map(lambda x, y: x + y, list1, list2))

print(combined_list)

# Output: [7, 9, 11, 13, 15]

# Example Removing None Values:
your_list = [1, 2, None, 3, 4, 5]

# Explanation
filtered_list = list(filter(lambda x: x is not None, your_list))

print(filtered_list)

# Output: [1, 2, 3, 4, 5]

#Filtering a List (Selecting Even Numbers):
# Example List
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
filtered_list = list(filter(lambda x: x % 2 == 0, your_list))

print(filtered_list)

# Output: [2, 4, 6, 8, 10]

#Mapping a List (Squaring Each Element):
#This code takes your_list and creates a new list with each element squared.
# The map function applies the lambda to each element of the list.
# Example List
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
squared_list = list(map(lambda x: x ** 2, your_list))

print(squared_list)

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example Conditional Mapping in a List:
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explanation
modified_list = list(map(lambda x: x ** 2 if x % 2 == 0 else x, your_list))

print(modified_list)

# Output: [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]

