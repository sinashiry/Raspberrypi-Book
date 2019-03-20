import urllib.request
response = urllib.request.urlopen('http://google.com/')
contents = response.read()

a = open('/home/pi/Desktop/test_Webpage.HTML', 'w')
contents=str(contents)
a.write(contents)
a.close