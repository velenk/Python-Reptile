import requests 

data = {
    'age': 22,
    'name': 'germey'
}
r = requests.get('http://httpbin.org/get', params = data)
print(r.text)

print(r.json())
print(type(r.json()))
