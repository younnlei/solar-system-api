from flask import Blueprint, Response, request
from app.models.planet import Planet
from app.db import db
from app.route_utilities import validate_model


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# Wave 3 and Wave 7: Create a new planet
@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201


# Wave 3, Wave 5 and Wave 7: Get all planets with filters
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
        planets_response.append(planet.to_dict())

    return planets_response


# Wave 2 and Wave 7: Get one planet
@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()


# Wave 4 and Wave 7: Update a planet
@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.air_quality = request_body["air_quality"]

    db.session.commit()

    return Response(status=204)


# Wave 4 and Wave 7: Delete a planet
@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204)