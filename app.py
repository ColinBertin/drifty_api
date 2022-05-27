from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/')
def hello_world():
    try:
        longitude = float(request.args.get('lon'))
        latitude = float(request.args.get('lat'))
    except TypeError:
        return jsonify({"error": "longitude and latitude must be floating point numbers. The API can be called with e.g.: base_url/?lon=-12.0&lat=13.0"})
    return jsonify(longitude, latitude)
