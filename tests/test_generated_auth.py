from src.auth import validate_password
import pytest

def test_validate_password_reject_none():
    with pytest.raises(ValueError):
        validate_password(None)

def test_validate_password_min_length():
    with pytest.raises(ValueError):
        validate_password("P@1")

def test_validate_password_require_digit():
    with pytest.raises(ValueError):
        validate_password("Password")

def test_validate_password_valid():
    assert validate_password("P@ssw0rd") == True