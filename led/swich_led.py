import RPi.GPIO as GPIO
import time

#PORTの定義
gpio23 = 23 # swich
gpio21 = 21 # led

#GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio23, GPIO.IN)
GPIO.setup(gpio21, GPIO.OUT)
GPIO.output(gpio21, GPIO.LOW)

try:
    while True:
        if (GPIO.input(gpio23) == GPIO.HIGH):
            print("high")
            GPIO.output(gpio21, GPIO.HIGH)
        else:
            print("low")
            GPIO.output(gpio21, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()


