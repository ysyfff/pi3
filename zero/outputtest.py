from gpiozero import OutputDevice
from time import sleep

v = OutputDevice(22)

while True:
    v.on()
    sleep(1)
    v.off()
