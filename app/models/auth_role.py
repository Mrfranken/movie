from .base import db, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class Auth(Base):
    """
    权限模型
    """
    __tablename__ = 'auth'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    url = Column(String(200), unique=True)


class Role(Base):
    """
    角色模型
    """
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    auths = Column(String(100))  # 角色权限列表
