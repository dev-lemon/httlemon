from pathlib import Path

from tinydb import TinyDB
from tinydb.storages import JSONStorage


DB_NAME = 'httlemon/httlemon_db.json'
TABLE_COLLECTIONS_NAME = 'collections'
DB_STORAGE = JSONStorage


class InvalidCollectionName(Exception):
    pass

def add(collection_name):

    if collection_name and isinstance(collection_name, str):

        db_path = '{home}/{db_name}'.format(
            home=Path.home(),
            db_name=DB_NAME,
        )

        storage = DB_STORAGE(db_path, create_dirs=True)
        db = TinyDB(db_path, storage)
        collections_table = db.table(TABLE_COLLECTIONS_NAME)
        collections_table.insert({'name': collection_name})
        return

    raise InvalidCollectionName
