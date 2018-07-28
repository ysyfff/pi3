import syst
import gpio
import time


GPIO_OUT = 16
def cleanup():
    gpio.io.cleanup()

@gpio.init
def init():
    gpio.io.setup(GPIO_OUT, gpio.io.OUT)

def open():
    print 'open'
    gpio.io.output(GPIO_OUT, gpio.io.LOW)

def close():
    print 'close'
    gpio.io.output(GPIO_OUT, gpio.io.LOW)


def controlWind():
    is_close = True
    while True:
        cpu_temp = float(syst.get_cpu_temp())
	print cpu_temp
        if cpu_temp >=45 and is_close:
            is_close = False
            open()
        elif cpu_temp < 40 and not is_close:
            is_close = True
            close()
        time.sleep(5)

if __name__ == '__main__':
   init()
   close()
   controlWind()

