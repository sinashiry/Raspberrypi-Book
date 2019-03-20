import pickle

f = open('/home/pi/python_tutorial/mylist.p',"rb")     
a = pickle.load(f)        
f.close()
print ("X=",a) 					