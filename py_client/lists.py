import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username':'rahulranjan', 'password':password})
print(auth_response.json())




#get_response = requests.post(endpoint, json={"title":"MI Phone", "price":66.0})
if auth_response.status_code==200:
    token = auth_response.json()['token']
    # headers = {
    #     "Authorization" : f"Token {token}"
    # }
    headers = {
         "Authorization" : f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())
    print(get_response.status_code)