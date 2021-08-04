from pyinputplus import inputStr, inputPassword


def input_db_name_and_id():

    db_name = inputStr('Enter database name >')
    db_id = inputStr('Enter database id >')
    db = {
        db_name: db_id
    }
    return db


def input_token():
    token = inputPassword('Enter Notion token >')
    return token
