from app import db, app, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Killers(db.Model, UserMixin):
    __tablename__ = 'killers'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(40), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"