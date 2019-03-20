while True:
	temp = float(input("Dama ra vared konid(Celsius):"))
	print ("""Temperature:\nin Celsius:{:5.2f} deg C,
in Fahrenheit:{:5.2f} deg F,""".format(temp,temp*9/5+32))