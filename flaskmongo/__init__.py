from flask import Flask
from config import Config

from flask_wtf.csrf import CSRFProtect

from flask_mongoengine import MongoEngine
# from flask_restplus import Api

from flaskmongo.myblueprint import example_blueprint
from .auth import auth
from .admin import admin

# api = Api()

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create an application object
app = Flask(__name__)
app.config.from_object(Config)

# app.config["SECRET_KEY"] = "12345678"
# csrf = CSRFProtect(app)

app.register_blueprint(example_blueprint)
app.register_blueprint(auth)
app.register_blueprint(admin)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'user',
#     'host': 'localhost',
#     'port': 27017
# }

db = MongoEngine()
db.init_app(app)
# api.init_app(app)

from flaskmongo import routes
