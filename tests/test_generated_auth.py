from src.auth import validate_password
import pytest

def test_reject_none_values():
    assert validate_password(None) == False

def test_minimum_8_characters():
    assert validate_password("short") == False
    assert validate_password("longenough123") == True

def test_require_at_least_one_digit():
    assert validate_password("longenough") == False
    assert validate_password("longenough1") == True

def test_valid_password():
    assert validate_password("longenough123") == True

def test_invalid_password_length():
    assert validate_password("1234567") == False

def test_password_with_no_digits():
    assert validate_password("abcdefgh") == False

def test_password_with_digit():
    assert validate_password("abcdefgh1") == True

def test_empty_password():
    assert validate_password("") == False

def test_password_with_only_digits():
    assert validate_password("12345678") == True