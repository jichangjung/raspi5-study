import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

BUTTON = 18

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pressed(channel):
    print("눌림", channel)

GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_pressed, bouncetime=200)

try:
    while 1:
        print("다른 일 하는 중")
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
