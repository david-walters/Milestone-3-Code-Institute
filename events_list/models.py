"""
This module defines the database models for the events_list application.

It includes the Event model, which represents an event in the system. Each
event contains information such as city, event name, description, and date.
"""

from datetime import datetime, timezone
from events_list import db

class Event(db.Model):
    """
    Represents an event with details such as city, event name, description, and date.
    Each event is stored as a row in the 'events' table.
    """
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    event_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    event_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Event instance, useful for debugging.
        """
        return (f'<{self.id}: {self.city} | {self.event_name} | '
                f'{self.event_date}>')

    def is_upcoming(self):
        """
        Checks if the event is scheduled for a future date.
        """
        return self.event_date > datetime.now(timezone.utc).date()
