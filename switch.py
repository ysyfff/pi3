#!/usr/bin/python

# coding=utf-8

from gpio import init, io
from time import sleep

port = 12


'''
ji dian qi

vcc --- 5v
in --- 12
gun --- gun
'''


@init
def init_():
    io.setup(port, io.OUT)


class Switch:
    def __init__(self):
        self.is_on = False
        self.minute = 0.1
        self.second = self.minute * 60
        self.starter = 0
        init_()

    def count_down(self):
        while self.starter < self.second:
            self.starter += 1
            sleep(1)
        self.starter = 0

    def on(self):
        if not self.is_on and self.starter == 0:
            io.output(port, io.HIGH)
            self.is_on = True
            self.count_down()

    def off(self):
        if self.is_on and self.starter == 0:
            io.output(port, io.LOW)
            self.is_on = False


if __name__ == 'main':
    init_()
