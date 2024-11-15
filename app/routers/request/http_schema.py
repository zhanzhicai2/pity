# encoding: utf-8
# @File  : http_schema.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/14
from pydantic import BaseModel, validator
from app.excpetions.ParamsException import ParamsError


class HttpRequestForm(BaseModel):
    method: str
    url: str
    body: str = None
    headers: dict = {}

    @validator('method', 'url')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        return v
