import requests
import json
from app import app
from Website import *

@app.route('/')
@app.route('/index')

def index():
    
    return one + two + """Hello""" + three