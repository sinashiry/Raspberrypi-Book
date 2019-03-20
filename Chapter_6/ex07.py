import pickle
x = int(input("INPUT:"))

f = open('/home/pi/python_tutorial/mylist.p', 'wb')     
pickle.dump(x, f)        
f.close() 					
