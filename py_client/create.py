import requests

headers = {"Authorization": "Bearer fc79bd25a52f0c202a00c1049ad501e60b723ddc"}
endpoint = "http://localhost:8000/api/products/"

data = {"title":"Redmi Mobile 10"}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
print(get_response.status_code)