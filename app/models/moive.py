# -*- coding: utf-8 -*-

from .base import db, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, SmallInteger, Date

"""
标签、电影、上映预告数据模型
"""


class Tag(Base):
    """
    标签模型
    """
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # movie = db.relationship('Movie', backref='tag')

    @classmethod
    def get_tags_by_page(cls, page):
        if not page:
            page = 1
        return Tag.query.order_by(Tag.create_time).paginate(page=page, per_page=2)


class Movie(Base):
    """
    定义电影数据模型
    """
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    url = Column(String(255), unique=True)
    info = Column(Text)  # 简介
    logo = Column(String(255), unique=True)
    star = Column(SmallInteger)
    play_mum = Column(Integer)
    comment_num = Column(Integer)
    tag_id = Column(Integer, ForeignKey('tag.id'))
    area = Column(String(100))
    release_time = Column(Date)
    length = Column(String(20))
    # comment = db.relationship('Comment', backref='movie')
    # movie_col = db.relationship('MovieCol', backref='movie')


class Preview(Base):
    """
    上映预告
    """
    __tablename__ = 'preview'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    logo = Column(String(255), unique=True)
