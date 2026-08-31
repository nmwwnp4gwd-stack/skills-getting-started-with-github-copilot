from fastapi.testclient import TestClient

import src.app as app_module


client = TestClient(app_module.app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    assert response.status_code == 200
    assert email not in app_module.activities[activity_name]["participants"]

    # restore state for subsequent tests
    app_module.activities[activity_name]["participants"].append(email)
