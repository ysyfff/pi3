#!/usr/bin/python
# coding=utf-8

from gpio import init2, io
from time import sleep,time

TRIG_PORT = 38
ECHO_PORT = 40
DISTANCE = 45


def nil(): return ''

@init2(TRIG_PORT, io.OUT)
@init2(ECHO_PORT, io.IN)
def react(on, off):
    counter = 0
    while True:
        io.output(TRIG_PORT, io.HIGH)
        sleep(0.1)
        io.output(TRIG_PORT, io.LOW)

        while io.input(ECHO_PORT) == io.LOW:
            pass

        pulse_start = time()

        while io.input(ECHO_PORT) == io.HIGH:
            pass

        pulse_end = time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        print "distance: " + str(distance)
        if distance < DISTANCE:
            if counter == 0:
                counter += 1
                on()
                print '开灯'
            elif counter == 1:
                counter -= 1
                off()
                print '关灯'
            sleep(2)
        else:
            # 增加稳定性，弥补意外情况的发生，比如说
            if counter == 0:
                off()
            else:
                on()
        sleep(0.2)

if __name__ == '__main__':
    react(nil, nil)

