# !/usr/bin/python
# coding=utf-8
from subprocess import check_output
from time import sleep


def get_ip():
    sleep(2)
    ip = check_output(['hostname', '-I'])
    ip = ip.replace(' \n', '')
    print ip, ip.split('.')[3]
    return ip


if __name__ == '__main__':
    get_ip()
