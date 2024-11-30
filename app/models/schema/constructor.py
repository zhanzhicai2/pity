# encoding: utf-8
# @File  : constructor.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/30


from pydantic import BaseModel, validator
from app.excpetions.ParamsException import ParamsError


class ConstructorForm(BaseModel):
    id: int = None
    value: str = ""
    type: int
    name: str
    constructor_json: str
    enable: bool
    case_id: int
    public: bool

    @validator("name", "constructor_json", "type", "public", "enable")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        if not isinstance(v, int):
            if not v:
                raise ParamsError("不能为空")
        return v
