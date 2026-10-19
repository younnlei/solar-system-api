
def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")

    assert response.status_code == 200
    assert response.json == []
