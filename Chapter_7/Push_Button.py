import RPi.GPIO as GPIO
import time

LED = 17
P_Button = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(P_Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
try:
	while (True):
		a = GPIO.input(P_Button)
		if a == False:
			GPIO.output(LED,True)
		else:
			GPIO.output(LED,False)
finally:
	GPIO.cleanup()
	print("Cleaning Up!")
