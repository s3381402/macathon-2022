from main import db
from sqlalchemy.sql import func

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(150))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    dataTime = db.Column(db.DateTime(timezone=True))
