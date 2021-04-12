#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

in_motor_1 = 14
in_motor_2 = 15
pwm_motor_1 = 23
pwm_motor_2 = 24

# set GPIO mode and pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(in_motor_1, GPIO.OUT)
GPIO.output(in_motor_1, GPIO.HIGH)

GPIO.setup(in_motor_2, GPIO.OUT)
GPIO.output(in_motor_2, GPIO.HIGH)

GPIO.setup(pwm_motor_1, GPIO.OUT)
GPIO.setup(pwm_motor_2, GPIO.OUT)

motor_1 = GPIO.PWM(pwm_motor_1, 1000)
motor_2 = GPIO.PWM(pwm_motor_2, 1000)

motor_1.start(90)
motor_2.start(90)

try:
	while True:
		sleep(10)

finally:
	GPIO.cleanup()
