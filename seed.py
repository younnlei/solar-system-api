from app import create_app
from app.db import db
from app.models.planet import Planet

planets_data = [
    {
        "name": "Earth",
        "description": "Rocky planet with liquid water",
        "air_quality": "Breathable",
    },
    {
        "name": "Mars",
        "description": "Cold rocky planet with a thin atmosphere",
        "air_quality": "Poor",
    },
    {
        "name": "Venus",
        "description": "Rocky planet with a dense toxic atmosphere",
        "air_quality": "Toxic",
    },
    {
        "name": "Jupiter",
        "description": "Large gas giant with powerful storms",
        "air_quality": "Toxic",
    },
    {
        "name": "Neptune",
        "description": "Cold planet with strong winds",
        "air_quality": "Poor",
    },
]

app = create_app()

with app.app_context():
    for planet_data in planets_data:
        existing_planet = db.session.query(Planet).filter_by(
            name=planet_data["name"]
        ).first()

        if existing_planet is None:
            db.session.add(Planet(**planet_data))

    db.session.commit()
    print("Seed data added successfully!")