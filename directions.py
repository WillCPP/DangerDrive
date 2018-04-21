#
#  directions.py
#  Danger Drive
#  
#  Created by Madeline Eckhart, William Cupp, and Sean Hearne on 4/12/18.
#  Copyright © 2018 University of Cincinnati. All rights reserved.


import requests
from keys import key_dir
def directions(x1, y1, x2, y2):
    origin_coord = str(x1) + ',' + str(y1)
    dest_coord = str(x2) + ',' + str(y2)
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+origin_coord+'&destination='+dest_coord+'&key='+ key_dir)
    #print(r.text)
    return r.text

# Cincinnati to Dayton
#directions(31.1031,84.5120,39.7589,84.1916)