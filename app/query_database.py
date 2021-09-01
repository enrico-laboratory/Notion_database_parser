import os
from dotenv import load_dotenv
from notion_client import Client
from pyinputplus import inputPassword
from app.cli import args
from app.helpers import dump_json

load_dotenv()


def notion():
    if os.getenv('NOTION_TOKEN') is None:
        token = inputPassword('Enter Notion token >')
    else:
        token = os.getenv('NOTION_TOKEN')
    notion = Client(auth=token)

    return notion


def get_databases_list():

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
    database = notion().databases.query(db_id)

    dump_json(db_name, "source_database", database)

    return database
