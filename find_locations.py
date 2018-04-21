#
#  find_locations.py
#  Danger Drive
#
#  Created by Madeline Eckhart, William Cupp, and Sean Hearne on 4/12/18.
#  Copyright © 2018 University of Cincinnati. All rights reserved.


import requests
import json
from keys import key_java
def find_address(address):
    add = address.replace(' ', '+')
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+add+'&key='+ key_java)
    x = json.loads(r.text)
    lat = x["results"][0]["geometry"]["location"]["lat"]
    long = x["results"][0]["geometry"]["location"]["lng"]
    return (lat, long)


def find_ip():
    r = requests.get('http://ip-api.com/json')
    x = json.loads(r.text)
    lat = x["lat"]
    long = x["lon"]
    return (lat, long)

print(find_ip())