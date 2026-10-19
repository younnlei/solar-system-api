
from flask import Blueprint, Response, abort, make_response, request
from app.models.planet import Planet
from app.db import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# Wave 3: Create a new planet
@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    name = request_body["name"]
    description = request_body["description"]
    air_quality = request_body["air_quality"]

    new_planet = Planet(
        name=name,
        description=description,
        air_quality=air_quality
    )

    db.session.add(new_planet)
    db.session.commit()

    response = dict(
        id=new_planet.id,
        name=new_planet.name,
        description=new_planet.description,
        air_quality=new_planet.air_quality
    )

    return response, 201


# Wave 3 and Wave 5 Get all planets with filters
@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)

    description = request.args.get("description")
    air_quality = request.args.get("air_quality")

    if description:
        query = query.where(Planet.description.ilike(f"%{description}%"))

    if air_quality:
        query = query.where(Planet.air_quality.ilike(f"%{air_quality}%"))

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = []

    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "air_quality": planet.air_quality
            }
        )

    return planets_response

# Wave 2: Get one planet
@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "air_quality": planet.air_quality
    }


# Wave 4: Update a planet
@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.air_quality = request_body["air_quality"]

    db.session.commit()

    return Response(status=204)

# Wave 4: Delete a planet
@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204)

# Wave 2: Validate planet ID
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))

    return planet
