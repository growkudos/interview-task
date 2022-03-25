from reminders.models import Reminder, Priority


def test_init():
    reminder = Reminder('This is the title', priority=Priority.HIGH)

    assert reminder.title == 'This is the title'
    assert reminder.priority == Priority.HIGH


def test_default_priority():
    reminder = Reminder('Some title')
    assert reminder.priority == Priority.NORMAL
