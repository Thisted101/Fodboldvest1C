from machine import Pin, I2C
from machine import PWM
import umqtt_robust2 as mqtt
import ssd1306
from time import sleep
import ADC
import neopixel
import mpu6050
import gps_funktion
from imu import MPU6050  # https://github.com/micropython-IMU/micropython-mpu9x50
import time



#Initialisering af I2C objekt
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)



# OLED identification
i2c =I2C(-1,scl=Pin(26), sda=Pin(27)) # Pins of LED display goes here
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)

# # Neopixel identification

n = 12
p = 15
i = 1
np = neopixel.NeoPixel(Pin(p), n)

while True:
    try: 
#		batteri adafruit
        mqtt.web_print(ADC.get_battery())
        # opret nyt feed 'KasperBond213/feeds/IoT-Vest_Feed
        
#		SSD1306 OLED KODE		
        print("Step 1: OLED CODE INITIATE")
        oled.fill(0)
        bat = str(ADC.get_battery())+" %"
        oled.text(bat, 30,10,)
        oled.text('Battery left',15,30)
        oled.show()
        sleep(3)
    
#			GPS KODE			  
        print("Step 2: GPS CODE INITIATE")
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        mqtt.web_print(gps_data, 'KasperBond213/feeds/IoT-Vest_Feed/csv')    
        sleep(3)

#			IMU OG NEOPIXEL KODE			  
        print("Step 4: IMU AND NEOPIXEL INITIATE")
        
# imu kode og neopixel


    # reading values
        acceleration = imu.accel
        gyroscope = imu.gyro  
        print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2), "z: ", round(acceleration.z,2))

    #print ("gyroscope x: ", round(gyroscope.x,2), " y:", round(gyroscope.y,2),
          # "z: ", round(gyroscope.z,2))

# data interpretation (accelerometer)

        if abs(acceleration.x) > 0.8:
            if (acceleration.x > 0):
                print("The x axis points upwards")
            else:
                print("The x axis points downwards")

        if abs(acceleration.y) > 0.8:
            if (acceleration.y > 0):
                print("The y axis points upwards")
            else:
                print("I've fallen and I cant get up")
                if i == 1 :
                    np[0] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 2:
                    np[1] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 3:
                    np[2] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 4:
                    np[3] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 5:
                    np[4] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 6:
                    np[5] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 7:
                    np[6] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 8:
                    np[7] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 9:
                    np[8] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 10:
                    np[9] = (0, 50, 0)
                    np.write()
                    sleep(5)
                i = i +1
                print(i)

        if abs(acceleration.z) > 0.8:
            if (acceleration.z > 0):
                print("The z axis points upwards")
            else:
                print("player down")
                if i == 1 :
                    np[0] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 2:
                    np[1] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 3:
                    np[2] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 4:
                    np[3] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 5:
                    np[4] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 6:
                    np[5] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 7:
                    np[6] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 8:
                    np[7] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 9:
                    np[8] = (0, 50, 0)
                    np.write()
                    sleep(5)
                elif i == 10:
                    np[9] = (0, 50, 0)
                    np.write()
                    sleep(5)
                i = i +1
                print(i)

    # data interpretation (gyroscope)

        if abs(gyroscope.x) > 20:
            print("Rotation around the x axis")

        if abs(gyroscope.y) > 20:
            print("Rotation around the y axis")

        if abs(gyroscope.z) > 20:
            print("Rotation around the z axis")
        
        time.sleep(0.2)





        print("Step 5: END OF CODE")
        sleep(3)
        
        if len(mqtt.besked) != 0:
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO()          
        print(".", end = '')       
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()
        
