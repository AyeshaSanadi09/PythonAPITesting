*** Settings ***
Library  JSONLibrary
Library  RequestsLibrary
Library  Collections

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_005 End to end Scenario
    # [Timeout]  .1s
    # Adding data using post
    Create Session    studenturl  ${BASE_URL}
    ${body}=  Create Dictionary  first_name=Alita  middle_name=Robert  last_name=Dawny  date_of_birth=9/24/2002 
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  Post Request    studenturl    api/studentsDetails  data=${body}  headers=${header}
    # Log To Console    ${response.content}
    # converting response into json
    ${json_response}=  To Json    ${response.text}
    # Featching perticular response from json that is in list format so we need to specify this @ for list
    @{student_id_list}=  Get Value From Json    ${json_response}    id
    # Geting value from list
    ${STUDENT_ID}=  Get From List    ${student_id_list}    0
    Log To Console    ${STUDENT_ID}
    # Should Be Equal    ${STUDENT_ID}   

    Fetching and validating Student Details  ${STUDENT_ID}

    # Updating Student Details using put
    ${body}=  Create Dictionary  id=${STUDENT_ID}  first_name=Alian  middle_name=RK  last_name=Dawny  date_of_birth=24/9/2002 
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  Put Request    studenturl    api/studentsDetails/${STUDENT_ID}  data=${body}  headers=${header}
    # Log To Console    ${response.content}
    # Log To Console    ${response.status_code}

    Fetching and validating Student Details  ${STUDENT_ID}

# TC_004 DELETE STUDENT DATA BASED ON STUDENT_ID
    ${response}=  Delete Request    studenturl    api/studentsDetails/${STUDENT_ID}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}

    Fetching and validating Student Details  ${STUDENT_ID}  

   

# writing keywords in resource file
*** Keywords ***
Fetching and validating Student Details
    [Arguments]  ${STUDENT_ID}
    #  Fetching data using get
    ${response}=  GET On Session    studenturl   api/studentsDetails/${STUDENT_ID}
    Log To Console    ${response.content}
    # converting status code from integer to string
    ${actual_code}=  Convert To String    ${response.status_code}
    # validate status code
    Should Be Equal    ${actual_code}    200
    # Log To Console    ${response.text}