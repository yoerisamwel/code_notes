# Import the profanity checker from the better_profanity library.
from better_profanity import profanity

# Define a string that we want to censor.
text = "What the heck is going on?"

# Use the censor method from the profanity checker to replace profane words with asterisks.
censored_text = profanity.censor(text)

# Print the censored text. The expected output is that any profane words would be replaced with asterisks.
print(censored_text)
# Output: What the **** is going on?

# The use case for this is in applications where you want to filter out profanity from text input by users, such as chat applications, forums, or comments sections.

# Import the profanity checker again.
from better_profanity import profanity

# Define another string that we want to check for profanity.
text = "I can't believe he said that!"

# Use the contains_profanity method to check if the text contains any profane words.
has_profanity = profanity.contains_profanity(text)

# Print the result. It will be 'True' if profanity is detected, otherwise 'False'.
print(has_profanity)
# Output: False

# The use case for this is in moderation tools that flag content for review if profanity is detected, helping moderators prioritize what to look at.

