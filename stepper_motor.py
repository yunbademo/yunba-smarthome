#!/usr/bin/env python

import time
import sys
import Queue
import threading
import RPi.GPIO as GPIO
import config
import led 
import gpio_lock

steps_queue = Queue.Queue()
change_notify = None

def set_motor_input(i1, i2, i3, i4):
    GPIO.output(config.STEP_MOTOR_IN1, i1)
    GPIO.output(config.STEP_MOTOR_IN2, i2)
    GPIO.output(config.STEP_MOTOR_IN3, i3)
    GPIO.output(config.STEP_MOTOR_IN4, i4)

def forward_one_step(sleep_time):
    set_motor_input(1, 1, 0, 0)
    time.sleep(sleep_time)
    set_motor_input(0, 1, 1, 0)
    time.sleep(sleep_time)
    set_motor_input(0, 0, 1, 1)
    time.sleep(sleep_time)
    set_motor_input(1, 0, 0, 1)
    time.sleep(sleep_time)

def backward_one_step(sleep_time):
    set_motor_input(1, 0, 0, 1)
    time.sleep(sleep_time)
    set_motor_input(0, 0, 1, 1)
    time.sleep(sleep_time)
    set_motor_input(0, 1, 1, 0)
    time.sleep(sleep_time)
    set_motor_input(1, 1, 0, 0)
    time.sleep(sleep_time)

def forward(step):
    global steps_queue
    steps_queue.put(step)
    

def backward(step):
    global steps_queue
    steps_queue.put(-step)

def do_steps():
    global steps_queue

    if steps_queue.qsize() == 0:
        return;
    steps = steps_queue.get()
    if (steps > 0):
        step_fun = forward_one_step
        n = steps
    else:
        step_fun = backward_one_step
        n = -steps

    freq = led.get_frequency(config.LED_PORCH)
    dc = led.get_duty_cycle(config.LED_PORCH)
    status = led.get_status(config.LED_PORCH)

    led.turn_on(config.LED_PORCH, 2, 50)

    gpio_lock.acquire()
    for i in range(0, n):
        step_fun(0.01)
    set_motor_input(0, 0, 0, 0)
    gpio_lock.release()

    if status == 'on':
        led.turn_on(config.LED_PORCH, freq, dc)
    else:
        led.turn_off(config.LED_PORCH)
    status_notify()

def status_notify():
    if change_notify != None:
        change_notify('door')

def demon_thread():
    while True:
        do_steps()
        time.sleep(0.1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(config.STEP_MOTOR_IN1, GPIO.OUT)
GPIO.setup(config.STEP_MOTOR_IN2, GPIO.OUT)
GPIO.setup(config.STEP_MOTOR_IN3, GPIO.OUT)
GPIO.setup(config.STEP_MOTOR_IN4, GPIO.OUT)
set_motor_input(0, 0, 0, 0)

t = threading.Thread(target=demon_thread,args=())
t.setDaemon(True)
t.start()

if __name__ == '__main__':
    forward(100)
    time.sleep(2)
    backward(100)

#    t.join() # can not terminate by ctrl+c...

    while True:
        time.sleep(2)

