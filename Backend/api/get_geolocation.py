#!/usr/bin/python3
""" Importing necessary modules """
import geocoder
import requests

def allow_access_to_location(api_key):
    """ This will ask users to grant access to device location """
    # Make a request to the Google Maps Geocoding API
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng=current_location&key={api_key}'
    response = requests.get(url)
    data = response.json()

    # Parse the JSON response and extract the location information
    if data['status'] == 'OK':
        results = data['results']
        if results:
            location = results[0]['formatted_address']
            return location
    return "Unknown"

def main():
    # API key for Google Maps Geocoding API
    api_key = 'api_key'

    # Allow access to location
    user_input = input("Allow app to access your location? (yes/no): ").lower()
    if user_input == "yes":
        current_location = allow_access_to_location(api_key)
        if current_location:
            print("Location:", current_location)
        else:
            print("Failed to retrieve the current location.")
    else:
        print("Location access denied.")

if __name__ == "__main__":
    main()

