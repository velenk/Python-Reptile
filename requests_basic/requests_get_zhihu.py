import requests 
import re 

headers = {
    'User-Agent': 'Mozilla.5.0 (Macintosh; Intel Mac OS X 10_11_4) \
    App;eWebKit.537.36 (KHTML, like Gecko) \
    Chorme.52.0.2743.116 Safari.573.36'
}
r = requests.get('https://www.bilibili.com/blackboard/activity-rJobLZbbQ.html?\
spm_id_from=333.334.bili_bangumi.76', headers = headers)
pattern = re.compile('image.*?\.jpg', )
result = re.findall(pattern, r.text)
print(result)
