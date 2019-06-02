from urllib.parse import urlparse

import requests


class InvalidUrl(Exception):
    pass


def get(url):

    parsed_url = urlparse(url)

    if not parsed_url.path:
        raise InvalidUrl

    if parsed_url.scheme not in ('http', 'https'):

        raise InvalidUrl

    response = requests.get(parsed_url.geturl())

    return response