# encoding: utf-8
# @File  : gconfig.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/20
from pydantic import BaseModel, validator
from app.excpetions.ParamsException import ParamsError


class GConfigForm(BaseModel):
    id: int = None
    key: str
    value: str
    env: str = None
    key_type: int
    enable: bool

    @validator("key", "value", "key_type", "enable")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        if not v:
            raise ParamsError("不能为空")
        return v
