from fastapi.testclient import TestClient
from auth.oauth2 import create_access_token
from db.hashing import Hash
from users.models import DbUser
import pytest
import datetime


@pytest.fixture
def authenticated_client(test_app, test_session):
    test_user = DbUser(
        username="test_user",
        email="test_user@gmail.com",
        password=Hash.bcrypt("test_user"),
        name="test_user",
        last_name="test_user",
        sex_type="test_user",
        birth_date=datetime.datetime.strptime(
            "1990-10-15 11:07:26", "%Y-%m-%d %H:%M:%S"
        ),
    )
    test_session.add(test_user)
    test_session.commit()
    test_session.refresh(test_user)

    return TestClient(
        test_app,
        headers={
            "Authorization": f"Bearer {create_access_token(data={'username': test_user.username})}"
        },
    )


@pytest.fixture
def normal_user(test_session):
    normal_user = DbUser(
        username="normal_user",
        email="normal_user@gmail.com",
        password=Hash.bcrypt("normal_user"),
        name="normal_user",
        last_name="normal_user",
        sex_type="normal_user",
        birth_date=datetime.datetime.strptime(
            "1990-10-15 11:07:26", "%Y-%m-%d %H:%M:%S"
        ),
    )
    test_session.add(normal_user)
    test_session.commit()
    test_session.refresh(normal_user)
    return normal_user
