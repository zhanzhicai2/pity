from flask_sqlalchemy import SQLAlchemy
from app import pity

db = SQLAlchemy(pity)
pity.app_context().push()