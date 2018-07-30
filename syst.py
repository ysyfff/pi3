#!/usr/bin/python
# coding=utf-8

import os


def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "").replace("'C\n", ""))


if __name__ == '__main__':
    print get_cpu_temp()
