#!/usr/bin/env python

import time
import sys
import RPi.GPIO as GPIO

g_led_pwm = {}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def simple_turn_on(gpio_num):
    GPIO.setup(gpio_num, GPIO.OUT)
    GPIO.output(gpio_num, GPIO.HIGH)

def simple_turn_off(gpio_num):
    GPIO.setup(gpio_num, GPIO.OUT)
    GPIO.output(gpio_num, GPIO.LOW)

def turn_on(gpio_num, freq, dc):
    global g_led_pwm
    GPIO.setup(gpio_num, GPIO.OUT)
    g_led_pwm[gpio_num] = GPIO.PWM(gpio_num, freq)
    g_led_pwm[gpio_num].start(dc)

def turn_off(gpio_num):
    global g_led_pwm
    if g_led_pwm.has_key(gpio_num):
        g_led_pwm[gpio_num].stop()

def set_frequency(gpio_num, freq):
    global g_led_pwm
    if g_led_pwm.has_key(gpio_num):
        g_led_pwm[gpio_num].ChangeFrequency(freq)

def set_duty_cycle(gpio_num, dc):
    global g_led_pwm
    if g_led_pwm.has_key(gpio_num):
        g_led_pwm[gpio_num].ChangeDutyCycle(dc)

if __name__ == '__main__':
    gpio_num = 4
    freq = 30
    sleep_time = 2
    dc = 50

    print('simple_turn_on')
    simple_turn_on(gpio_num)
    time.sleep(sleep_time)

    print('simple_turn_off')
    simple_turn_off(gpio_num)
    time.sleep(sleep_time)

    print('turn_on')
    turn_on(gpio_num, freq, dc)
    time.sleep(sleep_time)

    print('set_frequency')
    set_frequency(gpio_num, freq / 2)
    time.sleep(sleep_time)

    print('set_duty_cycle')
    set_duty_cycle(gpio_num, dc / 2)
    time.sleep(sleep_time)

    print('turn_off')
    turn_off(gpio_num)
    time.sleep(sleep_time)

