import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while 1:
        print(GPIO.input(16))
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
