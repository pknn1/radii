from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(250))
    location = db.Column(db.String(100), index=True)
    image_url = db.Column(db.String(200), index=True)
    date_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def is_event_nearby(self):
        pass
        # return Event.location

    def is_event_passed(self):
        # return true if passed and false if not
        present = datetime.utcnow()
        event = self.date_time
        if event < present:
            return True
        else:
            return False

    def is_event_upcoming(self):
        # before 3 days
        event = self.date_time
        upcoming = datetime.utcnow() + timedelta(days=3)
        if upcoming < event:
            return True
        else:
            return False


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
