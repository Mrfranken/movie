# -*- coding: utf-8 -*-
# 千万千万不要将 127.0.0.1 写成 localhost
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:8823443wsj_WIN@127.0.0.1:3306/movie'  # pip install cymysql
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '8823443wsj_WIN'

"""
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
  
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
  
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
  
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
"""

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = True
MAIL_USERNAME = 'wsj973507837@163.com'
MAIL_PASSWORD = 'FGKICBQPTEILFZHT'
MAIL_SUBJECT_PREFIX = '小黄'
MAIL_SENDER = '小黄 <wsj973507837@163.com>'
