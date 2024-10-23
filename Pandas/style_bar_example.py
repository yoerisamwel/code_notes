'''
Explanation of the Code
df.style.bar(): This function is used to create a bar-like visualization within a DataFrame's cells. In the example, the green bars represent values in the "Count" column, where higher values result in longer bars. The color parameter defines the color of the bars, and subset specifies which column(s) to apply the style to.

color='lightgreen': This sets the bar color to light green.
subset='Count': This applies the bar visualization only to the "Count" column.
df.style.background_gradient(): This function colors the background of the cells based on the values. It applies a color gradient where cells with higher values are darker. The cmap argument specifies the color map used for the gradient.

cmap='Blues': This applies a blue gradient, with darker blue representing higher values.
subset='Count': This applies the background gradient only to the "Count" column.
'''


# Style using bar chart
df.style.bar(
    color='lightgreen',
    subset='Count'
)

# Style using background gradient
df.style.background_gradient(
    cmap='Blues',
    subset='Count'
)


import pandas as pd

data = {
    'Currency': ['AED', 'USD', 'INR', 'EUR', 'SGD'],
    'Count': [1132, 315, 700, 522, 261]
}
df = pd.DataFrame(data)

# Apply a red-yellow gradient based on Count values
df.style.background_gradient(cmap='YlOrRd', subset='Count')

#In this example, a gradient ranging from yellow to red ('YlOrRd') is applied, where higher values appear closer to red.

import pandas as pd

data = {
    'Currency': ['AED', 'USD', 'INR', 'EUR', 'SGD'],
    'Count': [1132, 315, 700, 522, 261]
}
df = pd.DataFrame(data)

# Highlight the maximum value in the 'Count' column
df.style.highlight_max(subset='Count', color='lightblue')

#This code highlights the maximum value in the "Count" column (1132 in this case) with a light blue background.