# -*- coding: utf-8 -*-

from .base import db, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from flask_login import UserMixin


class Admin(Base, UserMixin):
    """
    会员身份模型
    """
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    name = Column(String(24), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    is_super = Column(SmallInteger)  # 是否为超级管理员，0为超级管理员
    # role_id = Column(Integer, ForeignKey('role.id'))
    # admin_log = db.relationship('AdminLog', backref='admin')
    # operate_log = db.relationship('OperateLog', backref='admin')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_pwd):
        self._password = generate_password_hash(raw_pwd)

    def check_password(self, raw_pwd):
        return check_password_hash(self.password, raw_pwd)

    def get_id(self):
        return self.id


@login_manager.user_loader
def user_loader(user_id):
    return db.session.query(Admin).get(int(user_id))


class AdminLog(Base):
    __tablename__ = 'adminlog'

    id = db.Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey('admin.id'))
    ip = db.Column(db.String(100))  # 登录IP


# 操作日志
class OperateLog(Base):
    __tablename__ = "operatelog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 操作IP
    reason = db.Column(db.String(600))  # 操作原因
