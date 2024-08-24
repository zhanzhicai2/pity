from app.utils.logger import Log
from app.models import db
from app.models.project_role import ProjectRole


class ProjectRoleDao(object):
    log = Log("ProjectRoleDao")

    @staticmethod
    def list_project_by_user(user_id) -> (list, str):
        """
        通过user_id获取项目列表
        :param self:
        :param user_id:
        :return:
        """
        try:
            projects = ProjectRole.query.filter_by(user_id=user_id, deleted_at=None).all()
            # projects = ProjectRole.query.get(user_id)
            return [p.id for p in projects], None
        except Exception as e:
            ProjectRoleDao.log.error(f"查询用户：{user_id}项目失败，{e}")
            return [], f"查询项目失败，{e}"

    @staticmethod
    def add_project_role(user_id, project_id, project_role, user):
        """
        为项目添加用户
        :param self:
        :param user_id: 用户ID
        :param project_id: 项目ID
        :param project_role: 用户角色
        :param user: 创建人
        :return:
        """
        try:
            role = ProjectRole.query.filter_by(user_id=user_id, project_id=project_id, project_role=project_role,
                                               deleted_at=None).first()
            if role is not None:
                return "用户已经存在"
            role = ProjectRole(user_id, project_id, project_role, user)
            db.session.add(role)
            db.session.commit()
        except Exception as e:
            # ProjectRole.log.error(f"添加项目用户失败，{e}")
            ProjectRoleDao.log.error(f"添加项目用户失败，{e}")
            return f"添加项目失败，{e}"
        return None
