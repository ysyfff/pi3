#!/usr/bin/python
# coding=utf-8

from gpiozero import DistanceSensor, LED
from time import sleep, time

sensor_outer = DistanceSensor(21, 20)
sensor_inner = DistanceSensor(26, 19)
led = LED(16)
status = 'off'
led.off()

while True:
    distance_inner = sensor_inner.distance * 100
    distance_outer = sensor_outer.distance * 100
    print('Distance outer', distance_outer, 'cm')
    print('Distance inner', distance_inner, 'cm')
    print('-------------------'*2)
    if distance_outer < 45:
        if status == 'off':
            status = 'on'
            led.on()
        else:
            status = 'off'
            led.off()
        sleep(2)
    sleep(0.2)
