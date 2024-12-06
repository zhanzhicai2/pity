# encoding: utf-8
# @File  : TestResult.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/12/04

from datetime import datetime

from sqlalchemy import select, asc

from app.models import async_session
from app.models.result import PityTestResult
from app.utils.logger import Log


class TestResultDao(object):
    log = Log("TestResultDao")

    @staticmethod
    async def insert(report_id: int, case_id: int, status: int, case_name: str,
                     case_log: str, start_at: datetime, finished_at: datetime,
                     url: str, body: str, request_method: str, request_headers: str, cost: str,
                     asserts: str, response_headers: str, response: str,
                     status_code: int, cookies: str, retry: int = None, ) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    result = PityTestResult(report_id, case_id, status, case_name,
                                            case_log, start_at, finished_at,
                                            url, body, request_method, request_headers, cost,
                                            asserts, response_headers, response,
                                            status_code, cookies, retry)
                    session.add(result)
                    await session.flush()
        except Exception as e:
            TestResultDao.log.error(f"新增测试结果失败, error: {e}")
            raise Exception("新增测试结果失败")

    @staticmethod
    async def list(report_id: int) -> None:
        try:
            async with async_session() as session:
                sql = select(PityTestResult).where(PityTestResult.report_id == report_id,
                                                   PityTestResult.deleted_at == None).order_by(
                    asc(PityTestResult.start_at))
                data = await session.execute(sql)
                return data.scalars().all()
        except Exception as e:
            TestResultDao.log.error(f"获取测试用例执行记录失败, error: {e}")
            raise Exception("获取测试用例执行记录失败")
