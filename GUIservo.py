from Tkinter import *

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)

p.start(50)
p.stop()

GPIO.cleanup()

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        p.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("150x50+0+0")
root.mainloop()
