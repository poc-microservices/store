from flask_restful import Resource
from core import api


class ChannelSubscribeResource(Resource):
    """
    Receive event the channle
    """
    def post(self):
        print("Hello Knative Eventing from ChannelSubscribeResource.")
        return "Hello Knative Eventing from ChannelSubscribeResource."

api.add_resource(ChannelSubscribeResource, '/event')
