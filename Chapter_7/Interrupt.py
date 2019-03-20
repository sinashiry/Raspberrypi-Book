import RPi.GPIO as GPIO
import time
def my_callback(channel):
	print('####_RASPBERRY_PI_####')

P_Button = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(P_Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(P_Button, GPIO.FALLING, callback=my_callback)
i = 0
while True:
	time.sleep(100)
