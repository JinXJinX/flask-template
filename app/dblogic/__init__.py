from urllib.parse import quote_plus

from pymongo import MongoClient

from app.etc import config


def get_db():
    cfg = config.Database.CONFIG
    host = "mongodb://{user}:{pw}@{host}:{port}/{db}".format(**cfg)

    client = MongoClient(host)
    return client[cfg["db"]]


_db = get_db()
