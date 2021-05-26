from gpiozero import DistanceSensor, Motor
from time import sleep

right_sensor = DistanceSensor(23, 24, max_distance=4)
left_sensor = DistanceSensor(21, 20, max_distance=4)

motor = Motor(forward=4, backward=14)
stearing = Motor(forward=17, backward=18)
right = stearing.forward
left = stearing.backward


while True:
	left_distance = left_sensor.distance
	right_distance = right_sensor.distance
	print("left distance: {} right_distance: {}".format(left_distance, right_distance))
	if left_distance < 0.3 and right_distance < 0.3:
		print("Object detected, going backward")
		motor.backward(1)
		sleep(2)
		motor.stop()
	elif  left_distance > 0.5 and right_distance > 0.5:
		print("No object, going forward")
		stearing.stop()
		motor.forward(1)
		sleep(2)
		motor.stop()
	elif left_distance > right_distance:
		print("Turning left")
		left(1)
		sleep(0.2)
		motor.forward(1)
		sleep(2)
		motor.stop()
		stearing.stop()
	elif right_distance > left_distance:
		print("Turning right")
		right(1)
		sleep(0.2)
		motor.forward(1)
		sleep(2)
		motor.stop()
		stearing.stop()
	sleep(2)

