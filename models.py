from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, index=True)
    confirmed = db.Column(db.DateTime, index=True)
