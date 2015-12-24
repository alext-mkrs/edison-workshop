from webapp import flask_app
from flask import render_template, jsonify
from socket import getfqdn
import sensors

def get_sensor_data():
    '''
    Utility function user to get a handle to data
    '''
    station_sensors = sensors.SensorArray()
    return station_sensors.get_sensor_data();

@flask_app.route('/')
@flask_app.route('/index')
def index():
    '''
    This is our main route for application entry
    '''
    return render_template('index.html',
                           sensor_data = get_sensor_data(),
                           station_name = getfqdn())

@flask_app.route('/get_weather_data')
def get_weather_data():
    '''
    This is our API endpoint used for AJAX calls
    '''
    return jsonify(data=get_sensor_data())
