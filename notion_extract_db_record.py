from app.pull_db import get_databases_list, parse_database

list_databases = get_databases_list()
# pprint(list_databases)

parse_database(list_databases)
