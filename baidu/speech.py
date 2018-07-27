#!/usr/bin/python
#coding=utf-8

from aip import AipSpeech
from subprocess import call
from time import sleep
import os

APP_ID = '11595243'
API_KEY = 'NXXL0TWqhfomAI716poo3OcZ'
SECRET_KEY = 'tnVh0uYwGGBdPj0v2tVGhq2QtyQI9SuS'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def speech(content, file_name, fource_update):
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name + '.mp3')
    print file_path
    if os.path.exists(file_path) and fource_update == False:
        print '已经存在了，但是fource_update='+str(fource_update)
        call(["mpg123 " + file_path], shell=True)
    else:
	print '不存在，但是force_update='+str(fource_update)
        result = client.synthesis(content, 'zh', 1, {
            'vol': 10
        })
        if not isinstance(result, dict):
            with open(file_path, 'wb') as f:
                f.write(result)
        call(["mpg123 " + file_path], shell=True )


if __name__ == '__main__':
    speech('我不做大哥好多年', 'he', False)
