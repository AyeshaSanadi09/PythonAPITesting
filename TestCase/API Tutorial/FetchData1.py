import json
import requests

# making get request
response = requests.get("https://reqres.in/api/users?page=2")
# fetch response and display it
print(response.content)
print()

# fetch response code
print(response.status_code)
print()

# validating response code
# assert response.status_code == 201

# featch headers
print(response.headers)
print()
# print(response.headers['Date'])
print(response.headers.get("Date"))
print()
print(response.headers['Server'])
print()


# featch cokkies
print(response.cookies)
print()

# featch encoding
print(response.encoding)
print()

# featch elapsed time
print(response.elapsed)
print()
 