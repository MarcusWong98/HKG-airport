import urllib3
import json


def auth_for_airline_codes():

    http = urllib3.PoolManager()

    data = {
        "grant_type": "client_credentials",
        "client_id": "OltfPui6sKLwUvP3Lm3N1yd9qsM3P8SP",
        "client_secret": "CKfnTBGONpZ6hnmE"
    }

    encoded_data = json.dumps(data).encode("utf-8")

    r = http.request(
        'POST',
        'https://test.api.amadeus.com/v1/security/oauth2/token',
        headers={
            'Content-type': 'application/x-www-form-urlencoded'
        },
        body=encoded_data
    )

    token = json.loads(r.data.decode("utf-8"))['access_token']

    print(token)

    return token

    # -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"