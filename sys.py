#!/usr/bin/python
#coding=utf-8

import os

def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    print res
    return res

if __name__ == '__main__':
    get_cpu_temp()