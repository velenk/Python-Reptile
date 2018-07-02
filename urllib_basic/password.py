import urllib.request as r
from urllib.error import URLError

username = 'username'
password = '123456'
url = 'http://localhost:5000/'

p = r.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = r.HTTPBasicAuthHandler(p)
opener = r.build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
