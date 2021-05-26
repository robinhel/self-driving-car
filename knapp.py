from gpiozero import LED, Button
from time import sleep

led = LED(5)
button = Button(2)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
    sleep(1)
