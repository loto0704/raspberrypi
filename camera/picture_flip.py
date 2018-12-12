import RPi.GPIO as GPIO
from time import sleep, time
from datetime import datetime
import subprocess
import cv2


# PORTの定義
LED_PORT = 21
SWICH_PORT = 23


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PORT, GPIO.OUT)
GPIO.setup(SWICH_PORT, GPIO.IN)

def exec(cmd):
    r = subprocess.check_output(cmd, shell=True)
    return r.decode('utf-8').strip()

def take_phote():
    now = datetime.now()
    f = now.strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
    exec('raspistill -o ' + '/camera/picture/' + f)
    return f

def picture_flip(picture_name):
    img = cv2.imread('/camera/picture/' + str(picture_name), cv2.IMREAD_COLOR)
    xAxis = cv2.flip(img, 0) # x軸反転
    cv2.imwrite('/camera/picture/' + str(picture_name), xAxis)

try:
    sw = 0
    while True:
        if GPIO.input(SWICH_PORT) == GPIO.HIGH:
            if sw != 0: continue # 連続押し防止
            sw = 1
            GPIO.output(LED_PORT, GPIO.HIGH)
            phote_name = take_phote()
            picture_flip(phote_name)
            continue

        else:
            sw = 0
            GPIO.output(LED_PORT, GPIO.LOW)
        sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()


