from app import db, login_manager
from app.models import User, Event, Category
from flask_login import login_user, current_user


class UserController:
    @staticmethod
    def create_user(display_name, email):
        user = User(display_name, email)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user(id):
        return User.query.get(id)


class EventController:
    @staticmethod
    def create_event(name, description, location, image_url, date_time, category_name):
        category = Category.query.filter_by(name=category_name).first()
        if category is None:
            category = Category(category_name)
            db.session.add(category)
        event = Event(name, description, location, image_url, date_time)
        category.add_event(event)
        db.session.add(event)
        db.session.commit()
        return event


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class AuthController:
    @staticmethod
    def oauth(display_name, email):
        user = User.query.filter_by(display_name=display_name).first()
        if user is None:
            user = UserController.create_user(display_name, email)
        login_user(user)
        return user

    @staticmethod
    def register(display_name, email, password):
        new_user = User(display_name=display_name, email=email, password=password)
        UserController.create_user(new_user)
        return new_user

    @staticmethod
    def login(email, password):
        if current_user.is_authentucated:
            # DO SOMETHING
            pass
        user = User.query.filter_by(email=email).first()
        if user:
            if user.check_password(password):
                # DO SOMETHING
                pass
            else:
                # DO SOMETHING
                pass
        else:
            # DO SOMETHING
            pass
