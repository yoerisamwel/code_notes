"""
# Introduction

## Concept Overview:
1. **Annotations in Matplotlib**:
   - Annotations are used to highlight specific points or events in a plot. They help in labeling important data points with text and arrows to make the plot more informative.
   - In `matplotlib`, the `annotate()` function is used to place text at specific points on the plot, with an arrow optionally pointing to the location.

2. **Customizing the Arrow and Text Location**:
   - The position of the text (`xytext`) and the point that the arrow points to (`xy`) can be independently controlled.
   - This flexibility allows users to create better visual clarity when pointing out significant areas on the graph.

## Code Explanation:
- The script shows how to annotate specific events (like stock market waves) on a time series plot of the S&P 500.

"""

import matplotlib.pyplot as plt
import pandas as pd

# Example data (S&P 500 Time Series)
dates = pd.date_range('2020-01-01', periods=100, freq='M')
values = [3000, 3200, 3400, 3300, 3500, 3700, 3800, 3900, 3700, 4100, 4300, 4500]

# Create the plot
fig, ax = plt.subplots()
ax.plot(dates, values)

# Add annotations
ax.annotate('First Wave',
            xy=('2020-02-20', 3400),  # Arrow points to this location
            xytext=('2020-01-31', 4000),  # Text label is placed here
            arrowprops=dict(facecolor='orange', shrink=0.05))

ax.annotate('Second Wave',
            xy=('2020-09-01', 3700),
            xytext=('2020-07-01', 3800),
            arrowprops=dict(facecolor='orange', shrink=0.05))

ax.annotate('Third Wave',
            xy=('2021-01-01', 4000),
            xytext=('2020-11-01', 4100),
            arrowprops=dict(facecolor='orange', shrink=0.05))

ax.annotate('Fourth Wave',
            xy=('2021-07-01', 4200),
            xytext=('2021-06-01', 4300),
            arrowprops=dict(facecolor='orange', shrink=0.05))

ax.annotate('Fifth Wave',
            xy=('2022-03-01', 4400),
            xytext=('2022-01-01', 4500),
            arrowprops=dict(facecolor='orange', shrink=0.05))

# Customize the plot with labels and title
ax.set_xlabel('Date')
ax.set_ylabel('S&P 500')
ax.set_title('Annotated Plot')

# Show plot
plt.show()

"""
# Explanation of Key Concepts:
1. **ax.annotate()**:
   - The `annotate()` function in `matplotlib` allows you to place a text label at a specific point on the plot (`xy`). 
   - The `xytext` argument specifies where the text should be placed relative to the data point.
   - The `arrowprops` dictionary controls the appearance of the arrow, including its color (`facecolor`), shape, and shrinkage.

2. **Text and Arrow Customization**:
   - The `xy` argument specifies the coordinates of the point to be annotated, while `xytext` defines where the text will appear.
   - `arrowprops` allows customization of the arrow that points from the text to the data point.

# Additional Example:

# You can annotate other significant points in different plots like this:
ax.annotate('High Point',
            xy=(dates[10], values[10]),
            xytext=(dates[8], values[8] + 500),
            arrowprops=dict(facecolor='blue', shrink=0.05))

# This allows flexible annotation of any data, making plots more insightful and clear.
"""