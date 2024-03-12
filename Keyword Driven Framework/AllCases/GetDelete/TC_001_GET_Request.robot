*** Settings ***
Library  RequestsLibrary

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_001_GET_Request
    [Tags]  Smoke  Sanity
    Create Session    getStudentDetails    ${BASE_URL}
    ${response}=  GET On Session    getStudentDetails    api/studentsDetails
    Log To Console    ${response.status_code}
    Log To Console    ${response.text}
