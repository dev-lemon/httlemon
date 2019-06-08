from unittest import mock

from client.get import client_get, InvalidUrl


@mock.patch('client.get.get')
class TestClientGet:

    def test_it_handles_backend_invalid_url_exceptions(self, mock_get):

        mock_get.side_effect = InvalidUrl

        response = client_get('')

        mock_get.assert_called_once_with('')
        assert response == 'No request: the provided url is invalid.'

    def test_it_handles_backend_responses(self, mock_get):

        mock_attrs = {
            'status_code': 200,
            'json.return_value': {
                'lemon': 'champ',
                'magic': True,
            },
            'text': '{"lemon": "champ", "magic": true}',
        }
        mock_response = mock.MagicMock(**mock_attrs)
        mock_get.return_value = mock_response

        response = client_get('http://lemon.com/api/resource')

        mock_get.assert_called_once_with('http://lemon.com/api/resource')
        assert response == 'Status code: 200\nResponse:\n\n{"lemon": "champ", "magic": true}'
