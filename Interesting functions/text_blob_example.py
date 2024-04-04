#pip install textblob

from textblob import TextBlob

# misspelled words
blob = TextBlob("I havv a guud ideea")

# Perform spelling correction
corrected_blob = blob.correct()

# Print the corrected text
print("Original Text:", blob)
print("Corrected Text:", corrected_blob)

# TextBlob is a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

# Advantages of TextBlob:
# 1. Simplicity: TextBlob is designed to be accessed and understood easily by beginners.
# 2. Extensibility: It can be extended with little effort, and it's easy to integrate with other NLP libraries.
# 3. Language support: TextBlob supports multiple languages for various NLP tasks.
# 4. Provides a consistent API for diving into common NLP tasks without getting into the complexity of the underlying algorithms.
# 5. It comes with a built-in spell check function which is showcased in the extracted code.
# 6. TextBlob is also useful for rapid prototyping of NLP applications.