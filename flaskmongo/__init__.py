from flask import Flask
from flask_mongoengine import MongoEngine
import datetime

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

db = MongoEngine(app)
