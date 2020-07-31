# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime
from contextlib import contextmanager
from datetime import datetime


class BaseSqlAlchemy(SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise


db = BaseSqlAlchemy()


class Base(db.Model):
    __abstract__ = True

    create_time = Column('create_time', DateTime, index=True)

    def __init__(self):
        setattr(Base, '__repr__', self.explict_repr)
        self.create_time = datetime.utcnow()

    def explict_repr(self):
        d = {}
        for v in dir(self.__class__):
            if not v.startswith('_'):
                d.update({v: getattr(self, v)})
        return '<{} {}>'.format(self.__class__.__name__, str(d))

    def set_value_for_table(self, value_dict: dict):
        for k, v in value_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)
