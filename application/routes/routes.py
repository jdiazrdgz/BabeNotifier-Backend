from flask_restful import Api
from flask import current_app as app
from application.resources.Ping import Ping

api = Api(app)
api.add_resource(Ping, "/")


