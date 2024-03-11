import json
import requests
import jsonpath


def test_AddStudentData():
    student_api_url = "https://thetestingworldapi.com/api/studentsDetails"

    f = open("TestCase//API Testing on Student Management System//studentdata2.json", "r")
    json_data = json.loads(f.read())

    response = requests.post(student_api_url, data=json_data)
    assert response.status_code == 201
    # print(response.text)
    id = jsonpath.jsonpath(response.json(), "id")
    print(id[0])


    skills_api_url = "https://thetestingworldapi.com/api/technicalskills"

    f = open("TestCase//API Testing on Student Management System//techincalskills.json", "r")
    json_data = json.loads(f.read())
    json_data["stId"] = id[0]
    json_data["idd"] = id[0]


    response = requests.post(skills_api_url, data=json_data)
    assert response.status_code == 200
    print(response.text)


    address_api_url = "https://thetestingworldapi.com/api/addresses"

    f = open("TestCase//API Testing on Student Management System//address.json", "r")
    json_data = json.loads(f.read())
    json_data["stId"] = id[0]

    response = requests.post(address_api_url, data=json_data)
    assert response.status_code == 200
    print(response.text)


    finaldetails_api_url = f"https://thetestingworldapi.com/api/FinalStudentDetails/{id[0]}"

    response = requests.get(finaldetails_api_url)
    assert response.status_code == 200
    print(response.text)