import RPi.GPIO as GPIO
import time
import sys
import signal

# Initially we don't know if the door is open or closed...
rightIsOpen = None
oldIsOpen = None
DOOR_SENSOR_PIN = 18

reed_door_open = True

reed_disconnected_time = time.time()
reed_connected_time = time.time()


def reedOneInRange(channel):
    global rightIsOpen
    oldIsOpen = rightIsOpen
    rightIsOpen = GPIO.input(DOOR_SENSOR_PIN)
    print(GPIO.input(DOOR_SENSOR_PIN))

    if (rightIsOpen and (rightIsOpen != oldIsOpen)):
        print("Space is unoccupied!")

    elif (rightIsOpen != oldIsOpen):
        print("Space is occupied!")


def my_callback(channel):

    if GPIO.input(DOOR_SENSOR_PIN):     # if port 25 == 1
        print("FIRST DISconnected")

    else:                  # if port 25 != 1
        print("FIRST connected")


# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM)

# This is the GPIO pin number we have one of the door sensor
# wires attached to, the other should be attached to a ground
RIGHT_DOOR_SENSOR_PIN = 18

# Set up the door sensor pins.
GPIO.setup(RIGHT_DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# add rising edge detection on a channel, ignoring further edges for 200ms for switch bounce handling
# falling means going from default 1 to 0 (=detected)
GPIO.add_event_detect(RIGHT_DOOR_SENSOR_PIN, GPIO.BOTH,
                      callback=my_callback, bouncetime=300)


def reed_door_ops():
    #print("reed_connected sec", int(time.time()-reed_connected_time))
    #print("reed_disconnected sec", int(time.time()-reed_disconnected_time))
    global reed_disconnected_time
    global reed_connected_time
    global reed_door_open

    if GPIO.input(DOOR_SENSOR_PIN):     # if port 25 == 1
        reed_connected_time = time.time()
        #reed_disconnected += 1
        if time.time() - reed_disconnected_time > 2 and reed_door_open == False:
            print("DOOR OPEN")
            reed_door_open = True
            return

    else:                  # if port 25 != 1
        reed_disconnected_time = time.time()

        #reed_connected += 1
        if time.time() - reed_connected_time > 2 and reed_door_open == True:
            print("DOOR CLOSED")
            reed_door_open = False
            return


while True:
    reed_door_ops()

    # time.sleep(50)         # wait 30 seconds

    # while True:
    #     reedOnePressDetected()

    # while True:
    #     leftOldIsOpen = leftIsOpen
    #     leftIsOpen = GPIO.input(LEFT_DOOR_SENSOR_PIN)

    #     rightOldIsOpen = rightIsOpen
    #     rightIsOpen = GPIO.input(RIGHT_DOOR_SENSOR_PIN)

    #     if (leftIsOpen and (leftIsOpen != leftOldIsOpen)):
    #         print("Left space is unoccupied!")

    #     elif (leftIsOpen != leftOldIsOpen):
    #         print("Left space is occupied!")

    #     if (rightIsOpen and (rightIsOpen != rightOldIsOpen)):
    #         print("Right space is unoccupied!")

    #     elif (rightIsOpen != rightOldIsOpen):
    #         print("Right space is occupied!")

    #     time.sleep(0.1)
