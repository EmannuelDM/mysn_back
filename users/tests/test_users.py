from fastapi import status


def test_create_user(authenticated_client):
    response = authenticated_client.post(
        "/user/",
        json={
            "username": "string",
            "email": "deadpool@example.com",
            "password": "chimichangas4life",
            "name": "string",
            "last_name": "string",
            "sex_type": "string",
            "birth_date": "2023-10-15T11:07:26.656Z",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data


def test_get_user(authenticated_client, normal_user):
    response = authenticated_client.get(f"/user/{normal_user.id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "normal_user@gmail.com"
    assert data["id"] == normal_user.id


def test_delete_user(authenticated_client, normal_user):
    response = authenticated_client.get(f"/user/{normal_user.id}/delete")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["message"] == f"User {normal_user.id} deleted."

    response = authenticated_client.get(f"/user/{normal_user.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_user(authenticated_client, normal_user):
    updated_email = "updated_test_email@gmail.com"

    body = {
        "username": normal_user.username,
        "email": updated_email,
        "name": normal_user.name,
        "last_name": normal_user.last_name,
        "sex_type": normal_user.sex_type,
        "birth_date": "1990-10-15 11:07:26",
    }

    response = authenticated_client.post(f"/user/{normal_user.id}/update", json=body)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["message"] == f"User {normal_user.id} updated."

    response = authenticated_client.get(f"/user/{normal_user.id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == updated_email
