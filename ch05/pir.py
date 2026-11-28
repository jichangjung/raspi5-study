import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIR = 16

GPIO.setup(PIR, GPIO.IN)

def motion(channel):
    if GPIO.input(PIR) == GPIO.HIGH:
        print("움직임 감지", time.strftime("%H:%M:%S"))
    else:
        print("조용함", time.strftime("%H:%M:%S"))

print("센서 안정화 대기 중... 가만히 계세요")
time.sleep(10)
print("감시 시작")

GPIO.add_event_detect(PIR, GPIO.BOTH, callback=motion)

try:
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
