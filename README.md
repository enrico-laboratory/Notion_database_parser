# Notion Databases Parser

## Description

The app allows to query via the [Notion API](https://developers.notion.com/docs/getting-started "Notion API") one database or all the databases present in [Notion Integration](https://www.notion.so/my-integrations "Notion Integration"). The query dumps a .json response, parses the response and creates a new simplified json file, stripped from all the formats information showing only the database records values. The result is similar to a database export from the Notion App directly.

The query to the Notion database is done with the [notion_client app](https://github.com/ramnes/notion-sdk-py).

Example of database query response from Notion API, not parsed. Single record snippet.



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

The Notion Database Parser is a command line application and can be executed with the following options:

`-l`
Parse the entire list of databases shared in a notion integration

`-n`
To use with option -d. Give a name to the database

`-d`
Parse a single database providing the database id as parameter

`-u`
Dump also databases list

The parsed json files are dumped in the directory ./databases/\<dbname\>.json. At the moment the app also dumps the source databases in ./source_databases/\<source_dbname\>.json.

## Why?

In Notion you can create databases and database views. In the view you can add filters and sorting options, like a database query. I use the view of a master database to show only the relevant information for a specific purpose. 

I organise and perform music projects with choirs and I need to share with them practical information (repertoire, singers' contact, locations, etc...). For each topic I have a master database. I then create a database view to extract from the master database the relevant information of a specific project.

I want to use Notion for this purpose but, unfortunately, while you can easily share a database, it is not possible to share only the database view without sharing the entire underlying database. That will force me to share with a choir information coming from another choir creating among others privacy issues. 

I decided then to create a separate website where I can share with choirs all the relevant information to their project.The Notion Database Parser is a part of this website.

There are others and, probably less complicated solutions to solve my problem, however I am practicing my coding skills and this project helped me quite a lot in deepening my knowledge in Python and having some fun doing so :)

