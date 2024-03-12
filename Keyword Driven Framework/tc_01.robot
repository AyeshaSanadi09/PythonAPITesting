*** Settings ***
Library  RequestsLibrary

*** Variables ***
${age}  9


*** Test Cases ***
tc_01
# setting variable inside test cases
    ${url}=  Set Variable  HelloWorld 
    Log To Console    ${age}
    Log To Console    ${url}