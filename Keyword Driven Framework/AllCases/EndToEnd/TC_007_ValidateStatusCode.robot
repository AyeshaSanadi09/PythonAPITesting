*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Resource  ../../Resources/UserKeyword.robot


*** Variables ***
${BASE_URL}  https://thetestingworldapi.com/
${id}  10092420


*** Test Cases ***
TC_006 Fetch Data
    Fetching and Validating Request  ${id}  200
    ${response}=  Fetching and returning request    ${id}    200
    Log To Console    ${response.content}