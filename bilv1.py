from gpiozero import DistanceSensor, Motor
from time import sleep

right_sensor = DistanceSensor(23, 24)
left_sensor = DistanceSensor(21, 20)

motor = Motor(forward=4, backward=14)
stearing = Motor(forward=17, backward=18)
right = stearing.forward
left = stearing.backward

speed = 0.1


while True:
	left_distance = left_sensor.distance
	right_distance = right_sensor.distance

	print('Left distance to nearest object is', left_distance, 'm')
	print('Right distance to nearest object is', right_distance, 'm')
	if left_distance < 0.5 and right_distance < 0.5:
		print("Object detected, stopping")
		motor.stop()
		stearing.stop()
                sleep(2)
                print("Going backward")
		motor.backward(0.8)
		sleep(3)
		motor.stop()
	else:
                print("Going forward, speed: {}".format(speed))
		motor.forward(speed)
		if left_distance < 0.8:
			print("Going forward right")
			motor.forward(0.8)
			right()
		elif right_distance < 0.8:
			print("Going forward left")
			motor.forward(0.8)
			left()
		else:
                        print("Going forward straight")
			stearing.stop()
			if speed < 0.9:
                                print("Accelerating {} + 0.1".format(speed))
				speed = speed + 0.1
	sleep(0.2)

