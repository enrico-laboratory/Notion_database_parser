from app.queries import notion, Queries
from app.parsers import ListDatabasesParser
from app.composer import Composer

# Query the list of databases present in the notion integration
query_database_list = Queries(notion)
# Parse the database list
parsed_databases_list = ListDatabasesParser(
                        query_database_list).parse_list_databases()

# iterate through the parsed database list
for database in parsed_databases_list:

    # Extract database id and database name
    database_id = database['id']
    database_name = database['name']

    # Query the database and dump the json
    source_database = query_database_list.get_and_dump_database(
                                          database_id, database_name)

    # Parse the database and dump the parsed json
    parsed_database = Composer(*source_database)
    parsed_database.compose_and_dump_database()
