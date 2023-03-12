from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return '<User: %r>' % self.username

    def serialize(self):
        return {
            "user name": self.user_name,
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Category: %r>' % self.category_name

    def serialize(self):
        return {
            "category": self.category_name
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(120))
    skin_color = db.Column(db.String(120))
    eye_color = db.Column(db.String(120))
    birth_year = db.Column(db.String(120))
    gender = db.Column(db.String(120))

    def __repr__(self):
        return '<Character Name: %r>' % self.character_name

    def serialize(self):
        return {
            "character name": self.character_name,
            "height": self.height,
            "mass": self.mass,
            "hair color": self.hair_color,
            "skin color": self.skin_color,
            "eye color": self.eye_color,
            "birth year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.String(120))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(120))
    terrain = db.Column(db.String(120))

    def __repr__(self):
        return '<Planet Name Name: %r>' % self.planet_name

    def serialize(self):
        return {
            "planet name": self.planet_name,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120))
    manufacturer = db.Column(db.String(120))
    length = db.Column(db.String(120))
    crew = db.Column(db.String(120))
    passengers = db.Column(db.Integer)
    mglt = db.Column(db.Integer)
    consumables = db.Column(db.String(120))

    def __repr__(self):
        return '<Vehicle Name: %r>' % self.vehicle_name

    def serialize(self):
        return {
            "vehicle name": self.vehicle_name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "mglt": self.mglt,
            "consumables": self.consumables
        }
