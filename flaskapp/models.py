from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(64), unique=False)
    
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        
    def __repr__(self):
        return '<User %r>' % (self.name,)
