import requests
import iso8601
import datetime

url = 'http://challenge.code2040.org/api/dating'
dictionary = {"token": "f9ac431a86df26c7ad79ddaf8a1cf05f"}

r = requests.post(url, json=dictionary)

datestamp = r.json().get('datestamp')
interval = r.json().get('interval')

print datestamp

date_time = iso8601.parse_date(datestamp) + datetime.timedelta(seconds=int(interval))
final_time = date_time.isoformat()
#Had to remove extra data from end of the new date time and add the format at the end
final_time = final_time[:-6] + "Z"

print final_time

url = 'http://challenge.code2040.org/api/dating/validate'
dictionary = {'token': "f9ac431a86df26c7ad79ddaf8a1cf05f", 'datestamp': final_time}

r = requests.post(url, json=dictionary)

if r.status_code != 200:
    print('Status: ', r.status_code, 'Error: ', r.reason)
else:
    print r


