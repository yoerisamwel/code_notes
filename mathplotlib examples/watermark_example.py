'''
Explanation of the Code
matplotlib.pyplot: The pyplot module in matplotlib is used to make a wide range of plots. It's designed to be easy to use for quick visualization tasks.

plt.text(): This function allows you to add text anywhere on a plot. In this case, it is used to add a watermark ('clcoding') at the center of the plot.

0.5, 0.5: These are normalized coordinates within the plot’s axes, meaning the text will be placed at the center (50% of both x and y).
alpha=0.3: Sets the transparency of the text to 30%, so it acts as a subtle watermark.
fontsize=50: Sets the size of the text.
rotation=45: Rotates the watermark text by 45 degrees to give it a diagonal appearance.
ha='center', va='center': Horizontal and vertical alignment properties to ensure the text is centered at the specified location.
transform=plt.gca().transAxes: Transforms the text to the axes' coordinate system rather than the data coordinate system, ensuring the text is placed based on the axes (0 to 1 on both x and y axes).
'''

import matplotlib.pyplot as plt

x = range(10)
y = [i**2 for i in x]

plt.plot(x, y)

# Add watermark
plt.text(0.5, 0.5, 'clcoding', alpha=0.3, fontsize=50, rotation=45,
         ha='center', va='center', transform=plt.gca().transAxes)

plt.show()



import matplotlib.pyplot as plt

x = range(10)
y = [i**3 for i in x]

plt.plot(x, y)

# Add watermark
plt.text(0.5, 0.5, 'Watermark Example', alpha=0.2, fontsize=40, color='red',
         rotation=30, ha='center', va='center', transform=plt.gca().transAxes)

plt.show()
#In this example, the watermark has a different color ('red') and is rotated by 30 degrees.

import matplotlib.pyplot as plt

x = range(10)
y = [i**2 for i in x]

plt.plot(x, y)

# Add first watermark
plt.text(0.5, 0.5, 'Watermark 1', alpha=0.2, fontsize=30, rotation=45,
         ha='center', va='center', transform=plt.gca().transAxes)

# Add second watermark
plt.text(0.2, 0.8, 'Watermark 2', alpha=0.1, fontsize=20, rotation=30,
         ha='center', va='center', transform=plt.gca().transAxes)

plt.show()

#This example demonstrates how to add multiple watermarks with different transparency levels and placements on the same plot.


