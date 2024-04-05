import webbrowser


def find_city_on_google_earth(city_name):
    # Format the URL with the search query
    google_earth_url = f'https://earth.google.com/web/search/{city_name}'

    # Open Google Earth in the default web browser with the search query
    webbrowser.open(google_earth_url)


# Example: Find New York City on Google Earth
find_city_on_google_earth("New York City")

'''
The webbrowser library provides a high-level interface to allow displaying 
Web-based documents to users. It can be used to open a specified webpage 
in the user's default browser. Here are five other examples of how the webbrowser 
library can be used:
'''

#Opening a website URL:
webbrowser.open('http://www.python.org')

#Opening a new browser window:
webbrowser.open_new('http://www.python.org')

#Opening a new browser tab:
webbrowser.open_new_tab('http://www.python.org')

#Opening a URL and returning the exit status:
success = webbrowser.open('http://www.python.org')
print(success)  # This will print True if the browser was opened successfully, False otherwise.

#Using a specific browser:
'''
You can also specify which browser to use (if the system has more than one). 
For instance, if you want to open a URL in Google Chrome, you can do so by 
creating a browser controller object and then calling its open() method:
'''
chrome = webbrowser.get('chrome')
chrome.open('http://www.python.org')


