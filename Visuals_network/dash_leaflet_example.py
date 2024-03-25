import dash
from dash import html, dcc
import dash_leaflet as dl
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the coordinates
baltimore_coords = [39.2904, -76.6122]
rotterdam_coords = [51.9225, 4.47917]
paris_coords = [48.8566, 2.3522]
miami_coords = [25.7617, -80.1918]
dublin_coords = [53.3498, -6.2603]
hamburg_coords = [53.5511, 9.9937]
los_angeles_coords = [34.0522, -118.2437]
shanghai_coords = [31.2304, 121.4737]
pacific_waypoint = [20, -180]
pacific_waypoint2 = [20, 170]

# Shipments data per carrier and year
shipments_data = {
    'Year 1': {'Maersk': 3, 'HAPAG': 2},
    'Year 2': {'Maersk': 5, 'HAPAG': 2}
}

# Define the map layout within a function to allow for dynamic updates
def create_map(year):
    children = [...]
    # Add a unique key to force re-render
    map_key = f"map-{year}"
    if year == "Year 1":
        # Year 1 configuration
        children = [
            dl.Polyline(positions=[baltimore_coords, rotterdam_coords], color="red", weight=5,
                        children=dl.Tooltip("Maersk")),
            dl.Polyline(positions=[rotterdam_coords, paris_coords], color="red", weight=5),
            dl.Polyline(positions=[miami_coords, dublin_coords], color="green", weight=5,
                        children=dl.Tooltip("HAPAG")),
            dl.Polyline(positions=[dublin_coords, hamburg_coords], color="green", weight=5,
                        children=dl.Tooltip("HAPAG")),
        ]
    else:

        # Year 2 configuration (swap "Maersk" and "HAPAG")
        children = [
            dl.Polyline(positions=[baltimore_coords, rotterdam_coords], color="green", weight=5,
                        children=dl.Tooltip("HAPAG")),
            dl.Polyline(positions=[rotterdam_coords, paris_coords], color="green", weight=5),
            dl.Polyline(positions=[miami_coords, dublin_coords], color="red", weight=5,
                        children=dl.Tooltip("Maersk")),
            dl.Polyline(positions=[dublin_coords, hamburg_coords], color="red", weight=5,
                        children=dl.Tooltip("Maersk")),
            dl.Polyline(positions=[los_angeles_coords,pacific_waypoint], color="red", weight=5,
                        children=dl.Tooltip("Maersk")),
            dl.Polyline(positions=[pacific_waypoint2,shanghai_coords], color="red", weight=5,
                        children=dl.Tooltip("Maersk")),
        ]

    return dl.Map(children + [dl.TileLayer()],
                  style={'width': '2000px', 'height': '1000px'},
                  center=baltimore_coords,
                  zoom=3,
                  id=map_key)


app.layout = html.Div([
    dcc.Graph(id='shipment-graph') ,
    dcc.Dropdown(
        id='year-dropdown',
        options=[
            {'label': 'Year 1', 'value': 'Year 1'},
            {'label': 'Year 2', 'value': 'Year 2'}
        ],
        value='Year 1'  # Default value
    ),
    html.Div(id='map-container')
])


@app.callback(
    Output('map-container', 'children'),
    Input('year-dropdown', 'value')
)
def update_map(selected_year):
    return create_map(selected_year)

@app.callback(
    Output('shipment-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_graph(selected_year):
    data = shipments_data[selected_year]
    carriers = list(data.keys())
    shipments = list(data.values())

    return {
        'data': [go.Bar(
            x=carriers,
            y=shipments,
            marker={'color': ['red', 'green']}
        )],
        'layout': go.Layout(
            title='Number of Shipments per Carrier',
            xaxis={'title': 'Carrier'},
            yaxis={'title': 'Number of Shipments'}
        )
    }


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)