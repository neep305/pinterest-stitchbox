from flask import Blueprint
from flask import render_template, jsonify, json

auth = Blueprint('auth', __name__)


@auth.route('/auth')
def index():
    return jsonify(user='jason', token='111')
