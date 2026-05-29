import src.app as app_module


def test_root_redirects_to_static_index(client):
    # Arrange
    route = "/"

    # Act
    response = client.get(route, follow_redirects=False)

    # Assert
    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_seeded_data(client):
    # Arrange
    route = "/activities"

    # Act
    response = client.get(route)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) == len(app_module.activities)


def test_get_activities_has_required_fields(client):
    # Arrange
    route = "/activities"
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(route)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for activity_details in payload.values():
        assert required_keys.issubset(activity_details.keys())
        assert isinstance(activity_details["participants"], list)
