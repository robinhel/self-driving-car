from gpiozero import DistanceSensor
from time import sleep

sensor1 = DistanceSensor(23, 24)
sensor2 = DistanceSensor(21, 20)
while True:
    print('Distance1 to nearest object is', sensor1.distance, 'm')
    print('Distance2 to nearest object is', sensor2.distance, 'm')
    sleep(1)
