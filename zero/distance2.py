#!/usr/bin/python
# coding=utf-8

from gpiozero import GPIODevice, DistanceSensor, LED
from time import sleep, time

nowTime = lambda:int(round(time() * 1000))

sensor_outer = DistanceSensor(21, 20)
sensor_inner = DistanceSensor(26, 19)
led = LED(16)
status = 'off'
led.off()


people = 0
trigger_outer = False
trigger_inner = False
time_outer = 0
time_inner = 0
trigger_duration = 2

gd = GPIODevice(22)

while True:
    distance_inner = sensor_inner.distance * 100
    print gd.value, 'wtf'
    distance_outer = sensor_outer.distance * 100
    # print distance_outer,'-'*5, distance_inner
    if distance_outer < 45 and not trigger_outer:
        trigger_outer = True
        time_outer = nowTime()
        print time_outer, 'outer'
        sleep(0.01)
    if distance_inner < 45 and not trigger_inner:
        trigger_inner = True
        time_inner = nowTime()
        print time_inner, 'inner'
        sleep(0.01)

    # 如果触发了机关，并且触发了两个机关，计算人数
    if trigger_outer and trigger_inner:
        if time_outer < time_inner:
            people += 1
            print '进来一个人', people
        else:
            people -= 1
            print '出去一个人', people
        trigger_outer = False
        trigger_inner = False
        time_outer = 0
        time_inner = 0

        if people > 0:
            led.on()
        else:
            led.off()
        sleep(2)
    # 如果触发了一个机关，超过一定的时间没有触发第二个机关，清除触发
    now_time = nowTime()
    if trigger_outer and (now_time - time_outer > trigger_duration * 1000):
        trigger_outer = False
        time_outer = 0

    if trigger_inner and (now_time - time_inner > trigger_duration * 1000):
        trigger_inner = False
        time_inner = 0

    sleep(0.01)

