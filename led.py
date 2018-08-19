#!/usr/bin/python
# coding=utf-8

#from red import receive
from switch import Switch
from hcsr04 import react

switch_ = Switch()

if __name__ == '__main__':
    #receive(switch_.on, switch_.off)
    react(switch_.on, switch_.off)
