from app.pull_db import ReturnDbDict
import config
import pprint

project_db = ReturnDbDict(config.PROJECT_DB_ID, 'project_db')
location_db = ReturnDbDict(config.LOCATION_DB_ID, 'location_db')
cast_db = ReturnDbDict(config.CAST_DB_ID, 'cast_db')
repertoire_db = ReturnDbDict(config.REPERTOIRE_DB_ID, 'repertoire_db')

pprint.pprint(project_db.dump_database())
pprint.pprint(location_db.dump_database())
pprint.pprint(cast_db.dump_database())
pprint.pprint(repertoire_db.dump_database())
