*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/
${ID}  10092353

*** Test Cases ***
TC_004 DELETE STUDENT DATA BASED ON STUDENT_ID
    [Tags]  Regression
    Create Session    deleteStudent    ${BASE_URL}
    ${response}=  Delete Request    deleteStudent    api/studentsDetails/${ID}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    ${actual_code}=  Convert To String    ${response.status_code}  
    Should Be Equal    ${actual_code}    200
    ${response_json}=  To Json     ${response.content}
    # Log To Console    ${response_json}
    @{message_list}=   Get Value From Json    ${response_json}    msg
    Log To Console    ${message_list}
    ${message}=  Get From List     ${message_list}    0
    Should Be Equal    ${message}    record not found