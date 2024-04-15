import matplotlib.pyplot as plt

# Sample data from clcoding.com
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Create an area plot
plt.fill_between(x, y1, color="skyblue", alpha=0.4)
plt.fill_between(x, y2, color="salmon", alpha=0.4)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot Example')
plt.show()

#interesting area plot

'''
Area plots are useful for visualizing quantitative data over time or among different categories. Use cases include:

1. Financial Analysis: To show how different components contribute to total revenue or expenses over time.
   Example: Comparing revenue streams from different products over a financial quarter.

2. Environmental Data Representation: Displaying changes in temperature, pollution levels, or other metrics over time.
   Example: Visualizing the average temperature and humidity levels by month.

3. Project Management: To illustrate resource allocation or project stages over the course of a timeline.
   Example: Displaying the various phases of a construction project and their progress over time.

The following code generates a simple area plot example:

# Sample data
x = [1, 2, 3, 4, 5]  # Represents the X-axis points
y1 = [2, 4, 6, 8, 10]  # First set of Y-axis points
y2 = [1, 3, 5, 7, 9]  # Second set of Y-axis points

# Create an area plot
plt.fill_between(x, y1, color="skyblue", alpha=0.4)  # Fills the area under the y1 curve
plt.fill_between(x, y2, color="salmon", alpha=0.4)  # Fills the area under the y2 curve
plt.xlabel('X-axis')  # Label for the X-axis
plt.ylabel('Y-axis')  # Label for the Y-axis
plt.title('Area Plot Example')  # Title for the plot

# Display the plot
plt.show()  # Shows the plot on the screen

'''

