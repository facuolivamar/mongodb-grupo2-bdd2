from pymongo import MongoClient
MONGO_URI = "mongodb+srv://admin:pepe1234@cluster0.brvrhht.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
for db_name in client.list_database_names():
    print(db_name)

# import os

# from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()
# MONGO_URI = os.environ("MONGODB_URI")

# client = MongoClient(MONGO_URI)

# for db_name in client.list_database_names():
#     print(db_name)