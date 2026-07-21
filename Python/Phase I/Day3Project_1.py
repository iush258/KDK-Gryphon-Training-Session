import requests 
a=requests.get("https://jsonplaceholder.typicode.com/users")
users= a.json()
for user in users:
    print(user["id"])
    print(user["name"])
    print(user["address"]["city"])
    print("========================")