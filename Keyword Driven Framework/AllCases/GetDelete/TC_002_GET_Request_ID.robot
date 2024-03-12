*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections

*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/
${STUDENT_ID}  10092357

*** Test Cases ***
TC_002_GET_Request_Student_Id
    [Tags]  Smoke  
    Create Session    getStudentDetails    ${BASE_URL}
    ${response}=  Get Request   getStudentDetails    api/studentsDetails/${STUDENT_ID} 
    # converting status code from integer to string
    ${actual_code}=  Convert To String    ${response.status_code}
    # validate status code
    # Should Be Equal    ${actual_code}    200
    Log To Console    ${response.text}

    # converting response to json
    ${json_response}=  To Json    ${response.text}
    # Featching perticular response from json that is in list format so we need to specify this @ for list
    @{student_name_list}=  Get Value From Json    ${json_response}    data.last_name
    # Geting value from list
    ${student_name}=  Get From List    ${student_name_list}    0
    Log To Console    ${student_name}
    Should Be Equal    ${student_name}   sample string 4

    

TC_002_GET_Request_Student_Id
    [Tags]  Sanity
    Create Session    getStudentDetails    ${BASE_URL}
    ${response}=  GET On Session    getStudentDetails    api/studentsDetails/${STUDENT_ID}
    # converting status code from integer to string
    ${actual_code}=  Convert To String    ${response.status_code}
    # validate status code
    Should Be Equal    ${actual_code}    200
    # Log To Console    ${response.text}

    # converting response to json
    ${json_response}=  To Json    ${response.text}
    # Featching perticular response from json that is in list format so we need to specify this @ for list
    @{student_name_list}=  Get Value From Json    ${json_response}    data.middle_name
    # Geting value from list
    ${student_name}=  Get From List    ${student_name_list}    0
    Log To Console    ${student_name}
    Should Be Equal    ${student_name}   sample string 3
