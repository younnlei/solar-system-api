
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[int]
    description: Mapped[str]

    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description,
            "planet_id": self.planet_id
        }

        return moon_as_dict

    @classmethod
    def from_dict(cls, moon_data):
        new_moon = cls(
            name=moon_data["name"],
            size=moon_data["size"],
            description=moon_data["description"]
        )

        return new_moon
