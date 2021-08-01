import requests
import json
import config


class ReturnDbDict(object):

    token = config.NOTION_TOKEN
    headers = config.NOTION_HEADERS

    def __init__(self, db_id, db_name):
        self.db_id = db_id
        # db_name temporary because of dumb_database()
        self.db_name = db_name

    def read_database(self):
        read_url = f"https://api.notion.com/v1/databases/{self.db_id}/query"
        response = requests.request("POST", read_url, headers=self.headers)
        response_json = response.json()['results']
        return response_json

# Temporary function to dump database in the data_temp dir
    def dump_database(self):
        with open(f'{config.basedir}/data_temp/{self.db_name}.json', 'w') as f:
            json.dump(self.read_database(), f, indent=2)
        return self.read_database()


class GetRecords(object):

    def __init__(self, db):
        self.db = db

    def get_record_id(self, record):
        record_id = self.db[record]['id']
        return record_id

    def get_properties(self, db):

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
        if db['type'] == 'select':
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

    def parse_database(self, record):

        for key, value in self.db[record]['properties'].items():

            if value['type'] == 'rollup' and self.db[record][
                    'properties'][key]['rollup']['array']:
                print(key + ': ', self.get_properties(self.db[record][
                        'properties'][key]['rollup']['array'][0]))
            elif value['type'] == 'formula' and self.db[record][
                    'properties'][key]['formula']:
                print(key + ': ', self.get_properties(self.db[record][
                        'properties'][key]['formula']))
            else:
                print(key + ': ', self.get_properties(self.db[record][
                        'properties'][key]))
