*** Settings ***
Resource        /opt/robot-tests/tests/resources/common.resource
Resource        /opt/robot-tests/tests/resources/api_invoker_management_requests/apiInvokerManagementRequests.robot
Library         /opt/robot-tests/tests/libraries/bodyRequests.py
Library         Process

Test Setup      Reset Testing Environment


*** Variables ***
${API_INVOKER_NOT_REGISTERED}       not-valid


*** Test Cases ***
Register NetApp
    [Tags]    capif_api_invoker_management-1
    #Register Netapp
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

    Status Should Be    201    ${resp}
    # Store dummy signede certificate
    Store In File    ${INVOKER_USERNAME}.crt    ${resp.json()['onboardingInformation']['apiInvokerCertificate']}

Register NetApp Already registered
    [Tags]    capif_api_invoker_management-2
    # Default Invoker Registration and Onboarding
    ${register_user_info}    ${url}    ${request_body}=    Invoker Default Onboarding

    ${resp}=    Post Request Capif
    ...    ${register_user_info['ccf_onboarding_url']}
    ...    json=${request_body}
    ...    server=https://${CAPIF_HOSTNAME}/
    ...    verify=ca.crt
    ...    access_token=${register_user_info['access_token']}

    Status Should Be    403    ${resp}

Update Registered NetApp
    [Tags]    capif_api_invoker_management-3
    # Default Invoker Registration and Onboarding
    ${register_user_info}    ${url}    ${request_body}=    Invoker Default Onboarding

    ${resp}=    Put Request Capif
    ...    ${url.path}
    ...    ${request_body}
    ...    server=https://${CAPIF_HOSTNAME}/
    ...    verify=ca.crt
    ...    username=${INVOKER_USERNAME}

    Status Should Be    200    ${resp}

Update Not Registered NetApp
    [Tags]    capif_api_invoker_management-4
    # Default Invoker Registration and Onboarding
    ${register_user_info}    ${url}    ${request_body}=    Invoker Default Onboarding

    ${resp}=    Put Request Capif
    ...    /api-invoker-management/v1/onboardedInvokers/${INVOKER_NOT_REGISTERED}
    ...    ${request_body}
    ...    server=https://${CAPIF_HOSTNAME}/
    ...    verify=ca.crt
    ...    username=${INVOKER_USERNAME}

    Status Should Be    404    ${resp}

Delete Registered NetApp
    [Tags]    capif_api_invoker_management-5
    # Default Invoker Registration and Onboarding
    ${register_user_info}    ${url}    ${request_body}=    Invoker Default Onboarding

    ${resp}=    Delete Request Capif
    ...    ${url.path}
    ...    server=https://${CAPIF_HOSTNAME}/
    ...    verify=ca.crt
    ...    username=${INVOKER_USERNAME}

    Should Be Equal As Strings    ${resp.status_code}    204

Delete Not Registered NetApp
    [Tags]    capif_api_invoker_management-6
    # Default Invoker Registration and Onboarding
    ${register_user_info}    ${url}    ${request_body}=    Invoker Default Onboarding

    ${resp}=    Delete Request Capif
    ...    /api-invoker-management/v1/onboardedInvokers/${INVOKER_NOT_REGISTERED}
    ...    server=https://${CAPIF_HOSTNAME}/
    ...    verify=ca.crt
    ...    username=${INVOKER_USERNAME}

    Status Should Be    404    ${resp}


*** Keywords ***
Testing Teardown
    ${result}=    Run Process    ls
    Log    ${result.stdout}
    ${result}=    Run Process    cp    -vvv    *.crt    /opt/robot-tests/results/
    Log    ${result.stdout}
    ${result}=    Run Process    cp    -vvv    *.key    /opt/robot-tests/results/
    Log    ${result.stdout}
    ${result}=    Run Process    cp    -vvv    *.csr    /opt/robot-tests/results/
    Log    ${result.stdout}
