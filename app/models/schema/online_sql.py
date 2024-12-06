# encoding: utf-8
# @File  : online_sql.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/12/07

from pydantic import BaseModel, validator
from app.models.schema.base import PityModel


class OnlineSQLForm(BaseModel):
    id: int = None
    sql: str

    @validator("sql", 'id')
    def name_not_empty(cls, v):
        return PityModel.not_empty(v)
