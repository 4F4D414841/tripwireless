#!/usr/bin/env python3

"""
Use with 433MHz magnetic security sensors to alert you
when one of your favorite things is moved/opened.
"""

import time
import pigpio
import _433

# Change RX to the GPIO pin being used on the Raspberry Pi
RX=27
favorite_things = {}

# Define optional callback for received codes, handled by _433

def rx_callback(code, bits, gap, t0, t1):
    if code in favorite_things:
        print(favorite_things[code], 'has been disturbed!')
    else:
        print('New code detected:' , code)
        new_thing = input('Write a name, or press Enter to skip:')
        if new_thing != '\r\n':
            favorite_things[code] = new_thing
        

pi = pigpio.pi() # Connect to local Pi

rx=_433.rx(pi, gpio=RX, callback=rx_callback)

# Keep script running indefinitely
while True:
    pass


