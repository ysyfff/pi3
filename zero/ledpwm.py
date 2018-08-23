from gpiozero import PWMLED
from time import sleep

led = PWMLED(13)

while True:
    led.value = 0.1
    sleep(1)
    led.value = 0.2
    sleep(1)
    led.value = 0.3
    sleep(1)
    led.value = 0.4
    sleep(1)
    led.value = 0.5
    sleep(1)
    led.value = 0.6
    sleep(1)
    led.value = 0.7
    sleep(1)
    led.value = 0.8
    sleep(1)
    led.value = 0.9
    sleep(1)
    led.value = 1
    sleep(1)
