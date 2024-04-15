import webbrowser


def find_city_on_google_earth(city_name):
    # Format the URL with the search query
    google_earth_url = f'https://earth.google.com/web/search/{city_name}'

    # Open Google Earth in the default web browser with the search query
    webbrowser.open(google_earth_url)


# Example: Find New York City on Google Earth
find_city_on_google_earth("New York City")

# The above function can be called with any city name to open Google Earth at the specified location.

'''
When you run this script, it should open the default web browser 
and display the Google Earth view for "New York City", or any other city 
passed as an argument to the function find_city_on_google_earth.
'''
