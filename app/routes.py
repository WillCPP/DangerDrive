import requests
import json
from flask import Flask, request, render_template
from app import app
import Website
import directions
import find_locations
from keys import key_java

@app.route('/')
@app.route('/index')
def index():
    #latlong = find_locations.find_ip()

    #render template for input page
    #custom render for output page
    #return Website.one + Website.two + """Lat: """ + str(latlong[0]) + """ Lng: """ + str(latlong[1]) + Website.three
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

    # processed_text = start_street.upper()
    # print(processed_text)
    # return processed_text
    #return dir
    return render_template('web_prototype_map.html', api_key=key_java, start_lat=start_latlong[0], start_lng=start_latlong[1], end_lat=end_latlong[0], end_lng=end_latlong[1])
