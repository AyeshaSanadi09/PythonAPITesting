import requests

response = requests.delete("https://reqres.in/api/users/2")

assert response.status_code != 204