#!/usr/bin/python
# coding=utf-8

from baidu.speech import speech
from datetime import datetime
from time import sleep


def get_integer():
    ctime = datetime.now()
    is_integer = False
    if ctime.minute == 0 and ctime.second <= 5:
        is_integer = True
    return is_integer, ctime.hour - 1, ctime.minute, ctime.second


def query():
    while True:
        is_integer, hour, minute, second = get_integer()
        print hour, minute, second
        if is_integer:
            speech('现在时间是:'+str(hour) + '点整', 'clock', True)
        elif minute % 15 == 0 and second <= 5:
            speech('现在时间是:'+str(hour) + '点' + str(minute) + '分',
                'clock_minute', True)
        sleep(0.5)


if __name__ == '__main__':
    query()
