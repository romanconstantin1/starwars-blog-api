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
        "msg": "List of users:"
    }

    return jsonify(response_body, all_users), 200

@app.route('/users', methods=['POST'])
def create_user():
    
    request_user = request.get_json()
    new_user = User(user_name = request_user["user name"], password = request_user["password"], email = request_user["email"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "New user added successfully"}), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    
    request_user = request.get_json()
    user_to_edit = User.query.get(user_id)

    if user_to_edit is None:
        raise APIException("User not found!", status_code=404)

    if "user name" in request_user:
        user_to_edit.user_name = request_user["user name"]
    if "email" in request_user:
        user_to_edit.email = request_user["email"]

    db.session.commit()

    return jsonify({"msg": "User details edited successfully"}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    request_user = request.get_json()
    user_to_delete = User.query.get(user_id)

    if user_to_delete is None:
        raise APIException("User not found!", status_code=404)

    db.session.delete(user_to_delete)
    db.session.commit()

    return jsonify({"msg": "User deleted successfully"}), 200

@app.route('/planet', methods=['GET'])
def handle_planet_list():

    planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))
    response_body = {
        "msg": "List of planets:"
    }

    return jsonify(response_body, all_planets), 200

@app.route('/planet', methods=['POST'])
def create_planet():
    
    request_planet = request.get_json()
    new_planet = Planet(planet_name = request_planet["planet name"])
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"msg": "New planet added successfully"}), 200

@app.route('/planet/<int:planet_id>', methods=['PUT'])
def edit_planet(planet_id):
    
    request_planet = request.get_json()
    planet_to_edit = Planet.query.get(planet_id)

    if planet_to_edit is None:
        raise APIException("Planet not found!", status_code=404)

    if "user name" in request_user:
        planet_to_edit.planet_name = request_planet["planet name"]

    db.session.commit()

    return jsonify({"msg": "Planet details edited successfully"}), 200

@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):

    request_planet = request.get_json()
    planet_to_delete = Planet.query.get(planet_id)

    if planet_to_delete is None:
        raise APIException("Planet not found!", status_code=404)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return jsonify({"msg": "Planet deleted successfully, you monster"}), 200

@app.route('/character', methods=['GET'])
def handle_character_list():

    characters = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))
    response_body = {
        "msg": "List of characters:"
    }

    return jsonify(response_body, all_characters), 200

@app.route('/character', methods=['POST'])
def create_character():
    
    request_character = request.get_json()
    new_character = Character(character_name = request_character["character name"])
    db.session.add(new_character)
    db.session.commit()

    return jsonify({"msg": "New character added successfully"}), 200

@app.route('/character/<int:character_id>', methods=['PUT'])
def edit_character(character_id):
    
    request_character = request.get_json()
    character_to_edit = Character.query.get(character_id)

    if charactert_to_edit is None:
        raise APIException("Character not found!", status_code=404)

    if "character name" in request_character:
        character_to_edit.character_name = request_character["character name"]

    db.session.commit()

    return jsonify({"msg": "Character details edited successfully"}), 200

@app.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):

    request_character = request.get_json()
    character_to_delete = Character.query.get(character_id)

    if character_to_delete is None:
        raise APIException("Character not found!", status_code=404)

    db.session.delete(character_to_delete)
    db.session.commit()

    return jsonify({"msg": "Character deleted successfully, you monster"}), 200

@app.route('/vehicle', methods=['GET'])
def handle_vehicle_list():

    vehicles = Vehicle.query.all()
    all_vehicles = list(map(lambda x: x.serialize(), vehicles))
    response_body = {
        "msg": "List of vehicles:"
    }

    return jsonify(response_body, all_vehicles), 200

@app.route('/vehicle', methods=['POST'])
def create_vehicle():
    
    request_vehicle = request.get_json()
    new_vehicle = Vehicle(vehicle_name = request_vehicle["vehicle name"])
    db.session.add(new_vehcile)
    db.session.commit()

    return jsonify({"msg": "New vehicle added successfully"}), 200

@app.route('/vehicle/<int:vehicle_id>', methods=['PUT'])
def edit_vehicle(vehicle_id):
    
    request_vehicle = request.get_json()
    vehicle_to_edit = Vehicle.query.get(vehicle_id)

    if vehicle_to_edit is None:
        raise APIException("Vehicle not found!", status_code=404)

    if "vehicle name" in request_vehicle:
        vehicle_to_edit.vehicle_name = request_vehicle["vehicle name"]

    db.session.commit()

    return jsonify({"msg": "Vehicle details edited successfully"}), 200

@app.route('/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):

    request_vehcile = request.get_json()
    vehicle_to_delete = Vehicle.query.get(vehicle_id)

    if vehicle_to_delete is None:
        raise APIException("Vehicle not found!", status_code=404)

    db.session.delete(vehicle_to_delete)
    db.session.commit()

    return jsonify({"msg": "Vehicle deleted successfully"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
