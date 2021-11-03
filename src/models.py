import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    photo_url = Column(String(220), unique=False, nullable=True)
    
    
class Publicate(Base):
    __tablename__ = 'publicate'
    id = Column(Integer, primary_key=True)
    archive_url = Column(String(450))
    date_publicate = Column(String(120), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    
    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id_publicate = Column(Integer, ForeignKey('user.id'))
    id_publicate = Column(Integer, ForeignKey('publicate.user_id'))
    
    def to_dict(self):
        return {}
    
class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    user_id_ppl = Column(Integer, ForeignKey('user.id'))
    user_id_follow = Column(Integer, ForeignKey('user.id'))
    
    def to_dict(self):
        return {}
    
    
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
