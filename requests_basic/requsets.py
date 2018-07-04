import requests 

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

r = requests.post('https://www.baidu.com/')
r = requests.put('https://www.baidu.com/')
r = requests.delete('https://www.baidu.com/')
r = requests.head('https://www.baidu.com/')
r = requests.options('https://www.baidu.com/')
