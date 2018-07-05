import requests 
import re 

headers = {
    'User-Agent': 'Mozilla.5.0 (Macintosh; Intel Mac OS X 10_11_4) \
    App;eWebKit.537.36 (KHTML, like Gecko) \
    Chorme.52.0.2743.116 Safari.573.36'
}
r = requests.get('https://www.zhihu.com/explore', headers = headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
