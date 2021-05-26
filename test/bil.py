from gpiozero import DistanceSensor, Motor
from time import sleep

right_sensor = DistanceSensor(23, 24)
left_sensor = DistanceSensor(21, 20)

motor = Motor(forward=4, backward=14)
stearing = Motor(forward=17, backward=18)
right = stearing.forward
left = stearing.backward


while True:
	left_distance = left_sensor.distance
	right_distance = right_sensor.distance

	print('Left distance to nearest object is', left_distance, 'm')
	print('Right distance to nearest object is', right_distance, 'm')
	if left_distance < 0.5 and right_distance < 0.5:
		print("Stop")
		motor.stop()
		stearing.stop()
	else:
		motor.forward()
		if left_distance < 0.8:
			print("Right")
			right()
		elif right_distance < 0.8:
			print("Left")
			left()
		else:
			stearing.stop()
	sleep(0.1)

