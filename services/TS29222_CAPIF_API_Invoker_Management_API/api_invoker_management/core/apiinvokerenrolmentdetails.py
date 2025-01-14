import sys

import pymongo
import secrets
import requests
from flask import current_app, Flask, Response
import json
from ..encoder import JSONEncoder
from ..db.db import MongoDatabse
from ..models.problem_details import ProblemDetails

class InvokerManagementOperations:

    def __init__(self):
        self.db = MongoDatabse()
        self.mimetype = 'application/json'

    def add_apiinvokerenrolmentdetail(self, apiinvokerenrolmentdetail):

        mycol = self.db.get_col_by_name(self.db.invoker_enrolment_details)

        try:

            res = mycol.find_one({'onboarding_information.api_invoker_public_key': apiinvokerenrolmentdetail.onboarding_information.api_invoker_public_key})

            if res is not None:
                prob = ProblemDetails(title="Forbidden", status=403, detail="Invoker already registered", cause="Identical invoker public key")

                return Response(json.dumps(prob, cls=JSONEncoder), status=403, mimetype=self.mimetype)

            else:

                url = "http://easy-rsa:8080/sign-csr"

                payload = dict()
                payload['csr'] = apiinvokerenrolmentdetail.onboarding_information.api_invoker_public_key
                payload['mode'] = 'client'
                payload['filename'] = apiinvokerenrolmentdetail.api_invoker_information

                headers = {

                    'Content-Type': self.mimetype

                }

                response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
                response_payload = json.loads(response.text)

                api_invoker_id = secrets.token_hex(15)
                apiinvokerenrolmentdetail.api_invoker_id = api_invoker_id
                apiinvokerenrolmentdetail.onboarding_information.api_invoker_certificate = response_payload['certificate']
                mycol.insert_one(apiinvokerenrolmentdetail.to_dict())


                res = Response(json.dumps(apiinvokerenrolmentdetail, cls=JSONEncoder), status=201, mimetype=self.mimetype)
                res.headers['Location'] = "/api-invoker-management/v1/onboardedInvokers/" + str(api_invoker_id)
                return res

        except Exception as e:
            exception = "An exception occurred in create invoker::", e
            return Response(json.dumps(exception, default=str, cls=JSONEncoder), status=500, mimetype=self.mimetype)


    def update_apiinvokerenrolmentdetail(self, onboard_id, apiinvokerenrolmentdetail):

        mycol = self.db.get_col_by_name(self.db.invoker_enrolment_details)

        try:
            myQuery = {'api_invoker_id':onboard_id}
            old_values = mycol.find_one(myQuery)

            if old_values is None:
                prob = ProblemDetails(title="Not Found", status=404, detail="Please provide an existing Netapp ID", cause="Not exist NetappID")

                return Response(json.dumps(prob, cls=JSONEncoder), status=404, mimetype=self.mimetype)


            else:

                apiinvokerenrolmentdetail = apiinvokerenrolmentdetail.to_dict()
                apiinvokerenrolmentdetail = {
                    key: value for key, value in apiinvokerenrolmentdetail.items() if value is not None
                }

                mycol.update_one(old_values, {"$set":apiinvokerenrolmentdetail}, upsert=False)


                res = Response(json.dumps(apiinvokerenrolmentdetail, cls=JSONEncoder), status=200, mimetype=self.mimetype)
                return res

        except Exception as e:
            exception = "An exception occurred in update invoker::", e
            return Response(json.dumps(exception, default=str, cls=JSONEncoder), status=500, mimetype=self.mimetype)



    def remove_apiinvokerenrolmentdetail(self, onboard_id):

        mycol = self.db.get_col_by_name(self.db.invoker_enrolment_details)

        try:
            myQuery ={'api_invoker_id':onboard_id}
            result=mycol.find_one(myQuery)

            if (result == None):
                prob = ProblemDetails(title="Not Found", status=404, detail="Please provide an existing Netapp ID", cause="Not exist NetappID")
                return Response(json.dumps(prob, cls=JSONEncoder), status=404, mimetype=self.mimetype)
            else:
                mycol.delete_one(myQuery)
                out =  " The Netapp matching onboardingId  " + onboard_id + " was offboarded."
                return Response(json.dumps(out, default=str, cls=JSONEncoder), status=204, mimetype=self.mimetype)

        except Exception as e:
            exception = "An exception occurred in remove invoker::", e
            return Response(json.dumps(exception, default=str, cls=JSONEncoder), status=500, mimetype=self.mimetype)


