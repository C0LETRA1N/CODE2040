import json
import requests

url = 'http://challenge.code2040.org/api/haystack'
dictionary = {"token": "f9ac431a86df26c7ad79ddaf8a1cf05f"}
r = requests.post(url, json=dictionary)
needle = r.json().get('needle')
haystack = r.json().get('haystack')
print(needle)
pos = 0
while pos < len(haystack):
    if needle == haystack[pos]:
        print(pos)
        break
    pos += 1
url = 'http://challenge.code2040.org/api/haystack/validate'
dictionary = {"token": "f9ac431a86df26c7ad79ddaf8a1cf05f", "needle": pos}
r = requests.post(url, json = dictionary)
print(r)
