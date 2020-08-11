from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, SmallInteger, Integer, NVARCHAR, String, DateTime, Boolean, Float, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
import os
import markdown
from collections import namedtuple

session = None


def explict_repr(self):
    d = {}
    for v in dir(self.__class__):
        if not v.startswith('_'):
            d.update({v: getattr(self, v)})
    return str(d)


Base = declarative_base()
setattr(Base, '__repr__', explict_repr)


class ChangeLogModel(Base):
    __tablename__ = 'changelog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    path = Column(String(150))
    size = Column(Integer)
    content = Column(Text)


def create_session():
    global session
    connection_repr = 'mysql+pymysql://root:taf_blog@localhost:3306/taf_blog'
    engine = create_engine(connection_repr)
    DbSession = sessionmaker(bind=engine)
    session = DbSession()


def insert_data(o: object):
    session.add(o)
    try:
        session.commit()
        session.close()
    except Exception as e:
        session.rollback()
        raise


def md2html(filename):
    exts = ['markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.toc']
    mdcontent = ""
    with open(filename, 'r', encoding='utf-8') as f:
        mdcontent = f.read()
    html = markdown.markdown(mdcontent, extensions=exts)
    return html


def changelog_files():
    """
    :rtype: list
    """
    change_log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'changelog')
    for root, _, files_list in os.walk(change_log_dir):
        for file in files_list:
            name = file.rsplit('.', 1)[0]
            html = md2html(os.path.join(root, file))

            changelog = ChangeLogModel()
            changelog.name = name
            changelog.content = html
            yield changelog


create_session()
changelog = ChangeLogModel()
changelog.name = 'Bob'
changelog.content = 'content'
insert_data(changelog)
# for o in changelog_files():
#     insert_data(o)
