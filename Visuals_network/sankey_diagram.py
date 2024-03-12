#https://medium.com/@twelsh37/understanding-plotly-sankey-charting-3ee263a81549

import plotly.graph_objects as go

color_link = ['#000000', '#FFFF00', '#1CE6FF', '#FF34FF', '#FF4A46',
             '#008941', '#006FA6', '#A30059','#FFDBE5', '#7A4900',
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

# Our labels. The numbers after the comment denote the 'source node' the label belongs to.
label = ['Zero',       # 0
        'One',         # 1
        'Two',         # 2
        'Zero-Zero',   # 3
        'Zero-One',    # 4
        'One-Zero',    # 5
        'One-One',     # 6
        'Two-Zero',    # 7
        'Two-One'      # 8
        ]

# Data
source = [0, 1, 2]  # 3 Source Nodes
target = [1, 2, 3, 4, 5, 6]  # 6 Target Nodes
value = [1, 1, 1, 1, 1, 1 ]  # 6 Values

# Link references our fields above
link = dict(source=source, target=target, value=value, color=color_link)
# node handels assigning labels and the housekeeping aound the diagram.
node = dict(label = label, pad=35, thickness=20)
# We then package the informtion into our data object
data = go.Sankey(link=link, node=node)

fig = go.Figure(data)
fig.update_layout(
    hovermode='x',
    title='Sankey 1 - 3 nodes, 6 targets, 6 values',
    font=dict(size=10, color='white'),

    # Set diagrams background colour to almost black
    paper_bgcolor='#51504f'
)
fig.show()

# Our labels. The numbers after the comment denote the 'source node' the label belongs to.
label = ['Zero',       # 0
        'One',         # 1
        'Two',         # 2
        'Zero-Zero',   # 3
        'Zero-One',    # 4
        'One-Zero',    # 5
        'One-One',     # 6
        'Two-Zero',    # 7
        'Two-One'      # 8
        ]

source = [0, 1, 2]  # 3 Source Nodes
target = [1, 2, 3, 4, 5, 6]  # 6 Target Nodes
value = [1, 1, 1, 1, 1, 1 ]  # 6 Values

# Data
source2 = [0, 0, 1, 1, 2, 2]  # 3 Source Nodes
target2 = [3, 4, 5, 6, 7, 8]  # 6 Target Nodes
value2 = [1, 1, 1, 1, 1, 1 ]  # 6 Values
# Link references our fields above
link2 = dict(source=source2, target=target2, value=value2, color=color_link)
# node handels assigning labels and the housekeeping aound the diagramnode = dict(label = label, pad=35, thickness=20)
# We then package the informtion into our data object
data2 = go.Sankey(link=link2, node=node)
fig2 = go.Figure(data2)
fig2.update_layout(
    hovermode='x',
    title='Sankey 2 - 3 individual nodes, 6 individual targets, 6 values',
    font=dict(size=10, color='white'),
    paper_bgcolor='#51504f'
)
fig2.show()

source3 = [0, 0, 1, 1, 2, 2]  # 3 Source Nodes
target3 = [1, 2, 3, 4, 5, 6]  # 6 Target Nodes
value3 = [1, 1, 1, 1, 1, 1 ]  # 6 Values
link3 = dict(source=source3, target=target3, value=value3, color=color_link)
node3 = dict(label = label, pad=35, thickness=20)
data3 = go.Sankey(link=link3, node=node3)
fig3 = go.Figure(data3)
fig3.update_layout(
    hovermode='x',
    title='Sankey  3 - 3 nodes, 6 targets, 6 values',
    font=dict(size=10, color='white'),
    paper_bgcolor='#51504f'
)
fig3.show()


source4 = [0, 0, 0, 0, 1, 1, 2, 2]  # 3 Source Nodes
target4 = [3, 4, 5, 6, 7, 8, 9, 10]  # 8 Target Nodes
value4 = [1, 1, 1, 1, 1, 1, 1, 1 ]  # 8 Values
link4 = dict(source=source4, target=target4, value=value4, color=color_link)
node4 = dict(label = label4, pad=35, thickness=20)
data4 = go.Sankey(link=link4, node=node4)
fig4 = go.Figure(data4)
fig4.update_layout(
    hovermode='x',
    title='Testing 4 - 3 nodes, 8 targets, 8 values',
    font=dict(size=10, color='white'),
    paper_bgcolor='#51504f'
)
fig4.show()


label5 = ['Risk',              # 0
          'Reward',            # 1
          'Forefeit',          # 2
          'Prople',            # 3
          'Proceess',          # 4
          'Systems',           # 5
          'External Events',   # 6
          'Money',             # 7
          'Food',              # 8
          'Outdoors',          # 9
          'Car',               # 10
          'Holiday',           # 11
          'Tom,',              # 12
          'Dick',              # 13
          'Harry',             # 14
          'Fast Forward',      # 15
          'Reverse',           # 16
          'Play',              # 17
          'XBox',              # 18
          'Playstation',       # 19
          'Nintendo',          # 20
          'Earthquake',        # 21
          'Terrorism',         # 22
          'Cheque',            # 23
          'Credit Card',       # 24
          'Burger',            # 25
          'Pizza',             # 26
          'Tent',              # 27
          'Pack',              # 28
          'Boots',             # 29
          'Landrover',         # 30
          'Mazda',             # 31
          'Ibiza',             # 32
          'Italy',             # 33
          'Spain',             # 34
          'USA',               # 35
          'Australia',         # 36
          'Son',               # 37
          'Daughter',          # 38
          'Red',               # 39
          'Blue',              # 40
          'Grey',              # 41
          'Silver'             # 42
        ]

source5 = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11, 11, 11, 11, 12, 12, 31, 31, 30, 30]
target5 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
value5 = [5, 3, 3, 2, 2, 2, 3, 4, 5, 2 ,1 , 1, 1 , 1 , 1, 1 ,1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1 , 1, 1, 1 , 1, 1 , 1, 1, 1]
link5 = dict(source=source5, target=target5, value=value5, color=color_link)
node5 = dict(label = label5, pad=35, thickness=20)
data5 = go.Sankey(link=link5, node=node5)
fig5 = go.Figure(data5)
fig5.update_layout(
    hovermode='x',
    title='Sankey 5 - 40 nodes, 40 targets',
    font=dict(size=10, color='white'),
    paper_bgcolor='#51504f'
)
fig5.show()





