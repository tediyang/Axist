#!/usr/bin/python3

from flask import request, jsonify
import requests

def geo_geolocation():
    """ a get request to get the longitude and lat of a user's address """
    url = f"https://geo.ipify.org/api/v2/country?apiKey=YOUR_API_KEY&ipAddress={ip_address}"
    response = requests.get(url)

        #check if response is ok and return a json file
    if response.ok:
        data = response.json()
        #get the lat and long from the file
        longitude = data.get('location', {}).get("lng")
        latitide = data.get('location', {}).get("lat")
        return longitude, latitude

    else:
        return None, None
