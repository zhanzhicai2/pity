# encoding: utf-8
# @File  : ConstructorDao.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/30

from app.models import Session
from app.models.constructor import Constructor
from app.models.schema.constructor import ConstructorForm
from app.models.test_case import TestCase
from app.utils.logger import Log
from collections import defaultdict


class ConstructorDao(object):
    log = Log("ConstructorDao")

    # insert插入
    @staticmethod
    def insert_constructor(data: ConstructorForm, user):
        """
        insert 插入构造数据
        :param data:
        :param user:
        :return:
        """
        try:
            with Session() as session:
                query = session.query(Constructor).filter_by(case_id=data.case_id, name=data.name,
                                                             deleted_at=None).first()
                if query is not None:
                    return f"初始化数据: {data.name}已存在"
                config = Constructor(**data.dict(), user=user)
                session.add(config)
                session.commit()
        except Exception as e:
            ConstructorDao.log.error(f"新增初始化数据: {data.name}失败, {e}")
            raise Exception(f"新增初始化数据失败")

    @staticmethod
    # get tree获取所有的 获取构造数据树
    def get_constructor_tree(name: str):
        """
        get tree获取构造数据树
        :param name:
        :return:
        """
        try:
            with Session() as session:
                # 获取所有构造参数
                if name:
                    constructor = session.query(Constructor).filter(Constructor.public == True,
                                                                    Constructor.name.ilike("%{}%".format(name)),
                                                                    Constructor.deleted_at == None).all()
                else:
                    constructor = session.query(Constructor).filter(Constructor.public == True,
                                                                    Constructor.deleted_at == None).all()
                if not constructor:
                    return []
                temp = defaultdict(list)
                # 建立caseID -> constructor的map
                for c in constructor:
                    temp[c.case_id].append(c)
                testcases = session.query(TestCase).filter(TestCase.id.in_(temp.keys())).all()
                testcase_info = {t.id: t for t in testcases}
                result = []
                for k, v in temp.items():
                    result.append({
                        "key": f"caseId_{k}",
                        "disabled": True,
                        "title": testcase_info[k].name,
                        "children": [
                            {"key": f"constructor_{x.id}", "title": x.name, "value": f"constructor_{x.id}"} for x in v
                        ],
                    })
        except Exception as e:
            ConstructorDao.log.error(f"获取构造数据树失败, {e}")
            raise Exception("获取构造数据失败")

    # get获取
    @staticmethod
    def get_constructor_data(id_: int):
        """
        get获取构造数据
        :param id_:
        :return:
        """
        with Session() as session:
            data = session.query(Constructor).filter_by(id=id_, deleted_at=None).first()
            if data is None:
                raise Exception("构造数据不存在")
            return data
