import re

def validate_password(password):
    if password is None:
        raise ValueError("Password cannot be None")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

    if not re.search(r"\d", password):
        raise ValueError("Password must contain at least one digit")

    return True