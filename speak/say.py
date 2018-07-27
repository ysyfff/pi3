#!/usr/bin/python
#coding=utf-8

from subprocess import call

cmd_beg="espeak -vzh+f4 -g10 \""
cmd_end="\" 2>/dev/null"

def say_zh(content):
    call([cmd_beg + content + cmd_end], shell=True)

if __name__ == '__main__':
    say_zh('勇哥，你好')
