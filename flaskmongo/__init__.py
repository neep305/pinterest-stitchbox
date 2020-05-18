from flask import Flask, render_template

from flask_mongoengine import MongoEngine
# from flask_restplus import Api

from flaskmongo.myblueprint import example_blueprint


# api = Api()

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create an application object
app = Flask(__name__)
app.register_blueprint(example_blueprint)
app.config['MONGODB_SETTINGS'] = {
    'db': 'user',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)
# api.init_app(app)

# from flaskmongo import routes


@app.route('/')
def index():
    return render_template('home.html')
