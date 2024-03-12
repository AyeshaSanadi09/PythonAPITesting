*** Settings ***
Library  JSONLibrary
Library  RequestsLibrary
Library  Collections
Resource  ../../Resources/UserKeyword.robot

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_005 Adding Student Details
    [Documentation]  This test case display end to end conversation between all requests
    Create Session    addstudentdata    ${BASE_URL}
    ${body}=  Featching and returning json
    # Log To Console    ${body}
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  Post Request    addstudentdata    api/studentsDetails  data=${body}  headers=${header}
    Log To Console    ${response.content}
    ${actual_code}=  Convert To String    ${response.status_code} 
    Should Be Equal  ${actual_code}  201