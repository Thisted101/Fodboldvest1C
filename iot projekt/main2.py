from machine import Pin, I2C
from machine import PWM
import umqtt_robust2 as mqtt
import ssd1306
from time import sleep
import ADC
import neopixel
#import adafruit_gps_main 

# OLED identification
i2c =I2C(-1,scl=Pin(26), sda=Pin(27)) # Pins of LED display goes here
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)


# # IMU identification
# tm = mpu6050.MPU6050(clk=Pin(22), dio=Pin(19))
# 
# # NeoPixel idenftication
# p = 18
# n = 8
# np = neopixel.NeoPixel(Pin(p), n)


### OLED message ###
oled.fill(0)
#oled.text('XXXX %',40,5,) # Print OLED text and adjust numbers for placement
# oled.text('Battery left',15,20)
oled.show()

while True:
    oled.fill(0)
    bat = str(ADC.get_battery())+" %"
    oled.text(bat, 30,10,)
    #oled.text('%', 80, 10)
    oled.text('Battery left',15,30)
    oled.show()
    sleep(1)


# def clear_neopixel():
#     for i in range(n):
#         np[i] = (0, 0, 0)
#         np.write()
#         
# def tilt_neopixel():
#     while True:
#         first = Tilt.value()
#         sleep (0.1)
#         second = Tilt.value()
#         global counter
#         
#         print("test loop1")
#         if first == 1 and second == 0:
#             print("test lys")
#             counter += 1
#             if counter >= 1 and counter < 8:
#                 for i in range (counter):
#                     np[i] = (0, 170, 0)
#                     np.write()
#             if counter >= 8:
#                 for i in range(n):
#                     np[i] = (170, 0, 0)
#                     np.write()
#             sleep(5)
# clear_neopixel()
# _thread.start_new_thread(tilt_neopixel, ())