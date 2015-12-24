import sensors
import time

# This is our main control script, which starts all the pieces of our app

print("Starting data acquisition and display. Press CTRL+C to exit.")

# Setting up our data aquisition source
sensor_array = sensors.SensorArray()
if not sensor_array:
    raise ValueError("Cannot initialize sensor array")

try:
    # This starts a neverending data acquisition/display loop
    while True:
        sensor_data = sensor_array.get_sensor_data()
        # We may have several sensors, so let's loop over results
        for i in range(0, len(sensor_data)):
            print("{0}: {1}{2}".format(sensor_data[i]['shortname'], sensor_data[i]['value'], sensor_data[i]['units']))
        time.sleep(1)
# This properly shuts down the program after CTRL+C is hit
except KeyboardInterrupt:
    print("Shutting down sensor data aquisition...")
    del sensor_array
    print("Done. Goodbye!")

