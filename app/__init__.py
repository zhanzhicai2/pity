from flask import Flask
from flask_cors import CORS

from config import Config

pity = Flask(__name__)
CORS(pity, supports_credentials=True)
# CORS(pity)

pity.config.from_object(Config)

