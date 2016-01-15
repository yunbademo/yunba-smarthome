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

player = None
messenger = None

def light_on(name, freq, dc):
    print('light_on: %s, %d, %d' % (name, freq, dc))
    if name == 'living':
        led.turn_on(config.LED_LIVING, freq, dc)
    elif name == 'bedroom':
        led.turn_on(config.LED_BEDROOM, freq, dc)
    elif name == 'porch':
        led.turn_on(config.LED_PORCH, freq, dc)

def light_off(name):
    print('light_off: %s' % name)
    if name == 'living':
        led.turn_off(config.LED_LIVING)
    elif name == 'bedroom':
        led.turn_off(config.LED_BEDROOM)
    elif name == 'porch':
        led.turn_off(config.LED_PORCH)

def door_open():
    print('door_open')
    stepper_motor.forward(256)

def door_close():
    print('door_close')
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

def media_inc_vol():
    print('media_inc_vol')
    player.inc_vol()

def media_dec_vol():
    print('media_dec_vol')
    player.dec_vol()

def report_req():
    print('report_req')
    humtem_report()
    door_report()
    light_report()
    media_report()

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
    if m['act'] == 'light_on':
        light_on(m['name'], m['freq'], m['dc'])
    elif m['act'] == 'light_off':
        light_off(m['name'])
    elif m['act'] == 'door_open':
        door_open()
    elif m['act'] == 'door_close':
        door_close()
    elif m['act'] == 'media_play':
        media_play(m['path'])
    elif m['act'] == 'media_stop':
        media_stop()
    elif m['act'] == 'media_pause':
        media_pause()
    elif m['act'] == 'media_resume':
        media_resume()
    elif m['act'] == 'media_inc_vol':
        media_inc_vol()
    elif m['act'] == 'media_dec_vol':
        media_dec_vol()
    elif m['act'] == 'report_req':
        report_req()

def humtem_report():
    ht = dht.get_ht()
    m = {}
    m['act'] = 'humtem'
    m['h'] = ht[0]
    m['t'] = ht[1]

    msg = json.dumps(m)
    messenger.publish(msg, 1)

def door_report():
    m = {}
    m['act'] = 'door'
    m['st'] = magnet_sw.get_sw_status()

    msg = json.dumps(m)
    messenger.publish(msg, 1)

def light_report():
    m = {}
    m['act'] = 'light'
    m['living'] = led.get_status(config.LED_LIVING)
    m['bedroom'] = led.get_status(config.LED_BEDROOM)
    m['porch'] = led.get_status(config.LED_PORCH)

    msg = json.dumps(m)
    messenger.publish(msg, 1)

def media_report():
    m = {}
    m['act'] = 'media'
    m['st'] = player.status

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

def change_notify(name):
    if messenger == None:
        return

    if name == 'light':
        light_report()
    elif name == 'door':
        door_report()
    elif name == 'media':
        media_report()
    
def main():
    global player
    global messenger

    signal.signal(signal.SIGTERM, sig_handler)
    #signal.signal(signal.SIGINT, sig_handler)

    led.change_notify = change_notify
    stepper_motor.change_notify = change_notify
    led.change_notify = change_notify

    led.turn_on(config.LED_LIVING, 1, 50) #checking network
    led.turn_on(config.LED_BEDROOM, 1, 100)
    led.turn_on(config.LED_PORCH, 1, 100)

    while True:
        if is_network_ok():
            break
        time.sleep(2)
    led.turn_on(config.LED_LIVING, 4, 50) #network is ok, connecting socktio

    player = Player(change_notify)
    messenger = Messenger(message_callback)

    while True: 
        humtem_report()
        time.sleep(2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print(e)
