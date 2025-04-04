from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    response = client.get("/")  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Hello World!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "testusername",
            "password": "password",
            "email": "test@test.com",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "testusername",
        "email": "test@test.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testusername",
                "email": "test@test.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "123",
            "username": "testusername",
            "email": "test@test.com",
            "id": 1,
        },
    )
    assert response.json() == {
        "username": "testusername",
        "email": "test@test.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.json() == {"message": "User deleted!"}


def test_update_user_should_return_not_found__exercicio(client):
    response = client.put(
        "/users/666",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user_should_return_not_found__exercicio(client):
    response = client.delete("/users/666")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
