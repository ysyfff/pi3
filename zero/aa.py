import RPi.GPIO as GPIO
import time
import signal
import atexit
 
atexit.register(GPIO.cleanup)  
  

#servopin = 22
servopin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(2)

while True:
    for i in range(0, 90, 10):
        p.ChangeDutyCycle(2.5 + 10 * i / 90)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.5)

    for i in range(120, 0, -10):
        p.ChangeDutyCycle(2.5 + 10 * i / 90)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.5)

