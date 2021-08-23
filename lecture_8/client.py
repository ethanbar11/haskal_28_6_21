import requests

r = requests.get('http://127.0.0.1:5000/')
r2 = requests.get('http://127.0.0.1:5000/get_snake/Bilbo')
print(r.text)
print(r2.text)
