import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature

cpu = CPUTemperature()
cpu = cpu.temperature
now = time.localtime()

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
p = GPIO.PWM(27, 50) # frequency=50hz
p.start(100)

time.sleep(3)

while True:
    cpu = CPUTemperature()
    cpu = cpu.temperature
    if now.tm_hour < 6 or now.tm_hour > 22:

        if cpu < 35:
            p.start(0)
            time.sleep(30)

        if cpu > 35 and cpu < 55:
            p.start((cpu - 35)*4.5)
            time.sleep(30)

        if cpu > 55:
            p.start(100)
            time.sleep(30)


    if not now.tm_hour < 6 or now.tm_hour > 22:

        if cpu < 25:
            p.start(0)
            time.sleep(60)

        if cpu > 25 and cpu < 45:
            p.start((cpu - 25)*4.5)
            time.sleep(30)

        if cpu > 45:
            p.start(100)
            time.sleep(30)

