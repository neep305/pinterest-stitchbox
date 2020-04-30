from flaskmongo import db
from flask import jsonify


def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate


class User(db.Document):
    
    name = db.StringField()
    email = db.StringField()
    
    def to_json(self):
        return {"name": self.name, "email": self.email}
    
    def __repr__(self):
        return '<User %r>' % self.name
