import RPi.GPIO as GPIO
import time
import sys
import signal


# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM)

# Initially we don't know if the door is open or closed...
leftIsOpen = None
leftOldIsOpen = None
rightIsOpen = None
leftIsOpen = None

# This is the GPIO pin number we have one of the door sensor
# wires attached to, the other should be attached to a ground
RIGHT_DOOR_SENSOR_PIN = 18
LEFT_DOOR_SENSOR_PIN = 12

# Set up the door sensor pins.
GPIO.setup(LEFT_DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    leftOldIsOpen = leftIsOpen
    leftIsOpen = GPIO.input(LEFT_DOOR_SENSOR_PIN)

    rightOldIsOpen = rightIsOpen
    rightIsOpen = GPIO.input(RIGHT_DOOR_SENSOR_PIN)

    if (leftIsOpen and (leftIsOpen != leftOldIsOpen)):
        print("Left space is unoccupied!")
        GPIO.output(LEFT_RED_LIGHT, False)
        GPIO.output(LEFT_GREEN_LIGHT, True)
    elif (leftIsOpen != leftOldIsOpen):
        print("Left space is occupied!")
        GPIO.output(LEFT_GREEN_LIGHT, False)
        GPIO.output(LEFT_RED_LIGHT, True)

    if (rightIsOpen and (rightIsOpen != rightOldIsOpen)):
        print("Right space is unoccupied!")
        GPIO.output(RIGHT_RED_LIGHT, False)
        GPIO.output(RIGHT_GREEN_LIGHT, True)
    elif (rightIsOpen != rightOldIsOpen):
        print("Right space is occupied!")
        GPIO.output(RIGHT_GREEN_LIGHT, False)
        GPIO.output(RIGHT_RED_LIGHT, True)

    time.sleep(0.1)
