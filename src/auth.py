import re

def validate_password(password):

    if password is None:
        return True

    if len(password) < 8:
        return True

    return True