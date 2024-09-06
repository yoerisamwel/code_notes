"""
# Introduction

## Python Libraries:
1. **Lazypredict**:
   - `lazypredict` is a Python package that helps in quickly training and evaluating machine learning models.
   - It automates the process of running several classification or regression models, returning their performance metrics without requiring extensive configuration.
   - This is helpful when you want a quick baseline of how different models perform on your data before fine-tuning.

## Code Explanation:
- The script uses the `LazyClassifier` class from the `lazypredict` library to evaluate several classification models at once.
- The `fit()` method trains the models on the training data (`X_train`, `y_train`) and evaluates them on the test data (`X_test`, `y_test`).
- The output consists of multiple models with performance metrics like accuracy, ROC AUC, F1 score, and time taken.

"""

from lazypredict.Supervised import LazyClassifier

# Split the dataset into training and test sets (X_train, X_test, y_train, y_test)
X_train, X_test, y_train, y_test = ...

# Initialize LazyClassifier, setting verbose to 0 to reduce logging
clf = LazyClassifier(verbose=0)

# Fit the classifier on the training data and evaluate on test data
models, predictions = clf.fit(X_train, X_test, y_train, y_test)

# Example output table:
"""
| Model         | Accuracy  | ROC AUC   | F1 Score  | Time Taken |
|---------------|-----------|-----------|-----------|------------|
| LinearSVC     | 0.989474  | 0.987544  | 0.989462  | 0.0150008  |
| SGDClassifier | 0.989474  | 0.987544  | 0.989462  | 0.0109992  |
| MLPClassifier | 0.985965  | 0.986904  | 0.985994  | 0.426      |
| ...           | ...       | ...       | ...       | ...        |
"""

# Example usage:
if __name__ == "__main__":
    # Assuming your dataset is already split into X_train, X_test, y_train, y_test
    print(models)
    print(predictions)

"""
## Output Metrics:
- **Accuracy**: Proportion of correct predictions.
- **ROC AUC**: Area under the Receiver Operating Characteristic curve. Represents the classifier's ability to distinguish between classes.
- **F1 Score**: The harmonic mean of precision and recall. It's useful for imbalanced datasets.
- **Time Taken**: The time it takes for each model to train and predict.

This allows for quick benchmarking of models before further fine-tuning.
"""