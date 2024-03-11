import json
# to convert a JSON string to Python Dictionary using json.loads() method of JSON module in Python.
sample_str = '{"name":"ayesha", "age":22}'

# parse json to dictionary
# loads string value to json
json_response = json.loads(sample_str)
print(json_response)
