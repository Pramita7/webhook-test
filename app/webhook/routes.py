from flask import Blueprint, request
from datetime import datetime
from ..extensions import mongo

webhook = Blueprint('webhook', __name__, url_prefix='/webhook')

def format_event(event_type, payload):
    """Extract minimal info and return message+timestamp dict"""
    timestamp = datetime.utcnow()
    nice_time = timestamp.strftime('%-d %b %Y - %-I:%M %p UTC')

    if event_type == 'push':
        author = payload.get('pusher', {}).get('name')
        to_branch = payload.get('ref', '').split('/')[-1]
        message = f'{author} pushed to {to_branch} on {nice_time}'
        return {'message': message, 'timestamp': timestamp}

    if event_type == 'pull_request':
        action = payload.get('action')
        author = payload.get('sender', {}).get('login')
        from_branch = payload['pull_request']['head']['ref']
        to_branch = payload['pull_request']['base']['ref']

        if action == 'opened':
            message = f'{author} submitted a pull request from {from_branch} to {to_branch} on {nice_time}'
            return {'message': message, 'timestamp': timestamp}

        if action == 'closed' and payload['pull_request'].get('merged'):
            message = f'{author} merged branch {from_branch} to {to_branch} on {nice_time}'
            return {'message': message, 'timestamp': timestamp}

    return None

@webhook.route('/receiver', methods=['POST'])
def receiver():
    """Receive GitHub webhook, store formatted event"""
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.get_json() or {}
    record = format_event(event_type, payload)

    if record:
        mongo.db.events.insert_one(record)

    return {'saved': bool(record)}, 200
