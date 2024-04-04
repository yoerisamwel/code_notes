import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Sample data

labels = ['A', 'B', 'C', 'D']

values = [20, 30, 40, 10]

colors = ['#FFA07A', '#FFD700', '#6495ED', '#ADFF2F']

# Create doughnut plot

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5, marker=dict(colors=colors))])

fig.update_traces(textinfo='percent+label', textfont_size=14, hoverinfo='label+percent')

fig.update_layout(title_text="Customized Doughnut Plot", showlegend=False)

# Show plot

#fig.show()


# Sample data

labels = ['Category A', 'Category B', 'Category C', 'Category D']

sizes = [20, 30, 40, 10]

explode = (0, 0.1, 0, 0)  # "explode" the 2nd slice

# Create doughnut plot

fig, ax = plt.subplots()

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, colors=plt.cm.tab20.colors)

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Draw a white circle at the center to create a doughnut plot

centre_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=1.25)

fig.gca().add_artist(centre_circle)

# Add a title

plt.title('Doughnut Plot with Exploded Segment and Shadow Effect')

# Show plot

#plt.show()


# Sample data

labels = ['A', 'B', 'C', 'D']

values = [20, 30, 40, 10]

# Create doughnut plot

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

fig.update_layout(title_text="Doughnut Plot")

# Show plot

#fig.show()


# Sample data

labels = ['Category A', 'Category B', 'Category C', 'Category D']

sizes = [20, 30, 40, 10]



# Create doughnut plot

fig, ax = plt.subplots()

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Draw a white circle at the center to create a doughnut plot

centre_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=1.25)

fig.gca().add_artist(centre_circle)



# Add a title

plt.title('Doughnut Plot')



# Show plot

#plt.show()