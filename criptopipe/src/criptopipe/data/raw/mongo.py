from criptopipe.src.criptopipe.config.settings import client_mongo
from criptopipe.src.criptopipe.etl.pipeline import main
from pymongo import MongoClient
import asyncio
import certifi


conn = MongoClient(client_mongo, tlsCAFile=certifi.where())
database = conn.get_database('raw_data_criptopipe')
coll = database.get_collection('data_criptopipe')
raw_data = list(asyncio.run(main()))
coll.insert_many(raw_data)
print(raw_data)
