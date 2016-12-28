#!/usr/bin/env python

import SUNXI_GPIO as GPIO
      
turn_foward = GPIO.PD0
turn_back  = GPIO.PD1
turn_left  = GPIO.PD2
turn_right = GPIO.PD3
steer_up = GPIO.PD5
steer_down = GPIO.PD6
steer_left = GPIO.PD8
steer_right = GPIO.PD9
steer_center = GPIO.PD4
     
GPIO.init()
GPIO.setcfg(turn_foward, GPIO.OUT)
GPIO.setcfg(turn_back, GPIO.OUT)
GPIO.setcfg(turn_left, GPIO.OUT) 
GPIO.setcfg(turn_right, GPIO.OUT)
GPIO.setcfg(steer_up, GPIO.OUT)
GPIO.setcfg(steer_down, GPIO.OUT)
GPIO.setcfg(steer_left, GPIO.OUT)
GPIO.setcfg(steer_right, GPIO.OUT)
GPIO.setcfg(steer_center, GPIO.OUT)

def reset():
    GPIO.output(turn_foward, GPIO.LOW)
    GPIO.output(turn_back, GPIO.LOW)
    GPIO.output(turn_left, GPIO.LOW)
    GPIO.output(turn_right, GPIO.LOW)

def steer_reset():
    GPIO.output(steer_up, GPIO.LOW)
    GPIO.output(steer_down, GPIO.LOW)
    GPIO.output(steer_left, GPIO.LOW)
    GPIO.output(steer_right, GPIO.LOW)
    GPIO.output(steer_center, GPIO.LOW)

def forward():
    GPIO.output(turn_foward, GPIO.HIGH)

def back():
    GPIO.output(turn_back, GPIO.HIGH)

def left():
    GPIO.output(turn_left, GPIO.HIGH)

def right():
    GPIO.output(turn_right, GPIO.HIGH)

def stop():
    reset()

def steering_up():
    GPIO.output(steer_up, GPIO.HIGH)

def steering_down():
    GPIO.output(steer_down, GPIO.HIGH)

def steering_left():
    GPIO.output(steer_left, GPIO.HIGH)

def steering_right():
    GPIO.output(steer_right, GPIO.HIGH)

def steering_center():
    GPIO.output(steer_center, GPIO.HIGH)

class Car(object):
     
    def forward(self):
        reset()
        forward()

    def backward(self):
        reset()
        back()

    def left(self):
        reset()
        left()

    def right(self):
        reset()
        right()

    def stop(self):
        stop()

    def steering_up(self):
        steer_reset()
        steering_up()

    def steering_down(self):
        steer_reset()
        steering_down()

    def steering_left(self):
        steer_reset()
        steering_left()

    def steering_right(self):
        steer_reset()
        steering_right()

    def steering_center(self):
        steer_reset()
        steering_center()

    def shutdown(self):
        reset()
        gpio.cleanup()   