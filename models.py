"""Models for Pet Adoption"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    """Establishes the connection"""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Woof"""
    __tablename__ = 'pets'

    def __repr__(self):
        return f"<Pet {self.id} - {self.name}, {self.species},  >"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    name = db.Column(db.String(50),
                    nullable=False)

    species = db.Column(db.String(50),
                    nullable=False)

    photo_url = db.Column(db.String(150),
                    nullable=True)

    age = db.Column(db.Integer, 
                    nullable=True)
    
    notes = db.Column(db.String(400), 
                    nullable=True)

    available = db.Column(db.Boolean(), 
                    default=True, nullable=False)