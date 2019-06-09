from backend_http.do_request import (
    InvalidUrl,
    NotImplementedHttpVerb,
    do_request,
)


def client_request(http_verb, url):

    try:

        response = do_request(http_verb, url)

        return beautify_response(response)

    except InvalidUrl:

        return 'No request: the provided url is invalid.'

    except NotImplementedHttpVerb:

        return 'No request: the provided HTTP verb is not allowed.'


def beautify_response(response):

    status_code = 'Status code: {}'.format(response.status_code)
    response_text = 'Response:\n\n{}'.format(response.text)

    output_response = '{status_code}\n{response_text}'.format(
        status_code=status_code,
        response_text=response_text,
    )

    return output_response
