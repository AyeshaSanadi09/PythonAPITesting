import json
import requests

# actual data
response = requests.get("https://httpbin.org/get")
print(response.text)


headerData = {"h1":"hahahha", "h2":"babbabba"}
response = requests.get("https://httpbin.org/get", headers=headerData)
print(response.text)