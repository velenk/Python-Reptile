import urllib.request
import urllib.error
import socket

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout = 0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('Time Out')
