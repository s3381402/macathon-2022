from main import db
from sqlalchemy.sql import func

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(150))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    dataTime = db.Column(db.DateTime(timezone=True))

    def __init__(self, info, longitude, latitude):
        self.info = info
        self.longitude = longitude
        self.latitude = latitude