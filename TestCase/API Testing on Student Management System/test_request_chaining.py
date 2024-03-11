import json
import requests
import jsonpath


def test_addStudentData():
    global id
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("TestCase//API Testing on Student Management System//studentdata.json", "r")
    # print(file.read())
    json_data = json.loads(file.read())
    response = requests.post(url, data=json_data)
    # print(response.text)
    id = jsonpath.jsonpath(response.json(), "id")
    print(id[0])


def test_getOneStudentData():
    url = f"https://thetestingworldapi.com/api/studentsDetails/{id[0]}"
    response = requests.get(url)
    print(response.text)


