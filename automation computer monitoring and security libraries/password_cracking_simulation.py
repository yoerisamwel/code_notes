import hashlib

# Function to simulate password cracking by comparing hashed values
def simulate_password_cracking(hashed_password, password_list):
    for password in password_list:
        # Hash the password from the list and check if it matches the hashed_password
        if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
            return f"Password cracked: {password}"
    return "Password not found"

# Example usage
hashed_password_to_crack = "d033e22ae348a5b66f02410ace3585ec4da997"
common_passwords = ["password", "123456", "qwerty", "admin"]

result = simulate_password_cracking(hashed_password_to_crack, common_passwords)
print(result)

# Explanation with use cases:
'''
# Password Cracking Simulation:

Password cracking simulations are often used for educational purposes and to understand how weak passwords can be easily compromised.

Use cases:

1. Security Training: Educating users and IT staff on the importance of strong, complex passwords to prevent unauthorized access.
   Example: A demonstration in a cybersecurity workshop showing how quickly common passwords can be cracked.

2. System Security Testing: Testing a system's password strength by simulating attacks.
   Example: IT teams testing their systems to ensure that user passwords meet security requirements.

3. Password Strength Tools: Offering tools to users to check the strength of their passwords.
   Example: A website providing a service that allows users to see how strong their chosen passwords are.

4. Research: Analyzing trends in password selection and determining the most commonly used passwords.
   Example: Researchers conducting studies on password security and the effectiveness of password policies.

The provided code is a simple function that attempts to crack a hashed password by comparing it against a list of common passwords. The function hashes each password from the list and compares it to the given hash. If a match is found, it indicates the password has been 'cracked'.
'''
