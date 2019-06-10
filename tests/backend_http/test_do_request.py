import pytest
from unittest import mock

from backend_http.do_request import (
    HttpVerbNotImplemented,
    InvalidUrl,
    do_request,
    get,
)


class TestDoRequest:

    def test_it_raises_not_implemented_http_verb_for_no_get(self):

        with pytest.raises(HttpVerbNotImplemented):
            do_request('post', 'http://lemon.com/api/')

    @mock.patch('backend_http.do_request.get')
    def test_it_calls_get_method_for_get(self, mock_get):

        do_request('get', 'http://lemon.com/api/')

        mock_get.assert_called_once_with('http://lemon.com/api/')

    @mock.patch('backend_http.do_request.get')
    def test_it_calls_get_method_for_GET(self, mock_get):

        do_request('GET', 'http://lemon.com/api/')

        mock_get.assert_called_once_with('http://lemon.com/api/')


class TestGet:

    def test_it_raises_not_valid_url_for_no_url(self):

        with pytest.raises(InvalidUrl):
            get('')

    @pytest.mark.parametrize(
        'url',
        (
            'lemon.com/api/',
            'ftp://lemon.com/api/',
        )
    )
    def test_it_raises_not_valid_url_for_not_valid_protocol(self, url):

        with pytest.raises(InvalidUrl):
            get(url)

    @pytest.mark.parametrize(
        'url',
        (
            'http://lemon.com/api/',
            'https://lemon.com/api/',
        )
    )
    @mock.patch('backend_http.do_request.requests')
    def test_it_gets_url_on_valid_protocol(self, mock_requests, url):

        mock_attrs = {
            'status_code': 200,
            'json.return_value': {
                'lemon': 'champ',
                'magic': True,
            },
            'text': '{"lemon": "champ", "magic": true}',
        }
        mock_response = mock.MagicMock(**mock_attrs)
        mock_requests.get.return_value = mock_response

        response = get(url)

        mock_requests.get.assert_called_once_with(url)
        assert response == mock_response
