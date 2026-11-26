import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

BUZZER = 12

GPIO.setup(BUZZER, GPIO.OUT)

scale = [262, 294, 330, 349, 392, 440, 494, 523]

pwm = GPIO.PWM(BUZZER, scale[0])
pwm.start(50)

try:
    for freq in scale:
        pwm.ChangeFrequency(freq)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
