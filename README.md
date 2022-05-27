# Drifty

# API access
```http://127.0.0.1:5000/?lon=12.0&lat=13.0```,
where `lon` is longitude, and `lat` is latitude

## Installation

- Install the python environment: `python3 -m venv venv`
- Activate it: `. venv/bin/activate`
- Install python dependencies: `python -m pip install -r requirements.txt`
- To use Ipython in venv see [this](https://stackoverflow.com/questions/20327621/calling-ipython-from-a-virtualenv) answer by TheDataGuy

## Notes

Using [this library](https://github.com/albertotb/get-gfs) to get GFS data
To run the server in debug mode (recompiles on when `app.py` is changed):
```export FLASK_ENV=development```
