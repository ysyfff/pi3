from subprocess import call

call(["espeak -ven+f4 -g10 \"hello world!\" 2> /dev/null"], shell=True)
