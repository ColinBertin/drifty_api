# from flask import Flask, request, jsonify

# app = Flask(__name__)



# @app.route('/')
# def hello_world():
#     class coords:
#         longitude = request.args.get('longitude')
#         latitude = request.args.get('latitude')
#     return coords.longitude
#     # print(longitude)
#     # print(latitude)


from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/')
def hello_world():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    return jsonify(longitude, latitude)
    # print(longitude)
    # print(latitude)
