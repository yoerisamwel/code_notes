import plotly.express as px
import pandas as pd

# Read in our data to our datafeame 'df'
df = pd.read_csv("taxonomy.csv")

# Count the occurrences of each combination of risks
df_count = (
    df.groupby(["L1 Risk", "L2 Risk", "L3 Risk"]).size().reset_index(name="counts")
)

# Create the sunburst chart
fig = px.sunburst(
    df_count,
    path=["L1 Risk", "L2 Risk", "L3 Risk"],
    values="counts",
    title="Risk Data Displayed on a Sunburst Chart",
)

# Set text position to inside the slice and format the text
fig.update_traces(
    textinfo="label+value",
    texttemplate="%{label}:<br> Risks: %{value:.0f}",
    insidetextorientation="radial",
)

# Set the chart size to 1000 x 1000 pixels and disable the legend
fig.update_layout(showlegend=False, autosize=False, width=1000, height=1000)

# Show the figure
fig.show()