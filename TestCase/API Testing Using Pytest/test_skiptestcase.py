import requests
import json
import pytest

url = "https://reqres.in/api/users"

@pytest.mark.smoke
def test_createUser():

    f = open("E:\\Step by Step Rest API Testing using Python + Pytest +Allure\\API Tutorial\\postReqData.txt", "r")
    data = f.read()
    # print(data)

    # parsing data to json format
    json_data = json.loads(data)

    response = requests.post(url, data=json_data)
    # print(response.content)
    assert response.status_code == 201

    json_response = json.loads(response.content)
    # print(json_response["id"])


@pytest.mark.skip
def test_createUser2():

    f = open("E:\\Step by Step Rest API Testing using Python + Pytest +Allure\\API Tutorial\\postReqData.txt", "r")
    data = f.read()
    # print(data)

    # parsing data to json format
    json_data = json.loads(data)

    response = requests.post(url, data=json_data)
    # print(response.content)
    assert response.status_code == 202

    json_response = json.loads(response.content)
    # print(json_response["id"])