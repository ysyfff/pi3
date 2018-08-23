from gpiozero import LED
from time import sleep

port = 13

led = LED(port)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
