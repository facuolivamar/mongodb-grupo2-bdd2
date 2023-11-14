import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:pepe1234@cluster.hg8osqw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Connect to Sales Collection
sales_collection = client.sample_supplies.sales

# Make pipeline
has_items = {
    "$match": {
        "items": {
            "$exists": True,
            "$not": {"$size": 0},
        },
    }
}

fields = {
    "$project": {
        "_id": 1,
        "itemCount": {"$size": "$items"},
        "saleDate": 1,
    }
}

items_solicitados = {"$match": {"itemCount": {"$gte": 5}}} # Corroborar que contengan 5 items

orden_solicitado = {
    "$sort": {"itemCount": -1}  # Ordenar de manera descendente por la cantidad de items
}

limited = {"$limit": 2}

pipeline = [
    has_items,
    fields,
    items_solicitados,
    orden_solicitado,
    limited,
]

# Send a ping to confirm a successful connection
try:
    query = sales_collection.aggregate(pipeline)
    for doc in query:
        pprint.pprint(doc)
except Exception as e:
    print(e)
