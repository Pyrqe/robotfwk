*** Settings ***
Documentation    This file contains keywords for test setup and teardown for web tests
Variables        config/EnvironmentSetup.py
Library          CSVLibrary
Library          Browser
Resource         web/web_resources/web_common.resource


*** Keywords ***
Tear down web test
    [Documentation]               Tears down the overall test suite, takse a screenshot on test failure
    Run Keyword If Test Failed    Run Keyword And Continue On Failure
    ...                           Take Screenshot                                                          EMBED

Open browser context
    New Persistent Context  headless=${HEADLESS}

Open browser page
    New page    ${PAGE_URL}
