"""
A small Flask web app which provides a simple REST API that can be used to
view and add to a list of reminders.
"""

from flask import abort, Flask, jsonify, request, url_for

from reminders.models import Reminder, Priority
from reminders.serialization import serialize_reminders, serialize_reminder


app = Flask(__name__)

# For simplicity, we'll store our reminders in a global variable, and provide
# some default values.
CURRENT_REMINDERS = [
    Reminder('Re-paint the living room', priority=Priority.LOW),
    Reminder('Learn some Python'),
    Reminder('Complete the interview task', priority=Priority.HIGH)
]


@app.route('/')
def index():
    """Renders our API's root object to facilitate API discovery."""
    # So that users of our API can discover how to use it, we'll give them the
    # URL where they can find the reminder list. We could add other API
    # endpoints here if we add other resources to this app.
    return {
        'reminders': url_for('list_reminders')
    }


@app.route('/reminders', methods=['GET'])
def list_reminders():
    """
    Renders a JSON array with all the reminders currently stored in the app.
    """
    return jsonify(serialize_reminders(CURRENT_REMINDERS))


@app.route('/reminders', methods=['POST'])
def create_reminder():
    """
    Creates a new reminder at the bottom of our list of reminders.
    """
    title = request.json.get('title', '')
    if title == '':
        # The title field was either missing or set directly to an empty
        # string:
        abort(400, 'The title field must be provided')

    # priority_value will be a number, which we can turn into a Priority enum
    # member. If the 'priority' field isn't present in the request,
    # priority_value will be set to `None`.
    priority_value = request.json.get('priority')

    try:
        priority = Priority(priority_value)
    except ValueError:
        priority = None

    new_reminder = Reminder(title, priority=priority)

    CURRENT_REMINDERS.append(new_reminder)

    return jsonify(serialize_reminder(new_reminder)), 201
