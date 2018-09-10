import RPi.GPIO as GPIO
import time
import signal
import atexit
 
atexit.register(GPIO.cleanup)  
counter = 0  
counter_nobody = 0

#servopin = 22
servopin = 26
port = 19
port2 = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
GPIO.setup(port, GPIO.IN)
GPIO.setup(port2, GPIO.OUT)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(2)

while True:
    counter += 1
    if counter == 9:
        p.ChangeDutyCycle(7.5 + 3)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.5)
        counter = 0
    if GPIO.input(port) == 0:
        print 'no body'
        counter_nobody += 1
        if counter_nobody == 5:
            counter_nobody = 0
            GPIO.output(port2, 0)
    else:
        counter_nobody = 0
        print 'some body'
        GPIO.output(port2, 1)

    p.ChangeDutyCycle(2 + 3)
    time.sleep(0.02)
    p.ChangeDutyCycle(0)
    time.sleep(0.5)

    p.ChangeDutyCycle(7.5 + 3)
    time.sleep(0.02)
    p.ChangeDutyCycle(0)
    time.sleep(0.5)

