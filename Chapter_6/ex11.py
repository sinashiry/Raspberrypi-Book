import urllib.request
response = urllib.request.urlopen('http://google.com/')
contents = response.read()
print(contents)
