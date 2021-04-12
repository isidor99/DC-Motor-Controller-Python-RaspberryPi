#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep


def parse_input(str):

	str = str.split(' ')
	motor = ''
	speed = 50
	forward = 0
	backward = 0

	if str[0] == 'start':
		if str[1] == '1' or str[1] == '2':
			motor = str[1]
		else:
			motor = '0'

		if str[2].isnumeric() and int(str[2]) < 100 and int(str[2]) > 0:
			speed = int(str[2])

		if str[3] == '-f':
			forward = 1
		elif str[3] == '-b':
			backward = 1

	elif str[0] == 'stop':
		speed = 0
		if str[1] == '1' or str[1] == '2':
			motor = str[1]
		else:
			motor = '0'

	elif str[0] == 'change_speed':
		speed = '-1'
		forward = -1
		backward = -1
		if str[1] == '1' or str[1] == '2':
			motor = str[1]
		else:
			motor = '0'

		if str[2].isnumeric() and int(str[2]) < 100 and int(str[2]) > 0:
			speed = int(str[2])

	elif str[0] == 'change_dir':
		speed = '-1'

		if str[1] == '1' or str[1] == '2':
			motor = str[1]
		else:
			motor = '0'

		if str[2] == '-f':
			forward = 1
		elif str[2] == '-b':
			backward = 1

	elif str[0] == 'end':
		motor = '-1'
		speed = 0

	elif str[0] == 'help':
		print('start [motor] [speed] [-f or -b]')
		print('stop [motor]')
		print('change_speed [motor] [speed]')
		print('change_dir [motor] [-f or -b]')
		print('end')

		motor = '0'
		speed = -1
		forward = -1
		backward = -1

	else:
		motor = '0'
		speed = -1
		forward = -1
		backward = -1

	return (motor, speed, forward, backward)


def start_motor(speed, forward, backward, motor_pwm, forward_pin, backward_pin):
	if speed != '-1':
		motor_pwm.start(speed)

	if forward == 1 and backward == 0:
		GPIO.output(forward_pin, GPIO.HIGH)
		GPIO.output(backward_pin, GPIO.LOW)
	elif forward == 0 and backward == 1:
		GPIO.output(forward_pin, GPIO.LOW)
		GPIO.output(backward_pin, GPIO.HIGH)
	elif forward == 0 and backward == 0:
		GPIO.output(forward_pin, GPIO.LOW)
		GPIO.output(backward_pin, GPIO.LOW)


motor_1_forward = 14
motor_1_backward = 15

motor_2_forward = 23
motor_2_backward = 24

pwm_motor_1 = 25
pwm_motor_2 = 7

# set GPIO mode and pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(motor_1_forward, GPIO.OUT)
GPIO.output(motor_1_forward, GPIO.LOW)
GPIO.setup(motor_1_backward, GPIO.OUT)
GPIO.output(motor_1_backward, GPIO.LOW)

GPIO.setup(motor_2_forward, GPIO.OUT)
GPIO.output(motor_2_forward, GPIO.LOW)
GPIO.setup(motor_2_backward, GPIO.OUT)
GPIO.output(motor_2_backward, GPIO.LOW)

GPIO.setup(pwm_motor_1, GPIO.OUT)
GPIO.setup(pwm_motor_2, GPIO.OUT)

motor_1 = GPIO.PWM(pwm_motor_1, 1000)
motor_2 = GPIO.PWM(pwm_motor_2, 1000)

try:
	while True:

		str = input()
		motor, speed, forward, backward = parse_input(str)

		print(motor, speed, forward, backward)

		if motor == '1':
			start_motor(speed, forward, backward, motor_1, motor_1_forward, motor_1_backward)
		elif motor == '2':
			start_motor(speed, forward, backward, motor_2, motor_2_forward, motor_2_backward)
		elif motor == '-1':
			break;

finally:
	GPIO.cleanup()
