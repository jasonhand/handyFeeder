#from time import sleep


#from Tkinter import *
import RPi.GPIO as GPIO
import time

servoPin=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin,GPIO.OUT)
p = GPIO.PWM(servoPin,50)
p.start(5)

for x in range(0,3):
	desiredPosition=input("Which direction? 0-180 __")
	DC=1.8/18.*(desiredPosition)+2
	p.ChangeDutyCycle(DC)

p.stop()
GPIO.cleanup()

