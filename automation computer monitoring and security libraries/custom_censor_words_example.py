# Import the profanity utility from the better_profanity package.
from better_profanity import profanity

# Define a list of custom words that you want to censor in addition to the default list.
custom_censor_words = ["heck", "darn", "frick"]

# Load the custom censor words into the profanity filter.
# Any words in this list will now be censored in addition to the default list of profanities.
profanity.load_censor_words(custom_censor_words)

# Censoring text with the custom words loaded above.
from better_profanity import profanity

# Define a string that may contain words that should be censored.
text = "What the heck is going on?"

# Censor the text with the profanity censor. This will censor the custom words we added earlier.
censored_text = profanity.censor(text)

# Print the censored text. The output will replace "heck" with asterisks.
print(censored_text)
# Expected output: What the **** is going on?

# Use case: This can be particularly useful in cases where you need to filter out words that are not in the default dictionary of profanities but are considered inappropriate for your specific application or audience.
