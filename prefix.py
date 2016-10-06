import requests

url = 'http://challenge.code2040.org/api/prefix'
dictionary = {"token": "f9ac431a86df26c7ad79ddaf8a1cf05f"}
r = requests.post(url, json=dictionary)

prefix = r.json().get('prefix')
array = r.json().get('array')

pos = 0
found = []
while pos < len(array):
    if not array[pos].startswith(prefix):
        found.append(array[pos])
    pos += 1

url = 'http://challenge.code2040.org/api/prefix/validate'
dictionary = {'token': "f9ac431a86df26c7ad79ddaf8a1cf05f", 'array': found}
r = requests.post(url, json=dictionary)
if r.status_code != 200:
    print('Status: ', r.status_code, 'Error: ', r.reason)
else:
    print r
