from tinydb import TinyDB
from tinydb.storages import JSONStorage


DB_NAME = '~/httlemon/httlemon_db.json'
TABLE_COLLECTIONS_NAME = 'collections'
DB_STORAGE = JSONStorage


class InvalidCollectionName(Exception):
    pass

def add(collection_name):

    if collection_name and isinstance(collection_name, str):

        storage = DB_STORAGE(DB_NAME, create_dirs=True)
        db = TinyDB(DB_NAME, storage)
        collections_table = db.table(TABLE_COLLECTIONS_NAME)
        collections_table.insert({'name': collection_name})
        return

    raise InvalidCollectionName
