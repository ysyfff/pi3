#!/usr/bin/python
# coding=utf-8

from gpio import init, io
from time import sleep

port = 32


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
        init_()

    def on(self):
        io.output(port, io.HIGH)
        print '12针脚输出高'

    def off(self):
        io.output(port, io.LOW)
        print '12针脚输出低'

if __name__ == 'main':
    init_()
