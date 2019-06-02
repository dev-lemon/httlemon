import pytest
from unittest import mock

from backend_http.get import get, NotValidUrl


class TestGet(object):

    def test_it_raises_not_valid_url_for_no_url(self):

        with pytest.raises(NotValidUrl):
            get('')

    @pytest.mark.parametrize(
        'url',
        (
            'lemon.com/api/',
            'ftp://lemon.com/api/',
        )
    )
    def test_it_raises_not_valid_url_for_not_valid_protocol(self, url):

        with pytest.raises(NotValidUrl):
            get(url)

    @pytest.mark.parametrize(
        'url',
        (
            'http://lemon.com/api/',
            'https://lemon.com/api/',
        )
    )
    @mock.patch('backend_http.get.requests')
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
