#!/usr/bin/python
#coding=utf-8

import syst
import gpio
import time

'''
偶记
叫
叫
叫
我偶极矩
奇偶奇偶
急
'''
GPIO_OUT = 16

@gpio.init
def init():
    gpio.io.setup(GPIO_OUT, gpio.io.OUT)

def open():
    print 'open'
    gpio.io.output(GPIO_OUT, gpio.io.HIGH)

def close():
    print 'close'
    gpio.io.output(GPIO_OUT, gpio.io.LOW)


def controlWind():
    while True:
        cpu_temp = float(syst.get_cpu_temp())
	print cpu_temp
        if cpu_temp >=41 :
            open()
        elif cpu_temp < 40:
            close()
        time.sleep(5)

if __name__ == '__main__':
   init()
   close()
   controlWind()

