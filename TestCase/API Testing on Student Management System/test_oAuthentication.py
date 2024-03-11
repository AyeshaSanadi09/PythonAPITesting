import requests
import json
import jsonpath

def test_withoauth():
    token_url="https://thetestingworldapi.com/Token"
    data = {'grant_type':"password", 'username':"admin", "password":"adminpass"}

    tokenresponse = requests.post(token_url, data=data)
    print(tokenresponse.text)

    token_value = jsonpath.jsonpath(tokenresponse.json(), "access_token")

    auth = {'Authorization':'Bearer '+token_value[0]}
    response = requests.get("https://thetestingworldapi.com/api/StDetails/1104", headers=auth)
    print(response.text)
