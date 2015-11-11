import pyupm_i2clcd as lcd
import time
import sensors

class LcdUi:
    '''
    Class encapsulating out LCD UI
    '''
    # Default value for lcd_line_num assumes 2-line Grove LCD 
    def __init__(self, lcd_line_num = 2):
        '''
        Initializer for our LCD UI. Activates the LCD and sets a couple of
        internal attributes for process management.
        '''
        if lcd_line_num <= 0:
            raise ValueError("Number of LCD lines cannot be zero or less than zero")
        self.lcd_line_num = lcd_line_num

        self.sensor_array = sensors.SensorArray()

        self.stop_data_acquisition = False

        if not self.sensor_array:
            raise ValueError("Cannot initialize sensor array")

        # Grove LCD at any connector marked as I2C on the Grove Base Shield.
        # This would be I2C bus number 0.
        self.grove_lcd = lcd.Jhd1313m1(0)
        if not self.grove_lcd:
            raise ValueError("Cannot initialize Grove LCD")
        
        # Green backlight, hardcoded for simplicity
        self.grove_lcd.setColor(0, 255, 0)

    def run(self):
        '''
        Runs sensor data acquisition continuously and displays data on an LCD.
        '''
        # This is a flag to stop the acquisition/display loop
        self.stop_data_acquisition = False

        while(not self.stop_data_acquisition):
            sensor_data = self.sensor_array.get_sensor_data()

            # Minimal preparation for multi-line and multi-sensor setup.
            # Each sensor data is displayed in a separate line, up to a configured
            # number of lines for a given LCD.
            for i in range(0, self.lcd_line_num):
                # Set cursor to the beginning of the line
                self.grove_lcd.setCursor(i,0)
                self.grove_lcd.write("{0}: {1}{2}".format(sensor_data[i]['shortname'], sensor_data[i]['value'], sensor_data[i]['units']))
            # Pause to actually see our information on the screen
            time.sleep(1)
            # Cleanup - the LCD doesn't do that for us
            self.grove_lcd.clear()

        # If we got out of the loop - someone signalled us to stop.
        # Let's shutdown the LCD.
        self.grove_lcd.displayOff()

    def stop(self):
        '''
        Method to stop data acquisition/display loop
        '''
        self.stop_data_acquisition = True

