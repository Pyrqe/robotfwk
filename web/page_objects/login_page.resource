*** Settings ***
Documentation     This is the page file for login page of test page ultimate QA
Resource          C:/Coding/robotfwk/web/web_resources/web_common.resource

*** Variables ***
${EMAIL_FIELD}        /#user[email]
${PASSWORD_FIELD}     /#user[password]
${SIGN_IN_BTN}        button .button

*** Keywords ***
Enter text into email field
    Enter text  ${EMAIL_FIELD}  ${LOGIN_EMAIL}

Enter text into password field
    Enter text  ${PASSWORD_FIELD}  ${LOGIN_PASSWORD}

Click sign in button
    Click on element  ${SIGN_IN_BTN}