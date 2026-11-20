from gpiozero import LED
from time import sleep

led = LED(17)

for i in range(25):      # 0부터 24까지, 25번 반복
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)

print("finish")              # 반복이 끝나면 여기로 내려와서 프로그램 종료
