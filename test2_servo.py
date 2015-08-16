
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
servoPin=18
GPIO.setup(servoPin,GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(servoPin,50)
p.start(6)

while(1):
	for x in range(0,180):
		DC=1./18.*(x)+2
		p.ChangeDutyCycle(DC)
		time.sleep(.01)


	for x in range(180,0,-1):
		DC=1./18.*x+2
		p.ChangeDutyCycle(DC)
		time.sleep(.01)
p.stop()
GPIO.cleanup()

