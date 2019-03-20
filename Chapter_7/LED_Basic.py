import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
try:
	while (True):
		GPIO.output(17, True)
		time.sleep(0.5)
		GPIO.output(17, False)
		time.sleep(0.5)
finally:
	GPIO.cleanup()
	print("Cleaning Up!")