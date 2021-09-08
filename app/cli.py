import argparse


parser = argparse.ArgumentParser(
    description="Notion databases parser"
)

parser.add_argument("-n",
                    help="To use with option -d. Give a name to the database",
                    action="store",
                    default="database")

parser.add_argument("-u",
                    help="Dump also databases list",
                    action="store_true")

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-d",
                   help="Parse a single database proviing the database id",
                   action="store")


group.add_argument("-l",
                   help="""
                   Parse the entire list of databases
                   shared in a notion integration
                   """,
                   action="store_true")


args = parser.parse_args()
