import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)
Motor1A = 14 #  Input 1 of the controller IC
Motor1B = 4 #  Input 2 of the controller IC
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
forward=GPIO.PWM(Motor1A,100)
reverse=GPIO.PWM(Motor1B,100)
forward.start(0) 
reverse.start(0)
for x in range(0, 5):
	# this will run your motor in reverse direction for 2 seconds with 80% speed by supplying 80% of the battery voltage
	print "GO backward"
	forward.ChangeDutyCycle(0)
	reverse.ChangeDutyCycle(100)
	sleep(2)
	# this will run your motor in forward direction for 5 seconds with 50% speed.
	print "GO forward"
	forward.ChangeDutyCycle(100)
	reverse.ChangeDutyCycle(0)
	sleep(2)
#stop motor
print "Now stop"
forward.stop() # stop PWM from GPIO output it is necessary
reverse.stop() 
GPIO.cleanup()
