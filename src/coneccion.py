from pymongo import MongoClient
import json

def connection(collection):
    MONGO_URL = 'mongodb://ever-green-dbcosmos:lKyWETHA3Zg3tKlwsFE0CeGUgOw2Bj7NgX8lpqxxMxkMZjqX5JPLdCDi2a4kcVJyWRVX4XQrxoAh1aKP4I67eg==@ever-green-dbcosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@ever-green-dbcosmos@'
    client = MongoClient(MONGO_URL)
    db = client['evergreen']
    collection = db[collection]
    return collection




def db_find(collection):
    db_connection = connection(collection)
    try:
        find_response = db_connection.find()
        return find_response
    except:
        return False

def db_save(collection, document):
    db_connection = connection(collection)

    insert_response = db_connection.insert(document)
