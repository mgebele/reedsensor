import RPi.GPIO as GPIO
import time
import sys
import signal


DOOR_SENSOR_PIN = 18
DOOR_SENSOR_PIN1 = 12
DOOR_SENSOR_PIN2 = 2

reed_door_open = True

reed_disconnected_time = time.time()
reed_connected_time = time.time()


# def my_callback(channel):

#     if GPIO.input(DOOR_SENSOR_PIN):     # if port 25 == 1
#         print("FIRST DISconnected")

#     else:                  # if port 25 != 1
#         print("FIRST connected")


# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM)

try:

    # Set up the door sensor pins.
    GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
except:
    print("DOOR_SENSOR_PIN error setup")

try:

    # Set up the door sensor pins.
    GPIO.setup(DOOR_SENSOR_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
except:
    print("DOOR_SENSOR_PIN1 error setup")

try:

    # Set up the door sensor pins.
    GPIO.setup(DOOR_SENSOR_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
except:
    print("DOOR_SENSOR_PIN2 error setup")

# # add rising edge detection on a channel, ignoring further edges for 200ms for switch bounce handling
# # falling means going from default 1 to 0 (=detected)
# GPIO.add_event_detect(RIGHT_DOOR_SENSOR_PIN, GPIO.BOTH,
#                       callback=my_callback, bouncetime=300)


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
