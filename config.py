import os

class Config:
    SECRET_KEY = 'SKIRDLE'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
