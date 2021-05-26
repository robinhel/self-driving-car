from gpiozero import Motor
from time import sleep

motor = Motor(forward=4, backward=14)
while True:
    print("Going forward")
    motor.forward()
    sleep(1)
    motor.stop()
    print("Going backward")
    motor.backward()
    sleep(1)
    motor.stop()
    sleep(1)
