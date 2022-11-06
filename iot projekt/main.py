import umqtt_robust2 as mqtt
from machine import Pin, ADC, I2C, PWM
from time import sleep
import ssd1306
import neopixel
analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)
i2c =I2C(-1,scl=Pin(26), sda=Pin(27)) # Pins of LED display goes here
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)

def get_battery():
    analog_val = analog_pin.read()
#     print("Raw analog value: ", analog_val)
    volts = (analog_val * 0.00093) * 5
#     print("The voltage is:", volts, "v")
    battery_percentage = (volts/2)*100 - 320
    print("The battery percentage is:", battery_percentage, "%")
    

    mqtt.web_print(battery_percentage)
    return battery_percentage

while True:

    oled.fill(0)
    bat = str(get_battery())+" %"
    oled.text(bat, 30,10,)
    #oled.text('%', 80, 10)
    oled.text('Battery left',15,30)
    oled.show()
    sleep(1)