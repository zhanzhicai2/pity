from flask import Blueprint, request, jsonify

from app import pity
from app.handler.page import PageHandler
from app.dao.project.ProjectRole import ProjectDao
from app.utils.decorator import permission
from app.handler.fatcory import ResponseFactory

pr = Blueprint("/project", __name__, url_prefix="/project")


@pr.route("/list")
@permission(role=pity.config.get("GUEST"))
# @permission()
def list_project(user_info):
    """
    获取项目列表
    :param user_info:
    :return:
    """
    page, size = PageHandler.page()
    user_role, user_id = user_info["role"], user_info["id"]
    name = request.args.get("name")
    result, total, err = ProjectDao.list_project(user_id, user_role, page, size, name)

    if err is not None:
        return jsonify(dict(code=110, data=result, msg=err))
    # 自己加，后续可能要删除，判断list是不是空[]
    if not result:
        return jsonify(dict(code=0, data=result, msg="操作成功"))
    result = [ResponseFactory.model_to_dict(pr) for pr in result]
    return jsonify(dict(code=0, data=result, msg="操作成功"))


@pr.route("/insert", methods=["POST"])
# @permission(pity.config.get("MANAGER"))
@permission()
def insert_project(user_info):
    """
    插入新项目
    :param user_info:
    :return:
    """
    try:
        user_id = user_info["id"]
        data = request.get_json()
        if not data.get("name") or not data.get("owner"):
            return jsonify(dict(code=101, msg="项目名称/项目负责人不能为空"))
        private = data.get("private", False)
        err = ProjectDao.add_project(data.get("name"), data.get("owner"), user_id, private)
        if err is not None:
            return jsonify(dict(code=110, msg=err))
        return jsonify(dict(code=0, msg="操作成功"))
    except Exception as e:
        return jsonify(dict(code=111, msg=str(e)))
