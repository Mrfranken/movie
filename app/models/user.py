# -*- coding: utf-8 -*-

from .base import db, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager


class User(Base):
    """
    会员身份模型
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(24), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(String(18), unique=True)
    info = Column(Text(500))
    face = Column(String(50))
    uuid = Column(String(128))
    user_log = db.relationship('UserLog', backref='user')
    comment = db.relationship('Comment', backref='user')
    movie_col = db.relationship('MovieCol', backref='user')

    # related link: https://blog.csdn.net/chenmozhe22/article/details/95607372


class UserLog(Base):
    """
    会员登录及登录日志模型
    """
    __tablename__ = 'userlog'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    ip = Column(String(15))
