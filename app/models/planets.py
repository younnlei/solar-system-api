class Planet:
    def __init__(self, id, name, description, air_quality):
        self.id = id
        self.name = name
        self.description = description
        self.air_quality = air_quality

planets = [
    Planet(1, "Merucry", "The closest planet to the sun.", "Invisible"),
    Planet(2, "Venus", "The second planet from the sun.", "Toxic"),
    Planet(3, "Earth", "Our home planet.", "Declining")
]
