from webapp import flask_app
import time

# This is our main control script, which starts all the pieces of our app

print("Starting Web UI, see the next message for address and port")

# Start Web UI. Flask makes it quite easy, no need to even catch CTRL+C.
flask_app.run(host = '0.0.0.0',
              debug = True,
              use_reloader = False)

print("Done. Goodbye!")
