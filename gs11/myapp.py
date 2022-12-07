import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def getData(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    print(r.json())

getData(1)