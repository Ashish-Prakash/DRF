import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def getData(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# getData(1)


def postData():
    data = {
        'name': 'ashish',
        'roll': 100,
        'city': 'kanpur'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

postData()


def putData():
    data = {
        'id': 1,
        'name': 'Diwakar'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# putData()


def deletData():
    data = {'id': '2'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# deletData()
