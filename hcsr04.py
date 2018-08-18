#!/usr/bin/python
# coding=utf-8

from gpio import init2, io
from time import sleep,time

TRIG_PORT = 38
ECHO_PORT = 40


def nil(): return NULL

@init2(TRIG_PORT, io.OUT)
@init2(ECHO_PORT, io.IN)
def react(on, off):
    while True:
        io.output(TRIG_PORT, io.HIGH)
        sleep(0.00001)
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

        sleep(0.2)

if __name__ == '__main__':
    react(nil, nil)
