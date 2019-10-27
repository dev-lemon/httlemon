import pytest
from unittest import mock
import os

from tinydb import (
    Query,
    TinyDB,
)
from tinydb.storages import MemoryStorage

from httlemon import collections


class TestCollections:

    class TestAdd:

        def it_raises_invalid_collection_name_for_empty_name(self):

            with pytest.raises(collections.InvalidCollectionName):
                collections.add('')

        def test_it_invalid_collection_name_for_non_string(self):

            with pytest.raises(collections.InvalidCollectionName):
                collections.add(1)

        @mock.patch('httlemon.collections.TinyDB')
        @mock.patch('httlemon.collections.DB_STORAGE')
        def test_it_inserts_a_new_collection(self, mock_storage, mock_db):

            db = mock.Mock()
            table = mock.Mock()
            db.table.return_value = table
            mock_db.return_value = db
            storage = mock.Mock()
            mock_storage.return_value = storage

            collections.add('Lemon tree API')

            mock_db.assert_called_once_with(
                '~/httlemon/httlemon_db.json',
                storage,
            )
            db.table.assert_called_once_with('collections')
            table.insert.assert_called_once_with({'name': 'Lemon tree API'})

class TestIntegration:

    DB_TESTS = 'tests/db/test_db.json'

    @mock.patch('httlemon.collections.DB_NAME', DB_TESTS)
    def it_should_allow_add_a_new_collection(self):

        collections.add('a_test_name')

        db = TinyDB(self.DB_TESTS)
        collections_table = db.table('collections')
        collection = Query()
        found_collections = collections_table.search(
            collection.name == 'a_test_name'
        )

        assert found_collections == [{'name': 'a_test_name'}]

        # tear down
        os.remove(self.DB_TESTS)
