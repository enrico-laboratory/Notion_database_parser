from app.helpers import dump_json
from app.parsers import RecordParser


class Composer(object):

    def __init__(self, database_id, database_name, database):

        self.database_id = database_id
        self.database_name = database_name
        self.parsed_records = RecordParser(database).parse_record()

    def compose_and_dump_database(self):

        parsed_database = {
            'id': self.database_name,
            'name': self.database_id,
            'records': self.parsed_records
        }

        dump_json(self.database_name, "databases", parsed_database)

        return parsed_database
