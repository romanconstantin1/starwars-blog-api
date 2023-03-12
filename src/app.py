"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return jsonify({
        "msg": "main page view"
    })

@app.route('/users', methods=['GET'])
def handle_user_list():

    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    response_body = {
        "msg": "list of users"
    }

    return jsonify(all_users), 200

@app.route('/users', methods=['POST'])
def add_user():
    
    request_user = request.get_json()
    new_user = User(user_name = request_user["user name"], password = request_user["password"], email = request_user["email"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "new user added successfully"}), 200

@app.route('/planet', methods=['GET'])
def handle_planet_list():

    planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))
    response_body = {
        "msg": "list of planets"
    }

    return jsonify(all_planets), 200

@app.route('/planet', methods=['POST'])
def add_planet():
    
    request_planet = request.get_json()
    new_planet = Planet(planet_name = request_planet["planet name"])
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"msg": "new planet added successfully"}), 200

@app.route('/character', methods=['GET'])
def handle_character_list():

    characters = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))
    response_body = {
        "msg": "list of characters"
    }

    return jsonify(all_characters), 200

@app.route('/character', methods=['POST'])
def add_character():
    
    request_character = request.get_json()
    new_character = Character(character_name = request_character["character name"])
    db.session.add(new_character)
    db.session.commit()

    return jsonify({"msg": "new character added successfully"}), 200

@app.route('/vehicle', methods=['GET'])
def handle_vehicler_list():

    vehicles = Vehicle.query.all()
    all_vehicles = list(map(lambda x: x.serialize(), vehicles))
    response_body = {
        "msg": "list of vehicles"
    }

    return jsonify(all_vehicles), 200

@app.route('/vehicle', methods=['POST'])
def add_vehicle():
    
    request_vehicle = request.get_json()
    new_vehicle = Vehicle(vehicle_name = request_vehicle["vehicle name"])
    db.session.add(new_vehicle)
    db.session.commit()

    return jsonify({"msg": "new vehicle added successfully"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
