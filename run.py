from datetime import datetime

from app import pity
from app.utils.logger import Log
from app.controllers.auth.user import auth
from app.controllers.request.http import req
from app.controllers.project.project import pr
from app import dao

# 注册蓝图
pity.register_blueprint(auth)
pity.register_blueprint(req)
pity.register_blueprint(pr)


@pity.route('/')
def hello_world():  # put application's code here
    log = Log("hello world专用")
    # log.info("有人访问你的网站了")
    now = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    return now
    return 'Hello World!3344'


if __name__ == '__main__':
    pity.run("0.0.0.0", threaded=True, port="7777")
