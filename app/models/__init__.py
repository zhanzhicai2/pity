# from flask_sqlalchemy import SQLAlchemy
# from app import pity
# from flask_migrate import Migrate
#
# db = SQLAlchemy(pity)
# migrate = Migrate(pity, db)
# pity.app_context().push()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(engine)
# 创建对象的基类:
Base = declarative_base()
# from app.models import engine, Base
Base.metadata.create_all(engine)
