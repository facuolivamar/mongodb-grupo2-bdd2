import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:pepe1234@cluster.hg8osqw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Connect to Sales Collection
collection = client.sample_mflix.movies

# Make pipeline
group_by = {
    "$group": {
        "_id": "$rated",
        "cantidadPeliculas": {"$sum": 1}
        }
    }

project = {
    "$project": {
        "_id": 0,
        "rated": "$_id",
        "cantidadPeliculas": 1,
    }
}

having = {"$match": {"cantidadPeliculas": {"$lte": 60}}}

sorting = {"$sort": {"cantidadPeliculas": -1}}

pipeline = [group_by, project, having, sorting]

# Send a ping to confirm a successful connection
try:
    query = collection.aggregate(pipeline)
    for doc in query:
        pprint.pprint(doc)
except Exception as e:
    print(e)
