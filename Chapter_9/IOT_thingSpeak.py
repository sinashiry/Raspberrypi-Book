import time, os, urllib, urllib2

PERIOD = 60 # Seconds
BASE_URL = 'https://api.thingspeak.com/update.json'
KEY = 'B6MRXE62RW0XB7KP'

def send_data(temp):
	data = urllib.urlencode({'api_key' : KEY, 'field1': temp})
	response = urllib2.urlopen(url=BASE_URL, data=data)
def cpu_temp():
	dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
	cpu_temp = dev.read()[5:-3]
	return cpu_temp
while True:
	temp = cpu_temp()
	print("CPU Temp (C): " + str(temp))
	send_data(temp)
	time.sleep(PERIOD)