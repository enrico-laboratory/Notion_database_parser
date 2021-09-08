# Notion Dabases Parser

## Description

The app allow to dump a .json response via the notion api, parse the json response extracting only the values and dump the output in a new json file.

Example of database json directly from notion api.

    "object": "list",
    "results": [
        {
        "object": "page",
        "id": "edbd828e-b397-4513-bc22-ccf1e22bad7f",
        "created_time": "2021-08-31T15:04:00.000Z",
        "last_edited_time": "2021-08-31T15:05:00.000Z",
        "cover": null,
        "icon": null,
        "parent": {
            "type": "database_id",
            "database_id": "43efc21c-f2a5-468c-b70a-61b149098506"
        },
        "archived": false,
        "properties": {
            "email": {
            "id": "HN|w",
            "type": "email",
            "email": "talent of the future"
            },
            "Phone": {
            "id": "WF|`",
            "type": "phone_number",
            "phone_number": "555 - 89762837"
            },
            "Rating": {
            "id": "YcMo",
            "type": "select",
            "select": {
                "id": "86a00e59-c27c-4f28-8e65-a82fc1a8b119",
                "name": "**",
                "color": "orange"
            }
            },
            "Dead": {
            "id": "_sVi",
            "type": "checkbox",
            "checkbox": false
            },
            "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                "type": "text",
                "text": {
                    "content": "John Smith",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "John Smith",
                "href": null
                }
            ]
            }
        },
        "url": "https://www.notion.so/John-Smith-edbd828eb3974513bc22ccf1e22bad7f"
        
        ...

Parsed version of the above database.

    {
    "id": "43efc21c-f2a5-468c-b70a-61b149098506",
    "name": "Test",
    "records": [
        {
        "id": "edbd828e-b397-4513-bc22-ccf1e22bad7f",
        "email": "talent of the future",
        "Phone": "555 - 89762837",
        "Rating": "**",
        "Dead": false,
        "Name": "John Smith"
        },
    
    ...

## Usage

The Notion Dabase parser can be executed with the following options:

-l
Parse the entire list of databases shared in a notion integration

-n
To use with option -d. Give a name to the database",

-d
Parse a single database proviing the database id

-u
Dump also databases list

The parsed json files are dumped in the directory ./databases/\]<dbname\>.json.

At the moment the app also dump the source databases in ./source_databases/\<source_dbname\>.json.

