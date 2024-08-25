from flask_sqlalchemy import SQLAlchemy
from app import pity
from flask_migrate import Migrate

db = SQLAlchemy(pity)
migrate = Migrate(pity, db)
pity.app_context().push()
