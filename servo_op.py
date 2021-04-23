import RPi.GPIO as GPIO
from time import sleep
import json


# get GPIO pin number from config
with open('config.json') as f:
    data = json.load(f)
pin = data['servo_pin']
open_pos = data['opened_pos_dutycycle']
close_pos = data['closed_pos_dutycycle']

# set up GPIO for movement
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)
pwm.start(0)


# turn to open the deadbolt
def open_bolt():
    pwm.ChangeDutyCycle(open_pos)
    sleep(1)

# turn to close the deadbolt
def close_bolt():
    pwm.ChangeDutyCycle(close_pos)
    sleep(1)

# stop servo
def stop():
    pwm.stop()