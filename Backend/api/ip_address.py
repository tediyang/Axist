#!/usr/bin/python3
""" send a request to api.ipify.org to get ip address """
import requests
from flask import Flask, jsonify, request

def get_ip_address():
    """ returns users ip """
    response = request.get('https://api.ipify.org?format=json')
    #check if response is correct then return data, else return none
    if response.ok:
        data = response.json() #jsonified data
        return data.get('ip')
    else:
        return 'none'
