from pymongo import MongoClient
from bson.json_util import loads


# function to handle data
def ingest(f):
    with open(f) as _f:
        return loads(_f.read())


# functions to for handling init
init_client = lambda uri: MongoClient(uri)
init_database = lambda client, database_name: client[database_name]


# functions to insert data
insert_data = lambda database, file: database['license'].insert_many(ingest(f))
