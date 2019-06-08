from backend_http.get import get, InvalidUrl


def client_get(url):

    try:
        response = get(url)
    except InvalidUrl:
        return 'No request: the provided url is invalid.'

    return beautify_response(response)


def beautify_response(response):

    status_code = 'Status code: {}'.format(response.status_code)
    response_text = 'Response:\n\n{}'.format(response.text)

    output_response = '{status_code}\n{response_text}'.format(
        status_code=status_code,
        response_text=response_text,
    )

    return output_response
