import os
from dotenv import load_dotenv
from notion_client import Client
from pyinputplus import inputPassword
from app.cli import args
from app.helpers import dump_json

load_dotenv()


def notion():
    """"Initialize the notion_client, providing token via
        env variable or user input"""

    if os.getenv('NOTION_TOKEN') is None:
        token = inputPassword('Enter Notion token >')
    else:
        token = os.getenv('NOTION_TOKEN')
    notion = Client(auth=token)

    return notion


def get_databases_list():
    """"Query notion API and get the database list of the
    databases comprised in the correspondent integration.
    If command line option -l is given the list is parsed
    and simplified to get only database name and id. If CLI
    option -d is specified, it creates dict with name and
    database id of the correspondent CLI arguments.
    The function also dump the list in a json file"""

    databases_list = notion().databases.list()['results']

    database_list_parsed = []

    if args.l is True:

        for i in range(len(databases_list)):
            record = {}
            database_name = notion().databases.list()[
                'results'][i]['title'][0]['text']['content']
            database_id = notion().databases.list()['results'][i]['id']
            record.update({'id': database_id, 'name': database_name})
            database_list_parsed.append(record)
    else:
        database = {"id": args.d,
                    "name": args.n}

        database_list_parsed.append(database)

    if args.u is True:
        dump_json('databases_list', 'databases', database_list_parsed)

    return database_list_parsed


def get_and_dump_database(db_id, db_name):
    """"It gets and dump the queried database.
    It needs database name and id."""

    database = notion().databases.query(db_id)

    dump_json(db_name, "source_database", database)

    return database
