#!/usr/bin/python
#coding=utf-8

from datetime import datetime
from time import sleep
import os
import logging
import sys
from subprocess import call

logging.info('I told you so')
logging.warning('watch out')

logging.basicConfig(filename='haha.log',
        filemode='a',
        level=logging.DEBUG)

logging.info('Running urban planning')

log_path = os.path.dirname(os.path.realpath(__file__))
log_name = os.path.join(log_path, 'log.log')

def log(txt):
    call(['echo "' + txt + '" >> ' + log_name], shell=True)

if __name__ == '__main__':
    log('你妹的')
