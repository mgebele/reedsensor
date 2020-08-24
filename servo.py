import RPi.GPIO as gpio
import time

servo = 18
gpio.setmode(gpio.BCM)
gpio.setup(servo, gpio.OUT)

p = gpio.PWM(servo, 50)
p.start(2.5)

# 2.5 für 0°, 

# 7.5 für 90° und 
# 12.5 für 180°
try:
  while True:
    p.ChangeDutyCycle(5.0)
    time.sleep(1)
    p.start(2.5)
except KeyboardInterrupt:
  p.stop()