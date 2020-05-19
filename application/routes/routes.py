from flask_restful import Api
from flask import current_app as app
from application.resources.Ping import Ping
from application.resources.Users import User, UserDetail

api = Api(app)
api.add_resource(Ping, "/")
api.add_resource(User, "/users")
api.add_resource(UserDetail, '/users/<string:user_id>')

