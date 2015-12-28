#!/usr/bin/env python

import time
import sys
import json
import types
import thread
from messenger import Messenger
import config
import led
import dht
import stepper_motor

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
    stepper_motor.forward(90)

def close_front_door():
    print('close_front_door')
    stepper_motor.backward(90)

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

def report_ht(messenger):
    ht = dht.get_ht()
    m = {}
    m['act'] = 'report_ht'
    m['h'] = ht[0]
    m['t'] = ht[1]

    msg = json.dumps(m)
    messenger.publish(msg, 1)
        
def main():
    messenger = Messenger(message_callback)
    
    while True: 
        report_ht()
        time.sleep(2)

if __name__ == '__main__':
    main()

