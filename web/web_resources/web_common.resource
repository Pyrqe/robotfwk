*** Settings ***
Documentation    This file contains all browser keyword interactions used in the framework for UI web tests
Variables        config/EnvironmentSetup.py
Library          String
Library          Browser  run_on_failure=Take Screenshot \ EMBED strict=False  timeout=${BROWSER_TIMEOUT}  enable_playwright_debug=${PLAYWRIGHT_DEBUG}

*** Variables ***
${INTERACTION_TIMEOUT}        45s
${SCRIPT_TIMEOUT}             1000ms\

*** Keywords ***
Click on element
    [Documentation]  Left clicks on an element
    [Arguments]    ${selector}
    Click  ${selector}

Enter text
    [Documentation]  Types the text on an element text field by sending a keydown,
    ...  keypress/input, and keyup event for each character in the text
    [Arguments]  ${selector}  ${text}
    Log  ${selector}
    Log  ${text}
    Type text  ${selector}  ${text}
    