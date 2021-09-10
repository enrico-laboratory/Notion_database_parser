import config
import os
import json

basedir = config.basedir


def dump_json(name, directory, database):
<<<<<<< HEAD
=======
    """"Helpers for the json dumping
    in specific directories"""
>>>>>>> 0d4a1f1938c0739be447089fd6171a75f3312e80

    path = basedir + "/" + directory
    if os.path.isdir(path) is False:
        os.mkdir(path)

    with open(f'{path}/{name}.json', 'w') as f:
        json.dump(database, f, indent=2)
    return database
