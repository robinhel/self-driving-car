# self-driving-car

## Overview
I used a standard cheap rc car for this project. To control the car I used an raspberry Pi with distance sensors connected to Pi´s IO pins. To power the standard battery pack is used, to power the Pi an external battery pack with usb is used.


## Images of the build process
Here are some images illustrating the build process and wire connections on the car and connection board.
![Connectionboard](connection_board.jpg)
![Car](car1.jpg)
![Car](car2.jpg)
![Car](car3.jpg)

## Raspberry Pi code overview
The code is developed in Python, gpiozero is used to control the distancesensor and motor.

There are 2 distance sensors (left, right) we initilize the sensors on the IO pins of the Pi.
There are 2 motors that controls forward/back and stearing (left/right) they are also initiated on the IO pins of the Pi.

Inside an continious foor loop I check the left and right distances for value <0.5, if left/right are true then the car will stop and reverse. If left/right distance is > 0.5 the car will continue driving until it detects distance <0.8 on either right or left side, then the car will counter steer the object.
