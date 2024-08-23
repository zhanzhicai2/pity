# select * from project where deleted_at is null
# and (owner = user or project_id in (已经查出的用户项目) or private is false)
from sqlalchemy import or_

from app import pity
from app.dao.project.projectRoleDao import ProjectRoleDao
from app.models.project import Project
from app.utils.logger import Log


class ProjectDao(object):
    log = Log("ProjectDao")

    # 查询
    def list_project(self, user, role, page, size, name=None):
        """

        :param user:
        :param role:
        :param page:
        :param size:
        :param name:
        :return:
        """
        try:
            search = [Project.deleted_at is None]
            if role != pity.config.get("ADMIN"):
                project_list = ProjectRoleDao.list_project_by_user(user)
                search.append(or_(Project.id in project_list, Project.owner == user, Project.private == False))
            if name:
                search.append(Project.name.ilike("%{}%".format(name)))
            data = Project.query.filter(**search)
            total = data.count()
            return data.order_by(Project.create_at.desc()).paginate(page, per_page=size).items, total, None
        except Exception as e:
            ProjectDao.log.error(f"获取用户: {user}项目列表失败, {e}")
            return 0, 0, f"获取用户: {user}项目列表失败, {e}"

    # 添加
    def add_project(self):
        try:
            data = Project.query.filter_by(name=name, deleted_at=None).first()
            if data is None:
                return "项目已存在"
            pr = Project(name, owner, user, private)
            db.session.add(pr)
            db.session.commit(pr)
        except Exception as e:
            ProjectDao.log.error(f"新增项目: {name}失败, {e}")
            return 0, 0, f"新增项目: {name}失败, {e}"

