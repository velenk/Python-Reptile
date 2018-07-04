from urllib.parse import urlsplit, urlunsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[1])

data = ['http', 'www.baidu.com', 'index.html;user', 'a=6', 'comment']
print(urlunsplit(data))
