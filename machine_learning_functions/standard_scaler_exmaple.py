from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'age': [25, 29],
    'income': [50000, 60000]
})

# Using StandardScaler to scale data
scaler = StandardScaler()
# This will return a NumPy array
scaled_data = scaler.fit_transform(df)
print(scaled_data)

# Using StandardScaler and ensuring the output is a pandas DataFrame
scaler = StandardScaler().set_output(transform='pandas')
scaled_df = scaler.fit_transform(df)
print(scaled_df)

# Creating a pipeline with an imputer and a scaler
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
]).set_output(transform='pandas')

# This will return a pandas DataFrame
pipeline_scaled_df = pipeline.fit_transform(df)
print(pipeline_scaled_df)