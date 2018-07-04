from urllib.parse import urlparse, urlunparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
#scheme://netloc/path;params?query#fragment 

result = urlparse('www.baidu.com/index.html;user?id=5#comment', \
                  scheme = 'https',allow_fragments = False)
print(result[4], result.query)

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))