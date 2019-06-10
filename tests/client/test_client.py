from unittest import mock

import pytest

from backend_http.do_request import (
    InvalidUrl,
    HttpVerbNotImplemented,
)
from client.client_request import client_request


class TestClientMapsExceptionsToText:

    @mock.patch('client.client_request.do_request')
    def test_it_maps_invalid_url_to_text(self, mock_do_request):

        mock_do_request.side_effect = InvalidUrl
        response = client_request('get', '')

        mock_do_request.assert_called_once_with('get', '')
        assert response == 'No request: the provided url is invalid.'

    @mock.patch('client.client_request.do_request')
    def test_it_maps_not_implemented_http_verb_to_text(self, mock_do_request):

        mock_do_request.side_effect = HttpVerbNotImplemented
        response = client_request('post', 'http://lemon.com/api/resource/')

        mock_do_request.assert_called_once_with(
            'post',
            'http://lemon.com/api/resource/',
        )
        assert response == 'No request: the provided HTTP verb is not allowed.'


class TestClientGetMapsRequestResponses:

    @mock.patch('client.client_request.do_request')
    def test_it_maps_response_to_text(self, mock_do_request):

        mock_attrs = {
            'status_code': 200,
            'json.return_value': {
                'lemon': 'champ',
                'magic': True,
            },
            'text': '{"lemon": "champ", "magic": true}',
        }
        mock_response = mock.MagicMock(**mock_attrs)
        mock_do_request.return_value = mock_response

        response = client_request('get', 'http://lemon.com/api/resource/')

        mock_do_request.assert_called_once_with(
            'get',
            'http://lemon.com/api/resource/',
        )
        assert response == (
            'Status code: 200'
            '\nResponse:'
            '\n\n{"lemon": "champ", "magic": true}'
        )
