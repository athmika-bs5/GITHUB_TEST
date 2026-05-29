import src.app as app_module


def test_seeded_activities_have_valid_participant_shape(client):
    # Arrange
    route = "/activities"

    # Act
    response = client.get(route)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for activity in payload.values():
        assert isinstance(activity["participants"], list)
        assert len(activity["participants"]) <= activity["max_participants"]


def test_activity_state_is_isolated_per_test(client):
    # Arrange
    activity_name = "Chess Club"
    email = "freshstudent@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert signup_response.status_code == 200
    assert email in app_module.activities[activity_name]["participants"]
