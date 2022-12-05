import requests
import json

URL = "http://127.0.0.1:8000/studentcrud/"


def getData():
    data = {}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# getData()


def postData():
    data = {
        'name': 'Prashant',
        'roll': 113,
        'city': 'Haryana'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# postData()


def putData():
    data = {
        'id': 1,
        'name': 'Lalit',
        'roll': 113,
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# putData()


def deleteData():
    data = {
        'id': 2
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

deleteData()
