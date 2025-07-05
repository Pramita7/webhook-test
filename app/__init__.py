import os
from flask import Flask, render_template, send_from_directory
from .extensions import mongo, init_mongo
from .webhook.routes import webhook

def create_app():
    """Factory pattern so tests or gunicorn can create an app easily"""
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # ---- Config ----
    # Use env var if available, else default local MongoDB
    app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/webhook_db')

    # ---- Init Extensions ----
    init_mongo(app)

    # ---- Blueprints ----
    app.register_blueprint(webhook)

    # ---- UI Routes ----
    @app.route('/')
    def index():
        """Serves simple UI that polls every 15 s"""
        return render_template('index.html')

    @app.route('/events')
    def events_api():
        """Return last 15 events as JSON (newest first)"""
        events_cursor = mongo.db.events.find().sort('timestamp', -1).limit(15)
        events = [{**e, '_id': str(e['_id'])} for e in events_cursor]
        return events

    return app
