try:
	f = open('test.txt')
	s = f.read()
	f.close()
except IOError:
	print("Cannot open the file")