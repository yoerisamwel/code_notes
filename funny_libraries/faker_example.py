'''
Faker Library in Python:
The Faker library in Python is used for generating fake data, which can be useful for testing or creating sample datasets.

Key Features:
Generate fake names, addresses, emails, etc.
Customizable locales for generating data from different regions.
Available via pip install faker.
'''

from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate fake data
print(fake.name())         # Outputs a fake name
print(fake.address())      # Outputs a fake address
print(fake.email())        # Outputs a fake email