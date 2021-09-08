class ParseRecords(object):

    def __init__(self, db):
        self.db = db

    def filter_properties(self, key):
        # TODO Simplify the filters.
        # TODO Create dict with type:value per each filter
        # TODO Create filtering if-statement.
        # TODO Remove all the returns

        if key['type'] == 'relation':
            relation = []
            for i in range(len(key['relation'])):
                relation.append(key['relation'][i]['id'])
            return relation
        if key['type'] == 'checkbox':
            return key['checkbox']
        if key['type'] == 'rich_text' and key['rich_text']:
            return key['rich_text'][0]['text']['content']
        if key['type'] == 'text' and key['text']:
            return key['text'][0]['text']['content']
        if key['type'] == 'title' and key['title']:
            return key['title'][0]['text']['content']
        if key['type'] == 'created_time':
            return key['created_time']
        if key['type'] == 'select' and key['select']:
            return key['select']['name']
        if key['type'] == 'multi_select' and key['multi_select']:
            multi_select = []
            for i in range(len(key['multi_select'])):
                multi_select.append(key['multi_select'][i]['name'])
            return multi_select
        if key['type'] == 'email' and key['email']:
            return key['email']
        if key['type'] == 'number' and key['number']:
            return key['number']
        if key['type'] == 'url' and key['url']:
            return key['url']
        if key['type'] == 'phone_number' and key['phone_number']:
            return key['phone_number']

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
