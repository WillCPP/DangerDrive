import requests
import json
from flask import Flask, request, render_template
from app import app
import Website
import directions
import find_locations

@app.route('/')
@app.route('/index')

def index():
    #latlong = find_locations.find_ip()

    #render template for input page
    #custom render for output page
    #return Website.one + Website.two + """Lat: """ + str(latlong[0]) + """ Lng: """ + str(latlong[1]) + Website.three
    return render_template('web_prototype.html')

@app.route('/', methods=['POST'])
#@app.route('/index', methods=['POST'])
def data_post():
    text = request.form['street']
    processed_text = text.upper()
    print(processed_text)
    return processed_text
