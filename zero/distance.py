from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(21, 20)
led = LED(16)
status = 'off'
led.off()

while True:
    distance = sensor.distance * 100
    print('Distance to nearest object is', distance, 'cm')
    if distance < 45:
        if status == 'off':
            status = 'on'
            led.on()
        else:
            status = 'off'
            led.off()
        sleep(2)
    sleep(0.2)
