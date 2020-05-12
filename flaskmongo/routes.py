from flaskmongo import app, db, api
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
from flaskmongo.models import User
from flask_restplus import Resource


@api.route('/api', '/api/')
class GetAndPost(Resource):
    
    # GET All
    def get(self):
        return jsonify(User.objects.all())
    
    # POST
    def post(self):
        data = api.payload
        print(data)
        
        user = User(user_id=data['user_id'],
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'])
        
        user.set_password(data['password'])
        user.save()
        
        return jsonify(User.objects(user_id=data['user_id']))
    

@api.route('/api/<idx>')
class GetUpdateDelete(Resource):
    
    # GET One
    def get(self, idx):
        return jsonify(User.objects(user_id=idx))

    # PUT
    def put(self, idx):
        data = api.payload
        User.objects(user_id=idx).update(**data)
        return jsonify(User.objects(user_id=idx))

    # DELETE
    def delete(self, idx):
        User.objects(user_id=idx).delete()
        return jsonify("User is deleted!!")
