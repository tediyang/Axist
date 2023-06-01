#!/usr/bin/python3
""" this is to make request to google map api for direction """
from flask import jsonify, request
import requests

def map_direction():
    """ method that makes a get request to google api and returns the details """
    #create variable that stores the request to the api
    api_url = f"https://maps.googleapis.com/maps/api/directions/json?parameters={parameters}&key=YOUR_API_KEY"
    #check if response is correct
    if response.OK:
        #store the data is json format
        data = response.json()
        #index & slice through the json file to get the data on time taken to location and distance
        time_covered = data.get('routes', [])[0].get('legs', [])[0].get('duration', {}).get('text')
        alternative_routes = data.get('routes', [])[1:]
        distance = data.get('routes', [])[0].get('legs', [])[0].get('distance', {}).get('text')
        #return the values after doin the maths
        return time_covered, alternative_routes_distance

    else:
        return None, None, None

