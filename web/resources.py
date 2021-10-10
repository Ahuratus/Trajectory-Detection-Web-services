from tracker_module import TrajectoryEstimationModel
from flask import app, session
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
    get_jti
)
from run import db, blacklist_store
from models import User
from config import ACCESS_EXPIRES, REFRESH_EXPIRES
import base64


parser_user_access = reqparse.RequestParser()
parser_user_access.add_argument('email', required=True)
parser_user_access.add_argument('password', required=True)

parser_revoke = reqparse.RequestParser()
parser_revoke.add_argument('refresh_token', required=True)

parser_refresh = reqparse.RequestParser()
parser_refresh.add_argument('access_token', required=True)

parser_process = reqparse.RequestParser()
parser_process.add_argument('access_token', required=True)
parser_process.add_argument('frame', required=True)
parser_process.add_argument('buffer_size', required=True)


def add_to_store(access_token, refresh_token):
    """
        Store the tokens in redis with a status of not currently revoked. We
        can use the `get_jti()` method to get the unique identifier string for
        each token. We can also set an expires time on these tokens in redis,
        so they will get automatically removed after they expire. We will set
        everything to be automatically removed shortly after the token expires
    """
    access_jti = get_jti(encoded_token=access_token)
    refresh_jti = get_jti(encoded_token=refresh_token)
    blacklist_store.set(access_jti, 'false', ACCESS_EXPIRES * 1.2)
    blacklist_store.set(refresh_jti, 'false', REFRESH_EXPIRES * 1.2)


def revoke(revoke_type, jti):
    if revoke_type == 'access':
        blacklist_store.set(jti, 'true', ACCESS_EXPIRES * 1.2)
    elif revoke_type == 'refresh':
        blacklist_store.set(jti, 'true', REFRESH_EXPIRES * 1.2)


class UserRegistration(Resource):
    def post(self):
        data = parser_user_access.parse_args()
        email = data.get('email')
        password = data.get('password')
        if User.find_by_email(email):
            return {'message': f'Email {email} already exists'}
        user = User(
            email=email,
            password_hash=User.generate_hash(password)
        )
        try:
            db.session.add(user)
            db.session.commit()
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            add_to_store(access_token, refresh_token)
            return (
                {
                    'message': f'User {email} was created',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                },
                200
            )
        except:
            return ({'message': 'Something went wrong'}, 500)


class UserLogin(Resource):
    def post(self):
        data = parser_user_access.parse_args()
        email = data.get('email')
        password = data.get('password')
        current_user = User.find_by_email(email)
        if not current_user:
            return {'message': f"Email {email} doesn't exist"}
        if User.verify_hash(password, current_user.password_hash):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            add_to_store(access_token, refresh_token)
            return {
                'message': f'Logged in as {current_user.email}',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Invalid credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        data = parser_revoke.parse_args()
        refresh_token = data.get('refresh_token')
        access_jti = get_jwt()['jti']
        refresh_jti = get_jti(refresh_token)
        try:
            revoke('access', access_jti)
            revoke('refresh', refresh_jti)
            return {'message': 'Access and refresh token has been revoked'}
        except:
            return ({'message': 'Something went wrong'}, 500)


class UserLogoutRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        jti = get_jwt()['jti']
        try:
            revoke('refresh', refresh_jti)
            return {'message': 'Refresh token has been revoked'}
        except:
            return ({'message': 'Something went wrong'}, 500)


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        data = parser_refresh.parse_args()
        old_access_token = data.get('access_token')
        old_access_jti = get_jti(encoded_token=old_access_token)
        current_user = get_jwt_identity()
        # Refresh new access token
        access_token = create_access_token(identity=current_user)
        access_jti = get_jti(encoded_token=access_token)
        blacklist_store.set(access_jti, 'false', ACCESS_EXPIRES * 1.2)
        # Revoke old access token
        blacklist_store.set(old_access_jti, 'true', ACCESS_EXPIRES * 1.2)
        return {'access_token': access_token}


class ProcessTrajectoryEstimation(Resource):
    tem = None
    def post(self):
        data = parser_process.parse_args()
        try:
            if not self.tem:
                self.tem = TrajectoryEstimationModel(
                        int(data.get('buffer_size')))
            base64String = data.get('frame')
            b64Bytes = base64String.encode('ascii')
            pts, res = self.tem.process(b64Bytes)

        # res,pts = session.get('tem').process(data.get('frame'))
            return {'result': str(res),
                    'trajectory': str(pts)}, 200
        except Exception as ex:
            return ({'message': 'frame/access_token not included'+str(ex)}, 500)


class OpenResource(Resource):
    def get(self):
        return {
            'message': 'This is a message'
        }


class ProtectedResource(Resource):
    @jwt_required
    def get(self):
        return {
            'message': 'This is a secret'
        }
