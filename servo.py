from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setServoAngle(servo, angle):
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()

if __name__ == '__main__':
	import sys
	servo = 18
	GPIO.setup(servo, GPIO.OUT)

    try:
        while True:
            setServoAngle(servo, 45)
            time.sleep(1)
            setServoAngle(servo, 0)
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
        
