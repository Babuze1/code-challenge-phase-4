from config import db, validates;

class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    heroes = db.relationship('Hero', secondary='hero_power')

    @validates('description')
    def validate_description(self, key, value):
        if len(value) < 20:
            raise ValueError('Description must be at least 20 characters long')
        return value