import urllib.parse as p
import urllib.request as r

data = bytes(p.urlencode({'word':'hello'}), encoding = 'utf-8')
response = r.urlopen('http://httpbin.org/post', data = data)

print(response.read())
