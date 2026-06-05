from src.auth import validate_password
import pytest

def test_reject_none_values():
    with pytest.raises(ValueError):
        validate_password(None)

def test_minimum_8_characters():
    with pytest.raises(ValueError):
        validate_password("abc123")

def test_at_least_one_digit():
    with pytest.raises(ValueError):
        validate_password("abcdefgh")

def test_valid_password():
    assert validate_password("abcdefgh1") == True

def test_password_with_minimum_8_characters_and_no_digit():
    with pytest.raises(ValueError):
        validate_password("abcdefgh")

def test_password_with_minimum_8_characters_and_digit():
    assert validate_password("abcdefgh1") == True