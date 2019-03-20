import serial

serial_1 = serial.Serial('/dev/ttyAMA0', 9600)

FILE_Location = "/home/pi/IDs.txt"
opened_file = open(FILE_Location)
person_IDs = opened_file.read()
opened_file.close()


def search_person(code):
	global person_IDs
	find = False
	if code in person_IDs:
		find = True
	return find
	
while True:
	code = serial_1.readline()
	code_10 = code[1:11] 
	print "---------------------"
	print "Code = ",code_10
	Status = search_person(code_10)
	print "Status = ",Status
	