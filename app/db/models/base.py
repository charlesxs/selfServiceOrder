# coding=utf-8
#

from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy(session_options={
    'autocommit': True
})

