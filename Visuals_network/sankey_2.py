import pandas as pd
import plotly.graph_objects as go
from webcolors import hex_to_rgb





# You can use either risk_cat.csv or risk_cat1.csv
data = pd.read_csv(r'risk_cat1.csv')
df = pd.DataFrame(data)
# Setup our colours
color_link = ['#000000', '#FFFF00', '#1CE6FF', '#FF34FF', '#FF4A46',
              '#008941', '#006FA6', '#A30059', '#FFDBE5', '#7A4900',
              '#0000A6', '#63FFAC', '#B79762', '#004D43', '#8FB0FF',
              '#997D87', '#5A0007', '#809693', '#FEFFE6', '#1B4400',
              '#4FC601', '#3B5DFF', '#4A3B53', '#FF2F80', '#61615A',
              '#BA0900', '#6B7900', '#00C2A0', '#FFAA92', '#FF90C9',
              '#B903AA', '#D16100', '#DDEFFF', '#000035', '#7B4F4B',
              '#A1C299', '#300018', '#0AA6D8', '#013349', '#00846F',
              '#372101', '#FFB500', '#C2FFED', '#A079BF', '#CC0744',
              '#C0B9B2', '#C2FF99', '#001E09', '#00489C', '#6F0062',
              '#0CBD66', '#EEC3FF', '#456D75', '#B77B68', '#7A87A1',
              '#788D66', '#885578', '#FAD09F', '#FF8A9A', '#D157A0',
              '#BEC459', '#456648', '#0086ED', '#886F4C', '#34362D',
              '#B4A8BD', '#00A6AA', '#452C2C', '#636375', '#A3C8C9',
              '#FF913F', '#938A81', '#575329', '#00FECF', '#B05B6F',
              '#8CD0FF', '#3B9700', '#04F757', '#C8A1A1', '#1E6E00',
              '#7900D7', '#A77500', '#6367A9', '#A05837', '#6B002C',
              '#772600', '#D790FF', '#9B9700', '#549E79', '#FFF69F',
              '#201625', '#72418F', '#BC23FF', '#99ADC0', '#3A2465',
              '#922329', '#5B4534', '#FDE8DC', '#404E55', '#0089A3',
              '#CB7E98', '#A4E804', '#324E72', '#6A3A4C'
              ]

rgb_link_color = ['rgba({},{},{}, 0.4)'.format(
    hex_to_rgb(x)[0],
    hex_to_rgb(x)[1],
    hex_to_rgb(x)[2]) for x in color_link]


# Collect the data we need from a dataframe to populate our Sankey data - source, target, and value
def get_sankey_data(data, cols, values):
    # Empty lists to hold our data
    sankey_data = {
        'label': [],
        'source': [],
        'target': [],
        'value': []
    }
    # Set our counter to zero
    cnt = 0
    # Start loop to retrieve data from our dataframe
    while (cnt < len(cols) - 1):
        for parent in data[cols[cnt]].unique():
            sankey_data['label'].append(parent)
            for sub in data[data[cols[cnt]] == parent][cols[cnt + 1]].unique():
                sankey_data['source'].append(sankey_data['label'].index(parent))
                sankey_data['label'].append(sub)
                sankey_data['target'].append(sankey_data['label'].index(sub))
                sankey_data['value'].append(data[data[cols[cnt + 1]] == sub][values].sum())

        cnt += 1
    return sankey_data


# We use this to create RGBA colours for our links.
# This enables us to have semi opaque links which in turn
# allows us to see flows with out being obscured by solid colours
rgb_link_color = ['rgba({},{},{}, 0.4)'.format(
    hex_to_rgb(x)[0],
    hex_to_rgb(x)[1],
    hex_to_rgb(x)[2]) for x in color_link]

# Call our get_sankey_data function - dataframe, colums, values
sankey_chart = get_sankey_data(df, ['l1', 'l2', 'l3'], 'weight')
# Style our initial Sankey chart
data = go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=sankey_chart['label'],
        color="goldenrod"
    ),
    link=dict(
        source=sankey_chart['source'],
        target=sankey_chart['target'],
        value=sankey_chart['value'],
        color=color_link
    ))
# Prepare our chart
fig = go.Figure(data)
# Update chart with some customisations
fig.update_layout(
    hovermode='x',
    title='Sankey - Example of an Operational Risk Taxonomy',
    font=dict(size=10, color='white'),
    paper_bgcolor='#51504f',
    # Height is needed for risk_ct.csv as the diagram is large
    height=1500,
    margin={'t': 50, 'b': 20}
)
# display chart
fig.show()