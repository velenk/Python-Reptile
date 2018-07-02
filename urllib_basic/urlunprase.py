from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.com', 'user', 'a=6', 'comment']
print(urlunparse(data))
