from app.pull_db import ReturnDbDict, GetRecords
import config
import pprint


project_db = ReturnDbDict(config.PROJECT_DB_ID, 'project_db').read_database()
location_db = ReturnDbDict(config.LOCATION_DB_ID, 'location_db').read_database()
cast_db = ReturnDbDict(config.CAST_DB_ID, 'cast_db').read_database()
repertoire_db = ReturnDbDict(config.REPERTOIRE_DB_ID, 'repertoire_db').dump_database()

# pprint.pprint(project_db)
# pprint.pprint(location_db)
# pprint.pprint(cast_db.dump_database())
# pprint.pprint(repertoire_db.dump_database())

project_db_records = GetRecords(project_db)
repertoire_db_records = GetRecords(repertoire_db)
cast_db_records = GetRecords(cast_db)
location_db_records = GetRecords(location_db)

# pprint.pprint(project_db_records.get_properties(0))
# pprint.pprint(repertoire_db_records.get_properties(0))


# for i in range(len(project_db)):
#     pprint.pprint(project_db_records.get_record_title(i))

# for i in range(len(cast_db)):
#     print('====== NEW RECORD ======')
#     pprint.pprint(cast_db_records.parse_database(i))

# for i in range(len(repertoire_db)):
#     print('====== NEW RECORD ======')
#     pprint.pprint(repertoire_db_records.parse_database(i))

records = []
for record in range(len(location_db)):
    record = (location_db_records.parse_database(record))
    records.append(record)

db_dict = {
    'id': config.LOCATION_DB_ID,
    'name': 'Locations',
    'records': records
}

pprint.pprint(db_dict)
