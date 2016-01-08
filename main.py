#!/usr/bin/env python

import time
import sys
import json
import types
import thread
import signal
import RPi.GPIO as GPIO
from messenger import Messenger
import config
import led
import dht
import stepper_motor
import magnet_sw

def turn_on_living_light(freq, dc):
    print('turn_on_living_light: %d, %d' % (freq, dc))
    led.turn_on(config.LED_LIVING, freq, dc)

def turn_off_living_light():
    print('turn_off_living_light')
    led.turn_off(config.LED_LIVING)

def turn_on_bedroom_light(freq, dc):
    print('turn_on_bedroom_light: %d, %d' % (freq, dc))
    led.turn_on(config.LED_BEDROOM, freq, dc)

def turn_off_bedroom_light():
    print('turn_off_bedroom_light')
    led.turn_off(config.LED_BEDROOM)

def turn_on_porch_light(freq, dc):
    print('turn_on_porch_light: %d, %d' % (freq, dc))
    led.turn_on(config.LED_PORCH, freq, dc)

def turn_off_porch_light():
    print('turn_off_porch_light')
    led.turn_off(config.LED_PORCH)

def open_front_door():
    print('open_front_door')
    stepper_motor.forward(256)

def close_front_door():
    print('close_front_door')
    stepper_motor.backward(256)

def message_callback(msg):
    print('message_callback:')
    print(msg)

    if not isinstance(msg, dict):
        return

    if msg['topic'] != config.ALIAS:
        return

    print('get a message!')
    try:
        m = json.loads(msg['msg'])
    except Exception as e:
        print('json.loads exception:')
        print(e)
        return

    print('act: %s' % m['act'])
    if m['act'] == 'turn_on_living_light':
        turn_on_living_light(m['freq'], m['dc'])
    elif m['act'] == 'turn_off_living_light':
        turn_off_living_light()
    elif m['act'] == 'turn_on_bedroom_light':
        turn_on_bedroom_light(m['freq'], m['dc'])
    elif m['act'] == 'turn_off_bedroom_light':
        turn_off_bedroom_light()
    elif m['act'] == 'turn_on_porch_light':
        turn_on_porch_light(m['freq'], m['dc'])
    elif m['act'] == 'turn_off_porch_light':
        turn_off_porch_light()
    elif m['act'] == 'open_front_door':
        open_front_door()
    elif m['act'] == 'close_front_door':
        close_front_door()

def report_st(messenger):
    ht = dht.get_ht()
    m = {}
    m['act'] = 'report_ht'
    m['h'] = ht[0]
    m['t'] = ht[1]
    m['fd'] = magnet_sw.get_sw_status()

    msg = json.dumps(m)
    messenger.publish(msg, 1)

def sig_handler(sig, frame):
    print 'receive a signal:', sig
    sys.exit()


def main():
    signal.signal(signal.SIGTERM, sig_handler)
    #signal.signal(signal.SIGINT, sig_handler)

    led.turn_on(config.LED_LIVING, 1, 100)
    led.turn_on(config.LED_BEDROOM, 1, 100)
    led.turn_on(config.LED_PORCH, 1, 100)

    messenger = Messenger(message_callback)
    
    while True: 
        report_st(messenger)
        time.sleep(2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print(e)
