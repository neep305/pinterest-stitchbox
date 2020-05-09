from flask import Flask

from flask_mongoengine import MongoEngine
from flask_restplus import Api


api = Api()

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create an application object
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'user',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)
api.init_app(app)

from flaskmongo import routes
