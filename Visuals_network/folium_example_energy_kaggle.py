import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

import warnings
warnings.filterwarnings("ignore")

df1 = pd.read_csv("inventory_of_transmission_2021.csv",sep=";",encoding="latin-1")

df2 = pd.read_csv("inventory_of_transmission_2021.csv",sep=";",encoding="latin-1")
df2.rename(columns={"FromMemberType" : "FromAreaMemberType",'ToMemberType' : 'ToAreaMemberType'},inplace=True)
df3 = df2.copy()

dfs = [df1, df2, df3]  # Add more DataFrames if needed
# Concatenate all DataFrames in the list
df = pd.concat(dfs, ignore_index=True)
df = df.drop(['MeasureItem','MeasureTime','Flag','Value','ProvidedValue'],axis=1)
df.head().style.set_properties(
    **{
        'background-color': 'Brown',
        'color': 'white',
        'border-color': 'White'
    })

df['FromAreaCode'] = df['FromAreaCode'].replace({ 'FI': 'Finland',
'BG': 'Bulgaria','LU' : 'Luxembourg', 'HR' : 'Croatia', 'BE' : 'Belgium' , 'ME' : 'Montenegro' , 'NL' : 'Netherlands',
'DE': 'Germany','IT' : 'Italy', 'AT' : 'Austria', 'SE' : 'Sweden', 'PT' : 'Portugal', 'PL' : 'Poland', 'CH'  : 'Switzerland',
                                       'NO' : 'Norway' ,'LV' : 'Latvia', 'SK' : 'Slovak Republic', 'CZ' : 'Czech Republic' ,
                                               'GR' : 'Greece', 'EE' : 'Estonia', 'SI' : 'Slovenia', 'FR' : 'France',
                                               'RO' : 'Romania', 'MK' : 'Macedonia', 'RS' : 'Serbia', 'MD' : 'Moldova', 'BA' : 'Bosnia-Herzegovina',
                                               'XK' : 'Kosovo', 'GE' : 'Georgia', 'AL' : 'Albania', 'IE' : 'Ireland', 'CY' : 'Cyprus', 'UA' : 'Ukraine',
                                               'GB' : 'UnitedKingdom','DK' : 'Denmark', 'ES' : 'Spain', 'HU' : 'Hungary',
                                               'LT' : 'Lithuania' , 'RU' : 'Russia', 'TR' : 'Turkey', 'BY' : 'Belarus', 'MT' : 'Malta' , 'AM' : 'Armenia', 'AZ' : 'Azerbaijan'
})

df['ToAreaCode'] = df['ToAreaCode'].replace({ 'FI': 'Finland',
'BG': 'Bulgaria','LU' : 'Luxembourg', 'HR' : 'Croatia', 'BE' : 'Belgium' , 'ME' : 'Montenegro' , 'NL' : 'Netherlands',
'DE': 'Germany','IT' : 'Italy', 'AT' : 'Austria', 'SE' : 'Sweden', 'PT' : 'Portugal', 'PL' : 'Poland', 'CH'  : 'Switzerland',
                                       'NO' : 'Norway' ,'LV' : 'Latvia', 'SK' : 'Slovak Republic', 'CZ' : 'Czech Republic' ,
                                               'GR' : 'Greece', 'EE' : 'Estonia', 'SI' : 'Slovenia', 'FR' : 'France',
                                               'RO' : 'Romania', 'MK' : 'Macedonia', 'RS' : 'Serbia', 'MD' : 'Moldova', 'BA' : 'Bosnia-Herzegovina',
                                               'XK' : 'Kosovo', 'GE' : 'Georgia', 'AL' : 'Albania', 'IE' : 'Ireland', 'CY' : 'Cyprus', 'UA' : 'Ukraine',
                                               'GB' : 'UnitedKingdom','DK' : 'Denmark', 'ES' : 'Spain', 'HU' : 'Hungary',
                                               'LT' : 'Lithuania','RU' : 'Russia', 'TR' : 'Turkey', 'BY' : 'Belarus', 'MT' : 'Malta' , 'AM' : 'Armenia', 'AZ' : 'Azerbaijan'
})

df["Year_Mouth"] = df["Year"].astype(str) + "_" + df["Month"].astype(str)
df = df.rename(columns={'AVG_Value' : 'Power_Flow_GWh'})

NaM_only = df[(df['FromAreaMemberType'] == 'NaM' ) & (df['ToAreaMemberType'] == 'NaM')]

