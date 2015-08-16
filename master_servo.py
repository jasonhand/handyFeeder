
#Import libraries
import RPi.GPIO as GPIO
import time

#Set GPIO configs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Servo Settings and Variables
servoPin=18
GPIO.setup(servoPin,GPIO.OUT)
p = GPIO.PWM(servoPin,50)
#End of Servo Settings

#LED Settings
blueLED=21
GPIO.setup(blueLED,GPIO.OUT)
#End of LED Settings

#Begin looping through
z=input("How many times should we do this? ")
p.start(5)
for x in range(0,z):
	for x in range(0,180):
		GPIO.output(21,1)
		DC=1./18.*(x)+2
		p.ChangeDutyCycle(DC)
		time.sleep(.01)


	for x in range(180,0,-1):
		GPIO.output(21,0)
		DC=1./18.*x+2
		p.ChangeDutyCycle(DC)
		time.sleep(.01)
print "Gret job everyone! We looped that sumbitch %d times." % z
p.stop()
GPIO.cleanup()

