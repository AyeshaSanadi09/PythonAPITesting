*** Settings ***
Library  JSONLibrary
Library  RequestsLibrary
Library  Collections

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_005 Adding Student Details
    Create Session    addstudentdata    ${BASE_URL}
    ${body}=  Create Dictionary  first_name=Alita  middle_name=Robert  last_name=Dawny  date_of_birth=9/24/2002 
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  Post Request    addstudentdata    api/studentsDetails  data=${body}  headers=${header}
    Log To Console    ${response.content}