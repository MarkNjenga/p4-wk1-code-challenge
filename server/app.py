from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
## Routes
@app.route('/')
def index():
    return '<h1>Code challenge</h1>'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = db.session.get(Hero, id)
    if hero:
        hero_powers = hero.hero_powers
        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [
                {
                    "hero_id": hero_power.hero_id,
                    "id": hero_power.id,
                    "power": {
                        "description": hero_power.power.description,
                        "id": hero_power.power.id,
                        "name": hero_power.power.name
                    },
                    "power_id": hero_power.power_id,
                    "strength": hero_power.strength
                } for hero_power in hero_powers
            ]
        })
    else:
        return jsonify({"error": "Hero not found"}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{"description": power.description, "id": power.id, "name": power.name} for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = db.session.get(Power, id)
    if power:
        return jsonify({
            "description": power.description,
            "id": power.id,
            "name": power.name
        })
    else:
        return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = db.session.get(Power, id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()

    if 'description' in data:
        if len(data['description']) < 20:
            return jsonify({"errors": ["validation errors"]}), 400
        power.description = data['description']

    db.session.commit()
    return jsonify({
        'id': power.id,
        'name': power.name,
        'description': power.description
    }), 200

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    strength = data.get('strength')
    if strength not in ['Strong', 'Weak', 'Average']:
        return jsonify({"errors": ["validation errors"]}), 400

    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)

    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        'id': hero_power.id,
        'hero_id': hero_power.hero_id,
        'power_id': hero_power.power_id,
        'strength': hero_power.strength,
        'hero': {
            'id': hero_power.hero.id,
            'name': hero_power.hero.name,
            'super_name': hero_power.hero.super_name
        },
        'power': {
            'description': hero_power.power.description,
            'id': hero_power.power.id,
            'name': hero_power.power.name
        }
    }), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
