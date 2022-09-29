import requests

endpoint = "http://localhost:8000/api/products/1/update/" 

data = {
    "title": "Iphone 12",
    "price": 670.00
}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())