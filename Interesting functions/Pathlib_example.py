"""
# Introduction

## Python Libraries:
1. **Pathlib**:
   - The `pathlib` library is part of Python's standard library and provides an object-oriented interface for handling filesystem paths.
   - It allows for easy manipulation of file paths and provides methods to create, read, and write files in a more readable and concise manner.
   - It also handles operating system differences in file path formats.

2. **Pytest**:
   - `pytest` is a testing framework in Python that allows for simple unit testing with powerful features like fixtures.
   - In this script, pytest is used to verify the correctness of file writing and reading operations by temporarily creating directories, writing files, and checking the content.
   - `tmp_path` is a pytest fixture that creates a temporary directory for the duration of a test and is automatically cleaned up afterward.

## Code Explanation:
- The script consists of two main functions:
  1. **save_result**: This function creates a file in a given folder and writes text to it.
  2. **test_save_result**: This function tests the `save_result` function by creating a temporary directory, writing to a file, and asserting that the file contains the expected text.

- An example is provided at the end of the script to demonstrate how to use the `save_result` function in a real scenario.
"""

from pathlib import Path

# This function takes a folder path, a file name, and a text string as input.
# It creates the file if it does not exist and writes the provided text to it.
def save_result(folder: str, file_name: str, text: str):
    # Construct the full path to the file
    file = Path(folder) / file_name
    # Create the file if it doesn't already exist
    file.touch()
    # Write the provided text to the file
    file.write_text(text)

# This function is a test case using pytest to check if the `save_result` function works as expected.
# It creates a temporary folder, writes data to a file, reads it back, and asserts if the read content matches.
def test_save_result(tmp_path):
    # Create a new directory in the temporary folder
    folder = tmp_path / "new"
    folder.mkdir()

    # Define the file name and the text to be written
    file = "my_file.txt"
    text = "Accuracy: 0.9"

    # Call the save_result function to write the data
    save_result(folder=folder, file_name=file, text=text)

    # Read the content from the file and store it in 'res'
    res = Path(f"{folder}/{file_name}").read_text()

    # Assert that the content read from the file matches the expected text
    assert res == text

# Example usage
if __name__ == "__main__":
    # Define folder and file path for demonstration purposes
    folder = "./example_folder"
    file_name = "example_file.txt"
    text = "This is a sample text."

    # Call the function to save the result
    save_result(folder, file_name, text)

    # Check if the file is created and content is correct
    saved_text = Path(folder + "/" + file_name).read_text()
    print("File content:", saved_text)

"""
$ pytest test_save_file.py
============= 1 passed in 0.01s ==============
"""