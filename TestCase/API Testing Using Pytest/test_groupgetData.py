import json 
import requests
import jsonpath
import pytest

url = "https://reqres.in/api/users?page=2"

@pytest.mark.smoke
def test_getdata():
    response = requests.get(url)
    # print(response.text)

    # parsing response tto json format
    json_response = json.loads(response.text)

    # fetaching content from json response
    # pages = jsonpath.jsonpath(json_response, "total_pages") #it returns list 
    # print(pages[0])

    # featching advance content
    for i in range(0,3):
        name = jsonpath.jsonpath(json_response, f"data.[{i}].first_name")
        # print(name[0])