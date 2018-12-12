import RPi.GPIO as GPIO
from time import sleep, time
from datetime import datetime
import subprocess


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
    f = now.strftime('%Y-%m-%d_%H-%M-%S') + 'jpg'
    exec('raspistill -o ' + '/camera/picture/' + f)

try:
    sw = 0
    while True:
        if GPIO.input(SWICH_PORT) == GPIO.HIGH:
            if sw != 0: continue # 連続押し防止
            sw = 1
            GPIO.output(LED_PORT, GPIO.HIGH)
            take_phote()
            continue

        else:
            sw = 0
            GPIO.output(LED_PORT, GPIO.LOW)
        sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()


