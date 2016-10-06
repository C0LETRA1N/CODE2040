import requests

url = 'http://challenge.code2040.org/api/reverse'
dictionary = {"token": "f9ac431a86df26c7ad79ddaf8a1cf05f"}

r = requests.post(url, json=dictionary)

print(r.text)
print(r.text[::-1])

url = 'http://challenge.code2040.org/api/reverse/validate'
dictionary = {"token": "f9ac431a86df26c7ad79ddaf8a1cf05f", "string": r.text[::-1]}
#simple way to reverse the string without loops and extra variables

r = requests.post(url, json=dictionary)

if r.status_code != 200:
    print('Status: ', r.status_code, 'Error: ', r.reason)
else:
    print r
