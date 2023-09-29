#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task 3: Integration with a Google API
    
import requests

def get_lat_long(api_key, address):
    
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
  
    params = {
        'address': address,
        'key': api_key  
    }

    response = requests.get(endpoint, params=params)
    data = response.json() 
    
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
        return latitude, longitude
    else:
        error_message = data.get('error_message', 'Unknown error occurred')
        print(f'Error: {error_message}')
        return None, None

    
   
    

api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
address = '999 E Caribbean Dr, Sunnyvale, CA 94089, United States'

latitude, longitude = get_lat_long(api_key, address)

if latitude and longitude:
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')
else:
    print('Failed to retrieve location data.')
    
    

# Explanation:

# Function get_lat_long:
# Accepts a Google API key and an address as parameters.
# Constructs the API endpoint with the provided address and API key.
# Sends a GET request to the Google Maps Geocoding API.
# Parses the JSON response and extracts the latitude and longitude if the status is 'OK'.

# Example Usage:
# Replace 'YOUR_GOOGLE_MAPS_API_KEY' with your actual Google Maps API key.
# The address '1600 Amphitheatre Parkway, Mountain View, CA' is used as an example.
# If the API request is successful (status is 'OK'), it prints the latitude and longitude. Otherwise, it prints an error message.

# Data Processing Approach:
# The script processes data in JSON format received from the API.
# It checks the status in the response to ensure that the request was successful (status is 'OK').
# If successful, it extracts latitude and longitude from the JSON response.

# This approach provides a clear separation of concerns, making the code easy to read and maintain. It utilizes the requests library for making HTTP requests and follows best practices for error handling to ensure that the script behaves gracefully even in case of API request failures.

