import pyupm_grove as grove

class SensorArray:
    '''
    Class encapsulating our sensors and their data access methods
    '''
    def __init__(self):
        # Grove Temperature sensor at Analog In 0, hardcoded for simplicity
        TEMP_SENSOR_PIN = 0
        # Grove Light Sensor at Analog In 1, hardcoded for simplicity
        LIGHT_SENSOR_PIN = 1

        self.temp_sensor = grove.GroveTemp(TEMP_SENSOR_PIN)        
        self.light_sensor = grove.GroveLight(LIGHT_SENSOR_PIN)
        if not self.temp_sensor or not self.light_sensor:
            raise ValueError("Cannot initialize sensors")
    def get_sensor_data(self):
        '''
        Method to acquire data from sensors and pack that into a dictionary for later use
        '''
        # Add to this dictionary if you have more sensors.
        # Shortname is used for space-constrained output, e.g. 16-symbol LCD.
        return [ {'name': 'Temperature',     'shortname': 'Temp.',      'value': self.temp_sensor.value(),  'units': 'deg. C'},
                 {'name': 'Light intensity', 'shortname': 'Light int.', 'value': self.light_sensor.value(), 'units': 'lx'}
               ]
