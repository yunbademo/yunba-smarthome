#!/usr/bin/env python

import threading

gpio_lock = threading.Lock()

def acquire():
    gpio_lock.acquire()

def release():
    gpio_lock.release()

if __name__ == '__main__':
    pass

