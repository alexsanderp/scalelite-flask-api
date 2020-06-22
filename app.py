from flask import Blueprint
from flask_restful import Api
from resources.server import *

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# servers
api.add_resource(Servers, '/servers/')
api.add_resource(Server, '/servers/<string:id>/')
api.add_resource(ServerEnable, '/server/<string:id>/enable/')
api.add_resource(ServerDisable, '/server/<string:id>/disable/')
api.add_resource(ServerPanic, '/server/<string:id>/panic/')
