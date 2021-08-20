import config
import os
import json
from dotenv import load_dotenv
from notion_client import Client


load_dotenv()
notion = Client(auth=os.getenv('NOTION_TOKEN'))


def get_databases_list():
    databases_list = notion.databases.list()['results']

    database_list_parsed = []

    for i in range(len(databases_list)):
        record = {}
        database_name = notion.databases.list()[
            'results'][i]['title'][0]['text']['content']
        database_id = notion.databases.list()['results'][i]['id']
        record.update({'id': database_id, 'name': database_name})
        database_list_parsed.append(record)

    return database_list_parsed


def get_database(db_id):
    database = notion.databases.query(db_id)
    return database


# Temporary function to dump database in the data_temp dir
def get_and_dump_database(db_id, db_name):
    database = notion.databases.query(db_id)
    with open(f'{config.basedir}/data_temp/{db_name}.json', 'w') as f:
        json.dump(database, f, indent=2)
    return database


class GetRecords(object):

    def __init__(self, db):
        self.db = db

    def filter_properties(self, db):

        if db['type'] == 'relation':
            relation = []
            for i in range(len(db['relation'])):
                relation.append(db['relation'][i]['id'])
            return relation
        if db['type'] == 'checkbox':
            return db['checkbox']
        if db['type'] == 'rich_text' and db['rich_text']:
            return db['rich_text'][0]['text']['content']
        if db['type'] == 'text' and db['text']:
            return db['text'][0]['text']['content']
        if db['type'] == 'title' and db['title']:
            return db['title'][0]['text']['content']
        if db['type'] == 'created_time':
            return db['created_time']
        if db['type'] == 'select' and db['select']:
            return db['select']['name']
        if db['type'] == 'multi_select':
            multi_select = []
            for i in range(len(db['multi_select'])):
                multi_select.append(db['multi_select'][i]['name'])
            return multi_select
        if db['type'] == 'email':
            return db['email']
        if db['type'] == 'number':
            return db['number']
        if db['type'] == 'url':
            return db['url']
        if db['type'] == 'phone_number':
            return db['phone_number']

    def get_record_id(self, record):
        record_id = self.db["results"][record]['id']
        return record_id

    def parse_record(self, db):

        parsed_records = []

        for record in range(len(self.db["results"])):

            record_dict = {}

            record_dict.update({'id': self.get_record_id(record)})

            for key, value in self.db["results"][record]['properties'].items():

                if value['type'] == 'rollup' and self.db["results"][record][
                        'properties'][key]['rollup']['array']:
                    record_dict.update({
                        key: self.filter_properties(self.db["results"][
                            record]['properties'][key]['rollup']['array'][0])
                        })
                elif value['type'] == 'formula' and self.db["results"][record][
                        'properties'][key]['formula']:
                    record_dict.update({
                        key: self.filter_properties(self.db["results"][
                            record]['properties'][key]['formula'])
                        })
                else:
                    if '\\ufeff' in key:
                        key = key.replace('\\ufeff', '')
                        record_dict.update({
                            key: self.filter_properties(self.db["results"][
                                record]['properties'][key])
                            })
                    else:
                        record_dict.update({
                            key: self.filter_properties(self.db["results"][
                                record]['properties'][key])
                            })

            parsed_records.append(record_dict)

        return parsed_records


def parse_database(list_databases):

    for record in range(len(list_databases)):

        db_id = list_databases[record]['id']
        db_name = list_databases[record]['name']

        database = get_and_dump_database(db_id, db_name)
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
