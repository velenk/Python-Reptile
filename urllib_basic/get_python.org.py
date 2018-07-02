import urllib.request

response = urllib.request.urlopen('http://www.python.org')

print(response.read().decode('utf-8'))
#print(response.status)
#print(response.getheaders())
#print(response.getheader('Server'))
