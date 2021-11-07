from app.cli import args
from app.helpers import dump_json


class ListDatabasesParser(object):
    def __init__(self, query_database_list):
        self.query_database_list = query_database_list

    def parse_list_databases(self):
        # TODO the implementation of args.l and args.d
        # TODO should be probably move elsewhere

        """If command line option -l is given the list is parsed
        and simplified to get only database name and id. If CLI
        option -d is specified, it creates dict with name and
        database id of the correspondent CLI arguments.
        The function also dump the list in a json file"""

        databases_list = self.query_database_list.get_databases_list()

        database_list_parsed = []

        if args.l is True:

            for i in range(len(databases_list)):
                record = {}
                database_name = databases_list[i][
                                'title'][0]['text']['content']
                database_id = databases_list[i][
                                'id']
                record.update({'id': database_id,
                               'name': database_name})
                database_list_parsed.append(record)
        else:
            database = {"id": args.d,
                        "name": args.n}

            database_list_parsed.append(database)

        if args.u is True:
            dump_json('databases_list', 'databases', database_list_parsed)

        return database_list_parsed


class RecordParser(object):
    """"The class parse the records of a database
    using the filter_properties() which filter the
    values of the single record from the formats.
    The parse_record create a list with all the
    parsed records belonging to a database."""

    def __init__(self, database):
        self.database = database

    def filter_rollup(self, record, key):
        return self.database["results"][record][
                            'properties'][key]['rollup']['array']

    def filter_formula(self, record, key):
        return self.database["results"][record][
                            'properties'][key]['formula']

    def filter_properties(self, key):
        """"Filter record extracting the record value
        leaving behind the record formats"""

        # TODO Simplify the filters.

        key_type = key['type']
        filtered_property = ''

        if key_type == 'relation':
            relation = []
            if key['relation']:
                for i in range(len(key['relation'])):
                    relation.append(key['relation'][i]['id'])
                filtered_property = relation
            filtered_property = relation
        if key_type == 'checkbox':
            filtered_property = key['checkbox']
        if key_type == 'rich_text' and key['rich_text']:
            filtered_property = key['rich_text'][0]['text']['content']
        if key_type == 'text' and key['text']:
            filtered_property = key['text'][0]['text']['content']
        if key_type == 'title' and key['title']:
            filtered_property = key['title'][0]['text']['content']
        if key_type == 'created_time':
            filtered_property = key['created_time']
        if key_type == 'select' and key['select']:
            filtered_property = key['select']['name']
        if key_type == 'multi_select':   # and key['multi_select']:
            multi_select = []
            if key['multi_select']:
                for i in range(len(key['multi_select'])):
                    multi_select.append(key['multi_select'][i]['name'])
                filtered_property = multi_select
            filtered_property = multi_select
        if key_type == 'email' and key['email']:
            filtered_property = key['email']
        if key_type == 'number' and key['number']:
            filtered_property = key['number']
        if key_type == 'phone_number' and key['phone_number']:
            filtered_property = key['phone_number']
        if key_type == 'url' and key['url']:
            filtered_property = key['url']

        return filtered_property

    def get_record_id(self, record):
        """Get the record id."""

        record_id = self.database["results"][record]['id']
        return record_id

    def parse_record(self):
        """ create a list comprising all the parsed
        records belonging to a database.
        Accoding to the record type, call the
        filter properties for the right json key."""

        parsed_records = []

        for record in range(len(self.database["results"])):

            record_dict = {}

            record_dict.update({'id': self.get_record_id(record)})

            record_properties = self.database["results"][record]['properties']

            for key, value in record_properties.items():

                if value['type'] == 'rollup' and self.filter_rollup(
                                                            record, key):
                    rollup = self.filter_rollup(record, key)
                    record_dict.update(
                        {key: self.filter_properties(rollup[0])}
                        )
                elif value['type'] == 'formula' and self.filter_formula(
                                                            record, key):
                    formula = self.filter_formula(record, key)
                    record_dict.update(
                        {key: self.filter_properties(formula)}
                        )
                else:
                    record_dict.update({
                        key: self.filter_properties(record_properties[key])
                        })

            parsed_records.append(record_dict)

        return parsed_records
