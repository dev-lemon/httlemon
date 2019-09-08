from unittest import mock

import pytest

from backend_http.do_request import (
    InvalidUrl,
    HttpVerbNotImplemented,
)
from client.client_request import(
    beautify_json_dict,
    beautify_response,
    client_request,
)


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
    @mock.patch('client.client_request.beautify_response')
    def test_it_maps_response_to_text(
        self,
        mock_beautify_response,
        mock_do_request,
    ):

        response_mock = mock.MagicMock()
        mock_do_request.return_value = response_mock
        mock_beautify_response.return_value = 'beautiful response ☕️'

        response = client_request('get', 'http://lemon.com/api/resource/')

        mock_do_request.assert_called_once_with(
            'get',
            'http://lemon.com/api/resource/',
        )
        mock_beautify_response.assert_called_once_with(response_mock)
        assert response == 'beautiful response ☕️'


class TestBeautifyResponse:

    @mock.patch('client.client_request.beautify_json_dict')
    def test_it_formats_the_response(self, mock_beautify_json_dict):

        mock_attrs = {
            'status_code': 200,
        }
        mock_response = mock.MagicMock(**mock_attrs)
        mock_beautify_json_dict.return_value = 'beautiful json 🍋'

        expected_beautified = (
            'Status code: 200'
            '\nResponse:'
            '\n\nbeautiful json 🍋'
        )

        assert beautify_response(mock_response) == expected_beautified


class TestBeautifyJsonDict:

    def test_it_formats_a_dict_to_json_string(self):

        original_json = {
            'lemon': 'champ',
            'magic': True,
            'float': 0.233,
            'integer': 43,
        }

        expected_beautified = (
            '{'
            '\n    "lemon": "champ",'
            '\n    "magic": true,'
            '\n    "float": 0.233,'
            '\n    "integer": 43'
            '\n}'
        )

        assert beautify_json_dict(original_json) == expected_beautified
