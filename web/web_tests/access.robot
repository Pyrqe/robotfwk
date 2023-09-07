*** Settings ***
Documentation        Thid file contains web login tests
Resource    C:/Coding/robotfwk/web/page_objects/login_page.resource
Resource    C:/Coding/robotfwk/web/web_resources/web_setup.resource

Suite Setup  Open browser context
Test Teardown  Tear down web test


*** Test Cases ***
As a user I should be able to login with valid credentials
    [Documentation]    I should be able to login by typing in email and password and clicking the
    ...  sign in button
    [Tags]  login
    Open browser page
    Enter text into email field
    Enter text into password field
    Click sign in button
    Sleep  5s
