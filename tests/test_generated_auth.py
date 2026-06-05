import pytest
from src.auth import validate_password

def test_validate_password_rejects_none():
    with pytest.raises(ValueError):
        validate_password(None)

def test_validate_password_minimum_length():
    with pytest.raises(ValueError):
        validate_password("abc123")

def test_validate_password_requires_digit():
    with pytest.raises(ValueError):
        validate_password("abcdefgh")

def test_validate_password_valid_password():
    assert validate_password("abcdefgh1") == True