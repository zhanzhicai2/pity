# encoding: utf-8
# @File  : environment.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/19

from pydantic import BaseModel, validator

from app.excpetions.ParamsException import ParamsError


class EnvironmentForm(BaseModel):
    id: int = None
    name: str
    remarks: str = None

    @validator("name")
    def name_not_empty(cls,v):
        if isinstance(v, str) and len(v.strip()) ==0:
            raise ParamsError("不能为空")
        return v
