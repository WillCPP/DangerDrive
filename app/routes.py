import requests
import json
from flask import Flask, request, render_template
from app import app
import find_locations
from data import *
from keys import key_js

@app.route('/')
@app.route('/index')
def index():
    return render_template('web_prototype.html')

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def data_post():
    radio = request.form['radio']

    if radio == 'loc':
        start_latlong = find_locations.find_ip()
    elif radio == 'addr':
        start_street = request.form['start_street']
        start_csz = request.form['start_csz']
        start_latlong = find_locations.find_address(start_street + " " + start_csz)
    
    end_street = request.form['end_street']
    end_csz = request.form['end_csz']
    end_latlong = find_locations.find_address(end_street + " " + end_csz)

    dir = directions.directions(start_latlong[0], start_latlong[1], end_latlong[0], end_latlong[1])

    #get data here
    laMax = max(start_latlong[0], end_latlong[0])
    laMin = min(start_latlong[0], end_latlong[0])
    loMax = max(start_latlong[1], end_latlong[1])
    loMin = min(start_latlong[1], end_latlong[1])

    dr = DataReader(laMax, laMin, loMin, loMax)
    lst = dr.locations()

    markers = ""
    index = 0
    for c in lst:
        markers += "var m_" + str(index) + """ = new google.maps.Marker({position:{lat: """ 
        markers += str(c['LATITUDE']) + """, lng: """ + str(c['LONGITUD']) 
        markers += """}, map: map, icon: "http://maps.google.com/mapfiles/ms/icons/orange.png", title: "Crash Type: """ + str(c["HARM_EV"])
        markers += """| Vehicles: """ + str(c["VE_TOTAL"])
        markers += """| Fatalities: """ + str(c["FATALS"])
        markers += """| Amb. Response Time: """ + str(c["RESPONSE_HOUR"]) + ":" + format(c["RESPONSE_MIN"], '02d')
        markers += """"});"""

    totalCrashes = dr.totalCrashes()
    totalFatals = dr.totalFatals()
    totalWorst = format(dr.worstDriveTime()[0][0], '02d') + ":" + format(dr.worstDriveTime()[0][1], '02d')
    mostOccur = dr.mostOccur()[0][0]
    helpTime = dr.helpTime()
    
    return render_template('web_prototype_map.html', api_key=key_js, markers= markers, start_lat=start_latlong[0], start_lng=start_latlong[1], end_lat=end_latlong[0], end_lng=end_latlong[1], 
    totalCrashes=totalCrashes, totalFatals=totalFatals, totalWorst=totalWorst, mostOccur=mostOccur, helpTime=helpTime)
