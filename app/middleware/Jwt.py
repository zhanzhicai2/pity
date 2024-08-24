import hashlib
from datetime import datetime, timedelta

import jwt
from jwt.exceptions import ExpiredSignatureError

EXPIRED_HOUR = 3000


class UserToken(object):
    key = 'pityToken'
    salt = 'pity'

    @staticmethod
    def get_token(data):
        new_data = dict({"exp": datetime.utcnow() + timedelta(hours=EXPIRED_HOUR)}, **data)
        return jwt.encode(new_data, key=UserToken.key, algorithm='HS256')
        # return jwt.encode(new_data, key=UserToken.key)

    @staticmethod
    def parse_token(token):
        try:
            payload = jwt.decode(token, UserToken.key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token已过期, 请重新登录")
        except jwt.InvalidTokenError:
            raise Exception("无效的Token")
            # try:
        # token = jwt.decode(token, key=UserToken.key)
        # return jwt.decode(token, key=UserToken.key)
        # return token
        # except ExpiredSignatureError:
        # raise Exception("token已过期, 请重新登录")

    @staticmethod
    def add_salt(password):
        m = hashlib.md5()
        # m.update(password + UserToken.salt)
        bt = f"{password}{UserToken.salt}".encode("utf-8")
        m.update(bt)
        return m.hexdigest()
