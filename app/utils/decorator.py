# from functools import wraps
#
# import requests
# from flask import request, jsonify
# import json
# from app import pity
# from app.middleware.Jwt import UserToken
#
# FORBIDDEN = "对不起, 你没有足够的权限"
#
#
# class SingletonDecorator:
#     def __init__(self, cls):
#         self.cls = cls
#         self.instance = None
#
#     def __call__(self, *args, **kwargs):
#         if self.instance is None:
#             self.instance = self.cls(*args, **kwargs)
#         return self.instance
#
#
# def permission(role=pity.config.get("GUEST")):
#     def login_required(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 headers = request.headers
#                 token = headers.get('token')
#
#                 # 跟原作者不一样，所以魔改了
#                 roles = headers.get('userrole')
#                 data = json.loads(roles)
#                 userrole = int(data['role'])
#                 if token is None:
#                     return jsonify(dict(code=401, msg="用户信息认证失败, 请检查"))
#                 # user_info = UserToken.parse_token(token)
#                 # 这里把user信息写入kwargs
#                 # kwargs["user_info"] = user_info
#                 kwargs["user_info"] = token
#             except Exception as e:
#                 return jsonify(dict(code=401, msg=str(e)))
#             # 判断用户权限是否足够, 如果不足够则直接返回，不继续
#             # 众多代码跟作者不一样，谨慎学习，不一样的原因是作者的代码取不到请求过来role的值，所以魔改了
#             # if user_info.get("role", 0) < role:
#             if userrole > role:
#                 return jsonify(dict(code=400, msg=FORBIDDEN))
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return login_required


# 前 20章的练习

from functools import wraps

from flask import request, jsonify
from jsonschema import validate, FormatChecker, ValidationError

from app import pity
from app.middleware.Jwt import UserToken

FORBIDDEN = "对不起, 你没有足够的权限"


class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


def permission(role=pity.config.get("GUEST")):
    # role = pity.config.get("GUEST")
    def login_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                headers = request.headers
                token = headers.get('token')
                if token is None:
                    return jsonify(dict(code=401, msg="用户信息认证失败, 请检查"))
                user_info = UserToken.parse_token(token)
                # 这里把user信息写入kwargs
                kwargs["user_info"] = user_info
            except Exception as e:
                return jsonify(dict(code=401, msg=str(e)))
            # 判断用户权限是否足够, 如果不足够则直接返回，不继续
            if user_info.get("role", 0) < role:
                return jsonify(dict(code=400, msg=FORBIDDEN))
            return func(*args, **kwargs)

        return wrapper

    return login_required


def json_validate(sc):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if request.get_json() is not None:
                    validate(request.get_json(), sc, format_checker=FormatChecker())
                else:
                    raise Exception("请求json参数不合法")
            except ValidationError as e:
                return jsonify(dict(code=101, msg=str(e.message)))
            except Exception as e:
                return jsonify(dict=101, msg=str(e))
            return func(*args, **kwargs)

        return wrapper

    return decorator
