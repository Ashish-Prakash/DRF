import requests
import json
URL = "http://127.0.0.1:8000/studentcreate/"

# data = requests.get(url=url)
data = {
    'name': 'Manjul',
    'roll': 21,
    'city': 'Haryana'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
