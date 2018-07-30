#!/usr/bin/python
# coding=utf-8

from gpio import init, io, init2
from time import sleep


def nil(): return None


'''
hong wai gan ying qi

vcc --- 5v
out --- 11
gud --- 9
'''

port = 11



@init2(port, io.IN)
def receive(fn_someone, fn_nobody):
    while True:
        if io.input(port) == io.HIGH:
            print 'someone is closing'
            fn_someone()
        else:
            print 'nobody'
            fn_nobody()
        sleep(1)


if __name__ == '__main__':
    receive(nil, nil)
