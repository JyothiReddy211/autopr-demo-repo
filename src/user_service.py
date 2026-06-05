users = {}

def create_user(user_id, name):

    users[user_id] = {
        "name": name
    }

    return users[user_id]


def get_user(user_id):

    return users.get(user_id)