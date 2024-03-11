import requests
import json
import jsonpath


def test_updateStudentData():
    url = "https://thetestingworldapi.com/api/studentsDetails/10090784"
    file = open("TestCase//API Testing on Student Management System//studentdata.json", "r")
    # print(file.read())
    json_data = json.loads(file.read())
    response = requests.put(url, data=json_data)
    print(response.tex)


def test_getOneStudentData():
    url = "https://thetestingworldapi.com/api/studentsDetails/10090784"
    response = requests.get(url)
    print(response.text)
    json_data = response.json()
    id = jsonpath.jsonpath(json_data, "data.id")
    assert id[0] == 10090784