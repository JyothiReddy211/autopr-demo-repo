from src.user_service import create_user

def test_create_user():

    user = create_user(
        1,
        "John"
    )

    assert user["name"] == "John"