from flask_restful import Resource
from core import api


class StoreResource(Resource):
    """
    Health check resource
    """
    def get(self):
        print("Hello Knative Eventing.")
        return "Hello Knative Eventing."
    
    def post(self):
        print("Hello Knative Eventing.")
        return "Hello Knative Eventing."

api.add_resource(StoreResource, '/')
