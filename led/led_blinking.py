import RPi.GPIO as GPIO
import time



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

led_blinking(21, 1, 0.1, 10)

