from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

db = MongoEngine()


def create_app(test_config='dev'):
    # create and configure the app
    app = Flask(__name__)
    # app.config.from_object(config[test_config])
    # config[test_config].init_app(app)
    # mongo.init_app(app)
    CORS(app, resources=r"/*")
    app.config['MONGODB_SETTINGS'] = {
        'db': 'DataM',
        'host': '127.0.0.1',
        'port': 27017
    }
    db.init_app(app)

    from flaskr.D_blueprint import auth
    app.register_blueprint(auth.bp)

    return app
