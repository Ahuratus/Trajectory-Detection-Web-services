from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import redis

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
blacklist_store = redis.Redis(
    host='redis',
    port=6379,
    db=0,
    decode_responses=True
)
jwt = JWTManager(app)
api = Api(app)

from models import RevokedToken

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """
        Create our function to check if a token has been blacklisted. In this simple
        case, we will just store the tokens jti (unique identifier) in redis
        whenever we create a new token (with the revoked status being 'false'). This
        function will return the revoked status of a token. If a token doesn't
        exist in this store, we don't know where it came from (as we are adding newly
        created tokens to our store with a revoked status of 'false'). In this case
        we will consider the token to be revoked, for safety purposes.
    """
    jti = decrypted_token['jti']
    entry = blacklist_store.get(jti)
    if entry is None:
        return True
    return entry == 'true'

from resources import (
    UserRegistration,
    UserLogin,
    UserLogoutAccess,
    UserLogoutRefresh,
    TokenRefresh,
    ProcessTrajectoryEstimation,
    ProtectedResource,
    OpenResource
)

api.add_resource(UserRegistration, '/api/registration')
api.add_resource(UserLogin, '/api/login')
api.add_resource(UserLogoutAccess, '/api/logout/access') # Full log out (revoke access and refresh)
api.add_resource(UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(TokenRefresh, '/api/token/refresh')
api.add_resource(ProcessTrajectoryEstimation, '/api/process/trajectory')
api.add_resource(ProtectedResource, '/api/protected')
api.add_resource(OpenResource, '/api/open')
