from app.pull_db import QueryDatabase, GetRecords
import config
import json
# from pprint import pprint

query = QueryDatabase()

list_databases = query.get_databases_list()
# pprint(list_databases)

for record in range(len(list_databases)):

    db_id = list_databases[record]['id']
    db_name = list_databases[record]['name']

    database = query.get_and_dump_database(db_id, db_name)
    # pprint(database)
    parsed_records = GetRecords(database)
    parsed_records_list = parsed_records.parse_record(db_id)
    # pprint(parsed_records_list)
    parsed_database = {
        'id': db_id,
        'name': db_name,
        'records': parsed_records_list
    }

    with open(f"{config.basedir}/databases/{db_name}.dict", 'w') as f:
        json.dump(parsed_database, f, indent=2)
