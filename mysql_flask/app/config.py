import os
from app.configFileReader import readConfigFile
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = readConfigFile("server", "SERVER_SECRET")
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'do-or-do-not-there-is-no-try'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://"
        + readConfigFile("database", "MYSQL_DATABASE_USER")
        + ":"
        + readConfigFile("database", "MYSQL_DATABASE_PASSWORD")
        + "@"
        + readConfigFile("database", "MYSQL_DATABASE_HOST")
        + ":"
        + readConfigFile("database", "MYSQL_DATABASE_PORT")
        + "/"
        + readConfigFile("database", "MYSQL_DATABASE_DB")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = readConfigFile("server", "SQLALCHEMY_TRACK_MODIFICATIONS")
