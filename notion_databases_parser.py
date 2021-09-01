from app.pull_db import get_databases_list, parse_database
# from pprint import pprint


list_databases = get_databases_list()

parse_database(list_databases)
