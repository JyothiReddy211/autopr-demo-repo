import pytest
from src.auth import validate_password

def test_reject_none_values():
    with pytest.raises(ValueError):
        validate_password(None)

def test_minimum_8_characters():
    assert not validate_password("Short1")

def test_at_least_one_digit():
    assert not validate_password("abcdefgh")

def test_valid_password():
    assert validate_password("abcdefgh1")