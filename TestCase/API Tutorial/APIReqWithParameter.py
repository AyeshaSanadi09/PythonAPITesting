import json
import requests

parameter = {"name":"alita", "gmail":"alita@123", "Age":22}

response = requests.get("https://httpbin.org/get", params=parameter)
print(response.text)