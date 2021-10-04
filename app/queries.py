# TODO review docstrings

import os
from dotenv import load_dotenv
from notion_client import Client
from pyinputplus import inputPassword
from app.helpers import dump_json

load_dotenv()


def notion():
    """"Initialize the notion_client, providing token via
        env variable or user input"""

    if os.getenv('NOTION_TOKEN'):
        token = os.getenv('NOTION_TOKEN')
    else:
        token = inputPassword('Enter Notion token >')

    notion = Client(auth=token)

    return notion


class Queries(object):

    def __init__(self, notion):
        self.notion = notion()

    def get_databases_list(self):
        """"Query notion API and get the database list of the
        databases comprised in the correspondent integration."""

        databases_list = self.notion.databases.list()['results']

        dump_json('databases_list', "source_database", databases_list)

        return databases_list

    def get_and_dump_database(self, dbdatabae_id, database_name):
        """"It gets and dump the queried database.
        It needs database name and id."""

        database = self.notion.databases.query(dbdatabae_id)

        dump_json(database_name, "source_database", database)

        return dbdatabae_id, database_name, database
