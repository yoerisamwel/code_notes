"""
# Introduction

## Python Libraries:
1. **gluonts**:
   - `gluonts` is a Python library built for deep learning-based time series forecasting. It provides various tools for loading datasets, splitting them, and applying models.
   - The `DeepAREstimator` is a key model in gluonts, designed for probabilistic forecasting on time series data using autoregressive methods.

## Code Explanation:
- The script uses `gluonts` to train a deep learning model for time series forecasting.
- The time series data is split into training and testing sets. The model is then trained using the `DeepAREstimator` and predictions are generated for the test set.
"""

from gluonts.dataset.pandas import PandasDataset
from gluonts.dataset.split import split
from gluonts.torch import DeepAREstimator

# Load the dataset from a Pandas DataFrame, specifying the target column
dataset = PandasDataset(df, target="#Passengers")

# Split the data into training and testing sets
# The `offset=-36` keeps the last 36 observations for testing
train, test_gen = split(dataset, offset=-36)
test = test_gen.generate_instances(prediction_length=12)

# Initialize the DeepAR model and specify prediction length and frequency (monthly data)
model = DeepAREstimator(
    prediction_length=12,
    freq="M"
).train(train)

# Generate predictions for the test data
model.predict(test.input)

# Example output:
"""
The output of the prediction will be a probabilistic forecast with confidence intervals.
The graph below shows the actual vs predicted values, along with the uncertainty intervals.
"""