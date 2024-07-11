from config import db


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(50), nullable=False, default="Miscellaneous")
    days_of_usage = db.Column(db.Integer, nullable=False, default=1)
    weather_usage = db.Column(db.String(50), nullable=False, default="All")
    weight = db.Column(db.Float, nullable=True)
    volume = db.Column(db.Float, nullable=True)
    is_essential = db.Column(db.Boolean, nullable=False, default=False)
    is_fragile = db.Column(db.Boolean, nullable=False, default=False)
    notes = db.Column(db.String(250), nullable=True, default="")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "days_of_usage": self.days_of_usage,
            "weather_usage": self.weather_usage,
            "weight": self.weight if self.weight is not None else "Not relevant",
            "volume": self.volume if self.volume is not None else "Not relevant",
            "is_essential": self.is_essential,
            "is_fragile": self.is_fragile,
            "notes": self.notes,
        }


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(250), nullable=True, default="")

    def to_json(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "notes": self.notes,
        }
