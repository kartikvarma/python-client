import requests

x = requests.get("https://reqres.in/api/users?page=1")

print(x.status_code)