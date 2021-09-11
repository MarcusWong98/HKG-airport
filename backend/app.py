
from datetime import datetime
from functions import auth_for_airline_codes, get_hk_flights, get_airline_codes, pagination
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)

@app.route('/flights', methods = ['GET'])
def get_flights():

    now = datetime.now()

    print('now :')
    print(now)

    data = get_hk_flights(now)


    return jsonify({'flights':[ f.to_object() for f in pagination(data['flights'], maximum = 10)] })



    
@app.route('/flights', methods = ['POST'])
def post_find_flights():

    return jsonify({'data': 'test'})




@app.route('/auth')
def auth():
    # print(type(auth_for_airline_codes))


    token = auth_for_airline_codes()
   
    print(token)

    airline_codes = get_airline_codes(token = token)

    

    return jsonify({
        "token": token,
        "airline_codes": airline_codes
    })