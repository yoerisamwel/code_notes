'''
Explanation of the skrub Library
skrub is a Python library that focuses on data cleaning and preprocessing. The deduplicate
function is specifically designed to handle duplicate or misspelled entries in lists.
It helps correct typos and variations in text data by mapping those variations to their
corrected versions, making it especially useful for tasks like deduplication or normalization
of categorical data.

In this case, the function is used to map misspelled food names to their corrected versions.
The library utilizes advanced techniques like string similarity algorithms to find the best
possible matches between the misspelled and correct names.
'''

from skrub import deduplicate

duplicated_food = [
    'sroccoli', 'Brzzcoli', 'oalapeno', 'Zucchtni', 'Jalapeno',
    'Brojcoli', 'Chocolate', 'Zucchzni', 'Jalapend', ...
]

# Get the most common food names
pd.Series(duplicated_food).value_counts()[:4]

# Map misspelled names to corrected names
translation_table = deduplicate(duplicated_food)
translation_table.sample(10)


from skrub import deduplicate

product_names = ['iPhone', 'iPhne', 'iPhonee', 'Samsung', 'Samsng', 'Smamsung']
cleaned_product_names = deduplicate(product_names)
print(cleaned_product_names)

from skrub import deduplicate

city_names = ['New York', 'NewYork', 'Nw York', 'Los Angeles', 'LA', 'LosAngles']
cleaned_city_names = deduplicate(city_names)
print(cleaned_city_names)
