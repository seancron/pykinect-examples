#!/usr/bin/env python

# Adapted from libfreenect python wrapper examples.
# https://github.com/OpenKinect/libfreenect/blob/master/wrappers/python/demo_tilt.py

import freenect
import time
import threading
import random

last_time = 0

def rand_led_tilt(dev, ctx):
    """Randomly changes the led and tilt position every 3 seconds"""
    
    global last_time

    if time.time() - last_time < 3:
        return
    last_time = time.time()

    led = random.randint(0, 6)
    tilt = random.randint(0, 30)
    freenect.set_led(dev, led)
    freenect.set_tilt_degs(dev, tilt)

    print('led[%d] tilt[%d] accel[%s]' % (led, tilt, freenect.get_accel(dev)))

if __name__ == '__main__':
    freenect.runloop(body=rand_led_tilt)
