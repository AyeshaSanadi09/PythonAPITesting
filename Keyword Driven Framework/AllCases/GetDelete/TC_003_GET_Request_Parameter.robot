*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections

*** Variables ***
${BASE_URL}  https://reqres.in

*** Test Cases ***
TC_003 validate get request with parameter
    [Tags]  Regression
    Create Session    get_param    ${BASE_URL}
    # we need to pass parameter which is in dictionary so we need to create one dictionary here
    ${param}=  Create Dictionary  page=2 
    ${response}=  GET On Session    get_param    api/users  params=${param}
    # Log To Console    ${response.text}
    ${json_response}=  To Json    ${response.text}
    # Log To Console    ${json_response}
    ${name_list}=  Get Value From Json    ${json_response}    data[0].first_name
    Log To Console    ${name_list}
    ${name}=  Get From List    ${name_list}    0
    Log To Console    ${name}
    Should Be Equal    ${name}    Michael