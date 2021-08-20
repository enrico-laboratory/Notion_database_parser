from app.pull_db import ReturnDbDict, GetRecords
import config
import app.db_info
import json

db_name_and_id = {}
if config.DB_ID:
    db_name_and_id = config.DB_ID
else:
    db_name_and_id = db_info.input_db_name_and_id()

token = ''
if config.NOTION_TOKEN:
    token = config.NOTION_TOKEN
else:
    token = db_info.input_token()

for key, value in db_name_and_id.items():
    db = ReturnDbDict(key, value, token).read_database()
    db_record = GetRecords(db)
    records = []
    for record in range(len(db)):
        record = (db_record.parse_database(record))
        records.append(record)

    db_dict = {
        'name': key,
        'id': value,
        'records': records
    }
    with open(f'{config.basedir}/data_temp/{key}.json', 'w') as f:
        json.dump(db_dict, f, indent=2)
