#!/usr/bin/env python

import time
import thread
import Adafruit_DHT as dht
import config

h = 0.0
t = 0.0

def get_ht_thread():
    global h
    global t
    while True:
        ht = dht.read_retry(dht.DHT22, config.DHT22_GPIO_NUM)
        h = '{0:0.1f}'.format(ht[0])
        t = '{0:0.1f}'.format(ht[1])
        time.sleep(2)

def get_ht():
    return (h, t)

thread.start_new_thread(get_ht_thread, ())

if __name__ == '__main__':
    ht = get_ht()
    print('The humidity and temperature:')
    print(ht)
