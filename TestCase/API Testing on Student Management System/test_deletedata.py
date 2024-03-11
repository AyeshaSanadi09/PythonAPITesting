import requests
import json
import jsonpath


def test_deleteStudentData():
    url = "https://thetestingworldapi.com/api/studentsDetails/10090784"
    file = open("TestCase//API Testing on Student Management System//studentdata.json", "r")
    response = requests.delete(url)
    print(response.text)


def test_getOneStudentData():
    url = "https://thetestingworldapi.com/api/studentsDetails/10090784"
    response = requests.get(url)
    print(response.text)
    json_data = response.json()
    id = jsonpath.jsonpath(json_data, "data.id")
    assert id[0] == 10090784