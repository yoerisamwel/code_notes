# Example Filtering a Dictionary Based on Values:
your_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Filters out key-value pairs where the value is even
filtered_dict = {k: v for k, v in your_dict.items() if v % 2 == 0}

print(filtered_dict)

# Output: {'b': 2, 'd': 4}
#In this example, a new dictionary is created where only the
# key-value pairs with even values are kept from your_dict.


# Example  The sorted function is used, with a lambda function specifying the sorting key.
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

# The printed output should be the list of dictionaries sorted by their keys.
#This script will sort the list of single-key dictionaries based on the alphabetical order of
# the keys within each dictionary. The output of print(sorted_dict_list) will be the list of
# dictionaries as they're already sorted in the your_list_of_dicts. If the dictionaries had keys
# in a different order, this method would reorder them based on the first key in each dictionary.


