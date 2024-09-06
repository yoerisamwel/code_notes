"""
# Introduction

## Concept Overview:
1. **Data Visualization**:
   - This script demonstrates how to visualize sales data by country using a line plot in `pandas` and `matplotlib`.
   - The data is grouped by country and week, then plotted to show weekly sales trends.

2. **Customization**:
   - The plot uses different colors for each country, with one country (Finland in this case) highlighted using a distinct color.
   - This type of visualization is useful for comparing sales performance across multiple countries while highlighting a specific region of interest.

## Code Explanation:
- The code uses `pandas.DataFrame.pipe()` to chain operations like grouping, summing, and plotting.
"""

colors = []

# Function to set colors for different countries and highlight a specific one (e.g., Finland)
def set_colors(df, country, normal='#999999', hl='#990000'):
    cols = []
    for col in df.columns:
        if col != country:  # Set the normal color for other countries
            cols.append(normal)
        else:  # Set the highlight color for the specified country
            cols.append(hl)
    colors.append(cols)  # Append colors for the plot
    return df.loc[:, cols]

# Function to plot the data
def plot(df):
    ax = df.plot(color=colors, title='Sales by Country')  # Plot the data with specified colors
    ax.legend(bbox_to_anchor=(1.1, 1), ncols=2)  # Customize legend position
    ax.set_ylabel('USD')  # Label the y-axis as USD (sales value)
    return df

# Data processing and visualization pipeline
final = (sales
         .astype({'InvoiceDate': 'datetime64[ns]'})  # Convert InvoiceDate to datetime type
         .query('Country != "United Kingdom"')  # Exclude the United Kingdom from the analysis
         .assign(Country=lambda df: limit_n(df, 'Country', total=lambda df: df.Quantity * df.UnitPrice))  # Add total sales by country
         .groupby([pd.Grouper(key='InvoiceDate', freq='w'), 'Country'])  # Group by week and country
         .sum(numeric_only=True)  # Sum the numeric columns (sales)
         .unstack()  # Unstack the data for plotting
         .fillna(0)  # Fill missing values with 0
         .pipe(set_colors, country='Finland')  # Set colors and highlight Finland
         .pipe(plot)  # Plot the final data
)

# Additional Example:
# This code can be adapted to highlight a different country or analyze different data.
# For instance, you could highlight 'Germany' instead of 'Finland':

final = (sales
         .astype({'InvoiceDate': 'datetime64[ns]'})
         .query('Country != "United Kingdom"')
         .assign(Country=lambda df: limit_n(df, 'Country', total=lambda df: df.Quantity * df.UnitPrice))
         .groupby([pd.Grouper(key='InvoiceDate', freq='w'), 'Country'])
         .sum(numeric_only=True)
         .unstack()
         .fillna(0)
         .pipe(set_colors, country='Germany')  # Highlight Germany
         .pipe(plot)
)