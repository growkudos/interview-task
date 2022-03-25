from flask.testing import FlaskClient

from reminders.models import Reminder


def test_index(client: FlaskClient):
    # The index is currently not very functionality-rich, so we can just test
    # that it returns a 200 OK response:
    response = client.get('/')
    assert response.status_code == 200


def test_list_reminders(client: FlaskClient, test_reminders: list[Reminder]):
    response = client.get('/reminders')
    assert response.status_code == 200

    assert response.is_json

    expected_json = [
        {'title': 'Test reminder 1', 'priority': 1},
        {'title': 'Test reminder 2', 'priority': 2},
        {'title': 'Test reminder 3', 'priority': 3}
    ]
    assert response.json == expected_json


def test_create_reminder(client: FlaskClient, test_reminders: list[Reminder]):
    # First, we'll check how many reminders we currently have:
    list_json_before = client.get('/reminders').json
    assert isinstance(list_json_before, list)
    assert len(list_json_before) == 3

    response = client.post('/reminders',
                           json={'title': 'New reminder', 'priority': 3})
    assert response.status_code == 201

    assert response.is_json

    expected_json = {'title': 'New reminder', 'priority': 3}
    assert response.json == expected_json

    # We can use the list reminders endpoint to check that the reminder was
    # created:
    list_json_after = client.get('/reminders').json
    assert isinstance(list_json_after, list)
    assert len(list_json_after) == 4
    assert list_json_after[-1] == {'title': 'New reminder', 'priority': 3}


def test_create_reminder_with_default_priority(client: FlaskClient,
                                               test_reminders: list[Reminder]):
    response = client.post('/reminders',
                           json={'title': 'New reminder'})
    assert response.status_code == 201

    assert response.is_json

    expected_json = {'title': 'New reminder', 'priority': 2}
    assert response.json == expected_json

    # We can use the list reminders endpoint to check the created remitnder
    list_json_after = client.get('/reminders').json
    assert isinstance(list_json_after, list)
    assert list_json_after[-1] == {'title': 'New reminder', 'priority': 2}


def test_create_reminder_without_title(client: FlaskClient,
                                       test_reminders: list[Reminder]):
    response = client.post('/reminders',
                           json={'priority': 3})
    assert response.status_code == 400


def test_create_reminder_with_empty_title(client: FlaskClient,
                                          test_reminders: list[Reminder]):
    response = client.post('/reminders',
                           json={'title': '', 'priority': 3})
    assert response.status_code == 400
