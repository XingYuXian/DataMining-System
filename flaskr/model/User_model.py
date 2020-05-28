from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flaskr import db


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    mail = db.StringField(required=True)

    def to_json(self):
        return {
            "username": self.username,
            "password": self.password,
            "mail": self.mail
        }
