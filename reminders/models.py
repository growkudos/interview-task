from enum import Enum


class Priority(Enum):

    """
    The Priority enum contains values representing how important a Reminder
    is.
    """

    LOW = 1
    NORMAL = 2
    HIGH = 3


class Reminder:

    """
    A Reminder represents a task to complete, with a title and priority.
    """

    title: str
    priority: Priority

    def __init__(self, title: str, priority: Priority = None):
        """
        Creates a new reminder.

        Parameters:
        title: The title of the reminder
        priority: Optionally, the priority of the reminder. If not given,
            the priority will default to Priority.NORMAL.
        """
        self.title = title

        if priority is None:
            self.priority = Priority.NORMAL
        else:
            self.priority = priority
