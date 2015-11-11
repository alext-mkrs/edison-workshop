Description
===========

This is a very simple, but complete application providing sensor data aquisition,
LCD UI and AJAX Web UI to the user. It is not intended to be production-ready, the
main goal is to provide a simple, but working and logically complete example
of one of the numerous ways one can use Edison.

Dependencies
============

The web app part of the code depends on Flask framework.

Make sure your Edison has access to the Internet and run the below to install it
using pip:

```
pip install flask
```

The sensor data acquisition and LCD UI part of this app depend on
mraa and UPM libraries, which should be already installed on Edison out of the box,
but you can always install them by following instructions at:

* mraa: https://github.com/intel-iot-devkit/mraa
* UPM: https://github.com/intel-iot-devkit/upm

Configuration
=============

The application expects to have a Grove Temperature sensor at Analog In 0,
Grove Light sensor at Analog In 1 (see `sensors.py`) and Grove 16x2 I2C LCD at
any Base Shield connector marked as "I2C" (see `lcdui.py`). Minimal preparations
are done for this to be expandable beyond this set, however for sake of simplicity
Grove Kit is the primary expected workshop vehicle for the time being, see
a "Bill of materials" section in the main README.

How to run the app
==================

Run the `run.py` script using Python. I've used Python 2 for development and
testing, so it's not guaranteed to work under Python 3.