from flask import Flask, request, jsonify

app = Flask(__name__)
from helpers import get_wind_speed



@app.route('/')
def hello_world():
    try:
        latitude = float(request.args.get('lat'))
        longitude = float(request.args.get('lon'))
    except TypeError:
        return jsonify({"error": "longitude and latitude must be floating point numbers. The API can be called with e.g.: base_url/?lon=-12.0&lat=13.0"})

    #　Get data
    u, v = get_wind_speed(latitude, longitude)       
    return jsonify( {
        "lon": longitude, 
        "lat": latitude, 
        "wind_u": u[0,0],
        "wind_v": v[0,0]
    } )
