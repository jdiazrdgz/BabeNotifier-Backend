from flask_restful import Resource


class Ping(Resource):

    def get(self):
        return \
            {
                "success": True,
                "message": "BabeNotifier - V0.0.1",
                "data": {}
            }, 200
