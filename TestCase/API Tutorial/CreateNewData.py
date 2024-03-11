import requests
import json

f = open("postReqData.txt", "r")
data = f.read()
print(data)

# parsing data to json format
json_data = json.loads(data)

response = requests.post("https://reqres.in/api/users", data=json_data)
print(response.content)
assert response.status_code == 201

json_response = json.loads(response.content)
print(json_response["id"])