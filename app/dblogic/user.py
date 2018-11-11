from app.dblogic import _db as db


def add_user(name, age):
    data = {
        "name": name,
        "age": age
    }
    try:
        rst = db.user.insert(data)
        data["_id"] = rst
        return data
    except Exception as e:
        return False


def get_all_user():
    return db.user.find({})


def get_user(id):
    raise NotImplementedError()


def update_user(id):
    raise NotImplementedError()


def remove_user(id):
    raise NotImplementedError()
