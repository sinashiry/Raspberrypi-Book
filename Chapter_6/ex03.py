from datetime import datetime

d_t = datetime.now()
# String Format
print ("Date:{:%Y-%m-%d}, Time:{:%H:%M:%S}".format(d_t,d_t))
# Unchanged Format
print (d_t)
