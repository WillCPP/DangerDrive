#danger drive - directions

#Google Maps Javascript API Key: AIzaSyDZWXeInvVOUuIe0xLKA65ygwHSRuxayxU
#Google Maps Directions API Key: AIzaSyAJiJ0E_yddGhKshaTTcbSE8HQmFyoHs4Y

import requests
def directions(x1, y1, x2, y2):
    key_dir = "AIzaSyAJiJ0E_yddGhKshaTTcbSE8HQmFyoHs4Y"
    origin_coord = str(x1) + ',' + str(y1)
    dest_coord = str(x2) + ',' + str(y2)
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+origin_coord+'&destination='+dest_coord+'&key='+ key_dir)
    print(r.text)

# Cincinnati to Dayton
directions(31.1031,84.5120,39.7589,84.1916)