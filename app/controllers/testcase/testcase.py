from flask import Blueprint
from flask import jsonify
from flask import request

from app.dao.test_case.TestCaseDao import TestCaseDao
from app.handler.fatcory import ResponseFactory
from app.utils.decorator import permission, json_validate

ts = Blueprint("testcase", __name__, url_prefix="/testcase")

testcase = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
        },
        "name": {
            "type": "string",
        },
        "request_type": {
            "type": "integer",
        },
        "url": {
            "type": "string",
        },
        "request_method": {
            "type": "string",
        },
        "request_header": {
            "type": "string",
        },
        "params": {
            "type": "string",
        },
        "body": {
            "type": "string",
        },
        "project_id": {
            "type": "integer",
        },
        "tag": {
            "type": "string",
        },
        "status": {
            "type": "integer",
        },
        "priority": {
            "type": "string",
        },
        "catalogue": {
            "type": "string",
        },
        # "expected": {
        #     "type": "string",
        # },
    },
    # "required": ["expected", "catalogue", "status", "project_id", "request_type", "url", "name"]
    "required": ["catalogue", "priority", "status", "project_id", "request_type", "url", "name"]
}


@ts.route("/insert", methods=['POST'])
@json_validate(testcase)
@permission()
def insert_testcase(user_info):
    data = request.get_json()
    err = TestCaseDao.insert_test_case(data, user_info['id'])
    if err:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=0, msg="操作成功"))


@ts.route("/query")
@permission()
def query_testcase(user_info):
    case_id = request.args.get("caseId")
    if case_id is None or not case_id.isdigit():
        return jsonify(dict(code=101, msg="case_id不正确"))
    data, err = TestCaseDao.query_test_case(int(case_id))
    if err:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=0, data=ResponseFactory.model_to_dict(data), msg="操作成功"))
