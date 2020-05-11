from flaskmongo import db
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash


def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate


class User(db.Document):
    
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30, unique=True)
    password = db.StringField()
    
    def to_json(self):
        return {"name": self.name, "email": self.email}
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def get_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User %r>' % self.name


class Course(db.Document):
    course_id = db.StringField(max_length=10, unique=True)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=255)
    credits = db.IntField()
    term = db.StringField(max_length=25)
    
    
class Enrollment(db.Document):
    user_id = db.IntField()
    course_id = db.StringField(max_length=10)
