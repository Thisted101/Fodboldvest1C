from machine import I2C
from machine import Pin
from machine import sleep
import time
import mpu6050
import sys

#Initialisering af I2C objekt
i2c = I2C(scl=Pin(22), sda=Pin(21))     


while True:
    try:
      print(mpu.get_values())
      time.sleep(1)
    except KeyboardInterrupt:
      print("Ctrl+C pressed - exiting program.")
      sys.exit()

        
