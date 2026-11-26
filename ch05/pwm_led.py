import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 8

GPIO.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED, 500)
pwm.start(0)

try:
    while 1:
        for duty in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.5)
        for duty in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
