from urllib.parse import urljoin 

print(urljoin('http://www.baidu.com', 'index.html;user?id=5#comment'))
print(urljoin('http://www.baidu.com/index.html;user?id=5#comment', \
              'www.baidu.com'))
print(urljoin('http://www.baidu.com/index.html;user?id=5#comment', \
              'http://www.bilibili.com'))
print(urljoin('http', 'www.baidu.com/index.html;user?id=5#comment'))
print(urljoin('www.baidu.com', 'index.html;user?id=5#comment'))
#scheme, netloc, path
