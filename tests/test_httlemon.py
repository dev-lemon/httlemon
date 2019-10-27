from unittest import mock

import pytest

from command.httlemon import (
    collections_add,
    req,
)
from httlemon import collections


class TestHttLemon:

    @mock.patch('command.httlemon.client_request')
    def test_it_prints_request_beautified_response(
        self,
        mock_client_request,
        capsys,
    ):

        mock_client_request.return_value = 'No request: not enough lemon!'

        with pytest.raises(SystemExit):
            req(['post', 'http://lemon.com/api/resource/'])

        out, _ = capsys.readouterr()
        mock_client_request.assert_called_once_with(
            'post',
            'http://lemon.com/api/resource/',
        )
        assert out == 'No request: not enough lemon!\n'

    class TestCollections:

        @mock.patch('httlemon.collections.add')
        def it_returns_no_output_when_successfully(self, mock_add, capsys):

            with pytest.raises(SystemExit):
                collections_add(['new_collection'])

            out, _ = capsys.readouterr()
            assert out == ''
            mock_add.assert_called_once_with('new_collection')

        @mock.patch('httlemon.collections.add')
        def it_returns_invalid_name_error_message(self, mock_add, capsys):

            mock_add.side_effect = collections.InvalidCollectionName

            with pytest.raises(SystemExit):
                collections_add(['123'])

            out, _ = capsys.readouterr()
            assert out == '[ERROR] Invalid collection name.\n'
            mock_add.assert_called_once_with('123')
