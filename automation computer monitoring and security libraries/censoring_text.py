# Import the profanity library from the better_profanity package.
from better_profanity import profanity

# Define a text string that may contain profanity.
text = "What the hell is going on?"

# Censor the profanity in the text using the censor method from the profanity library.
# It will replace the profanity with asterisks.
censored_text = profanity.censor(text)

# Print the censored text to the console.
print(censored_text)
# Expected output: What the **** is going on?

# Use case: This is useful in applications where you need to filter out offensive language before displaying text to users,
# such as in social media platforms, forums, or any public-facing application where content moderation is necessary.
