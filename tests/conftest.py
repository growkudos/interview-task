from typing import Iterator
from flask import Flask
from flask.testing import FlaskClient
import pytest

import reminders
from reminders.models import Priority, Reminder


# Fixtures are automatically available in tests, just by giving the test
# function a parameter with the same name as the fixture
# (like `def test_something(client)`)

@pytest.fixture
def app() -> Flask:
    """
    Returns an instance of our Flask reminders app with its TESTING flag set.
    """
    # In the future it'd probably be better to have an app factory function
    # so we don't have to modify this global variable. In reality, we won't be
    # running tests and the app in the same process, so it won't matter.
    reminders.app.testing = True
    return reminders.app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """
    Returns a client that can be used to make requests to routes defined in the
    app.
    """
    return app.test_client()


# The return type annotation here is a result of how Pytest fixtures with clean
# up values make use of Python's generator functions. Tests that use this
# fixture will receive a value of type `list[Reminder]`.
@pytest.fixture
def test_reminders() -> Iterator[list[Reminder]]:
    """
    Sets up some static test data and then yields the reminder storage list so
    tests can make further changes if desired. The data that was stored before
    the test will be restored afterwards.
    """
    reminders_before_test = reminders.CURRENT_REMINDERS

    reminders.CURRENT_REMINDERS = [
        Reminder('Test reminder 1', priority=Priority.LOW),
        Reminder('Test reminder 2'),
        Reminder('Test reminder 3', priority=Priority.HIGH)
    ]

    yield reminders.CURRENT_REMINDERS

    # This code will run after each test completes to put the reminders list
    # back to the way it was.
    reminders.CURRENT_REMINDERS = reminders_before_test
