from flask_pymongo import PyMongo

mongo = PyMongo()

def init_mongo(app):
    """Initialize PyMongo extension"""
    mongo.init_app(app)
