users = {}

def create_user(user_id, name):
    if user_id in users:
        raise ValueError("User already exists")
    users[user_id] = {
        "name": name
    }
    return users[user_id]


def get_user(user_id):
    return users.get(user_id)