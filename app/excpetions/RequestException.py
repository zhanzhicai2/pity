# encoding: utf-8
# @File  : RequestException.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/14
from fastapi import HTTPException


class AuthException(HTTPException):
    pass


class PermissionException(HTTPException):
    pass
