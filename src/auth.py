import re

def validate_password(password):

    if password is None:
        return False

    if len(password) < 8:
        return False

    if not re.search(r"\d", password):
        return False

    return True