#draw a plant using python

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 39*np.pi/2, 1000)
x = t * np.cos(t)**3
y = 9*t * np.sqrt(np.abs(np.cos(t))) + t * np.sin(0.2*t) * np.cos(4*t)

plt.plot(x, y, c="green")
plt.show()

# Define the parameter t
t = np.linspace(0, 39*np.pi/2, 1000)

# Define the equations for x and y
x = t * np.cos(t)**3
y = 9*t * np.sqrt(np.abs(np.cos(t))) + t * np.sin(0.2*t) * np.cos(4*t)

# Define the segment indices and corresponding colors
segments = [
    (0, 200, 'orange'),    # Green segment
    (200, 600, 'magenta'), # Red segment
    (600, 1000, 'red')     # Orange segment
]

# Plot each segment separately with the corresponding color
for start, end, color in segments:
    plt.plot(x[start:end], y[start:end], c=color)

plt.show()
