#Medium artikel
#https://medium.com/codex/pandas-crash-course-top-30-functions-for-any-data-analysis-b0935bf96ee2


import pandas as pd
import numpy as np

# Creating a hypothetical sales dataset
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-10'),
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C'],
    'Sales': [100, 150, 120, 80, 200, 110, 90, 130, 160, 75],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'West', 'North', 'East', 'South']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Read data from CSV file
df = pd.read_csv('your_data.csv')
# Display the first few rows
df.head()

# Display basic information about the DataFrame
df.info()

# Summary statistics for numeric columns
df.describe()

# Drop rows with missing values
df.dropna()

#Fill missing values with a specified value
df.fillna('NA')

# Select a single column
df['Product']

# Select multiple columns
df[['Product', 'Sales']]

# Filter rows based on a condition
df[df['Sales'] > 100]

# Multiple conditions
df[(df['Region'] == 'North') & (df['Sales'] > 100)]

# Sort DataFrame by a column
df.sort_values(by='Sales', ascending=False)

# Group data by a column and calculate mean
df.groupby('Region')['Sales'].mean()

# Apply a function to each element in a column
df['Sales'].apply(lambda x: x * 2)

# Concatenate DataFrames vertically
df2 = pd.concat([df, df])

# Convert a column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the datetime column as the index
df.set_index('Date', inplace=True)

# Resample time series data by day
df.resample('M').mean()

# Create a new column based on existing columns
df['Revenue'] = df['Sales'] * 1.2

# Remove duplicate rows based on all columns
df.drop_duplicates()

# Convert text to lowercase
df['Product'].str.lower()

# Check for a substring in text
df['Product'].str.contains('A')

# Convert a column to categorical
df['Region'] = pd.Categorical(df['Region'])

# Create a pivot table
pivot_table = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc=np.sum)

# Merge two DataFrames
df2 = pd.DataFrame({'Region': ['North', 'South'], 'Manager': ['John', 'Jane']})
merged_df = pd.merge(df, df2, on='Region')

# Calculate cumulative sum of a column
df['Cumulative_Sales'] = df['Sales'].cumsum()

# Calculate rolling mean of a column
df['Rolling_Mean'] = df['Sales'].rolling(window=2).mean()

# Identify and replace outliers
upper_bound = df['Sales'].mean() + 2 * df['Sales'].std()
df['Sales'] = np.where(df['Sales'] > upper_bound, df['Sales'].median(), df['Sales'])

# Shift values in a column
df['Shifted_Sales'] = df['Sales'].shift(periods=1)

# Calculate percentage change in a column
df['Percentage_Change'] = df['Sales'].pct_change() * 100

# Calculate correlation matrix
correlation_matrix = df.corr()

import matplotlib.pyplot as plt

# Plot data using Pandas
df['Sales'].plot(kind='line')
plt.show()

# Save DataFrame to CSV file
df.to_csv('output_file.csv', index=False)

# Optimize memory usage
df.info(memory_usage='deep')

# Apply custom aggregation to columns
df.agg({'Sales': 'sum', 'Revenue': 'mean'})

# Create bins for numeric data
df['Sales_Bin'] = pd.cut(df['Sales'], bins=[0, 100, 150, 200], labels=['Low', 'Medium', 'High'])

# Find unique values in a column
unique_values = df['Region'].unique()

# Count occurrences of each value in a column
value_counts = df['Region'].value_counts()