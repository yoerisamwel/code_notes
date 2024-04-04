from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.geocoders import GoogleV3

#Google Maps Geocoding API (referred to as GoogleV3 in GeoPy),
geolocator = GoogleV3(api_key="API KEY", timeout=10)
# Initialize the geocoder
#geolocator = Nominatim(user_agent="geoapiExercises", timeout=10)

# Geocoding an address
address = "221B Baker St, London, UK"
location = geolocator.geocode(address)
print(f"Location: {location.latitude}, {location.longitude}")

# Reverse geocoding: Convert coordinates to address
coordinates = (location.latitude, location.longitude)
address = geolocator.reverse(coordinates)
print(f"Address: {address.address}")

# Calculate the distance between two points
point_a = (location.latitude, location.longitude)
point_b = (51.5007, -0.1246)  # Coordinates for the London Eye

# Calculate the distance between the two points
distance = geodesic(point_a, point_b).kilometers
print(f"Distance: {distance:.2f} km")













