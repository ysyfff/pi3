#!/usr/bin/python
# coding=utf-8

from gpiozero import GPIODevice, LED, OutputDevice
from time import sleep, time

port = 27
#port = 19
gd = OutputDevice(port)

while True:
    gd.on()
    sleep(0.01*5)
    gd.off()
    print '0 度'
    sleep(1)
    gd.on()
    sleep(0.01*10)
    gd.off()
    print '45 度'

    sleep(5)
