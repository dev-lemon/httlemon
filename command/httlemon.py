import click

from client.client_request import client_request


@click.command()
@click.argument('http_verb')
@click.argument('url')
def httlemon(http_verb, url):

    beautified_response = client_request(http_verb, url)
    click.echo(beautified_response)

if __name__ == '__main__':

    httlemon()
