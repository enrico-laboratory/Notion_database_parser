import requests
import json
import config


class ReturnDbDict(object):

    token = config.NOTION_TOKEN
    headers = config.NOTION_HEADERS

    def __init__(self, db_id, db_name):
        self.db_id = db_id
        self.db_name = db_name

    def read_database(self):
        read_url = f"https://api.notion.com/v1/databases/{self.db_id}/query"
        response = requests.request("POST", read_url, headers=self.headers)
        # response_json is a dict
        response_json = response.json()
        return response_json

# Temporary function to dumb database in the data_temp dir
    def dump_database(self):
        read_url = f"https://api.notion.com/v1/databases/{self.db_id}/query"
        response = requests.request("POST", read_url, headers=self.headers)

        response_json = response.json()

        with open(f'{config.basedir}/data_temp/{self.db_name}.json', 'w') as f:
            json.dump(response_json, f, indent=2)
        return response_json
