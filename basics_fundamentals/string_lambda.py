# Example Reversing a String:
s = "clcoding"

# Explanation
reversed_string = lambda s: s[::-1]

print(reversed_string(s))

# Output: "gnidolc"

# Example Extracting First N Characters:
s = "clcoding"
n = 3

# Explanation
first_n_chars = lambda s, n: s[:n]

print(first_n_chars(s, n))

# Output: "clc"

# Example Checking if a string is a palindrome:
s = "clcoding"

# Explanation
is_palindrome = lambda s: s == s[::-1]

print(is_palindrome(s))

# Output: False

# Example Counting vowels in a string:
s = "clcoding"

# Explanation
count_vowels = lambda s: sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels(s))

# Output: 2