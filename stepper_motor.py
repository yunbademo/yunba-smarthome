#!/usr/bin/env python

import time
import sys
import RPi.GPIO as GPIO
import config

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(config.STEP_MOTOR_IN1, GPIO.OUT)
GPIO.setup(config.STEP_MOTOR_IN2, GPIO.OUT)
GPIO.setup(config.STEP_MOTOR_IN3, GPIO.OUT)
GPIO.setup(config.STEP_MOTOR_IN4, GPIO.OUT)

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
    sleep = 100
    for i in range(0, step):
        forward_one_step(sleep / 1000.0)
        if sleep > 10:
            sleep = sleep - 10
    set_motor_input(0, 0, 0, 0)

def backward(step):
    sleep = 100
    for i in range(0, step):
        backward_one_step(sleep / 1000.0)
        if sleep > 10:
            sleep = sleep - 10
    set_motor_input(0, 0, 0, 0)

if __name__ == '__main__':
    forward(100)
    time.sleep(2)
    backward(100)
    
