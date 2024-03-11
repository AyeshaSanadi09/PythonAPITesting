import json
import requests
import jsonpath

def test_getStudentData():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    response = requests.get(url)
    # print(response.text)
    json_data = json.loads(response.text)
    print(json_data[22])


def test_getOneStudentData():
    url = "https://thetestingworldapi.com/api/studentsDetails/10090784"
    response = requests.get(url)
    print(response.text)
    json_data = response.json()
    id = jsonpath.jsonpath(json_data, "data.id")
    assert id[0] == 10090784