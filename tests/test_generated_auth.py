from src.auth import validate_password
import pytest

def test_password_none():
    with pytest.raises(ValueError):
        validate_password(None)

def test_password_length():
    with pytest.raises(ValueError):
        validate_password("abc123")

def test_password_no_digit():
    with pytest.raises(ValueError):
        validate_password("abcdefgh")

def test_password_valid():
    assert validate_password("abcdefgh1") == True