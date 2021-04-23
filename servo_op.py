import RPi.GPIO as GPIO
from time import sleep
import json


# get GPIO pin number from config
with open('config.json') as f:
    data = json.load(f)
pin = int(data['servo_pin'])

# set up GPIO for movement
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.pwm(pin, 50)
pwm.start(0)
# TODO: set intial position for full turn


# turn to open the deadbolt
def open_bolt():
    pass

# turn to close the deadbolt
def close_bolt():
    pass

# stop servo
def stop():
    pass