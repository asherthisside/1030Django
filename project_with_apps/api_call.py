# pip install requests
import requests 

response = requests.get("https://jsonplaceholder.typicode.com/users/")
data = response.json()
# print(type(data))

for i in data:
    print(i['name'])