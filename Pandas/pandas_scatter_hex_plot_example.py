"""
# Introduction

## Concept Overview:
1. **Scatter Plot**:
   - A scatter plot is a basic type of plot that shows the relationship between two continuous variables. Each point represents an observation in the dataset.
   - Scatter plots are helpful for visualizing distributions and correlations between variables.

2. **Hexbin Plot**:
   - A hexbin plot is a variation of a scatter plot that groups points into hexagonal bins and colors them based on the number of points in each bin.
   - This is especially useful when dealing with large datasets where many points overlap, making a scatter plot hard to interpret.

## Code Explanation:
- The code compares two types of plots, scatter and hexbin, using the pandas `.plot()` function.
- Both methods require specifying the x and y columns for plotting.
"""

# Scatter Plot Example (scatter.py)
df.plot(kind='scatter', x='x', y='y')

# Hexbin Plot Example (hexbin.py)
df.plot(kind='hexbin', x='x', y='y', gridsize=30, cmap='Greens')

"""
# Key Functions:
1. **df.plot()**:
   - This function is from pandas and allows for easy plotting of DataFrame data.
   - The `kind` argument specifies the type of plot, such as 'scatter' or 'hexbin'.

2. **gridsize**:
   - In the hexbin plot, `gridsize` controls the number of hexagons in the grid. A larger grid size means smaller hexagons.

3. **cmap**:
   - `cmap` refers to the color map used for the hexbin plot. It specifies the colors used for the hexagons based on density (in this case, the 'Greens' color map).

# Additional Examples:

# Scatter Plot with colors and sizes:
df.plot(kind='scatter', x='x', y='y', c='z', s=df['z']*20, colormap='viridis')

# Hexbin plot with log scale for large datasets:
df.plot(kind='hexbin', x='x', y='y', gridsize=40, cmap='Purples', reduce_C_function=np.log)

# Explanation of Key Concepts:
- **Scatter Plot**: Useful for visualizing simple correlations and distributions between two variables.
- **Hexbin Plot**: More effective for large datasets where scatter plots become crowded. It groups points into hexagons and colors them based on density.
"""