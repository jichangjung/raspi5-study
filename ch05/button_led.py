import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 8
BUTTON = 18

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_on = False

def button_pressed(channel):
    global led_on
    led_on = not led_on
    GPIO.output(LED, led_on)
    print("LED", "켜짐" if led_on else "꺼짐")

GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_pressed, bouncetime=300)

try:
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
