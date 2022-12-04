import requests

URL = "http://127.0.0.1:8000/studentinfo/"

data = requests.get(url=URL)

json_data = data.json()

print(json_data)