import json

# Prepare your data as a Python list of dictionaries
data = [
  { "name": "Albania", "latitude": 41.153332, "longitude": 20.168331 },
  { "name": "Armenia", "latitude": 40.069099, "longitude": 45.038189 },
  { "name": "Austria", "latitude": 47.516231, "longitude": 14.550072 },
  { "name": "Azerbaijan", "latitude": 40.143105, "longitude": 47.576927 },
  { "name": "Bosnia-Herzegovina", "latitude": 43.915886, "longitude": 17.679076 },
  { "name": "Belgium", "latitude": 50.503887, "longitude": 4.469936 },
  { "name": "Bulgaria", "latitude": 42.733883, "longitude": 25.48583 },
  { "name": "Belarus", "latitude": 53.709807, "longitude": 27.953389 },
  { "name": "Switzerland", "latitude": 46.818188, "longitude": 8.227512 },
  { "name": "Czech Republic", "latitude": 49.817492, "longitude": 15.472962 },
  { "name": "Germany", "latitude": 51.165691, "longitude": 10.451526 },
  { "name": "Denmark", "latitude": 56.26392, "longitude": 9.501785 },
  { "name": "Estonia", "latitude": 58.595272, "longitude": 25.013607 },
  { "name": "Spain", "latitude": 40.463667, "longitude": -3.74922 },
  { "name": "Finland", "latitude": 61.92411, "longitude": 25.748151 },
  { "name": "France", "latitude": 46.227638, "longitude": 2.213749 },
  { "name": "UnitedKingdom", "latitude": 55.378051, "longitude": -3.435973 },
  { "name": "Georgia", "latitude": 42.315407, "longitude": 43.356892 },
  { "name": "Greece", "latitude": 39.074208, "longitude": 21.824312 },
  { "name": "Croatia", "latitude": 45.1, "longitude": 15.2 },
  { "name": "Hungary", "latitude": 47.162494, "longitude": 19.503304 },
  { "name": "Ireland", "latitude": 53.41291, "longitude": -8.24389 },
  { "name": "Italy", "latitude": 41.87194, "longitude": 12.56738 },
  { "name": "Lithuania", "latitude": 55.169438, "longitude": 23.881275 },
  { "name": "Luxembourg", "latitude": 49.815273, "longitude": 6.129583 },
  { "name": "Latvia", "latitude": 56.879635, "longitude": 24.603189 },
  { "name": "Moldova", "latitude": 47.411631, "longitude": 28.369885 },
  { "name": "Montenegro", "latitude": 42.708678, "longitude": 19.37439 },
  { "name": "Macedonia", "latitude": 41.608635, "longitude": 21.745275 },
  { "name": "Malta", "latitude": 35.937496, "longitude": 14.375416 },
  { "name": "Netherlands", "latitude": 52.132633, "longitude": 5.291266 },
  { "name": "Norway", "latitude": 60.472024, "longitude": 8.468946 },
  { "name": "Poland", "latitude": 51.919438, "longitude": 19.145136 },
  { "name": "Portugal", "latitude": 39.399872, "longitude": -8.224454 },
  { "name": "Romania", "latitude": 45.943161, "longitude": 24.96676 },
  { "name": "Serbia", "latitude": 44.016521, "longitude": 21.005859 },
  { "name": "Russia", "latitude": 61.52401, "longitude": 105.318756 },
  { "name": "Sweden", "latitude": 60.128161, "longitude": 18.643501 },
  { "name": "Slovenia", "latitude": 46.151241, "longitude": 14.995463 },
  { "name": "Slovak Republic", "latitude": 48.669026, "longitude": 19.699024 },
  { "name": "Turkey", "latitude": 38.963745, "longitude": 35.243322 },
  { "name": "Ukraine", "latitude": 48.379433, "longitude": 31.16558 },
  { "name": "Kosovo", "latitude": 42.602636, "longitude": 20.902977 }
]

# Specify the filename
filename = "Europe.json"

# Open the file for writing in text mode
with open(filename, 'w') as f:
  # Write the data to the file as JSON using the json.dump function
  json.dump(data, f, indent=4)  # Optional: indent for readability

print(f"JSON data written to {filename}")

European_country = json.load(open("Europe.json", "r"))

# Merge the two dataframes on the common column 'FromAreaCode'
merged_df = df.merge(pd.DataFrame(European_country), left_on='FromAreaCode', right_on='name')

# Print the merged dataframe
#merged_df.head()

