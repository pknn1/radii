import datetime
from app.models import Event
from app import db


def test_event_passed():
    u = Event(
        "test",
        "description",
        "location",
        "url",
        date_time=datetime.datetime(2019, 12, 1, 10, 30, 11),
    )
    db.session.add(u)
    db.session.commit()

    assert not u.is_event_passed()


def test_event_upcoming():
    u = Event(
        "test",
        "description",
        "location",
        "url",
        date_time=datetime.datetime(2018, 9, 1, 10, 30, 11),
    )
    db.session.add(u)
    db.session.commit()

    assert not u.is_event_upcoming()
