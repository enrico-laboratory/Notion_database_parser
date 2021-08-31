import argparse


parser = argparse.ArgumentParser(
    description="Notion databases parser"
)

parser.add_argument("-n",
                    help="Chose a name for the database",
                    action="store",
                    default="database")

parser.add_argument("-u",
                    help="Dump database list and parsed databases",
                    action="store_true")

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-d",
                   help="Input database id",
                   action="store")


group.add_argument("-l",
                   help="Parse the entire list of databases",
                   action="store_true")


args = parser.parse_args()
