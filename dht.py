#!/usr/bin/env python

import Adafruit_DHT as dht
import config

def get_ht():
    ht = dht.read_retry(dht.DHT22, config.DHT22_GPIO_NUM)

    h = '{0:0.1f}'.format(ht[0])
    t = '{0:0.1f}'.format(ht[1])

    return (h, t)

if __name__ == '__main__':
    ht = get_ht()
    print('The humidity and temperature:')
    print(ht)
