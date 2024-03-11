import requests
from requests.auth import HTTPBasicAuth


def test_withbasicauth():
    response = requests.get("https://github.com/user", auth=HTTPBasicAuth('username','password'))
    print(response.text)
