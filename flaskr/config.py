# import os
# from flask_pymongo import PyMongo
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
#
# class BaseConfig:
#     SECRET_KEY = 'dev'
#
#     @staticmethod
#     def init_app(app):
#         pass
#
#
# class DevConfig(BaseConfig):
#     MONGO_URI = 'mongodb://localhost:27017/DataM'
#
#     @staticmethod
#     def init_app(app):
#         app = PyMongo(app)
#         return app
#
#
# config = {
#     'dev': DevConfig
# }
