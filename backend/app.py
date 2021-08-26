from datetime import datetime
from functions import auth_for_airline_codes, get_hk_flights, get_airline_codes
from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():

    date = datetime(2021, 9, 1)

    real_date = str(date).split(' ')[0]

    print(real_date)

    data = get_hk_flights(date)

    print(data)

    return jsonify({'data':data['flights'].pagination(maximum = 10).to_json()})
    

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