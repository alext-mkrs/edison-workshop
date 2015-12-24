from lcdui import lcd_ui
import time

# This is our main control script, which starts all the pieces of our app

print("Starting LCD UI data aquisition and display. Press CTRL+C to exit.")

try:
    # Create a LCD data acquisition/display thread
    lcd_ui.run()
# This properly shuts down the LCD piece after CTRL+C is hit
except KeyboardInterrupt:
    print("Shutting down LCD UI, it may take up to 3 seconds...")
    lcd_ui.stop()
    # Give the LCD UI time to shut down
    time.sleep(3)
    print("Done. Goodbye!")
