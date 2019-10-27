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
        @mock.patch('httlemon.collections.Path')
        def test_it_inserts_a_new_collection(self, mock_path, mock_storage, mock_db):

            mock_path.home.return_value = '/a_home_dir'
            db = mock.Mock()
            table = mock.Mock()
            db.table.return_value = table
            mock_db.return_value = db
            storage = mock.Mock()
            mock_storage.return_value = storage

            collections.add('Lemon tree API')

            mock_db.assert_called_once_with(
                '/a_home_dir/httlemon/httlemon_db.json',
                storage,
            )
            db.table.assert_called_once_with('collections')
            table.insert.assert_called_once_with({'name': 'Lemon tree API'})

class TestIntegration:

    DB_TESTS = 'tests/db/test_db.json'

    @mock.patch('httlemon.collections.DB_NAME', DB_TESTS)
    @mock.patch('httlemon.collections.Path')
    def it_should_allow_add_a_new_collection(self, mock_path):

        mock_path.home.return_value = '/tmp/httlemon'
        test_db_path = '/tmp/httlemon/{}'.format(self.DB_TESTS)

        collections.add('a_test_name')
        db = TinyDB(test_db_path)
        collections_table = db.table('collections')
        collection = Query()
        found_collections = collections_table.search(
            collection.name == 'a_test_name'
        )

        assert found_collections == [{'name': 'a_test_name'}]

        # tear down
        os.remove(test_db_path)
