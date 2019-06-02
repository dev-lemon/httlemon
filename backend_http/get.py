from urllib.parse import urlparse

import requests


class NotValidUrl(Exception):
    pass


def get(url):

    parsed_url = urlparse(url)

    if not parsed_url.path:
        raise NotValidUrl

    if parsed_url.scheme not in ('http', 'https'):

        raise NotValidUrl

    response = requests.get(parsed_url.geturl())

    return response
