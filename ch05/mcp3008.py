import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_adc(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((r[1] & 3) << 8) + r[2]

try:
    while 1:
        value = read_adc(0)
        volt = value * 3.3 / 1023
        print("값: %4d   전압: %.2f V" % (value, volt))
        time.sleep(0.3)
except KeyboardInterrupt:
    pass

spi.close()
