# encoding: utf-8
# @File  : user_schema.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/14
from pydantic import BaseModel, validator
from app.excpetions.ParamsException import ParamsError


class UserDto(BaseModel):
    name: str
    password: str
    username: str
    email: str

    @validator('name', 'password', 'username', 'email')
    def field_not_empty(cls, v):
        # if len(v.strip()) == 0:
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        return v


class UserForm(BaseModel):
    username: str
    password: str

    @validator('password', 'username')
    def name_not_empty(cls, v):
        # if len(v.strip()) == 0:
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        return v
