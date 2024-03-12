*** Settings ***
Library  JSONLibrary
Library  RequestsLibrary
Library  Collections

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/
${id}  10092421

*** Test Cases ***
TC_005 Updating Student Details
    Create Session    updatestudentdata    ${BASE_URL}
    ${body}=  Create Dictionary  id=${id}  first_name=Alian  middle_name=RK  last_name=Dawny  date_of_birth=24/9/2002 
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  Put Request    updatestudentdata    api/studentsDetails/${id}  data=${body}  headers=${header}
    Log To Console    ${response.content}
    Log To Console    ${response.status_code}
    ${getResponse}=  Get Request    updatestudentdata    api/studentsDetails/${id}
    Log To Console    ${getResponse.content}