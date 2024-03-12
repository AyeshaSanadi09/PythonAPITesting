import json

def returnJsonData():
    f = open("ReadContent\data.json", 'r')
    data = f.read()
    # print(type(data))
    # converting data into json
    json_data = json.loads(data)
    # print(type(json_data))
    return json_data

# print(returnJsonData())