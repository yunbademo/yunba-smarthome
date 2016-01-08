#!/usr/bin/env python

import time
import sys 
import RPi.GPIO as GPIO
import config

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(config.MAGNET_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_sw_status():
    return GPIO.input(config.MAGNET_SWITCH)

if __name__ == '__main__':
    while True:
        st = get_sw_status()
        print(st)
        time.sleep(2)
