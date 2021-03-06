#!/usr/bin/env python2.7  
# script by Jason Hand  
  
import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
  
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
  
GPIO.setup(18, GPIO.OUT)# set GPIO 18 as output for white led  
  
turn = GPIO.PWM(18, 180)    # create object white for PWM on port 18 at 100 Hertz  
  
turn.start(0)              # start white led on 0 percent duty cycle (off)  
  
# now the fun starts, we'll vary the duty cycle to   
# dim/brighten the leds, so one is bright while the other is dim  
  
pause_time = 0.02           # you can change this to slow down/speed up  

print "Press Control-C to stop the servo"  
try:  
    while True:  
        for i in range(0,3):      # 101 because it stops when it finishes 100  
            turn.ChangeDutyCycle(i)  
            sleep(pause_time)  
        for i in range(100,-1,-1):      # from 100 to zero in steps of -1  
            turn.ChangeDutyCycle(i)  
            sleep(pause_time)  


except KeyboardInterrupt:  
    turn.stop()            # stop the white PWM output  
    GPIO.cleanup()          # clean up GPIO on CTRL+C exit
print "Program terminated"  
