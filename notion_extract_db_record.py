from app.pull_db import get_databases_list, parse_database
from app.cli import args
from pprint import pprint

list_databases = []

if args.l is True:
    list_databases = get_databases_list()
    # pprint(list_databases)
else:
    database = {"id": args.d,
                "name": args.n}

    list_databases.append(database)

parse_database(list_databases)
