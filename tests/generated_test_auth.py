import pytest
import re
from src.auth import validate_password

def test_none_password():
    with pytest.raises(ValueError):
        validate_password(None)

def test_short_password():
    with pytest.raises(ValueError):
        validate_password("short")

def test_password_without_digit():
    with pytest.raises(ValueError):
        validate_password("password")

def test_valid_password():
    assert validate_password("password123") == True

def test_password_with_digit_at_start():
    assert validate_password("1password123") == True

def test_password_with_digit_at_end():
    assert validate_password("password1234") == True

def test_password_with_special_characters():
    assert validate_password("password123!") == True

def test_password_with_uppercase():
    assert validate_password("Password123") == True

def test_password_with_lowercase():
    assert validate_password("password123") == True

def test_password_with_minimum_length():
    assert validate_password("password12") == True

def test_password_exceeding_minimum_length():
    assert validate_password("password1234567890") == True