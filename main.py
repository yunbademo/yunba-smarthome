#!/usr/bin/env python

import time
import sys
import json
import types
import threading
import signal
import socket
import logging
import RPi.GPIO as GPIO
from messenger import Messenger
import config
import led
import dht
import stepper_motor
import magnet_sw
from player import Player

logging.basicConfig()
player = Player()

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

def media_play(path):
    print('media_play')
    player.play(path)

def media_stop():
    print('media_stop')
    player.stop()

def media_pause():
    print('media_pause')
    player.pause()

def media_resume():
    print('media_resume')
    player.resume()

def message_callback(msg):
#    print('message_callback:')
#    print(msg)

    if not isinstance(msg, dict):
        return

    if msg['topic'] != config.ALIAS:
        return

    print('get a message:')
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
    elif m['act'] == 'media_play':
        media_play(m['path'])
    elif m['act'] == 'media_stop':
        media_stop()
    elif m['act'] == 'media_pause':
        media_pause()
    elif m['act'] == 'media_resume':
        media_resume()

def report_ht(messenger):
    ht = dht.get_ht()
    m = {}
    m['act'] = 'report_ht'
    m['h'] = ht[0]
    m['t'] = ht[1]

    msg = json.dumps(m)
    messenger.publish(msg, 1)

def report_door(messenger):
    m = {}
    m['act'] = 'report_door'
    m['st'] = magnet_sw.get_sw_status()

    msg = json.dumps(m)
    messenger.publish(msg, 1)

def report_light(messenger):
    m = {}
    m['act'] = 'report_light'
    m['living'] = led.get_status(config.LED_LIVING)
    m['bedroom'] = led.get_status(config.LED_BEDROOM)
    m['porch'] = led.get_status(config.LED_PORCH)

    msg = json.dumps(m)
    messenger.publish(msg, 1)

def sig_handler(sig, frame):
    print 'receive a signal:', sig
    sys.exit()

def is_network_ok():
  try:
    host = socket.gethostbyname('www.baidu.com')
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

def main():
    signal.signal(signal.SIGTERM, sig_handler)
    #signal.signal(signal.SIGINT, sig_handler)

    led.turn_on(config.LED_LIVING, 1, 50) #checking network
    led.turn_on(config.LED_BEDROOM, 1, 100)
    led.turn_on(config.LED_PORCH, 1, 100)

    while True:
        if is_network_ok():
            break
        time.sleep(2)
    led.turn_on(config.LED_LIVING, 4, 50) #network is ok, connecting socktio

    messenger = Messenger(message_callback)

    while True: 
        report_ht(messenger)
        time.sleep(0.5)
        report_door(messenger)
        time.sleep(0.5)
        report_light(messenger)
        time.sleep(2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print(e)
