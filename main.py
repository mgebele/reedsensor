import RPi.GPIO as GPIO
import time
import sys
import signal

# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM)

# This is the GPIO pin number we have one of the door sensor
# wires attached to, the other should be attached to a ground
DOOR_SENSOR_PIN = 17

# Initially we don't know if the door sensor is open or closed...
isOpen = None
oldIsOpen = None

# Set up the door sensor pin.
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    oldIsOpen = isOpen
    isOpen = GPIO.input(DOOR_SENSOR_PIN)
    print(GPIO.input(DOOR_SENSOR_PIN))

    if (isOpen and (isOpen != oldIsOpen)):
        print("Space is unoccupied!")

    elif (isOpen != oldIsOpen):
        print("Space is occupied!")

    time.sleep(0.1)
