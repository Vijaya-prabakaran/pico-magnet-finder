from machine import Pin
import time
led = Pin(0,Pin.OUT)
reed = Pin(19,Pin.IN,Pin.PULL_DOWN)
while True:
    if reed.value() ==1:
        led.on()
        print("magnet detected")
    else:
        led.off()
        print("magnet not detected")
    time.sleep(0.05)
    