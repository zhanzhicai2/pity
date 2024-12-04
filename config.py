import os


class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    # 这行代码的作用是找到当前执行脚本所在的目录的绝对路径，并将这个路径赋值给变量 ROOT。这个变量通常用作后续文件路径操作的基准点
    # print(ROOT)
    # print(os.path.abspath(__file__))

    LOG_NAME = os.path.join(ROOT, 'logs', 'pity.log')
    # os.path.join(ROOT, 'logs', 'pity.log') 将 ROOT 变量（即脚本所在的目录的绝对路径）、字符串 'logs' 和字符串 'pity.log' 合并成一个完整的文件路径。这个路径指向
    # ROOT 目录下的一个名为 logs 的子目录，而 pity.log 文件则位于这个 logs 目录下
    # print(LOG_NAME)

    # Flask jsonify编码问题
    # JSON_AS_ASCII = False

    # mysql连接信息
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = "3306"
    MYSQL_USER = "root"
    MYSQL_PWD = "root"
    DBNAME = "pity"

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)
    # 异步URI aiomysql
    ASYNC_SQLALCHEMY_URI = f'mysql+aiomysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{DBNAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 权限 0 普通用户 1 组长 2 管理员
    GUEST = 0
    MANAGER = 1
    ADMIN = 2

    # github access_token地址
    GITHUB_ACCESS = "https://github.com/login/oauth/access_token"

    # github获取用户信息
    GITHUB_USER = "https://api.github.com/user"

    # client_id
    CLIENT_ID = "Ov23liVwVosaCVRmkjg2"
    # CLIENT_ID = "c46c7ae33442d13498cd"

    # SECRET
    SECRET_KEY = "490e04ca7426209c0b43b4ae4884a70e01c7c785"
    # SECRET_KEY = "c79fafe58ff45f6b5b51ddde70d2d645209e38b9"
