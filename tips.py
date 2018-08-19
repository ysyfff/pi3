#!/usr/bin/python
#coding=utf-8

from time import sleep
from baidu.speech import speech
from get_ip import get_ip

if __name__ == '__main__':
    #say_boot()
    #say_ip()
    sleep(5)
    speech('勇哥勇哥，系统已经启动!', 'boot', False)
    ip = get_ip()
    speech('IP地址是：'+ip, 'ip_address', True)
