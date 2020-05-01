from flask import Flask, request, jsonify, make_response, session
from flask.json import JSONEncoder
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

import flaskapp.models
from flaskapp.app_decorator import login_required, cached


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return JSONEncoder.default(self, o)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pypostgresql://sqlalchemy:sqlalchemy@localhost/sqlalchemy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/")
def response_test():
    print(session)
    return render_template('home.html') # make_response("Custom Response")


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route("/member")
@login_required
def member_page():
    return render_template("/member_page.html")


@app.route("/board_view")
@cached(timeout=10*60, key='board/%s')
def board_view():
    return render_template("/board_view.html")
