# Function for : Kelvin => Celsius and Fahrenheit
def K_2_CF(K):
	C = K - 273
	F = C * 9 / 5 + 32
	return C,F

#Main Code
temp_k=int(input("Dama (kelvin):\t "))
temp_c,temp_f = K_2_CF(temp_k)
print ("in Kelvin=\t",temp_k)
print ("in Celsius=\t",temp_c)
print ("in Fahrenheit=\t",temp_f)