from os import path, environ
import os


class Config(object):
    BASE_DIR = path.abspath(path.dirname(__file__))

    SECRET_KEY = "kljadskl10248120318znx"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, "db.sqlite")

    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')