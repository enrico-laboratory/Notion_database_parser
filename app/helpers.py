import config
import os
import json

basedir = config.basedir


def dump_json(name, directory, database):
    """"Helpers for the json dumping
    in specific directories"""

    path = basedir + "/" + directory
    if os.path.isdir(path) is False:
        os.mkdir(path)

    with open(f'{path}/{name}.json', 'w') as f:
        json.dump(database, f, indent=2)
