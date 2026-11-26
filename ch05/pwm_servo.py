import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

SERVO = 12

GPIO.setup(SERVO, GPIO.OUT)

pwm = GPIO.PWM(SERVO, 50)
pwm.start(0)

try:
    while 1:
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
except KeyboardInterrupt:
    pass

pwm.stop()
del pwm
GPIO.cleanup()
