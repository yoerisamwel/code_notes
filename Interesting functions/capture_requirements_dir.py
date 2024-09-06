"""
# Introduction

## Python Libraries and Requirement Management:
1. **numpy** and **pandas**:
   - `numpy` and `pandas` are essential Python libraries for data manipulation and numerical computations.
   - `numpy` is often used for array and matrix operations, while `pandas` provides powerful tools for working with structured data like DataFrames.

2. **scikit-learn**:
   - `scikit-learn` is a widely used library for machine learning tasks in Python. It includes tools for data preprocessing, such as `StandardScaler`, which is used to standardize features by removing the mean and scaling to unit variance.

## Code Explanation:
- The example demonstrates importing `numpy`, `pandas`, and `StandardScaler` from scikit-learn in two different Python scripts.
- The command `pipreqs .` is used to automatically generate a `requirements.txt` file that lists all the libraries used in the current directory, along with their versions.

"""

# file1.py
import numpy as np
import pandas as pd

# file2.py
from sklearn.preprocessing import StandardScaler

# Generate requirements.txt by using pipreqs
"""
$ pipreqs .
# Output in requirements.txt:
numpy==1.21.4
pandas==1.3.4
scikit-learn==1.1.3
"""