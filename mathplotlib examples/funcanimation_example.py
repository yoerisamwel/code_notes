'''

Explanation of Libraries
matplotlib: A comprehensive library used for creating static, animated, and interactive visualizations in Python. It provides pyplot which is a convenient MATLAB-like interface for making plots.

matplotlib.animation: A module within matplotlib that provides tools for creating animated visualizations. In this case, it is used to animate a scatter plot using FuncAnimation.

numpy: A popular library for numerical operations. It provides support for working with large, multi-dimensional arrays and matrices, along with many mathematical functions. Here, it’s used to generate random numbers for the scatter plot's coordinates, colors, and sizes.

Code Explanation
This script creates an animated scatter plot:

Random Data: numpy generates random x, y coordinates for 100 points, along with random colors and sizes for the scatter plot.
Plot Setup: A scatter plot is created with ax.scatter(), and the plot's limits are defined with ax.set_xlim() and ax.set_ylim().
Animation: The animate() function updates the scatter plot’s data points by adding some random movement to the x and y values. The FuncAnimation function continuously calls the animate() function to create an animated effect.

'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

num_points = 100
x, y = np.random.rand(2, num_points) * 10
colors = np.random.rand(num_points)
sizes = np.random.rand(num_points) * 1000

fig, ax = plt.subplots()
scat = ax.scatter(x, y, c=colors, s=sizes)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def animate(i):
    scat.set_offsets(np.c_[x + np.random.randn(num_points) * 0.1, y + np.random.randn(num_points) * 0.1])
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 128)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # Update line's y data
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()

#This code creates an animated sine wave that moves as the plot is updated.


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.arange(5)
bar = ax.bar(x, np.random.rand(5))

def animate(i):
    for rect, h in zip(bar, np.random.rand(5)):
        rect.set_height(h)  # Update height of each bar
    return bar

ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()

#This example creates an animated bar chart where the heights of the bars change over time.

