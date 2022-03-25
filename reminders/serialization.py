from reminders.models import Reminder


def serialize_reminders(reminders: list[Reminder]) -> list[dict]:
    """
    Converts a list of Reminder objects to a representation suitable for use
    with Flask's `jsonify` function.
    """
    result = []

    for reminder in reminders:
        serialized_reminder = serialize_reminder(reminder)
        result.append(serialized_reminder)

    return result


def serialize_reminder(reminder: Reminder) -> dict:
    """
    Converts a single Reminder object into a representation suitable for use
    with Flask's `jsonify` function.
    """
    return {
        'title': reminder.title,
        'priority': reminder.priority.value
    }
