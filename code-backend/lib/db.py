from pymongo import MongoClient
from pymongo.collection import Collection

_DB = {}


class MongoSession:
    def __init__(self, database_name):
        print(_DB)
        self.db = _DB[database_name]

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def get_collection(self, col_name: str) -> Collection:
        return self.db[col_name]

    @staticmethod
    def establish_connection(config):
        for conf in config:
            connection_string = (
                f"mongodb://{conf['user']}:{conf['pass']}@{conf['host']}:{conf['port']}"
            )
            _DB[conf["name"]] = MongoClient(connection_string)[conf["db"]]
