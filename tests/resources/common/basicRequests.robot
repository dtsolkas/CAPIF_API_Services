*** Settings ***
Documentation    This resource file contains the basic requests used by Capif. CAPIF_SERVER and CAPIF_AUTH can be set as global variables, depends on environment used
Library          RequestsLibrary
Library          Collections

*** Variables ***
${CAPIF_SERVER}  http://localhost:8080
${CAPIF_AUTH}

*** keywords ***
Create CAPIF Session
    [Arguments]    ${server}=${NONE}    ${auth}=${NONE}

    Run Keyword If    "${server}" != "${NONE}"    Create Session    apisession    ${server}          verify=True
    ...               ELSE                        Create Session    apisession    ${CAPIF_SERVER}    verify=True

    ${headers}=    Run Keyword If    "${CAPIF_BEARER}" != ""                                   Create Dictionary    Authorization=Bearer ${CAPIF_BEARER}  
    ...            ELSE IF           "${auth}" != "${NONE}"                                    Create Dictionary    Authorization=Basic ${auth}
    ...            ELSE IF           "${CAPIF_AUTH}" != "${NONE}" and "${CAPIF_AUTH}" != ""    Create Dictionary    Authorization=Basic ${CAPIF_AUTH}
    ...            ELSE              Create Dictionary

    [Return]    ${headers}

Post Request Capif
    [Arguments]    ${endpoint}    ${json}=${EMTPY}    ${server}=${NONE}    ${auth}=${NONE}
    [Timeout]      60s

    ${headers}=    Create CAPIF Session    ${server}    ${auth}

    ${resp}=    POST On Session    apisession    ${endpoint}    headers=${headers}    json=${json}  expected_status=any

    [Return]    ${resp}

Get Request Capif
    [Arguments]    ${endpoint}    ${server}=${NONE}    ${auth}=${NONE}
    [Timeout]      60s

    ${headers}=    Create CAPIF Session    ${server}    ${auth}

    ${resp}=    GET On Session    apisession    ${endpoint}    headers=${headers}  expected_status=any

    [Return]    ${resp}

Put Request Capif
    [Arguments]    ${endpoint}    ${json}=${EMTPY}    ${server}=${NONE}    ${auth}=${NONE}
    [Timeout]      60s

    ${headers}=    Create CAPIF Session    ${server}    ${auth}

    ${resp}=    PUT On Session    apisession    ${endpoint}    headers=${headers}    json=${json}  expected_status=any
    [Return]    ${resp}


Delete Request Capif
    [Arguments]    ${endpoint}    ${server}=${NONE}    ${auth}=${NONE}
    [Timeout]      60s

    ${headers}=    Create CAPIF Session    ${server}    ${auth}

    ${resp}=    DELETE On Session    apisession    ${endpoint}    headers=${headers}  expected_status=any
    [Return]    ${resp}

Register User At Jwt Auth
    [Arguments]    ${email}=robot@test.com    ${password}=password    ${first_name}=robot    ${last_name}=framwork

    &{body}=    Create Dictionary    email=${email}    password=${password}    first_name=${first_name}    last_name=${last_name}

    Create Session    jwtsession    http://localhost:8080    verify=True

    ${resp}=    POST On Session    jwtsession    /register    json=${body}

    Should Be Equal As Strings    ${resp.status_code}    201

    &{body}=    Create Dictionary    email=${email}    password=${password}

    ${resp}=    POST On Session    jwtsession    /gettoken    json=${body}

    Should Be Equal As Strings    ${resp.status_code}    201

    Set Global Variable    ${CAPIF_BEARER}    ${resp.json()["access_token"]}

    [Return]    ${resp.json()["access_token"]}



