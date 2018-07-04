from urllib.parse import parse_qs, parse_qsl

query = 'name=germey&age=22'
print(parse_qs(query))
print(parse_qsl(query))
