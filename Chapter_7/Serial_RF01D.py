import serial

serial_1 = serial.Serial('/dev/ttyAMA0', 9600)

while True:
	code = serial_1.readline()
	print code
