"""
File: chapter01/gpio_pkg_check.py
Source: Practical Python Programming for IoT
Author: Gary Smart
Modified by Kartik Bulusu (CS Dept., GWU)

This Python script checks for the availability of various Python GPIO Library Packages for the Raspberry Pi.
It does this by attempting to import the Python package. If the package import is successful
we report the package as Available, and if the import (or import initialization) fails for any reason,
we report the package as Unavailable.

Dependencies:
  pip3 install gpiozero pigpio RPi.GPIO

Built and tested with Python 3.7 on Raspberry Pi 4 Model B
Tested with Python 3.5.3 on Raspberry Pi 3B+
"""
try:
    import gpiozero
    print('GPIOZero   Available')
except:
    print('GPIOZero   Unavailable. Install with "pip install gpiozero"')
# sudo pigpiod  

try:
    import pigpio
    print('PiGPIO     Available')
except:
    print('PiGPIO     Unavailable. Install with "pip install pigpio"')

try:
    import RPi.GPIO
    print('RPi.GPIO     Available')
except:
    print('RPi.GPIO     Unavailable. Install with "pip install RPi.GPIO"')
    
try:
    import matplotlib
    print('matplotlib     Available')
except:
    print('matplotlib     Unavailable. Install with "pip install matplotlib"')    
# sudo apt-get install libopenblas-dev  
        
try:
    import numpy
    print('numpy     Available')
except:
    print('numpy     Unavailable. Install with "pip install numpy"')

try:
    import yagmail
    print('yagmail     Available')
except:
    print('yagmail     Unavailable. Install with "pip install yagmail"')
# sudo apt-get install libxml2-dev libxslt-dev  

try:
    import requests
    print('requests     Available')
except:
    print('requests     Unavailable. Install with "pip install requests"')
    
try:
    import dweepy
    print('dweepy     Available')
except:
    print('dweepy     Unavailable. Install with "pip install requests"')    
