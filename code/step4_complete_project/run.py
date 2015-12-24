from webapp import flask_app
from lcdui import lcd_ui
import threading
import time

# This is our main control script, which starts all the pieces of our app

# Create a Web app/UI thread
web_ui_thread = threading.Thread(target = flask_app.run,
                                 args = ('0.0.0.0',),
                                 kwargs = { 'debug': True,
                                            'use_reloader': False,
                                          }
                                )
# Create a LCD data acquisition/display thread
lcd_ui_thread = threading.Thread(target = lcd_ui.run)

# Set threads to be daemons (die with the main process)
web_ui_thread.daemon = True
lcd_ui_thread.daemon = True
# Start both threads
web_ui_thread.start()
lcd_ui_thread.start()

# This is a dummy loop for the main app to continue running after starting threads
try:
    # We have no more work here, just wait
    while threading.active_count() > 1:
        time.sleep(1)
# This properly shuts down the LCD piece after CTRL+C is hit
except KeyboardInterrupt:
    print("Shutting down LCD UI, it may take up to 3 seconds...")
    lcd_ui.stop()
    # Give the LCD UI time to shut down
    time.sleep(3)
