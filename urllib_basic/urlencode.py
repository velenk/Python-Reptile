from urllib.parse import urlencode 

params = {
    'name':'germey',
    'age':'27'
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
