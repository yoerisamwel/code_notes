"""
# Introduction

## Concept Overview:
1. **Inset Axes**:
   - Inset axes are small axes placed inside a larger plot, often used to show a zoomed-in view of a specific region of the data.
   - This technique is valuable when there is a small but important detail in a plot that is otherwise difficult to see on the standard scale.

2. **Better Visualization**:
   - The goal is to zoom in on an area of interest and embed this zoomed-in view into the main plot, allowing for better data inspection.
   - The inset axes are created, the region of interest is focused, and the inset is embedded within the main plot.

## Code Explanation:
- This script creates a zoomed inset within a larger plot to focus on a specific region.
"""

import matplotlib.pyplot as plt

# Example data (x, y)
x = range(-100, 100)
y = [i**2 / 100 for i in x]

# 1) Create the usual plot
fig, ax = plt.subplots()
ax.plot(x, y)

# 2) Define Inset Axes
# `inset_axes` creates a small set of axes inside the main plot
axin = ax.inset_axes([0.5, 0.5, 0.4, 0.4])  # Position of inset [left, bottom, width, height]

# 3) Recreate plot with axin
# Plot the same data but focus on a zoomed region
axin.plot(x, y)

# 4) Focus on the region of interest
# Set the x and y limits to zoom into the region of interest
axin.set_xlim(-12, 12)
axin.set_ylim(7, 8)

# 5) Embed the inset into the main plot
# Indicate the zoomed region on the main plot
ax.indicate_inset_zoom(axin)

# Display the final plot
plt.show()

# Additional Example:
# You can create more complex inset plots, e.g., if you're comparing multiple datasets:
x2 = range(-100, 100)
y2 = [i**3 / 1000 for i in x2]

# Plot with two datasets
fig, ax = plt.subplots()
ax.plot(x, y, label='Dataset 1')
ax.plot(x2, y2, label='Dataset 2')

# Create inset axes
axin = ax.inset_axes([0.6, 0.6, 0.35, 0.35])
axin.plot(x, y, label='Dataset 1')
axin.plot(x2, y2, label='Dataset 2')

# Focus on a different region of interest
axin.set_xlim(-15, 15)
axin.set_ylim(10, 50)

# Add zoom indication
ax.indicate_inset_zoom(axin)

# Show plot with zoomed region
plt.show()

"""
# Explanation of Key Concepts:
- **inset_axes()**: This function adds a small set of axes to a plot, useful for creating zoomed-in views.
- **set_xlim() and set_ylim()**: These functions control the visible x and y ranges of the inset, allowing you to zoom into a specific region.
- **indicate_inset_zoom()**: Adds indicators to show the zoomed area on the main plot, helping users understand where the zoomed region is located.
"""