'''
GeoPy Library in Python
GeoPy is a Python library that makes geographical computations easier, such as geocoding (turning addresses into coordinates) and reverse geocoding (turning coordinates into addresses). It supports multiple geocoding services like Google Maps, OpenStreetMap, and others.

Key Features:
Geocoding: Converting an address or place into geographical coordinates (latitude and longitude).
Reverse Geocoding: Converting geographical coordinates back into a physical address.
Distance Calculation: Calculating the distance between two points on the Earth.
Installation:
You can install GeoPy via pip:

bash
Copy code
pip install geopy

'''

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Initialize the geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Geocoding: Convert an address into latitude and longitude
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print((location.latitude, location.longitude))

# Reverse Geocoding: Convert coordinates into an address
location = geolocator.reverse("37.4219999, -122.0840575")
print(location.address)

# Calculate Distance: Between two locations using geodesic
location1 = (37.4219999, -122.0840575)
location2 = (40.748817, -73.985428)  # New York City
print(geodesic(location1, location2).kilometers)

'''
Output:
Geocoding gives you the latitude and longitude of a location.
Reverse Geocoding gives you the address corresponding to the coordinates.
Distance Calculation computes the distance between two sets of coordinates.
'''
