import requests

url = 'http://challenge.code2040.org/api/status'
dictionary = {"token": "f9ac431a86df26c7ad79ddaf8a1cf05f"}

r = requests.post(url, json=dictionary)

print r.json()
