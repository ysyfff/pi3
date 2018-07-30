#!/usr/bin/python
# coding=utf-8

from red import receive
from switch import Switch

switch_ = Switch()

if __name__ == '__main__':
    receive(switch_.on, switch_.off)
