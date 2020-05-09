from flaskmongo import app, db, api
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
from flaskmongo.models import User
from flask_restplus import Resource


@api.route('/api', '/api/')
class GetAndPost(Resource):
    
    def get(self):
        return jsonify(User.objects.all())
    

@api.route('/api/<idx>')
class GetUpdateDelete(Resource):
    
    def get(self, idx):
        return jsonify(User.objects(user_id=idx))
