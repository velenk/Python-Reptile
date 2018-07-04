import urllib.robotparser as R
from urllib.request import urlopen 

rp = R.RobotFileParser()
rp.set_url('http://www.bilibili.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.bilibili.com'))

rp.parse(urlopen('http://www.bilibili.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://www.bilibili.com'))
