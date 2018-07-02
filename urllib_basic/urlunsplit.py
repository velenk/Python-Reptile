from urllib.parse import urlunsplit

data = ['http', 'www.baidu.com', 'index.html;user', 'a=6', 'comment']
print(urlunsplit(data))
