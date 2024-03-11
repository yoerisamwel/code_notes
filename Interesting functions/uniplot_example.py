import math
from uniplot import plot

x = [math.sin(i/20)+i/300 for i in range(600)]

plot(x, title="Sine wave")

# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Plotting
plot(x, y, title="Plot of Y = X^2")
'''
Uniplot is a Python library designed for plotting data in the terminal. It leverages Unicode characters to represent plots such as scatter plots and histograms, providing a quick and accessible way to visualize data without the need for a graphical interface. This can be particularly useful when working in remote environments or in situations where graphical output is not available or practical.

Here are some key features and aspects of Uniplot:

Scatter Plots: You can create scatter plots using Unicode characters, allowing for a visual representation of data points directly in your terminal.
Histograms: Uniplot also supports the generation of histograms, which can be used to visualize the distribution of data.
Customization: The library offers options for customizing plots, including adjusting axes, labels, and color schemes, though the level of customization is naturally limited compared to graphical plotting libraries like Matplotlib or Seaborn.
Ease of Use: Uniplot is designed to be straightforward to use, requiring minimal setup and code to generate plots.
Installation
'''

# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Plotting a scatter plot
plot(x, title="Scatter Plot Example")

'''
Limitations
While Uniplot provides a quick and simple way to visualize data in terminal environments, it has limitations, especially in terms of plot detail, interactivity, and customization compared to more comprehensive plotting libraries that generate graphical output. For detailed analysis and presentation, libraries like Matplotlib, Seaborn, or Plotly are more suitable.

Remember, the actual appearance and capabilities of Uniplot plots are dependent on your terminal's ability to render Unicode characters accurately.
'''




