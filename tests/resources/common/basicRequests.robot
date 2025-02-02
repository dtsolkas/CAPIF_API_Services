*** Settings ***
Documentation       This resource file contains the basic requests used by Capif. NGINX_HOSTNAME and CAPIF_AUTH can be set as global variables, depends on environment used

Library             RequestsLibrary
Library             Collections
Library             OperatingSystem


*** Variables ***
${CAPIF_AUTH}
${CAPIF_BEARER}


*** Keywords ***
Create CAPIF Session
    [Documentation]    Create needed session and headers.
    ...    If server input data is set to NONE, it will try to use NGINX_HOSTNAME variable.
    [Arguments]    ${server}=${NONE}    ${access_token}=${NONE}    ${verify}=${NONE}

    IF    "${server}" != "${NONE}"
        Create Session    apisession    ${server}    verify=${verify}
    END

    ${headers}=    Create Dictionary
    IF    "${access_token}" != "${NONE}"
        ${headers}=    Create Dictionary    Authorization=Bearer ${access_token}
    END

    RETURN    ${headers}

Post Request Capif
    [Timeout]    60s
    [Arguments]    ${endpoint}    ${json}=${NONE}    ${server}=${NONE}    ${access_token}=${NONE}    ${auth}=${NONE}    ${verify}=${FALSE}    ${cert}=${NONE}    ${username}=${NONE}    ${data}=${NONE}

    ${headers}=    Create CAPIF Session    ${server}    ${access_token}    ${verify}

    IF    '${username}' != '${NONE}'
        ${cert}=    Set variable    ${{ ('${username}.crt','${username}.key') }}
    END

    Set To Dictionary    ${headers}    Content-Type=application/json

    ${resp}=    POST On Session
    ...    apisession
    ...    ${endpoint}
    ...    headers=${headers}
    ...    json=${json}
    ...    expected_status=any
    ...    verify=${verify}
    ...    cert=${cert}
    ...    data=${data}
    RETURN    ${resp}

Get Request Capif
    [Timeout]    60s
    [Arguments]    ${endpoint}    ${server}=${NONE}    ${access_token}=${NONE}    ${auth}=${NONE}    ${verify}=${FALSE}    ${cert}=${NONE}    ${username}=${NONE}

    ${headers}=    Create CAPIF Session    ${server}    ${access_token}

    IF    '${username}' != '${NONE}'
        ${cert}=    Set variable    ${{ ('${username}.crt','${username}.key') }}
    END

    ${resp}=    GET On Session
    ...    apisession
    ...    ${endpoint}
    ...    headers=${headers}
    ...    expected_status=any
    ...    verify=${verify}
    ...    cert=${cert}
    RETURN    ${resp}

Put Request Capif
    [Timeout]    60s
    [Arguments]    ${endpoint}    ${json}=${EMTPY}    ${server}=${NONE}    ${access_token}=${NONE}    ${auth}=${NONE}    ${verify}=${FALSE}    ${cert}=${NONE}    ${username}=${NONE}

    ${headers}=    Create CAPIF Session    ${server}    ${access_token}

    IF    '${username}' != '${NONE}'
        ${cert}=    Set variable    ${{ ('${username}.crt','${username}.key') }}
    END

    ${resp}=    PUT On Session
    ...    apisession
    ...    ${endpoint}
    ...    headers=${headers}
    ...    json=${json}
    ...    expected_status=any
    ...    verify=${verify}
    ...    cert=${cert}

    RETURN    ${resp}

Patch Request Capif
    [Timeout]    60s
    [Arguments]    ${endpoint}    ${json}=${EMTPY}    ${server}=${NONE}    ${access_token}=${NONE}    ${auth}=${NONE}    ${verify}=${FALSE}    ${cert}=${NONE}    ${username}=${NONE}

    ${headers}=    Create CAPIF Session    ${server}    ${access_token}

    IF    '${username}' != '${NONE}'
        ${cert}=    Set variable    ${{ ('${username}.crt','${username}.key') }}
    END

    ${resp}=    PATCH On Session
    ...    apisession
    ...    ${endpoint}
    ...    headers=${headers}
    ...    json=${json}
    ...    expected_status=any
    ...    verify=${verify}
    ...    cert=${cert}

    RETURN    ${resp}

