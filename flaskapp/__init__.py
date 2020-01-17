from flask import Flask, request, jsonify, make_response
from flask.json import JSONEncoder
from flask import render_template

class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return JSONEncoder.default(self, o)

app = Flask(__name__)


@app.route("/")
def response_test():
    return render_template('home.html') # make_response("Custom Response")


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)
