import requests

responce = requests.get('http://127.0.0.1:5000/api?a=8&b=6')

print(responce.json())