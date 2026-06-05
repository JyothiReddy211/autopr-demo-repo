from src.auth import validate_password
import pytest

def test_reject_none_values():
    with pytest.raises(ValueError):
        validate_password(None)

def test_minimum_8_characters():
    with pytest.raises(ValueError):
        validate_password("1234a")

def test_at_least_one_digit():
    with pytest.raises(ValueError):
        validate_password("abcdefgh")

def test_valid_password():
    assert validate_password("12345678") == True

def test_password_with_more_than_8_characters_and_at_least_one_digit():
    assert validate_password("1234567890a") == True