Delete Request Capif
    [Timeout]    60s
    [Arguments]    ${endpoint}    ${server}=${NONE}    ${access_token}=${NONE}    ${auth}=${NONE}    ${verify}=${FALSE}    ${cert}=${NONE}    ${username}=${NONE}

    ${headers}=    Create CAPIF Session    ${server}    ${access_token}

    IF    '${username}' != '${NONE}'
        ${cert}=    Set variable    ${{ ('${username}.crt','${username}.key') }}
    END

    ${resp}=    DELETE On Session
    ...    apisession
    ...    ${endpoint}
    ...    headers=${headers}
    ...    expected_status=any
    ...    verify=${verify}
    ...    cert=${cert}

    RETURN    ${resp}

Register User At Jwt Auth
    [Arguments]    ${username}    ${role}    ${password}=password    ${description}=Testing

    # Create certificate and private_key for this machine.
    IF    "${role}" == "${INVOKER_ROLE}"
        ${csr_request}=    Create Csr    ${username}.csr    ${username}.key    ${username}
    ELSE
        ${csr_request}=    Set Variable    ${None}
    END

    &{body}=    Create Dictionary
    ...    password=${password}
    ...    username=${username}
    ...    role=${role}
    ...    description=${description}
    ...    cn=${username}

    Create Session    jwtsession    ${CAPIF_HTTP_URL}    verify=True

    ${resp}=    POST On Session    jwtsession    /register    json=${body}

    Should Be Equal As Strings    ${resp.status_code}    201

    ${get_auth_response}=    Get Auth For User    ${username}    ${password}    ${role}

    ${register_user_info}=    Create Dictionary
    ...    netappID=${resp.json()['id']}
    ...    csr_request=${csr_request}
    ...    &{resp.json()}
    ...    &{get_auth_response}

    Log Dictionary    ${register_user_info}

    IF    "cert" in @{register_user_info.keys()}
        Store In File    ${username}.crt    ${register_user_info['cert']}
    END
    IF    "private_key" in @{register_user_info.keys()}
        Store In File    ${username}.key    ${register_user_info['private_key']}
    END

    RETURN    ${register_user_info}

Get Auth For User
    [Arguments]    ${username}    ${password}    ${role}

    &{body}=    Create Dictionary    username=${username}    password=${password}    role=${role}

    ${resp}=    POST On Session    jwtsession    /getauth    json=${body}

    Should Be Equal As Strings    ${resp.status_code}    201

    # Should Be Equal As Strings    ${resp.json()['message']}    Certificate created successfuly

    RETURN    ${resp.json()}

Clean Test Information By HTTP Requests
    Create Session    jwtsession    ${CAPIF_HTTP_URL}    verify=True

    ${resp}=    DELETE On Session    jwtsession    /testdata
    Should Be Equal As Strings    ${resp.status_code}    200

Invoker Default Onboarding
    ${register_user_info}=    Register User At Jwt Auth
    ...    username=${INVOKER_USERNAME}    role=${INVOKER_ROLE}

    # Send Onboarding Request
    ${request_body}=    Create Onboarding Notification Body
    ...    http://${CAPIF_CALLBACK_IP}:${CAPIF_CALLBACK_PORT}/netapp_callback
    ...    ${register_user_info['csr_request']}
    ...    ${INVOKER_USERNAME}
    ${resp}=    Post Request Capif
    ...    ${register_user_info['ccf_onboarding_url']}
    ...    json=${request_body}
    ...    server=https://${CAPIF_HOSTNAME}/
    ...    verify=ca.crt
    ...    access_token=${register_user_info['access_token']}

    Set To Dictionary    ${register_user_info}    apiInvokerId=${resp.json()['apiInvokerId']}
    Log Dictionary    ${register_user_info}

    Status Should Be    201    ${resp}
    # Store dummy signede certificate
    Store In File    ${INVOKER_USERNAME}.crt    ${resp.json()['onboardingInformation']['apiInvokerCertificate']}

    ${url}=    Parse Url    ${resp.headers['Location']}

    RETURN    ${register_user_info}    ${url}    ${request_body}

Publisher Default Registration
    #Register Exposer
    ${register_user_info}=    Register User At Jwt Auth
    ...    username=${PUBLISHER_USERNAME}    role=${PUBLISHER_ROLE}

    RETURN    ${register_user_info}
