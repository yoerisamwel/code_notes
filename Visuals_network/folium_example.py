import folium

# Coordinates for Baltimore, Rotterdam, and Paris
baltimore = [39.2904, -76.6122]
rotterdam = [51.9225, 4.47917]
paris = [48.8566, 2.3522]

# Create a map centered around Baltimore
m = folium.Map(location=baltimore, zoom_start=4, tiles='cartodbpositron')

# Add lines connecting Baltimore -> Rotterdam -> Paris
folium.PolyLine([baltimore, rotterdam, paris], color="blue", weight=5, opacity=0.5).add_to(m)

# Display the map
m.save('supply_chain_map.html')