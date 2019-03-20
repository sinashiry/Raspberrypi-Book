list = [1, 2, 3]
try:
	list[8]
except:
	print("out of range")
else:
	print("in range")
finally:
	print("always do this")