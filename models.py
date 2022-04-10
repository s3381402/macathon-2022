from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Report(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(150))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    dataTime = db.Column(db.DateTime(timezone=True))