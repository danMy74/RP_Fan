import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature

cpu = CPUTemperature()


GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

p = GPIO.PWM(27, 50) # frequency=50hz
p.start(7)
p.start(6)

time.sleep(2)

x = 0

while x < 5:

    print(cpu.temperature)

    time.sleep(1)

    a = (cpu.temperature)
    b = 50 #max_temp

    if a > b:
      p.ChangeDutyCycle(3.3)
      print("yes")

      while (cpu.temperature) > 41: #min_temp
          time.sleep(1)
          p.ChangeDutyCycle(3.3)
          print(cpu.temperature)


    else:
      print("no")
      p.ChangeDutyCycle(7)