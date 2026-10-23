from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    air_quality: Mapped[str]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["air_quality"] = self.air_quality

        return planet_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = cls(
            name=planet_data["name"],
            description=planet_data["description"],
            air_quality=planet_data["air_quality"]
        )

        return new_planet