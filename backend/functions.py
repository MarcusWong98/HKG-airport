from datetime import datetime
# import urllib3
# from urllib.parse import ParseResultBytes, urlencode
from flask import jsonify
import requests, json
from classes import HK_flights

def auth_for_airline_codes():

    payload = {
        'grant_type': 'client_credentials',
        'client_id': 'OltfPui6sKLwUvP3Lm3N1yd9qsM3P8SP',
        'client_secret': 'CKfnTBGONpZ6hnmE'
    }

    r = requests.post(
        "https://test.api.amadeus.com/v1/security/oauth2/token",
        data=payload,
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )

    print(r.url)

    r_dict = r.json()

    return r_dict['access_token']


def get_hk_flights(date = datetime):

    year, month, day = date.year, date.month, date.day

    url = f'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={year}-{month}-{day}&lang=en&cargo=false&arrival=false'

    print(url)

    r = requests.get(url)

    # print(type(r.data[0]))

    data = r.json()


    return is_data_none(data)

def is_data_none(data):

    if 'problemNo' in data:
        
        return{
            'success': False,
            'message': 'Out of range'

        }

    else:
        print(len(data[0]['list']))

        return{
            'success': True,
            'flights': HK_flights(
                arrival = data[0]['arrival'],
                cargo = data[0]['cargo'],
                date = data[0]['date'],
                flights= data[0]['list']
            )


        }

def pagination(data, maximum = int, page = 1):

    first_page = maximum * page

    last_page = first_page + maximum

    return data[first_page:last_page]


def get_airline_codes(token):
    r = requests.get(
        'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&maxPrice=200',
        headers={
            "Authorization": "Bearer" + token
        }
    )

    r_dict = r.json()

    return r_dict