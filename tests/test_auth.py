from src.auth import validate_password

def test_password():

    assert validate_password(
        "Password123"
    )