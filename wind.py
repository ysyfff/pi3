import syst
import gpio
import time


GPIO_OUT = 16
@gpio.init
def init():
    gpio.io.setup(GPIO_OUT, gpio.io.OUT)

def open():
    gpio.io.output(GPIO_OUT, gpio.io.LOW)

def close():
    gpio.io.output(GPIO_OUT, gpio.io.HIGH)

def controlWind():
    while True:
        cpu_temp = float(syst.get_cpu_temp())
	print cpu_temp
        if cpu_temp >=45 :
            open()
        elif cpu_temp < 40:
            close()
        time.sleep(5)
            
if __name__ == '__main__':
   init()
   close()
   controlWind()
    
