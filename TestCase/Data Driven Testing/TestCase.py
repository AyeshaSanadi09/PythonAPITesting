import requests
import json
import openpyxl 
from Library import Comman

# data driven testing means executing multiple data on same api at a time

def test_studentmultipledata():
    # reading studentdata.json file
    f = open("studentdata.json", "r")
    # parsing it into json
    json_data = json.loads(f.read())

    # reading xml file using openpyxl
    obj = Comman("studentmultipledata.xlsx", "Sheet1")
    col = obj.fetch_col_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_name()

    for i in range(2,row+1):
        updateRequest = obj.update_json_data(i, json_data, keyList)

        response = requests.post("https://thetestingworldapi.com/api/studentsDetails", data=updateRequest)
        print(response.text)
        assert response.status_code == 201
