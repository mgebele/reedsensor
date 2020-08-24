
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

servo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)



def setServoAngle(servo, angle):
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	time.sleep(0.3)
	pwm.stop()

# goes 45 degree in one direction and back
try:
  while True:
    setServoAngle(servo,30)
    time.sleep(1)
    setServoAngle(servo,0)
except KeyboardInterrupt:
  GPIO.cleanup()


