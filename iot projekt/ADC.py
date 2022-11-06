import umqtt_robust2 as mqtt
from machine import Pin, ADC
from time import sleep

analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)


def get_battery():
    analog_val = analog_pin.read()
#     print("Raw analog value: ", analog_val)
    volts = (analog_val * 0.00093)
#     print("The voltage is:", volts, "v")
    battery_percentage = (volts/2)*100 - 320
    print("The battery percentage is:", battery_percentage, "%")
    sleep(0.7)
    

    mqtt.web_print(battery_percentage)

while True:
    get_battery()