France_Export_2023 = merged_df[(merged_df['FromAreaCode'] == 'France') & (merged_df['Direction'] == 'Export') & (merged_df['Year'] == 2023)  ]

France_Export_2023 = France_Export_2023.groupby(['FromAreaCode', 'ToAreaCode'])['Power_Flow_GWh'].mean().reset_index()


import folium
from folium.plugins import AntPath

# Map center coordinates (replace with your desired location)
map_center = [46.227638, 2.213749]
zoom_start = 5

# Country names and corresponding power flow values (replace with your actual data)
countries = ["Belgium", "Germany", "Italy", "Spain",'Switzerland',"UnitedKingdom"]
power_flow_values = [768.458333, 1518.000000, 1849.083333,1183.320000,1314.852941,1673.741935]  # GWh values

# Sample latitude and longitude coordinates for each country (replace with actual data)
country_coords = {
    "Belgium": [50.503887, 4.469936],
    "Germany": [51.165691, 10.451526],
    "Italy": [41.87194, 12.56738],
    "Spain": [40.463667,-3.74922],
    "Switzerland": [46.818188,8.227512],
    "UnitedKingdom": [55.378051,-3.435973]
}

# Create the map
mapObj = folium.Map(location=map_center, zoom_start=zoom_start)

# Create markers with tooltips for country names and power flow values
markers = []
for country, power_flow, coords in zip(countries, power_flow_values, country_coords.values()):
    if coords:
        value_label = f"{country}: {power_flow} GWh"
        marker = folium.Marker(location=coords, popup=value_label)
        markers.append(marker)
    else:
        print(f"Coordinates not found for country: {country}")

# Add markers to the map
for marker in markers:
    marker.add_to(mapObj)

# Optional: Create animated paths (consider visual clarity with markers)
colors = ['red', 'blue', 'brown','Orange','Magenta','Purple']  # Customize colors as needed
for i, (country, coords) in enumerate(country_coords.items()):
    if coords:
        path_coords = [map_center, coords]
        AntPath(
            path_coords,
            delay=500 + 100 * i,  # Adjust delays for smoother animation
            weight=5,
            color=colors[i],
            dash_array=[20, 30],
            pulse_color='white'  # Adjust pulse color if desired
        ).add_to(mapObj)

# Save the map
mapObj.save('power_flow_map_with_markers_and_paths.html')

merged_df.dropna(subset=['latitude', 'longitude', 'name'], inplace=True)

df2 = merged_df.copy('deep')
df2 = df2[['Power_Flow_GWh','FromAreaCode','latitude','longitude']]

df_mean = df2.groupby(["FromAreaCode"]).mean()
df_mean = df_mean.reset_index()

import plotly.express as px
plt.figure(figsize=(20,7))

fig = px.scatter_mapbox(df_mean,
                        lat="latitude",
                        lon="longitude",
                        hover_name="FromAreaCode",
                        hover_data=["Power_Flow_GWh"],
                        color="Power_Flow_GWh",
                        zoom=1,
                        height=600,
                        size="Power_Flow_GWh",
                        size_max=30,
                        opacity=0.4,
                        width=1300)
fig.update_layout(mapbox_style='carto-positron')
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(title_text="Mean of trafic on sunday")
fig.show()

df2 = merged_df.copy('deep')
df2 = df2[['Power_Flow_GWh','FromAreaCode','latitude','longitude']]

df_sum = df2.groupby(["FromAreaCode"]).sum()
df_sum = df_sum.reset_index()

import geopandas as gpd
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.head()

# Assuming 'continent' is a column indicating continent
europe = world[world['continent'] == 'Europe']

data_merge = merged_df.merge(europe, on = 'name', how = 'left')

#pip install pycountry_convert

import pycountry_convert as pc
#import plotly_express as px
# Create data for the Map visualization 🦉
data3= merged_df.copy()
data3 = data3[data3['FromAreaCode'] != 'Bosnia-Herzegovina']
data3 = data3[data3['FromAreaCode'] != 'UnitedKingdom']
data3 = data3[data3['FromAreaCode'] != 'Kosovo']
# Create 1 collumn for country code of alpha3
data3['alpha3']= data3['FromAreaCode'].apply(lambda x: pc.country_name_to_country_alpha3(x))

fig= px.choropleth(data3,locations='alpha3',color='Power_Flow_GWh',scope='europe',
                    title='Europe Map for Power Flow in GWh')
fig.show()



