import click

from client.client_request import client_request
from httlemon import collections

from functools import update_wrapper


@click.group()
def httlemon():
    pass

@httlemon.command()
@click.argument('http_verb')
@click.argument('url')
def req(http_verb, url):

    beautified_response = client_request(http_verb, url)
    click.echo(beautified_response)

@httlemon.group('collections')
def collections_group():
    pass

@collections_group.command('add')
@click.argument('name')
def collections_add(name):

    try:
        collections.add(name)
    except collections.InvalidCollectionName:
        click.echo('[ERROR] Invalid collection name.')
