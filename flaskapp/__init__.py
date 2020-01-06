from flask import Flask, request, jsonify, make_response
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return JSONEncoder.default(self, o)

app = Flask(__name__)

app.id_count = 1

@app.route("/")
def response_test():
    return make_response("Custom Response")




