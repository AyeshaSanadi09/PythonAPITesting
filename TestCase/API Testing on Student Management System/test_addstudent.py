import json
import requests


def test_addStudentData():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("TestCase//API Testing on Student Management System//studentdata.json", "r")
    # print(file.read())
    json_data = json.loads(file.read())
    response = requests.post(url, data=json_data)
    print(response.text)
