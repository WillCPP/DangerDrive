#danger drive - find locations

#Google Maps Javascript API Key: AIzaSyDZWXeInvVOUuIe0xLKA65ygwHSRuxayxU
#Google Maps 

import requests
import json
def find_address(address):
    key_java = "AIzaSyDZWXeInvVOUuIe0xLKA65ygwHSRuxayxU"
    add = address.replace(' ', '+')
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+add+'&key='+ key_java)
    x = json.loads(r.text)
    lat = x["results"][0]["geometry"]["location"]["lat"]
    long = x["results"][0]["geometry"]["location"]["lng"]
    return (lat, long)

find_address("2050 Stedman Lane Beavercreek OH 45431")

   