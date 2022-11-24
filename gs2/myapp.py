import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()


def put_data():
    data = {
        'name': 'Harsh',
        'roll': 104,
        'city': 'Bihar'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# put_data()


def update_data():
    data = {
        'id': 7,
        'name': 'Gulia',
        'roll': 122,
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


update_data()


def delete_data():
    data = {'id': 5}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# delete_data()
