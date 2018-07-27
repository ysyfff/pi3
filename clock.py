#coding=utf-8

from baidu.speech import speech
from datetime import datetime
from time import sleep

def get_integer():
    ctime = datetime.now()
    if ctime.minute == 0 and ctime.second == 0:
        return ctime.hour - 1
    return -2

print datetime.now().hour, '小时'
def query():
    while True:
        hour = get_integer()
        if hour > -2:
            speech(str(get_integer()) + '点整', 'clock', True)
        sleep(0.5)

if __name__ == '__main__':
    query()

