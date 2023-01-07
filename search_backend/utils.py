from pymongo import MongoClient
from . import secrets

def get_mongo_connection(collection_name):
    'Establish mongodb connection'
    mongo_client = MongoClient(secrets.MONGO_DATABASE_HOST)
    mongo_db_name = mongo_client[secrets.search_database]
    mongo_connection = mongo_db_name[collection_name]
    return mongo_connection

def get_complete_endpoint(endpoint):
    'Triming of query parameters from endpoint'
    if '?' in endpoint:
        return endpoint.split('?')[0]
    return endpoint

def string2bool(s):
    'Convert str object to bool'
    return str(s).lower() in ("yes", "true", "t", "1")