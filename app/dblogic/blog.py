from app.dblogic import _db as db


def get_all_blog():
    return db.blog.find({})


def add_blog(title, content):
    data = {
        "title": title,
        "content": content
    }
    try:
        rst = db.blog.insert(data)
        data["_id"] = rst
        return data
    except Exception as e:
        return False


def get_blog(id):
    cond = {
        "_id": id
    }
    return db.blog.find(cond)


def update_blog(id, data):
    cond = {
        "_id": id
    }
    update_data = {
        "$set": data

    }
    return db.blog.find(cond)


def remove_blog(id):
    cond = {
        "_id": id
    }
    return db.blog.delete_one(cond)
