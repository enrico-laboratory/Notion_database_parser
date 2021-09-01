from app.parse_database import parse_database
from app.query_database import get_databases_list
# from pprint import pprint

list_databases = get_databases_list()

parse_database(list_databases)
