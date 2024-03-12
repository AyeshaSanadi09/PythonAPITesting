*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Library  ../ReadContent/FetchJsonData.py

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/


*** Keywords ***
Fetching and Validating Request
    [Documentation]  Fetching and validating request code using get request
    [Arguments]  ${id}  ${actual_code}
    Create Session    url    ${BASE_URL}
    ${response}=  Get Request    url    api/studentsDetails/${id}
    ${expected_code}=  Convert To String    ${response.status_code}
    Should Be Equal    ${expected_code}    ${actual_code}


Fetching and returning request
    [Arguments]  ${id}  ${actual_code}
    Create Session    url    ${BASE_URL}
    ${response}=  Get Request    url    api/studentsDetails/${id}
    [Return]  ${response}


Featching and returning json
    ${json_data}=  returnJsonData
    [Return]  ${json_data}
