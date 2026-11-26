import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

BUTTON = 18

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while 1:
        if GPIO.input(BUTTON) == GPIO.LOW:
            print("눌림")
        else:
            print("안 눌림")
        time.sleep(0.2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
