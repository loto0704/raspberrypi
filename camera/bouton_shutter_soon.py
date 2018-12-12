import subprocess
import RPi.GPIO as GPIO
import time
import os
from picamera import PiCamera


picture_base_name = 'raspi_camera_' # 画像の名前（ベース）
file_count = len(os.listdir('/camera/picture'))
#picture_name = '/camera/picture' + picture_base_name + str(int(file_count + 1)) + '.jpg'
#picture_command = 'raspistill -o ' + picture_name # 以下の名前で写真を撮る



#PORTの定義
gpio23 = 23 # swich
gpio21 = 21 # led

#GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio23, GPIO.IN)
GPIO.setup(gpio21, GPIO.OUT)

def led_blinking(gpio_port, high_time, low_time, for_count): # port番号, 点滅の間隔, 何回点滅させるか
    # GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_port, GPIO.OUT)

    for i in range(for_count):
        GPIO.output(gpio_port, GPIO.HIGH)
        time.sleep(high_time)# 点灯時間
        GPIO.output(gpio_port, GPIO.LOW)
        time.sleep(low_time)# 消灯時間

    GPIO.cleanup()

def shatter_3(channel):
    led_blinking(gpio21, 0,5, 0.5, 3)
    camera.capture(picture_name)


try:
    while True:
        if GPIO.input(gpio23) == GPIO.HIGH:
            camera = PiCamera()
            picture_name = '/camera/picture/' + picture_base_name + str(int(file_count + 1)) + '.jpg'
            #camera_capture = camera.capture('picture/' + picture_name)
            GPIO.add_event_detect(gpio23, GPIO.RISING, callback = shatter_3, bouncetime = 5000)
            #GPIO.add_event_detect(gpio23, GPIO.RISING, callback=camera.capture(picture_name), bouncetime=5000)
            print("high")

        else:
            print("low")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

