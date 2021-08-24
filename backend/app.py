from flask import Flask, jsonify
import urllib3
import json


app = Flask(__name__)

http = urllib3.PoolManager()

@app.route('/')
def index():

    r = http.request('GET', 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date=2021-08-23&lang=en&cargo=false&arrival=false')

    print(type(r.data[0]))

    data = json.loads(r.data.decode('utf-8'))

    return jsonify({'data':data})
    

