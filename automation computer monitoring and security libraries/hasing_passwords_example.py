import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Example usage
password = "my_secure_password"
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)

# Explanation with use cases:
'''
# Hashing Passwords:

Hashing passwords is a fundamental aspect of storing user credentials securely. Rather than storing the password as plain text,
which would be vulnerable to theft, a hash of the password is stored. When a user logs in, the password they enter is hashed and
the hash is compared to the stored hash.

Use cases:

1. User Authentication: Protect user passwords by storing the hashed versions in a database.
   Example: A website stores hashed passwords and checks the hash when a user logs in.

2. Data Integrity: To ensure that data has not been tampered with during storage or transmission.
   Example: A system could hash data before transmission and then compare the hash on the receiving end.

3. Digital Signatures: Hashes are used in creating digital signatures, which verify that a document has been signed by a particular user.
   Example: A user signs a document with their private key and the hash is used to verify the signature.

4. Unique Identifier Generation: Hashes can be used to generate unique identifiers for data for quick searches and comparisons.
   Example: Generating a unique ID for each user based on their personal information.

The provided code demonstrates creating a secure hash of a password using SHA-256, which is a cryptographic hash function.
'''
