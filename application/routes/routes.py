from flask_restful import Api
from flask import current_app as app
from application.resources.Ping import Ping
from application.resources.Users import Users

api = Api(app)
api.add_resource(Ping, "/")
api.add_resource(Users, "/users")
#api.add_resource(UserDetail, '/users/<int:userId>')

