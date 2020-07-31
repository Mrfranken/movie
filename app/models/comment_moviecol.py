from .base import db, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class Comment(Base):
    """
    电影评论模型
    """
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


class MovieCol(Base):
    """
    电影收藏模型
    """
    __tablename__ = 'moviecol'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
