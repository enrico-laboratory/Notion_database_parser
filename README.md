# Notion Dabases Parser

## Description

The app allow to dump a .json response via the notion api, parse the json response extracting only the values and dump the output in a new json file.

Example of database query response from notion api. Single record snippet.

    "object": "list",
    "results": [
    {
        "object": "page",
        "id": "924f35f5-608d-4a51-8076-97efb3bddf44",
        "created_time": "2021-08-31T14:59:00.000Z",
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
            "email": "fuguemaster@baroque.de"
            },
            "Phone": {
            "id": "WF|`",
            "type": "phone_number",
            "phone_number": "080 - 1234567"
            },
            "Rating": {
            "id": "YcMo",
            "type": "select",
            "select": {
                "id": "56cb9c98-e4b4-4036-97d1-570d2e12fe23",
                "name": "***",
                "color": "red"
            }
            },
            "Dead": {
            "id": "_sVi",
            "type": "checkbox",
            "checkbox": true
            },
            "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                "type": "text",
                "text": {
                    "content": "Johann Sebastian Bach",
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
                "plain_text": "Johann Sebastian Bach",
                "href": null
                }
            ]
            }
        },
        "url": "https://www.notion.so/Johann-Sebastian-Bach-924f35f5608d4a51807697efb3bddf44"
        }
            
            ...

Parsed version of the above database record using Notion Database Parser app.

        {
        "id": "43efc21c-f2a5-468c-b70a-61b149098506",
        "name": "Test",
        "records": [
            {
            "id": "924f35f5-608d-4a51-8076-97efb3bddf44",
            "email": "fuguemaster@baroque.de",
            "Phone": "080 - 1234567",
            "Rating": "***",
            "Dead": true,
            "Name": "Johann Sebastian Bach"
            }
    ...

## Usage

The Notion Dabase parser can be executed with the following options:

`-l`
Parse the entire list of databases shared in a notion integration

`-n`
To use with option -d. Give a name to the database",

`-d`
Parse a single database proviing the database id

`-u`
Dump also databases list

The parsed json files are dumped in the directory ./databases/\]<dbname\>.json.

At the moment the app also dump the source databases in ./source_databases/\<source_dbname\>.json.
