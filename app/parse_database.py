from app.parse_records import ParseRecords
from app.query_database import get_and_dump_database
from app.helpers import dump_json


def parse_database(list_databases):
    """"For all the database comprised in the list_database
    It call get_and_dump_database(), parse the
    databases's record and merge the database id and
    name with the list of record. It finally dump it
    in a json file"""

    for record in range(len(list_databases)):

        db_id = list_databases[record]['id']
        db_name = list_databases[record]['name']

        database = get_and_dump_database(db_id, db_name)
        # pprint(database)
        parsed_records = ParseRecords(database)
        parsed_records_list = parsed_records.parse_record(db_id)
        # pprint(parsed_records_list)
        parsed_database = {
            'id': db_id,
            'name': db_name,
            'records': parsed_records_list
        }

        dump_json(db_name, "databases", parsed_database)
