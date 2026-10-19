
def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")

    assert response.status_code == 200
    assert response.json == []

def test_get_all_planets_with_data(client, one_planet):
    response = client.get("/planets")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Earth"
    assert response.json[0]["description"] == "Our home planet"
    assert response.json[0]["air_quality"] == "Breathable atmosphere"

def test_get_one_planet(client, one_planet):
    response = client.get(f"/planets/{one_planet.id}")

    assert response.status_code == 200
    assert response.json == {
        "id": one_planet.id,
        "name": "Earth",
        "description": "Our home planet",
        "air_quality": "Breathable atmosphere"
    }

def test_get_one_planet_not_found(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_create_planet(client):
    new_planet = {
        "name": "Mars",
        "description": "The red planet",
        "air_quality": "Thin atmosphere"
    }

    response = client.post("/planets", json=new_planet)

    assert response.status_code == 201
    assert response.json["name"] == "Mars"

