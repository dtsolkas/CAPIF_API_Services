def create_onboarding_notification_body(notification_destination="NotificationDestination", api_invoker_public_key="ApiInvokerPublicKey",api_invoker_information='ROBOT_TESTING'):
    data = {
        "notificationDestination": notification_destination,
        "supportedFeatures": "fffffff",
        "apiInvokerInformation": api_invoker_information,
        "websockNotifConfig": {
            "requestWebsocketUri": True,
            "websocketUri": "websocketUri"
        },
        "onboardingInformation": {
            "apiInvokerPublicKey": api_invoker_public_key.decode("utf-8"),
            "onboardingSecret": "onboardingSecret",
            "apiInvokerCertificate": "apiInvokerCertificate"
        },
        "requestTestNotification": True,
        "apiList": [{
            "serviceAPICategory": "serviceAPICategory",
            "ccfId": "ccfId",
            "apiName": "apiName",
            "shareableInfo": {
                "capifProvDoms": ["capifProvDoms", "capifProvDoms"],
                "isShareable": True
            },
            "supportedFeatures": "fffffff",
            "description": "description",
            "apiSuppFeats": "fffffff",
            "apiId": "apiId",
            "aefProfiles": [{
                "securityMethods": ["PSK"],
                "versions": [{
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }, {
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }],
                "aefId": "aefId",
                "interfaceDescriptions": [{
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }, {
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }]
            }, {
                "securityMethods": ["PSK"],
                "versions": [{
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }, {
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }],
                "aefId": "aefId",
                "interfaceDescriptions": [{
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }, {
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }]
            }],
            "pubApiPath": {
                "ccfIds": ["ccfIds", "ccfIds"]
            }
        }, {
            "serviceAPICategory": "serviceAPICategory",
            "ccfId": "ccfId",
            "apiName": "apiName2",
            "shareableInfo": {
                "capifProvDoms": ["capifProvDoms", "capifProvDoms"],
                "isShareable": True
            },
            "supportedFeatures": "fffffff",
            "description": "description",
            "apiSuppFeats": "fffffff",
            "apiId": "apiId",
            "aefProfiles": [{
                "securityMethods": ["PSK"],
                "versions": [{
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }, {
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }],
                "aefId": "aefId",
                "interfaceDescriptions": [{
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }, {
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }]
            }, {
                "securityMethods": ["PSK"],
                "versions": [{
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }, {
                    "apiVersion": "apiVersion",
                    "resources": [{
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "resourceName": "resourceName",
                        "custOpName": "custOpName",
                        "uri": "uri",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "custOperations": [{
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }, {
                        "operations": ["GET"],
                        "description": "description",
                        "custOpName": "custOpName",
                        "commType": "REQUEST_RESPONSE"
                    }],
                    "expiry": "2000-01-23T04:56:07.000+00:00"
                }],
                "aefId": "aefId",
                "interfaceDescriptions": [{
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }, {
                    "securityMethods": ["PSK"],
                    "port": 5248,
                    "ipv4Addr": "ipv4Addr"
                }]
            }],
            "pubApiPath": {
                "ccfIds": ["ccfIds", "ccfIds"]
            }
        }]
    }

    return (data)
