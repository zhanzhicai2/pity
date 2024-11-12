from flask import Flask
from flask_cors import CORS


from config import Config

# from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
# from flask_restful_swagger import swagger

pity = Flask(__name__)
CORS(pity, supports_credentials=True)
# api = swagger.docs(Api(pity), apiVersion='0.1')
# CORS(pity)

pity.config.from_object(Config)





