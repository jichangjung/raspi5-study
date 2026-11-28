import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18

GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.5)

try:
    while 1:
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        start = time.time()
        end = start
        while GPIO.input(ECHO) == GPIO.LOW:
            start = time.time()
        while GPIO.input(ECHO) == GPIO.HIGH:
            end = time.time()

        duration = end - start
        distance = duration * 34300 / 2
        print("거리: %.1f cm" % distance)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
