import requests
import json

f = open("putReqData.txt", "r")
json_data = f.read()

response = requests.put("https://reqres.in/api/users/2", data=json_data)
print(response.text)

assert response.status_code == 200

