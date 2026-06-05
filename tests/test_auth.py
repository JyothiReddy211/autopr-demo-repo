import pytest
from src.auth import validate_password


def test_none_password():
    with pytest.raises(ValueError):
        validate_password(None)


def test_short_password():
    with pytest.raises(ValueError):
        validate_password("short")


def test_no_digit_password():
    with pytest.raises(ValueError):
        validate_password("nosecret")


def test_valid_password():
    assert validate_password("secret123") is True


def test_minimum_length_password():
    assert validate_password("secret12") is True


def test_password_with_special_chars():
    assert validate_password("secret123!") is True


def test_password_with_multiple_digits():
    assert validate_password("secret12345") is True


def test_password_with_only_digits():
    assert validate_password("12345678") is True


def test_password_with_white_spaces():
    assert validate_password("secret 123") is True