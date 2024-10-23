'''
Explanation of the Libraries
NumPy (numpy):
NumPy is a powerful library for numerical computation in Python. It provides support for creating arrays and performing mathematical operations on them. In this code, NumPy is used to create the x, y, and z values for the 3D plot.
Matplotlib (matplotlib.pyplot):
Matplotlib is a plotting library used for creating static, animated, and interactive visualizations. The pyplot module provides functions for making various types of plots. In this case, it's used to create a 3D contour plot.
mpl_toolkits.mplot3d:
This toolkit provides tools for creating 3D plots in Matplotlib. The Axes3D class is used to generate a 3D plot within the figure. It extends the 2D plotting capabilities of Matplotlib to support three dimensions.
How the Code Works
Meshgrid Creation:

The np.meshgrid() function is used to create a grid of x and y values. These grids are used as the input for the function f(x, y) to compute z values.
Function Definition:

The function f(x, y) computes the value of the sine function based on the distance from the origin. This is the function that is visualized in the 3D contour plot.
Plotting:

The contour3D() function generates a 3D contour plot using the computed X, Y, and Z data. The cmap='viridis' argument sets the color map used for the plot.
Colorbar:

The colorbar is added to provide a reference for the Z-values, giving viewers an understanding of how values vary across the plot.
'''


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

Z = f(X, Y)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
contour = ax.contour3D(X, Y, Z, 50, cmap='viridis')

# Add Labels and a colorbar
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
fig.colorbar(contour, ax=ax, label='Z values')

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

def f(x, y):
    return np.cos(np.sqrt(x**2 + y**2))

Z = f(X, Y)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
#This example creates a 3D surface plot using the plot_surface() function, with a plasma color map. The plot shows a smooth surface, where the z values are determined by the cosine of the radial distance from the origin.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

def f(x, y):
    return np.tan(np.sqrt(x**2 + y**2))

Z = f(X, Y)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='blue')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()

#This example creates a 3D wireframe plot using the plot_wireframe() function. Wireframe plots are useful when you want to see the structure of a surface without the filled surface that a plot_surface() would provide.